import os
import boto3
from boto3.dynamodb.conditions import Attr

class GetDetails:
    def __init__(self,customer_id=None,application_no=None):
        if os.environ.get('REGION_NAME') is None: 
            print("region name is none in environment variable")
        self.dynamodb = boto3.resource('dynamodb',region_name=os.environ.get('REGION_NAME'))
        self.customer_id=customer_id
        self.application_no=application_no
    
    def Scandynamodb(self,tablename):
        """takes tablename,scans for a particular application no and customer id in the table,sends response to scan_with_LastEvaluatedKey function 
        which checks LastEvaluatedKey exists or not in response and performs more operation
        py::function
        
        Args:
            tablename(str):table name to be checked
            
        Returns:
            scan_with_LastEvaluatedKey(dict): sends the reponse to another function for LastEvaluatedKey checking
        """
        self.tablename=tablename
        item_table=self.dynamodb.Table(self.tablename)
        #application number is stored in int format in the SURVEYFORM table 
        res= item_table.scan( FilterExpression=Attr("application_no").eq(int(self.application_no)) & Attr("customer_id").eq(self.customer_id))
        return self.scan_with_LastEvaluatedKey(res)
        
    def scan_with_LastEvaluatedKey(self,res):
        """takes response,checks whether LastEvaluatedKey exists or not,if exists performs scan operation in while loop until LastEvaluatedKey exits
        or we get the details for a particular record, returns response 
        """
        while 'LastEvaluatedKey' in res:
            if  res['Count']!=0:
                return res
            LastEvaluatedKey=res['LastEvaluatedKey']
            res= item_table.scan( FilterExpression=Attr("application_no").eq(int(self.application_no)) & Attr("customer_id").eq(self.customer_id)
            ,ExclusiveStartKey=LastEvaluatedKey)
            
        return res