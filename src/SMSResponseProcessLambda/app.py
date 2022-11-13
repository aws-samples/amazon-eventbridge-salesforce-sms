import boto3
import os
import botocore
import json

def lambda_handler(event, context):
      messageJson = json.loads(event['Records'][0]['Sns']['Message'])
      number = messageJson['originationNumber']
      message = messageJson['messageBody']
      
      client = boto3.client('events')
      response = client.put_events(
            Entries=[
                  {
                        'Detail': json.dumps({'PhoneNumber__c': number, 'Message__c': message}),
                        'DetailType': 'smsResponse',
                        'Source': 'com.salesforce.sms'
                  }
            ]
      )

      return {"result":"SUCCEEDED"}
