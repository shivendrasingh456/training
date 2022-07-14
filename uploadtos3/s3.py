import json
import boto3
import base64
import six
import io
from boto3.dynamodb.conditions import Attr

class S3:
    def __init__(self,bucket_name):
        self.client = boto3.client('s3')
        self.resource= boto3.resource('s3')
        self.bucket_name=bucket_name
    
    def upload_to_s3(self,base64_file,key):
        """
        base64_file(string): file in base64 format 
        key(string): complete address of object including its name
        """
        file = self.decode_base64_file(base64_file)
        res=self.client.upload_fileobj(
            file,
            self.bucket_name,
            key,
            ExtraArgs={'ACL':'public-read'}
        )
        return res
    
    def upload_file(self,filename,Key):
        self.resource.meta.client.upload_file(filename, self.bucket_name, Key)
        
    def decode_base64_file(self,data):
        """
        Fuction to convert base 64 to readable IO bytes and auto-generate file name with extension
        :param data: base64 file input
        :return: tuple containing IO bytes file and filename
        """
        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')
    
            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                TypeError('invalid_image')
    
            return io.BytesIO(decoded_file)