import boto3
import config

def download():
    s3 = boto3.resource('s3', aws_access_key_id =config.aws["secret_id"] ,aws_secret_access_key = config.aws["access_key"],region_name=config.aws["region"])

    # Replace with your bucket name and download directory
    bucket_name = s3.Bucket('connect-hist-calls')
    path = './data/'

    # Download file into your download directory (/data)
    for s3_object in bucket_name.objects.all():
        file_path = s3_object.key
        filename = file_path.split("/")[6]
        filename=filename.replace(":","_")
        bucket_name.download_file(file_path, path + filename)
    return

def download_live():
    s3_live = boto3.resource('s3', aws_access_key_id=config.aws["secret_id"], aws_secret_access_key=config.aws["access_key"],region_name=config.aws["region"])

    # Replace with your bucket name and download directory
    bucket_name_live = s3_live.Bucket('amazon-connect-3c22ce0802db')
    path = './live_data/'

    # Download file into your download directory (/data)
    for s3_object in bucket_name_live.objects.all():
        file_path = s3_object.key
        filename = file_path.split("/")[6]
        filename = filename.replace(":", "_")
        bucket_name_live.download_file(file_path, path + filename)
    return
