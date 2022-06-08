from post_file import Payload_mobibooks,Mobibooks,Dynamodb,Preparedata
import os

def lambda_handler(event, context):
    
    if event is None or len(event)==0 or type(event) != dict:
        raise Exception("event is none or empty or not dict")
    # It sets the user pool autoConfirmUser flag after validating the email domain
    # print('event')
    
    event['response']['autoConfirmUser'] = True
    
    # Set the email as verified if it is in the request
    if 'email' in event['request']['userAttributes']:
        event['response']['autoVerifyEmail'] = True

    # Set the phone number as verified if it is in the request
    if 'phone_number' in event['request']['userAttributes']:
        event['response']['autoVerifyPhone'] = True

    payload = Payload_mobibooks(event)
    a = Mobibooks(os.environ.get('MOBI_HOST'),os.environ.get('MOBI_USER'),os.environ.get('MOBI_PASSWORD'),os.environ.get('MOBI_LOCATION'),
    os.environ.get('MOBI_CUSTOMER'))
    a.login()
    print("session created")
    
    #1st call on mobibboks
    output = a.post('subledger/',payload)
    if output.get('id'):
        sl_id = output['id']
        print("details are posted on mobibboks")
    else:
        raise Exception("deatils are not posted on mobibooks")
    
    #2nd call on mobiboooks
    output = a.get('subledger/',sl_id)
    if output.get('id'):
        print(f"details are present with sl_id : {sl_id} and giving response id : {output['id']}")
    else:
        raise Exception("2nd api call is not successful ")
    
    #posting data on dynamodb
    data = Preparedata(event["userName"],payload,sl_id)
    # inserting data in dynamodb table after posting on mobibooka
    tablename = "Customer"
    b = Dynamodb()
    output = b.putitem(tablename,data)
    print(f"output of posting on dynamodb : {output}")
    
    
    # Return to Amazon Cognito
    return event