## Big Data Systems and Int Analytics
 
## Assignment 4

#### Team Information

| NAME              |     NUID        |
|------------------ |-----------------|
|   Tanvi Gurav     |   001306848     |
|   Keerti Ojha     |   001050173     |
| Priyanka Malpekar |   001302741     |
 

**Submission Date**: 16th April'21


## CLAAT Link

https://codelabs-preview.appspot.com/?file_id=1WyL7lPodRg0nSyOGtHt-9u56J0Ni0m47SBC1Gkgrd68#0

## About

The aim of this assignment is creating an API that anonymizes the data through masking using AWS comprehend and step functions, build a sentiment analysis model and generate sentiments using Albert, then using FAST API to serve the model, dockerize the API and then building a reference app in Streamlit. Demonstrating test cases using Pytest and performing load testing using Locust.


## Dataset

Dataset provided to us was the scraped data from **Edgar datasets**.

It consisted of financial data of 50 companies.

## Architecture

![ass4 (4)](https://user-images.githubusercontent.com/59594174/115077185-a2b12480-9ecb-11eb-862b-5a9f8b2fe3b1.png)

## Requirements

- Python 3.7+
- Signup for an AWS Account [here](https://portal.aws.amazon.com/billing/signup#/start).
- Install the `requirements.txt` file with command `pip install -r requirements.txt`
- Configure AWS CLI 
  * Open command line tool of choice on your machine and run `aws configure`. Enter your access and secret access keys and leave the default region name and output format as null. 

    ```
    $ aws configure
    AWS Access Key ID [None]: <access-key-from-aws-account>
    AWS Secret Access Key [None]: <secret-access-key-from-aws-account>
    Default region name [None]: 
    Default output format [None]: json
    ```


## Setup

### Creating the API's using AWS services

**Reference File: Part1-AWS-Serverless-Lambda/**

* Create three lambda functions each having different use case from the reference folder
  * Lambda1: Accessing data from S3 bucket
  * Lambda2: Named Entity Recognition using AWS comprehend
  * Lambda3: Mask/Anonymize Data using AWS comprehend


## TensorFlow model using TensorFlow Extended (TFX)

**Reference File: Part2-TFX/TFX_Pipeline_for_Bert_Preprocessing.ipynb**

* Use the reference colab notebook to train the pretrained albert model on IMDB reviews dataset from Tensorflow Hub. Save the model to the S3 bucket and google drive


![ARch2](https://user-images.githubusercontent.com/59594174/115078006-fc661e80-9ecc-11eb-9971-0ce15adf4761.png)


## Serve the model as a FastAPI

**Reference File: Part3-FastApi-Pytest-Docker/**

* Run the `download-model.py` to download the model under `/model` folder
* Once the model is downloaded we are ready to server the model as a FastApi using docker

![FastAPI1](https://user-images.githubusercontent.com/59594174/115078155-2ddeea00-9ecd-11eb-821a-de8ac9701da3.png)


**Predicting the Sentiments:**


![FastAPI2](https://user-images.githubusercontent.com/59594174/115078167-3505f800-9ecd-11eb-946b-d88c590a3f91.png)


### Dockerize the FastApi service

**Reference File: Part3-FastApi-Pytest-Docker/Docker**

* Navigate to the project directory and build the docker image `docker build -t <image_name> .`
* Run the container on port 8000 `docker run -d --name <container_name> -p 80:80 <image_name>`
* You can access the Swagger UI on http://127.0.0.1/docs


![DOcker](https://user-images.githubusercontent.com/59594174/115077630-60d4ae00-9ecc-11eb-96b1-4659ea761d26.png)


## Pytest  

**Reference File: Part3-FastApi-Pytest-Docker/test_fastapi.py**

From the terminal run command `pytest` to check if all test cases written are passed

![Pytest](https://user-images.githubusercontent.com/59594174/115077738-8e215c00-9ecc-11eb-89e7-a10a9f260658.png)


## Locust

Load testing on FastApi endpoints: `locust -f assignment4-FastApi.py`

Load testing on AWS Api Gateway endpoints: `locust -f assignment4-ApiGateway.py`

This will start the locust console on http://127.0.0.1:8089 in the browser

**Locust UI**

![Locust](https://user-images.githubusercontent.com/59594174/115077432-09364280-9ecc-11eb-9397-3c31717e586d.png)

**Testing our end-points in Locust**


![Locust1](https://user-images.githubusercontent.com/59594174/115077350-e60b9300-9ecb-11eb-8bdd-d1c07b77a286.png)


![Locust2](https://user-images.githubusercontent.com/59594174/115077359-ea37b080-9ecb-11eb-9c87-ba54da8b87b7.png)


## Streamlit

**Reference Folder: Streamlit/**

* Run the streamlit app using command `streamlit run app.py`
* You can access the app from your browser on https://localhost:8501

![ezgif com-gif-maker](https://user-images.githubusercontent.com/59594174/115085461-941d3a00-9ed8-11eb-94fb-0436c9ab5d49.gif)



## References
* https://curiousily.com/posts/deploy-bert-for-sentiment-analysis-as-rest-api-using-pytorch-transformers-by-hugging-face-and-fastapi/
* https://blog.tensorflow.org/2020/03/part-1-fast-scalable-and-accurate-nlp-tensorflow-deploying-bert.html
* https://blog.tensorflow.org/2020/06/part-2-fast-scalable-and-accurate-nlp.html
* https://tfhub.dev/google/albert_base/3
* https://testdriven.io/blog/fastapi-streamlit/
* https://medium.com/python-data/how-to-deploy-tensorflow-2-0-models-as-an-api-service-with-fastapi-docker-128b177e81f3
* https://fastapi.tiangolo.com/deployment/docker/


