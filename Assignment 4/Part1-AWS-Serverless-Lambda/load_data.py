import json
import boto3


def lambda_handler(event, context):
    bucket_name = event['params']['path']['bucket']
    file = event['params']['querystring']['file']
    print(bucket_name, file)
    s3 = boto3.resource('s3')

    obj = s3.Object(bucket_name, file)
    body = obj.get()['Body'].read()

    return {
        'statusCode': 200,
        'body': json.loads(json.dumps(body, default=str))
    }

