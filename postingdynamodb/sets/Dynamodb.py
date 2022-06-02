import boto3
from .getid import GetId

class Dynamodb:
    def __init__(self):
        self.client = boto3.client('dynamodb',region_name = 'us-east-1')
        self.Item = {}
        self.attribute = []
        self.keyschema = []
        self.variant = []

    def create(self, tablename, pkey):
        """takes table name,partition key,creats table in dynamodb and returns None
        py:function::
                    
        Args:
            tablename(str),pkey(str): credentials to be used to create table

        Returns:
            None

        """
        tables =self.getTables()
        try:
            if tablename in tables:
                raise Exception(f"Table name as : {tablename} exists already")

            attributes ={pkey:'HASH'}
            for att in attributes:
                self.attribute.append({
                        'AttributeName': att,
                        'AttributeType': 'S'
                    })
                self.keyschema.append({
                        'AttributeName': att,
                        'KeyType': attributes[att]
                    })
            

            self.table = self.client.create_table(
                AttributeDefinitions= self.attribute,
                TableName=tablename,
                KeySchema= self.keyschema,
                BillingMode='PROVISIONED',
                ProvisionedThroughput={
                    'ReadCapacityUnits': 123,
                    'WriteCapacityUnits': 123
                }
            )
        except Exception as e:
            print(str(e))



    def putitem(self,tablename,list_dict):
        """takes table name,list of dictionary,add details to dynamodb table,returns success code
        py:function::

        Args:
            tablename(str),list_dict(list): table name and the data to be used

        Returns:
            items['ResponseMetadata']['HTTPStatusCode'](status code): returns status code
        """


        # service_table()
        if list_dict is None or len(list_dict) ==0 or type(list_dict) !=list:
            raise Exception("list is None or empty or any other datatype")

        for row in list_dict:
            details = row
            details['id'] = GetId(details)
            details['name'] = details['id']
            
            if details.get('id') is None:
                raise Exception("partition key is None")
            if len(details.get('id'))==0:
                raise Exception("partition key cannot be empty string")
            if details.get('variants') is None:
                raise Exception(f"deliverable,description,display name and similar data is not available")
            else:
                self.variant = []
                for variant in details['variants']:
                    variant_dict={}
                    dict ={}
                    for key in variant:                
                        dict[key] ={
                            "BOOL" if type(variant[key])==bool else "S" if type(variant[key])==str else "NULL" if variant[key]is None else "N": variant[key] if type(variant[key]) ==bool else str(variant[key]) if variant.get(key) is not None else True
                        }

                    variant_dict['M'] = dict  
                    self.variant.append(variant_dict)
                                                                                                        
                self.Item['variants'] = {
                    "L": self.variant
                }  
                details.pop('variants')  

                # otherthan variants    
                for key in details:
                    self.Item[key] = {
                        "BOOL"if type(details[key])==bool else "S" if type(details[key])==str else "NULL" if details[key]is None else "N": details[key] if type(details[key]) ==bool else str(details[key]) if details.get(key) is not None else True
                    }           


                items = self.client.put_item(
                    TableName=tablename,
                    Item=self.Item
                )

        return items['ResponseMetadata']['HTTPStatusCode']


    # def service_table (tablename,list_dict):
    #     pass
    def getTables(self):
        return self.client.list_tables()["TableNames"]