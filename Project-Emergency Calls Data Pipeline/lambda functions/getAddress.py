import json
import boto3

def getitem(audiofile):
    dynamodb = boto3.client('dynamodb',aws_access_key_id ='' ,aws_secret_access_key = '' ,region_name = 'us-east-1')
    response = dynamodb.get_item(TableName='911emergencycalls', Key={'audiofile': {'S': audiofile}})

    # address = response['Item']['location']['S']
    # type = response['Item']['type']['S']
    return response
    
def lambda_handler(event, context):
    print(event['params']['querystring']['filename'])
    response=getitem(event['params']['querystring']['filename'])
    # TODO implement
    return {
        'statusCode': 200,
        'body': response
    }