from .mobibooks import Mobibooks
import os
from .payload import Payload_mobibooks,Preparedata
from .dynamodb import Dynamodb
import boto3
from boto3.dynamodb.conditions import Attr

class Signup:
    def __init__(self,event=None):
        
        self.a = Mobibooks(os.environ.get('MOBI_HOST'),os.environ.get('MOBI_USER'),os.environ.get('MOBI_PASSWORD'),os.environ.get('MOBI_LOCATION'),
        os.environ.get('MOBI_CUSTOMER'))
        self.event = event
    
    def making_connection(self):
        self.a.login()
        
    def post_mobibooks(self):
        #1st call on mobibooks
        self.payload = Payload_mobibooks(self.event)
        
        #testing whether the given phone number exists in mobibooks or not
        subledger_url = 'subledger/'
        output = self.a.get(subledger_url,'api',self.payload)
        
        if output['id'] != 0:
            print(f"Details with name: {self.payload['display_name']} already exists with sl_id : {output['id']} in Mobibooks")
            self.sl_id = output['id']
        else:
            output = self.a.post('subledger/',self.payload)
            if output.get('id'):
                self.sl_id = output['id']
                print("details are posted on mobibboks")
            else:
                raise Exception(output)
                
            #2nd call on mobibooks
            output = self.a.get('subledger/','api',self.sl_id)
            if output.get('id'):
                print(f"details are posted on mobibboks with sl_id : {self.sl_id} and giving response id : {output['id']}")
            else:
                raise Exception(output)
            
    def postdynamodb(self):
        
        self.data = Preparedata(self.event["userName"],self.payload,self.sl_id)
        
        #checking whether name is present inside the dynamodb or not 
        res = self.scandynamodb(self.data['name'])
        
        if res['Count'] ==0:
            # inserting data in dynamodb table 
            tablename = "CUSTOMERS"
            b = Dynamodb()
            res = b.putitem(tablename,self.data)
            print("new details are posted on dynamodb")
            
        else:
            if res['Items'][0]['sl_id'] is None:
                res['Items'][0]['sl_id'] = self.sl_id
            else:
                print(f"Details aleardy exists in dynamodb with name: {self.data['name']} and sl_id : {self.sl_id}")
    
        
    def scandynamodb(self,name):
        dynamodb = boto3.resource('dynamodb',region_name= os.environ.get('REGION_NAME'), endpoint_url='https://dynamodb.'+os.environ.get('REGION_NAME')+'.amazonaws.com/')
        item_table = dynamodb.Table('CUSTOMERS')
        response = item_table.scan(
            FilterExpression=Attr('name').eq(name)
        )
        return response
       