import sys
import json
import datetime
import pybase64


def lambda_handler(event, context):
    datetime_now     = datetime.datetime.now()
    current_datetime = str(datetime_now.strftime("%d-%m-%Y %H:%M:%S"))
    
    if 'body' not in event:
        PAYLOAD = "NOT PROVIDED"
    else:
        PAYLOAD = str(pybase64.b64decode(event['body']),'utf-8')
        
    response = {
        "statusCode": 200,
        "headers"   : { "Content-Type": "application/json" },
        "body": json.dumps({
            "APIVersion": "v1.12345+",
            "Message"   : "AWS Lambda with Docker and Python!",
            "Developer" : "Denis Astahov",
            "Python"    : str(sys.version),
            "TimeStamp" : current_datetime,
            "Payload"   : PAYLOAD
        })
    }

    return response