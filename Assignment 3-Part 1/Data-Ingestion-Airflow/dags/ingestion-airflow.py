#Importing Libraries
import datetime as dt
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
#from sqlalchemy import create_engine
import os
import boto3
import shutil
import sqlalchemy as sql
import pandas as pd
from sqlalchemy.dialects import registry
import snowflakecfg as cfg

#Initializing
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(0),
    'concurrency': 1,
    'retries': 0,
    'depends_on_past': False,
}


#Function1-Upload files to S3
def upload_files():

    # Connect to Boto3
    s3 = boto3.resource(
        service_name='s3',
        region_name='us-east-1')

    # Replace this with your S3 Bucket name
    bucket_name = 'lending-club-ass3'

    model_files = [os.path.abspath(os.path.join(os.path.dirname(__file__), '.','dataset', 'lending_club_info.csv'))]
                  os.path.abspath(os.path.join(os.path.dirname(__file__), '.','dataset', 'lending_club_loan_two.csv'))]

    for file in model_files:
        # -----------------------------------------------------------------------------------------------
        # Example: upload_file(Filename='/tmp/hello.txt', Key='hello.txt')
        # Filename = C:\Users\Priyanka Malpekar\PycharmProjects\Assignment3\data\lending_club_info.csv
        # Key = lending_club_info.csv
        # -----------------------------------------------------------------------------------------------
        s3.Bucket(bucket_name).upload_file(Filename=file, Key=os.path.basename(file))

    print('Upload Complete!')

#upload_files()

#Function2-Download files

def download_data():
    s3 = boto3.resource('s3')

    # Replace with your bucket name
    bucket_name = s3.Bucket('lending-club-ass3')

    # Replace with the name of the directory on your local where you want to download the data
    path = '/home/priyanka/PycharmProjects/Assignment3/dags/data/'

    # Read all the csv files in the S3 bucket. Note: Make sure the csv are not in any subfolder
    for s3_object in bucket_name.objects.all():

        # s3.object.key is the name of the eg. lending_club_info.csv
        print('Downloading file {}..'.format(s3_object.key))
        filename = s3_object.key
        bucket_name.download_file(s3_object.key, path+filename)
    print('Download Complete!')

# download_data()

#FUction3-Ingesting data to Snowflake
def ingesting_data():

    registry.register('snowflake', 'snowflake.sqlalchemy', 'dialect')

# Setup an SQL Alchemy Engine object
# This will provide a connection pool for Pandas to use later

engine = sql.create_engine(
    'snowflake://{u}:{p}@{a}/{d}/{s}?warehouse={w}&role={r}'.format(
        u=cfg.snowflake["username"],
        p=cfg.snowflake["password"],
        a=cfg.snowflake["region"],
        r=cfg.snowflake["role"],
        d=cfg.snowflake["database"],
        s=cfg.snowflake["schema"],
        w=cfg.snowflake["warehouse"]
    )
)


try:
    # Directory where the downloaded data is present
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'data'))

    for file in os.listdir(data_dir):

        data = pd.read_csv(data_dir+ "/" +file)
        table_name = file[:-4]  # Removing the extension .csv
        data.to_sql(table_name, con=engine, index=False, if_exists='append', chunksize=16000)
        print("Data loaded in table {t}".format(t=table_name))

finally:
    engine.dispose()

#ingesting_data()


# Airflow Pipeline
with DAG('ingestion-pipeline',
         catchup=False,
         default_args=default_args,
         schedule_interval='@once',
         ) as dag:
    t0_start = PythonOperator(task_id='UploadingFiles',
                              python_callable=upload_files)
    t1_start = PythonOperator(task_id='DownloadingData',
                              python_callable=download_data)
    t2_start = PythonOperator(task_id='IngestingData',
                              python_callable=ingesting_data)

t0_start >> t1_start >> t2_start