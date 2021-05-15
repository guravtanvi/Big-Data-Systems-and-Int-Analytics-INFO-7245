import boto3

def download_data():
    s3 = boto3.resource('s3')

    # Replace with your bucket name and download directory
    bucket_name = s3.Bucket('airflow-ingest-data')
    path ='./data/'

    # download file into current directory
    for s3_object in bucket_name.objects.all():
        print('Downloading file {}..'.format(s3_object.key))
        filename = s3_object.key
        bucket_name.download_file(s3_object.key, path+filename)
    print('Download Complete!')

download_data()
