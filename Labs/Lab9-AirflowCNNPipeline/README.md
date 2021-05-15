## Big Data Systems and Int Analytics

### Team Information

| NAME              |     NUID        |
|------------------ |-----------------|
|   Tanvi Gurav     |   001306848     |
|   Keerti Ozha     |   001050173     |
| Priyanka Malpekar |   001302741     |


## Lab 9 - Acne Type Classification Pipeline using CNN 

#### CLAAT Link
https://codelabs-preview.appspot.com/?file_id=1CnjVfvr_sCzdwPA1lF4MeIoD4AmcN5XVtOfdC7jY0M0#0

## About

**This lab demonstrates how to create a training pipeline that aims to identify the type of Acne-Rosacea, by training a model with images scraped from dermnet.com with a confidence score. The front-end application uses Streamlit to predict using the trained model.**

![Datapipeline](https://user-images.githubusercontent.com/59594174/111717031-a77fab80-882d-11eb-8339-860b06ca5076.png)


#### Airflow Tasks

- Replace cron jobs: Monitoring cron jobs is hard and tedious. Instead of manually ssh to servers to find out if/why your jobs fail, you can visually see whether your code run or not through the UI and have Airflow notifies you when a job fails.
- Extract data: Airflow, with its many integrations, are used a lot for data engineering tasks. You can write tasks to extract data from your production databases, check data quality, and write the results to your on-cloud data warehouse.
- Transform data: You can interface with external services to process your data. For example, you can have a pipeline that submits a job to EMR to process data in S3 with Spark and writes the results to your Redshift data warehouse.
- Train machine learning models: You can extract data from a data warehouse, do feature engineering, train a model, and write the results to a NoSQL database to be consumed by other applications.
- Crawl data from the Internet: You can write tasks to periodically crawl data from the Internet and write to your database. For instance, you can get daily competitor’s prices or get all comments from your company’s Facebook page.

### Requirements

**Note: This tutorial is performed using Python 3.7.9**

1. Install the packages/libraries by running the `requirements.txt` 
```
pip install -r requirements.txt
```

2. Update S3 Bucket details by adding the S3 bucket name (`bucket_name` parameter) in `s3_uploader/upload_models.py`


3. Once Airflow is successfully installed, proceed with the configuration by executing the following commands

```
# Setting the current working directory as airflow home
export AIRFLOW_HOME=~(pwd)

# Export Python Path to allow use
export PYTHONPATH="${PYTHONPATH}:${AIRFLOW_HOME}"

# Initialization of the database
airflow db init

# User Creation

airflow users create \
    --username admin \
    --firstname YourName \
    --lastname YourLastName \
    --role Admin \
    --email example@example.com
```

4. Start the Airflow server in daemon & Airflow Scheduler

```
airflow webserver -D

airflow scheduler
```

Access the Airflow console from http://127.0.0.1:8080/home

Incase if of any issues or to restart the webserver, first, kill the Airflow webserver daemon using `kill <pid>` where pid can be obtained from below command
```
lsof -i tcp:8080  
```

### Running the Pipeline

Once Airflow is configured, trigger the `CNN-Training-Pipeline` DAG from console and monitor the same


### API Usage

The API endpoints allow the following:
- Starting the Airflow Webserver & Scheduler
- Starting the training pipeline
- Inference

Start the API server by running
```
cd api
uvicorn main:app --reload
```

API Documentation can be viewed by visiting 127.0.0.1:8000/docs


### Using the Streamlit App

We can validate our retrained model by running the streamlit app which calculates the confidence score for its acne condition for each new uploaded images based on the retrained model with scraped images. 

Start the server by running `streamlit run app.py` from your terminal and access the application from http://localhost:8501

![Streamlit1](https://user-images.githubusercontent.com/59594174/111716965-7a32fd80-882d-11eb-952e-b53ad58517e7.png)



![Streamlit2](https://user-images.githubusercontent.com/59594174/111716979-815a0b80-882d-11eb-94c5-695a8ea3fd95.png)


### References

- https://airflow.apache.org/docs/apache-airflow/stable/index.html
- https://medium.com/@dustinstansbury/understanding-apache-airflows-key-concepts-a96efed52b1a
- https://towardsdatascience.com/getting-started-with-airflow-locally-and-remotely-d068df7fcb4
