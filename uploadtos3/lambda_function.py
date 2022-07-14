import os
from User import User
from s3 import S3
import boto3

def lambda_handler(event, context):

    # try:
        #Getting the customer id from cognito to store data in s3 bucket in the respective file names
        # user = User()
        # customer = user.getUser(event)
        # id = customer.get("sub")
        id='shivudu123456'
        
       
        bucket_name=os.environ.get('BUCKET_NAME')
        filetype=event['arguments']['input']['type']
        path='serviceimgs' if filetype=='PIMG' else 'category' if filetype=='CIMG' else 'required_documents' if filetype=='REQDOCS' else ''
        file_object=event['arguments']['input'].get('file')
        
        
        file_name=event['arguments']['input'].get('name')
        #This is the complete path of inserting object
        key=path+'/'+id + '/' +file_name
        
        a=S3(bucket_name)
        res=a.upload_to_s3(file_object,key)
        print('upload_response-{}'.format(res))
        url = 'https://'+bucket_name+'.s3.me-south-1.amazonaws.com/'+key
        event['url'] = url
        return event
    # except Exception as e:
    #     raise e
    
