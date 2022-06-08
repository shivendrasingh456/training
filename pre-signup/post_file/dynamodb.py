import boto3
from .getid import GetId
from boto3.dynamodb.conditions import Attr
from boto3.dynamodb.types import TypeDeserializer

class Dynamodb:
    def __init__(self):
        self.client = boto3.client('dynamodb',region_name = 'us-east-1')
        self.Item = {}
        self.attribute = []
        self.keyschema = []
        self.variant = []

    def create(self, tablename, pkey,skey=None):
        """takes table name,partition key or skey if availabe,creats table in dynamodb and returns None
        py:function::
    
        Args:
            tablename(str),pkey(str),skey(str-if available): credentials to be used to create table

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


    def putitem(self,tablename,dict):
        serializer = boto3.dynamodb.types.TypeSerializer()
        self.Item = {k: serializer.serialize(v) for k,v in dict.items()}
                
        items = self.client.put_item(
            TableName=tablename,
            Item=self.Item
        )
        return items['ResponseMetadata']['HTTPStatusCode']

    def getTables(self):
        """takes none,returns all tables present in dynamodb at a particular region
        py:function::

        Args:
            None

        Returns:
            self.client.list_tables()["TableNames"][list] : list containing tablenames
        
        """
        return self.client.list_tables()["TableNames"]


    #scanning table
    # def scan_table(self,id):
    #     dynamodb = boto3.resource('dynamodb',region_name= "us-east-1", endpoint_url='https://dynamodb.us-east-1.amazonaws.com/')
    #     item_table = dynamodb.Table('service_table')
    #     response = item_table.scan(
    #         FilterExpression=Attr('name').eq(id)
    #     )
    #     print(f"response : {response}")
