from .getid import GetId
from datetime import datetime 

def Payload_mobibooks(data):
    
    payload ={'display_name' : data['request']['userAttributes']['name'] ,'mobile' : data['request']['userAttributes']['phone_number'][3:],
    'status' : '','party_type': 'U','alias': data['request']['userAttributes']['phone_number'][3:] }
    
    return payload
    
def Preparedata(id,payload,sl_id):
   
    name = GetId(payload['display_name'])
    data = {'display_name': payload['display_name'],'name':name,'mobile': payload['mobile'], 'sl_id' : sl_id,'id': id,'party_type':'U','status':'A',
    'upd_by':payload['display_name'],'upd_on' : datetime.now().strftime('%m-%d-%Y, %H:%M:%S')
    }
    return data