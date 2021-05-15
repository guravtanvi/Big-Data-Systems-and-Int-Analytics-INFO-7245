import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

# Imports the modules
import requests
#from bs4 import BeautifulSoup
import os
import shutil

# Root URL

#root_URL = 'http://www.dermnet.com/'



# Function to convert images to downloadble link for the images





def upload_models():
    import boto3
    from datetime import datetime
    import os
    # Connect to Boto3
    s3 = boto3.resource(
        service_name='s3',
        region_name='us-east-1')

    # Replace this with your S3 Bucket
    bucket_name = 'sevir-bucket'

    model_files = [os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Sevir_metadata.csv')),
                   os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'StormEvents_details_2018.csv')),
                   os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'StormEvents_details_2019.csv')),
                   os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'StormEvents_fatalities_2018.csv')),
                   os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'StormEvents_fatalities_2019.csv'))]
    for file in model_files:
        print(file)
        s3.Bucket(bucket_name).upload_file(Filename=file,
                                           Key='data/' + datetime.today().strftime(
                                               '%Y-%m-%d-%H:%M:%S') + '_' + os.path.basename(file))
        print('Upload Complete')

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(0),
    'concurrency': 1,
    'retries': 0,
    'depends_on_past': False,
}


with DAG('Sevir-Pipeline',
         catchup=False,
         default_args=default_args,
         schedule_interval='@once',
         ) as dag:
    t0_start = PythonOperator(task_id='UploadModels',
                              python_callable=upload_models)


t0_start