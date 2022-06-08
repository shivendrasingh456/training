from .getid import GetId
from datetime import datetime

def Payload_mobibooks(data):
    if data is None or len(data) ==0 or type(data) !=dict :
        raise Exception("incoming event is null or empty or list")
        
    try:     
        payload ={'display_name' : data['request']['userAttributes']['name'] ,'mobile' : data['request']['userAttributes']['phone_number'][3:],
        'status' : '','party_type': 'U','alias': data['request']['userAttributes']['phone_number'][3:] }
    except Exception as e1:
        print(f"Generic errror : {e1}")
    return payload
    
def Preparedata(id,payload,sl_id):
    if id is None or len(id)==0:
        raise Exception("userName is null or empty")
    name = GetId(payload['display_name'])
    data = {'display_name': payload['display_name'],'name':name,'mobile': payload['mobile'],'status': '', 'sl_id' : sl_id,'id': id,'party_type':'U','status':'A',
    'upd_by':payload['display_name'],'upd_on' : datetime.now().strftime('%m-%d-%Y, %H:%M:%S')
    }
    return data