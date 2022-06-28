import json
from User import User
from dynamodb import Dynamodb

def lambda_handler(event, context):
    # try:
        # print(f"event : {event}")
        application_no=event['arguments']['input']['application_no']
        customer_id=event['arguments']['input']['customer_id']
        status_code=event['arguments']['input']['status_code']
        
        print(f"event : {event}")
        #getting user name from cognito userpool with access token from event
        a=User() 
        cognito_details = a.getUser(event)
        upd_by= cognito_details['name']
        
        #getting status from status table with the status code
        # tablename,column_name,data='Status','status_code',status_code
        b = Dynamodb()
        # res=b.getitems(tablename,column_name,data)
        # if res.get('Item') is not None:
        #     formStatus=res['Item']['name']
        # else:
        #     raise Exception("invalid status code")
        
        formStatus='SUBMITED'
        #checking SURVEYFORM table for customer id and application no, if exists then updating data otherwise throwing exception
        tablename,fieldname1,data1,fieldname2,data2='SURVEYFORM','customer_id',customer_id,'application_no',application_no
        res=b.scandynamodb(tablename,fieldname1,data1,fieldname2,data2)
        # id=res['Items'][0]['id']
        return res
        
        #inserting status,upd_by,upd_on on SURVEYFORM table with the help of application no and customer id 
        # tablename='SURVEYFORM'
        # dict={
            
        # }
        # b.put_item()
        
        return {'message':"success","is_error":False}
    # except Exception as e:
    #     return {'message':f"failed : {e}","is_error":True}