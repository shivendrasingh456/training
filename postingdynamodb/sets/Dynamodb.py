import boto3
from .getid import GetId

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



    def putitem(self,list_dict):
        """takes list of dictionary,add details to dynamodb table,returns success code
        py:function::

        Args:
            tablename(str),list_dict(list): table name and the data to be used

        Returns:
            items['ResponseMetadata']['HTTPStatusCode'](status code): returns status code
        """

        #storing data in service table
        tablename ='service_table'
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
                self.Item = {}
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

                #storing data in categories table 
                dict_details ={'id' : details['id'],'display_name' : details['display_name']}
                self.Categories(dict_details)



    def Categories(self,dict_details):
        """takes dictionary,adds data to the categories dynamodb table,returns None
        py:function::

        Args:
            dict_details(dict): dictionary conatining id and name data from json

        Returns:
            None
        """
        tablename = 'Categories'
        self.Item ={}
        dict_details['name'] = dict_details['id']
        for key in dict_details:
                    self.Item[key] = {
                        "BOOL"if type(dict_details[key])==bool else "S" if type(dict_details[key])==str else "NULL" if dict_details[key]is None else "N": dict_details[key] if type(dict_details[key]) ==bool else str(dict_details[key]) if dict_details.get(key) is not None else True
                    } 


        items = self.client.put_item(
                    TableName=tablename,
                    Item=self.Item
                )
    def getTables(self):
        """takes none,returns all tables present in dynamodb at a particular region
        py:function::

        Args:
            None

        Returns:
            self.client.list_tables()["TableNames"][list] : list containing tablenames
        
        """
        return self.client.list_tables()["TableNames"]