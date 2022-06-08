from .mobibooks import Mobibooks
import os
from .payload import Payload_mobibooks,Preparedata
from .dynamodb import Dynamodb
import boto3

class Signup:
    def __init__(self,event):
        self.a = Mobibooks(os.environ.get('MOBI_HOST'),os.environ.get('MOBI_USER'),os.environ.get('MOBI_PASSWORD'),os.environ.get('MOBI_LOCATION'),
        os.environ.get('MOBI_CUSTOMER'))
        self.event = event
    
    def making_connection(self):
        self.a.login()
        
    def post_mobibooks(self):
        #1st call on mobibooks
        self.payload = Payload_mobibooks(self.event)
        
        # #testing whether the given phone number exists in mobibooks or not
        # output = self.a.get('mobile/','9807645321')
        # print(f"output : {outpnut}")
        
        output = self.a.post('subledger/',self.payload)
        if output.get('id'):
            self.sl_id = output['id']
            print("details are posted on mobibboks")
        else:
            raise Exception(output)
            
        #2nd call on mobibooks
        output = self.a.get('subledger/',self.sl_id)
        if output.get('id'):
            print(f"details are present with sl_id : {self.sl_id} and giving response id : {output['id']}")
        else:
            raise Exception(output)
            
    def postdynamodb(self):
        self.data = Preparedata(self.event["userName"],self.payload,self.sl_id)
        # inserting data in dynamodb table after posting on mobibooka
        tablename = "Customer"
        b = Dynamodb()
        output = b.putitem(tablename,self.data)
        
        return output
        
        
    def post_queue(self,error):
        client=boto3.client('sqs',region_name=os.environ.get('REGION_NAME'))
        customer_id = boto3.client('sts').get_caller_identity()['Account']
        queue_name = os.environ.get('ERROR_QUEUE_NAME')
        res=client.send_message(QueueUrl=f'https://sqs.us-east-1.amazonaws.com/{customer_id}/{queue_name}',MessageBody=str(error))
        
        
        