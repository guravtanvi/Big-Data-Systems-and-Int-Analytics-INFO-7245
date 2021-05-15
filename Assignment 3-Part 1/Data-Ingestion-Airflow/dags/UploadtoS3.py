import boto3
from datetime import datetime
import os


def upload_models():
    import boto3
    from datetime import datetime
    import os
    #Connect to Boto3
    s3 = boto3.resource(
        service_name='s3',
        region_name='us-east-1')


    #Replace this with your S3 Bucket
    bucket_name = 'lending-club-ass3'
    print(bucket_name)

    model_files = [os.path.abspath(os.path.join(os.path.dirname(__file__), '.','dataset', 'lending_club_info.csv')),
                   os.path.abspath(os.path.join(os.path.dirname(__file__), '.','dataset', 'lending_club_loan_two.csv'))]
    print(model_files)

    for file in model_files:
        #print(file)
        s3.Bucket(bucket_name).upload_file(Filename=file,
                                            Key='data/' + datetime.today().strftime(
                                                '%Y-%m-%d-%H:%M:%S') + '_' + os.path.basename(file))
    print('Upload Complete')

upload_models()

