import os
import json
import boto3
from boto3.dynamodb.conditions import Attr

class InvoiceData:
    def __init__(self):
        self.dynamodb = boto3.client('dynamodb', region_name='us-east-1')
        self.dynamoDbUrl = os.environ.get('DYNAMODBURL')

    def prepre_invoice(self,data):
        inv_data = []
        # print('prepare_json-{}'.format(data))
        # print(f"dynamodburl : {self.dynamoDbUrl}")
        inv_obj = {}
        inv_obj['customer']= self.customer_json(data) # get customer address from dynamoDb customer table & this should be the billing address
        inv_obj['transport'] = self.transport_json(data) #get shipping address from RDS SubscriptionEvnets tables & this should be the delivery address
        inv_obj['id'] = 0
        inv_obj['location_id'] = os.environ.get('LOCATION_ID')
        inv_obj['invoice_type'] = "IV"
        inv_obj['taxes_inclusive'] = True
        inv_obj['desktop'] = True
        customer=self.getCustomerByName(data['customer'].get('name'))
        inv_obj['customer_id']=int(customer['sl_id'])
        inv_obj['generalledger_id']=os.environ.get('GENERALLEDGER_ID')
        inv_obj['lines']=self.itemLines_json(data,inv_obj['taxes_inclusive'])
        inv_data.append(inv_obj)
        return inv_data

    def customer_json(self,item):
        customer_obj={}
        addr_dict = ['customer_name','aline1','aline2','community','landmark','city','state','postalcode','tag']
        delivery_address = item.get('delivery_address','').split('\n')
        address_obj = {addr_dict[i]:delivery_address[i] for i in range(len(delivery_address))}
        customer_obj['address1'] = address_obj.get('aline1')
        customer_obj['address2'] = address_obj.get('aline2')
        customer_obj['mobile'] = item['customer'].get('mobile')
        customer_obj['display_name'] = item['customer'].get('display_name')
        customer_obj['pin'] = address_obj.get('postalcode')
        customer_obj['gstin']= ""
        customer_obj['city']=address_obj.get('city')
        return customer_obj

    def transport_json(self,item):
        transport_obj={}
        addr_dict = ['customer_name','aline1','aline2','community','landmark','city','state','postalcode','tag']
        delivery_address = item.get('delivery_address','').split('\n')
        address_obj = {addr_dict[i]:delivery_address[i] for i in range(len(delivery_address))}
        transport_obj['shp_address1']=address_obj.get('aline1')
        transport_obj['shp_address2']=address_obj.get('aline2')
        transport_obj['shp_city']=address_obj.get('city')
        transport_obj['shp_state']=address_obj.get('state')
        transport_obj['person_name']=item['customer'].get('display_name')
        transport_obj['person_phone']=item['customer'].get('mobile')
        transport_obj['narration']=""
        transport_obj['shp_pin']=address_obj.get('postalcode')
        transport_obj['gstin']=""
        transport_obj['pin']=address_obj.get('postalcode')
        return transport_obj

    def itemLines_json(self,data,taxes_inclusive):
        lines_obj = []
        for product in data['product']:
            seq=1
            # print(f"product of name : {product['name']}")
            item = self.getItemByName(product['name'])
            if item is None:
                raise Exception('No Item Found.')
            taxmethod_name = product['tax_methods'] if 'tax_methods' in product and product['tax_methods'] is not None else os.environ.get('TAX_METHODS')
            tax=self.getTaxMethodByName(taxmethod_name)
            # print(f"tax : {tax['taxmethod_id']}")
            # print(f"tax : {type(tax)}")
            product_obj = {}
            product_obj['store_id'] = item['store_id'] if 'store_id' in item and item['store_id'] is not None else os.environ.get('STORE_ID')
            product_obj['seq']=seq
            product_obj['storeitem_id'] = int(item['storeitem_id'])
            product_obj['uom_name']=product['uom']
            product_obj['Unit']=product['uom']
            product_obj['qty'] = product['qty']
            product_obj['status'] = product['status']
            product_obj['taxmethod_id']=int(tax['taxmethod_id'])
            product_obj['price']=product['sale_val'] if product['sale_val'] is not None else os.environ.get('MEAL_PRICE')
            tax_amount= self.calculate_tax(product_obj['taxmethod_id'],product_obj['price'],taxes_inclusive)
            product_obj['unitprice']=int(product_obj['price'])
            product_obj['invoice_amt']=product_obj['unitprice']*product_obj['qty']
            product_obj['amount']=product_obj['invoice_amt']+tax_amount
            product_obj['hsn']=item.get('hsn')
            product_obj['sac']=item.get('sac')
            product_obj['IsServc']="N"
            product_obj['delivered']=True
            product_obj['uomtypec_id']=int(item['uomtypec_id'])
            product_obj['uom_id']=int(item['uom_id'])
            lines_obj.append(product_obj)
            seq=seq+1
        return lines_obj
    
    def calculate_tax(self,tax_method_id,sale_val,taxes_inclusive):
        if taxes_inclusive:
            #calculate tax
            return 0
            
    def getTaxMethodByName(self,taxmethod_name):
        # print(f"taxmethod_name: {taxmethod_name}")
        dynamodb = boto3.resource('dynamodb',region_name = "us-east-1", endpoint_url=self.dynamoDbUrl)
        tax_table = dynamodb.Table('Taxes')
        response = tax_table.scan(
            FilterExpression=Attr('name').eq(taxmethod_name)
        )
        # print(f"response of Tax table : {response}")
        if response['Count'] > 0:
            return response['Items'][0]
        else:
            return ''

    def getItemByName(self,item_name):
        dynamodb = boto3.resource('dynamodb',region_name = "us-east-1", endpoint_url=self.dynamoDbUrl)
        item_table = dynamodb.Table('ItemTable')
        response = item_table.scan(
            FilterExpression=Attr('name').eq(item_name)
        )
        if response['Count'] > 0:
            return response['Items'][0]
        else:
            return ''

    def getCustomerByName(self,customer_name):
        cusomter_name = ''.join(e.upper() for e in customer_name if e.isalnum())
        dynamodb = boto3.resource('dynamodb',region_name= "us-east-1", endpoint_url=self.dynamoDbUrl)
        item_table = dynamodb.Table('Customer')
        response = item_table.scan(
            FilterExpression=Attr('name').eq(customer_name)
        )
        if response['Count'] > 0:
            return response['Items'][0]
        else:
            return ''