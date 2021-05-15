import json
import boto3

def lambda_handler(event, context):
    # boto3 S3 initialization
    s3_client = boto3.client("s3",aws_access_key_id ='' ,aws_secret_access_key = '' ,region_name = 'us-east-1')
    destination_bucket_name = 'connect-hist-calls'

    print("Event :", event)

    source_bucket_name = 'amazon-connect-3c22ce0802db'

    file_key_name = event['params']['querystring']['filename']

    copy_source_object = {'Bucket': source_bucket_name, 'Key': file_key_name}


    s3_client.copy_object(CopySource=copy_source_object, Bucket=destination_bucket_name, Key=file_key_name)
    print(file_key_name + " has been copied to " + destination_bucket_name + " bucket!\n")

    s3_client.delete_object(Bucket=source_bucket_name, Key=file_key_name)
    print(file_key_name + " has been deleted from " + source_bucket_name + " bucket!")

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Call moved to historical bucket')
    }
