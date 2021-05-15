import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from sqlalchemy import create_engine
# Imports the modules
#import requests
#from bs4 import BeautifulSoup
import os
import shutil

engine = create_engine(
    'snowflake://{user}:{password}@{account}/{database}/{schema}?warehouse={warehouse_name}&role={role_name}'.format(
        user='***********',
        password='**********',
        account='********.us-east-1',
        database='sevir',
        schema='public',
        warehouse_name='COMPUTE_WH',
        role_name='sysadmin'

    )
)
def snowflake_connect():

    try:
        connection = engine.connect()
        results = connection.execute('select current_version()').fetchall()
        print(results)
    finally:
        connection.close()
        engine.dispose()

def join_sevir_storm():
    try:
        connection = engine.connect()
        results = connection.execute('create table sevir_storm AS (select s.ID,s.FILE_NAME,s.EVENT_ID,s.EVENT_TYPE,s.EPISODE_ID,d.BEGIN_YEARMONTH, d.END_YEARMONTH, d.STATE,d.DEATHS_DIRECT,d.FLOOD_CAUSE from SEVIR_METADATA s JOIN StormEvents_Details_2019 d ON s.EVENT_ID = d.EVENT_ID)').fetchall()
        #print(results)
    finally:
        connection.close()
        engine.dispose()



# DAG Scheduler Tasks

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(0),
    'concurrency': 1,
    'retries': 0,
    'depends_on_past': False,
}

with DAG('snowflake-pipeline',
         catchup=False,
         default_args=default_args,
         schedule_interval='@once',
         ) as dag:
    t0_start = PythonOperator(task_id='SnowflakeConnect',
                              python_callable=snowflake_connect)
    t1_start = PythonOperator(task_id='JoinSevirStorm',
                              python_callable=join_sevir_storm)



t0_start >> t1_start
