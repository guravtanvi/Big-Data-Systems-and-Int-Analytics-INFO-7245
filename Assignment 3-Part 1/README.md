## Big Data Systems and Int Analytics
 
## Assignment 3

#### Team Information

| NAME              |     NUID        |
|------------------ |-----------------|
|   Tanvi Gurav     |   001306848     |
|   Keerti Ojha     |   001050173     |
| Priyanka Malpekar |   001302741     |
 

**Submission Date**: 2nd April'21


### CLAAT Link

https://codelabs-preview.appspot.com/?file_id=1jTHf8qaN4N300bceYkY12fPi7ERu2TbfQh8D3kCbA0w#1

## About

**Moody's Analytics** provides financial intelligence and analytical tools to help business leaders make better, faster decisions. It provides a robust set of APIs that enable users to interact with their economic and credit solutions.

**How do they Work?**

* Moody Analytics provides various API's as per the requirements of the applications
* Create a developer account -> Register an App -> Provides API key to access the API's
* In order to access the API's an access code is required which authorizes the user.
* New Apps can be created and accessed by using the Promo Code
* API's are displayed in an interactive swagger UI which assist in understanding the various API methods

## Dataset

**Lending Club  Datasets**

We are using two csv’s for our implementation viz:

* Lending_club_info.csv
* Lending_club_loan_two.csv

Kaggle Link to Dataset: https://www.kaggle.com/hadiyad/lendingclub-data-sets

## Architecture

**Moody Architecture**

![moody-architecture](https://user-images.githubusercontent.com/59594174/113445641-437bec00-93c4-11eb-8f11-4c0550fe650a.png)

**Proposed Architecture**

![Architecture](https://user-images.githubusercontent.com/59594174/113439421-889a2100-93b8-11eb-8ddf-de5ca21af2c6.png)

#### Note: Install `requirements.txt` before replicating the project

## Task 1: Data Ingestion - Airflow

Analyzing the raw data before ingestion using **XSV** for getting an insight on different aspects like number of columns, count of rows in each csv and over stats of the files.

1. Uploading data to S3
2. Downlaoding Data
3. Ingesting data in Snowflake database

**Reference Folder: Data-Ingestion-Airflow/**

Download the dags folder, file `Data-Ingestion-Airflow/dags/ingestion-airflow.py` contains the airflow logic. Once below commands are executed, access the Airflow UI by visiting http://127.0.0.1:8080/home on your browser.
```
# Use your present working directory as
# the airflow home
export AIRFLOW_HOME=~(pwd)

# export Python Path to allow use
# of custom modules by Airflow
export PYTHONPATH="${PYTHONPATH}:${AIRFLOW_HOME}"


# initialize the database
airflow db init

airflow users create \
    --username admin \
    --firstname <YourName> \
    --lastname <YourLastName> \
    --role Admin \
    --email example@example.com
    
 airflow webserver -D
 
 airflow scheduler
 ```

![Airflow](https://user-images.githubusercontent.com/59594174/113439427-8b951180-93b8-11eb-9c0d-0bc6a2153fe3.png)

Alternatively, you can also run Airflow from Windows using Docker.
Reference file: `Data-Ingestion-Airflow/dags/airflow-docker.py`, `Data-Ingestion-Airflow/Docker`, `Data-Ingestion-Airflow/docker-compose.yml`
Execute the commnad `docker-compose up --build` where `docker-compuse.yml` is located. Once the webserver is up and running access http://127.0.0.1:8080/home on your browser to see DAG `Windows-Pipeline` on the console

![image](https://user-images.githubusercontent.com/59846364/113449984-01a37380-93cd-11eb-8035-3e17fb853680.png)


## Task 2: FastAPI

**Reference Folder: FastApi-Authentication-Pytest/**

1. `api.py`: Contains logic for all the developing the api. Execute the file using command `uvicorn api:app --reload` and access it on browser using `http://localtest.me:8000/`. Explore the various end points by accessing the swaggerUI through `http://localtest.me:8000/documentation?access_token=1234567asdfgh`
2. `snowflakecfg`: Configuration file for Snowflake credentials. Replace with your own snowflake credentials before replicating the project
3. `test_api.py`: Contains logic for performing unit test on our designed API. Execute the same using command `pytest`

## Designing FastAPI

![FastAPI](https://user-images.githubusercontent.com/59594174/113440163-dcf1d080-93b9-11eb-951d-7fcdc1805125.png)

## Task 3: API Key Authentication

![Auth1](https://user-images.githubusercontent.com/59594174/113440173-e1b68480-93b9-11eb-80bd-a4d45b9d19f4.png)


![Auth2](https://user-images.githubusercontent.com/59594174/113440182-e54a0b80-93b9-11eb-9057-5617bf7c20bc.png)


![Auth3](https://user-images.githubusercontent.com/59594174/113440186-e7ac6580-93b9-11eb-872b-eb1308e57c22.png)

## Task 4: Pytest & Locust 

![Pytest](https://user-images.githubusercontent.com/59594174/113440194-ed09b000-93b9-11eb-84d6-597b20ad4514.png)

## Locust

**Reference Folder: Locust/**

Execute command `locust -f locus-Final.py`. This will start the locust console on `http://127.0.0.1:8089` in the browser

**Locust UI**

![Locust1](https://user-images.githubusercontent.com/59594174/113439437-92238900-93b8-11eb-9ae7-714f98426c0a.png)

**Testing our end-points in Locust**

![Locust2](https://user-images.githubusercontent.com/59594174/113439441-951e7980-93b8-11eb-90f4-aa7b0d152a47.png)


## Streamlit

**Reference Folder: Streamlit/**

The Streamlit application pulls the data from the live FastApi and validates authentication configured. Hence, make sure that the FastApi is active before starting Streamlit execution.

Command to start the app:  `streamlit run streamlit-app.py`

![ezgif com-gif-maker (2)](https://user-images.githubusercontent.com/59846364/113446744-7921d480-93c6-11eb-8bd6-3f181ea88372.gif)



## References
* https://medium.com/data-rebels/fastapi-authentication-revisited-enabling-api-key-authentication-122dc5975680
* https://ma.moodys.com/2020_9_AMER_EBU_PortalIntroductionandAPILibraryOverview_WebTel_MAU12329_ThankYou.html
* https://github.com/mingrammer/diagrams
* https://fastapi.tiangolo.com/tutorial/
* https://www.kaggle.com/hadiyad/lendingclub-data-sets

