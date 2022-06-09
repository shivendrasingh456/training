
import boto3,os

def Post_Queue(error):
    client=boto3.client('sqs',region_name=os.environ.get('REGION_NAME'))
    customer_id = boto3.client('sts').get_caller_identity()['Account']
    queue_name = os.environ.get('ERROR_QUEUE_NAME')
    res=client.send_message(QueueUrl=f'https://sqs.us-east-1.amazonaws.com/{customer_id}/{queue_name}',MessageBody=str(error))