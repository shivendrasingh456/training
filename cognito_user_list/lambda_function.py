import json
from cognito_pool import VLpool

def lambda_handler(event, context):
    
    try:
        a = VLpool(event)
        return a.list_user()
    except Exception as e1:
        print(f"exception raised as : {e1}")
        return e1
        
    