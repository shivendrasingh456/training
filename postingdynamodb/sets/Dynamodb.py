import boto3
import sys
from .getid import GetId

class Dynamodb:
    def __init__(self):
        self.client = boto3.client('dynamodb',region_name = 'us-east-1')
        self.Item = {}
        self.attribute = []
        self.keyschema = []

    def create(self, tablename, pkey):
        """takes table name,partition key and sort key,returns status code
        py:function::

        Args:
            tablename(str),pkey(str),skey(str): credentials to be used to create table

        Returns:
            self.table['TableDescription']['ResponseMetadata']['HTTPStatusCode'](satus code) : returns status code

        """
        tables =self.getTables()
        try:
            if tablename in tables:
                raise Exception("TableName Already Exists")

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
            return self.table['TableDescription']['ResponseMetadata']['HTTPStatusCode']
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
        if list_dict is None or len(list_dict) ==0 or type(list_dict) !=list:
            raise Exception("list is None or empty or any other datatype")

        for row in list_dict:
            row['id'] = GetId(row)
            row['name'] = row['id']
            # print(row['id'])
            if None in (row.get('name'),row.get('id')):
                raise Exception("partition key or sort key")
            if len(row.get('name')) ==0 or len(row.get('id'))==0:
                raise Exception("partition key or sort key cannot be empty string")
            if row.get('variants') is None:
                raise Exception(f"deliverable,description,display name and similar data is not available")
            else:
                num=1
                for data in row['variants']:
                    for variant_data in data:
                        index = variant_data.find('_')
                        self.Item[variant_data[0:index -1] + str(num)+variant_data[index :]] = {
                            "S"if type(data[variant_data])== str else "N" if data.get(variant_data) is not None else "NULL":  str(data[variant_data]) if data.get(variant_data) is not None else data[variant_data]
                        }
                    num = num +1
            row.pop('variants')
            
            for key in row:
                self.Item[key] = {
                    "BOOL"if type(row[key])==bool else "S" if type(row[key])==str else "N" if data.get(variant_data) is not None else "NULL":row[key] if type(row[key]) ==bool else str(row[key]) if data.get(variant_data) is not None else data[variant_data]
                }            

        items = self.client.put_item(
            TableName=tablename,
            Item=self.Item
        )

        return items['ResponseMetadata']['HTTPStatusCode']

    def getTables(self):
        return self.client.list_tables()["TableNames"]