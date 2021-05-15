## Big Data Systems and Int Analytics

## Lab8 - Airflow_tfx

#### Team Information

| NAME              |     NUID        |
|------------------ |-----------------|
|   Tanvi Gurav     |   001443824     |
|   Keerti Ojha     |   001050173     |
| Priyanka Malpekar |   001302741     |

#### CLAAT Link

https://codelabs-preview.appspot.com/?file_id=1D1P62udG1BmrV2hgDzfJeGB2yLcQzIf_AKevBEd1nhs#0


## Airflow

This lab demonstrates the functionalities of Airflow to programmatically automate, author, schedule and monitor workflows. 

![pasted image 0 (1)](https://user-images.githubusercontent.com/59594174/111711315-c9733100-8821-11eb-8e2f-afdcf4ee900d.png)

- Airflow is a platform to programmatically automate, schedule and monitor workflows. 
- In Airflow, a DAG – or a Directed Acyclic Graph – is a collection of all the tasks you want to run, organized in a way that reflects their relationships and   dependencies. 
- The Airflow scheduler executes your tasks on an array of workers while following the specified dependencies. 
- Rich command line utilities make performing complex surgeries on DAGs a snap. 
- The rich user interface makes it easy to visualize pipelines running in production, monitor progress, and troubleshoot issues when needed. 



#### Experiment Setup

1. Create a new project and install the required dependencies.

```
pip install apache-airflow.
```
2. export AIRFLOW_HOME - Enter the path of the present working directory

3. Initialize the instance.

```
airflow db init
```

4. Create an admin user.

airflow users create \
    --username admin \
    --firstname YourName \
    --lastname YourLastName \
    --role Admin \
    --email example@example.com

5. Start the Daemon in the background. It usually runs on port 8080.

```
airflow webserver -D
```

6. To check whether Airflow Daemon is running:

List the services running on port 8080

lsof -i tcp:8080 

7. Start the Airflow Scheduler

```
airflow scheduler
```

Once both are running - you should be able to access the Airflow UI by visiting http://127.0.0.1:8080/home on your browser.

8. To kill the Airflow webserver daemon - First list the running processes on port 8080

```
lsof -i tcp:8080  
```

Kill the process by running `kill <PID>`

9. Create folder dags inside AIRFLOW_HOME

10. Place the python file under the ‘dags’ folder.

- Dags can be scheduled and run every minute or hourly/daily
- You can also pause/unpause the dag depending on the requirement

## Use Case - Taxi Pipeline

![pasted image 0 (2)](https://user-images.githubusercontent.com/59594174/111711458-1e16ac00-8822-11eb-8643-50c82341f0d4.png)
