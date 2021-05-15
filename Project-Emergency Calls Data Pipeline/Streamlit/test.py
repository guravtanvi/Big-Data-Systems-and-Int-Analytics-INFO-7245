import json
import boto3

# boto3 S3 initialization
s3_client = boto3.client("s3")

destination_bucket_name = 'aws-connect-hist-calls'

# event contains all information about uploaded object


# Bucket Name where file was uploaded
# source_bucket_name = event['Records'][0]['s3']['bucket']['name']

source_bucket_name = 'aws-connect-live-calls'

# Filename of object (with path)
# file_key_name = event['Records'][0]['s3']['object']['key']

file_key_name = 'train.csv'

# Copy Source Object
copy_source_object = {'Bucket': source_bucket_name, 'Key': file_key_name}

# S3 copy object operation
s3_client.copy_object(CopySource=copy_source_object, Bucket=destination_bucket_name, Key=file_key_name)
print(file_key_name + " has been copied to " + destination_bucket_name + " bucket!\n")
s3_client.delete_object(Bucket=source_bucket_name, Key=file_key_name)
print(file_key_name + " has been deleted from " + source_bucket_name + " bucket!")