## Big Data Systems and Int Analytics

## Assignment1

#### Team Information

| NAME              |     NUID        |
|------------------ |-----------------|
|   Tanvi Gurav     |   001443824     |
|   Keerti Ojha     |   001050173     |
| Priyanka Malpekar |   001302741     |
 
 Submission Date: 4th March'21

#### Data Pipeline in AWS

#### CLAAT Link

https://codelabs-preview.appspot.com/?file_id=1FmkLOCi61pkc1FG695ZvLO8oxSu-EfqBIaazIRPfew0#0

## About

**Implementing a data pipeline of SEVIR and Storm Events using Amazon Web Services S3 bucket for storage,
Amazon Glue for ETL and Amazon Quicksight for Visualization and Dashboard creation.**

![AWS_Architecture](https://user-images.githubusercontent.com/59594174/110067698-3ecf0400-7d42-11eb-8111-ef37d95e4114.PNG)

## Requirements

1. Configuring Apache Airflow to upload data files in S3 bucket

2. Configuring AWS Glue to create pipeline

3. Adding Glue Crawlers for each dataset to create table in Glue Data Catalog

5. Creating Jobs in AWS Glue Studio and configuring Job Details for running the job

6. Creating Quicksight account for Visulization

7. Configuring Dataset in AWS QuickSight

## Test Results

#### Creating script to upload data in S3 bucket using "Boto3" in Apache Airflow

- exceuted **Sevir Pipeline** in DAG Console

#### Data Preprocessing and Transformation in Glue

**AWS Glue** is a serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development.

- Created a new Glue Database
- Added Glue Crawlers and executed them to access data from S3 bucket in Glue Data Catalog Table
- Created ETL Jobs in Glue Studio to clean, rename columns, drop columns, create a new column, join the two Data Catalog tables
- Provided the target path of the ETL jobs as S3 bucket
- Configured ETL Jobs and provided IAM role with Glue ServiceRole access for execution

```
1. Combined Storm Event Details 2018 data with Storm Events Fatality 2018 data
2. Transformed Sevir Metadata(Catalog) and added a new ID column excluding character in dataset
3. Used the new ID column of Sevir data to join with Storm Event Details

```

#### Data Query Using Athena and Visualization in Quicksight

**Athena** is used to query the dataset created in AWS Glue Data Catalog

**Amazon QuickSight** is a scalable, serverless, embeddable, machine learning-powered business intelligence (BI) service built for the cloud. 
QuickSight lets you easily create and publish interactive BI dashboards that include Machine Learning-powered insights.

- Loaded the dataset in Quicksight deom S3 bucket storage
- Uploaded manifest.json file with the location of the S3 bucket folder
- We can create the Dashboard in the Analysis console of Quicksight

```
1. Combined Sevir Metadata(catalogue) with Storm Events Details 2018 Dashboard
- Showing count of image-types(vis,vil,ir069,ir107,lght) County wise
- Sum of injuries by State distributed by timezones
- Magnitude of event by State and Event Type
- Showing datewise, idwise, count of image types

2. Combined Storm Event Details 2018 and Storm Events Fatality 2018 dashboard
- Sum of deaths by year and state
- Sum of deaths by Event Type
- Sum of deaths by Sex and County
- Damaged Property by state

```

## GCP

## SEVIR Data Pipelining Using Google Cloud Platform

We have implemented a data pipeline using different GCP components, Google Cloud Storage, Datalab, Apache Beam, Dataflow, Google Bigquery and Google Data Studio. The following is the data architecture for implementing a pipeline on Google Cloud Platform:

![GCP-Architecture-Diagram](https://user-images.githubusercontent.com/59594174/110068476-cec17d80-7d43-11eb-9bec-c541d6bfdb23.png)


## Steps to Regenerate GCP Architecture

1. Download [SEVIR Metadata (CATALOG)](https://s3.console.aws.amazon.com/s3/object/sevir?region=us-west-2&prefix=CATALOG.csv) and Storm Data for [2018](https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/StormEvents_details-ftp_v1.0_d2018_c20201216.csv.gz) and [2019](https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/StormEvents_details-ftp_v1.0_d2019_c20210223.csv.gz)
2. Create a new Project, and enable the `BigQuery`, `AI Platform`, `Cloud Source Repositories`, `Dataflow`, and `Datalab APIs`
3. Create a GCP Bucket and a Bigquery Dataset on your GCP Account.
4. Upload the downloaded CSV files to the created bucket
5. Using Cloud Shell:
    * Project Configuration on Cloud Shell: `gcloud config set project <PROJECT_ID>`
    * Creating Datalab: `datalab create --zone <ZONE_NAME> <DATALAB_NAME>`
    * Launch Datalab `http://localhost:8081/`
6. Upload file `Sevir-GCP-pipeline.ipynb` to Datalab
7. Replace the Project_ID, bucket path to the CSV files, BigQuery dataset name and run the notebook
8. Navigate to the Datalab Dashboard and monitor the pipeline
9. Validate if the tables are created and data is loaded in the mentioned dataset

#### Lesson Learned
1. Learned to set up a project in Google Cloud and instantiate DataLab from Cloud shell editor using shell commands.
2. Data exploration in Datalab and creating Apache Beam Pipeline using Google Dataflow
3. Drawing visual insights using Google Data Studio


## Snowflake

![Snowflake](https://user-images.githubusercontent.com/59594174/110068095-f6fcac80-7d42-11eb-9218-497c194573da.PNG)

1. Loading sample sevir and storm data in Snowflake database.

2. Querying the database and gaining insights from the database viz:

Top 5 states with maximum deaths
Top 3 reasons of Death
Deaths By Gender

3. Creating relevant Views in the database to combine Sevir and Storm data.

Storm_events_2019
Storm_events_2018
SevirStormData

4. Connecting Snowflake Database ‘Sevir’ with ‘Sql Alchemy’.

Using package **‘snowflake-sqlalchemy’** for querying and accessing data from Snowflake database.

5. Accessing data from snowflake using **‘snowflake connector’**

6. Installing Apache Superset on Oracle Virtual Machine

**Enter the URL in your Browser:- http://127.0.0.1:8088/ to access the application**

User: admin123
Password: admin

7. Connecting snowflake with Apache Superset for visualization

## Airflow

Automating tasks in Snowflake using **Airflow**

1. Connecting SQL ALchemy with Snowflake
2. Joining Sevir and Storm Data

![pasted image 0](https://user-images.githubusercontent.com/59594174/110068774-69ba5780-7d44-11eb-8f05-5dc41b5e0074.png)

## Streamlit

We have implemented a Streamlit app to explore SEVIR Image data and Storm fatalites data

1. Download [SEVIR Metadata (CATALOG)](https://s3.console.aws.amazon.com/s3/object/sevir?region=us-west-2&prefix=CATALOG.csv) and any of the Storm Data from [NOAA Site](https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/)
2. Create a new Pycharm project and replicate `sevir-viz.py` 
3. Install the following packages/libraries:
```
    pip install streamlit
    pip install h5py
    pip install s3fs
    pip install pandas
    pip install matplotlib
```
4. Start the app by running `streamlit run sevir-viz.py` where `sevir-viz.py` is your Python script.

## References & Citation
https://github.com/streamlit/demo-uber-nyc-pickups
https://github.com/streamlit/demo-self-driving
https://docs.streamlit.io/en/stable/tutorial/create_a_data_explorer_app.html
https://www.streamlit.io/gallery

![image](https://user-images.githubusercontent.com/59846364/110069262-6d9aa980-7d45-11eb-81ec-6ee8a3f5afb5.png)

![image](https://user-images.githubusercontent.com/59846364/110069343-96bb3a00-7d45-11eb-8dce-9b4f9c5446d3.png)


## Dashboards

### AWS Dashboard

![Details-Fatality-2018](https://user-images.githubusercontent.com/59594174/110068829-88b8e980-7d44-11eb-8763-35b26129fb3d.png)

![Sevir_Details_2018](https://user-images.githubusercontent.com/59594174/110068840-8fdff780-7d44-11eb-9f4e-1ec0e1f3d5be.png)

### GCP Dashboard

![DeathAnalysisByState](https://user-images.githubusercontent.com/59594174/110068964-c9b0fe00-7d44-11eb-9c03-1f8660eca010.PNG)

### Apache Superset Dashboard

![pasted image 0 (1)](https://user-images.githubusercontent.com/59594174/110068796-78a10a00-7d44-11eb-8c71-80821c1c0934.png)
