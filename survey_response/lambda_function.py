import boto3
import json
import os 
from scanfile import GetDetails
from User import User #from layer version 6 importing User class

def lambda_handler(event, context):
    
    try: 
        if event is None or len(event)==0:
            raise Exception(f"event is none")

        try:
            application_no = event['params']['querystring']['application_no']
        except KeyError:
            raise Exception(f"application id is not provided")
        
        #getting details from cognito using the accesstoken from event
        a=User() 
        cognito_details = a.getUser(event)
        customer_id= cognito_details['sub']
        
        ##Retrieving details from dynamodb with customer id from previous response and application no from the event
        tablename='SURVEYFORM'
        b = GetDetails(customer_id,application_no)
        res=b.Scandynamodb(tablename)
        
        if  res['Count']!=0:
            return res['Items']
        else:
            return {}
        
    except Exception as e1:
        print(f"Generic errror : {e1}")
        return e1