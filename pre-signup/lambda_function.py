from post_file import Signup
import os

def lambda_handler(event, context):
    
    # It sets the user pool autoConfirmUser flag after validating the email domain
    event['response']['autoConfirmUser'] = True
    
    # Set the email as verified if it is in the request
    if 'email' in event['request']['userAttributes']:
        event['response']['autoVerifyEmail'] = True

    # Set the phone number as verified if it is in the request
    if 'phone_number' in event['request']['userAttributes']:
        event['response']['autoVerifyPhone'] = True

    try :
        if event is None or len(event)==0 or type(event) != dict:
            raise Exception("event is none or empty or not dict")
        a = Signup(event)
        #making connection to mobibooks
        a.making_connection()
        print("session created")
    
        #post details on mobibboks
        a.post_mobibooks()
        
        #posting data on dynamodb
        return a.postdynamodbb()
        
    except Exception as e1 :
        print(f"exception : {e1}")
        a = Signup(event)
        a.post_queue(e1)
        
        