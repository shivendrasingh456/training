import json
from dynamodb import Dynamodb
from datetime import timezone
import datetime

def lambda_handler(event, context):
    try:
        #data storing in dynmaodb
        data=event['arguments']['input']
        data['date']=datetime.datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        
        #putting data in 'Deliverables table using application no(partition key) and date(sort key)'
        tablename='Deliverables'
        a=Dynamodb()
        res=a.putitem(tablename,data)
        
        return data
    except Exception as e:
        raise e