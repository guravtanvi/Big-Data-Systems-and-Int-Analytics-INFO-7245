import os
import re
import string
import boto3
import flat_table
import sys
import json
import pandas as pd
from pandas.io.json import json_normalize
import time
from sklearn.pipeline import FeatureUnion, Pipeline, make_pipeline
from sklearn import set_config
set_config(display='diagram')
#from sklearn.compose import make_column_transformer
#from sklearn.base import BaseEstimator, TransformerMixin
import luigi
from luigi import contrib
import luigi.contrib.s3
import json
import os
# import urllib3.util.ssl_
# #import requests.packages

#urllib3.util.ssl_requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
import ibm_watson
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, SentimentOptions


class Preprocess_Luigi(luigi.Task):

        def output(self):
            return luigi.LocalTarget("outfile")

        def run(self):
            for files in os.walk("call_transcripts"):
                for filename in files[2]:
                    print(filename)
                    if filename == ".DS_Store":
                        continue
                    else:
                        with open(os.path.join('call_transcripts/', filename)) as infile, open(os.path.join('Clean_data', 'Cleaned_annotation.txt'), 'a') as outfile:
                            for line in infile:
                                if not line.strip(): continue
                                string.punctuation = '!"#&'
                                new_line = ' '.join(word.strip(string.punctuation) for word in line.split())
                                outfile.write(new_line + '\n')  # non-empty line. Write it to output

class uploadtoS3(luigi.Task):

    def requires(self):
        return Preprocess_Luigi()

        # Connect to Boto3

    def output(self):
        s3 = boto3.resource(
            service_name='s3',
            region_name='us-east-1')
        bucket_name = 'clean-data-assign2'
        model_files = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'Clean_data'))


        for files in os.walk(model_files):
            for filename in files[2]:
                path_files = model_files + '/' + filename
                s3.Bucket(bucket_name).upload_file(Filename=path_files, Key='data/' + filename)
        print('Upload Complete')
        return luigi.contrib.s3.S3Target('s3://clean-data-assign2/data/')

class ibmfeatures(luigi.Task):
    def requires(self):
        return uploadtoS3()

    def output(self):
        return luigi.LocalTarget("temp.json")

    def run(self):
        c=0
        authenticator = IAMAuthenticator('EKLHgx0kP2YPgbXIuLhb5LZAvepAjmPitUSpsJoxIGB2')
        natural_language_understanding = NaturalLanguageUnderstandingV1(
            version='2020-08-01',
            authenticator=authenticator)

        # IBM Service URL for your selected region in IBM Cloud
        natural_language_understanding.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/e3f72bb8-213a-482b-84b3-d0b8d0086624')
        with open(os.path.join('Clean_data', 'Cleaned_annotation.txt')) as infile:
            for line in infile:
                    response = natural_language_understanding.analyze(
                        text=line[:-1],
                        features=Features(sentiment=SentimentOptions(targets=[line[:-1]])),
                        language='en').get_result()

                    if os.path.exists('temp.json'):
                        data = json.load(open('temp.json'))

                        # convert data to list if not
                        if type(data) is dict:
                            data = [data]

                        # append new item to data lit
                        data.append(response)

                        # write list to file
                        with open('temp.json', 'w') as outfile:
                            json.dump(data, outfile)

                    else:
                        with open('temp.json', 'w') as temp_file:
                            json.dump(response, temp_file)

class jsontocsv(luigi.Task):
    def requires(self):
        return ibmfeatures()

    def output(self):
        return luigi.LocalTarget("labeled_data.csv")

    def run(self):
        data = json.load(open("temp.json"))
        df = json_normalize(data)
        table = flat_table.normalize(df)
        table.to_csv("labeled_data.csv", index=False)

class csvtos3(luigi.Task):
    def requires(self):
        return jsontocsv()

    def output(self):
     s3 = boto3.resource(
        service_name='s3',
        region_name='us-east-1')
     bucket_name = 'clean-data-assign2'
     path_files = 'labeled_data.csv'
     s3.Bucket(bucket_name).upload_file(Filename=path_files, Key='labeled-data/' + 'labeled_data.csv')
     print('Upload Complete')
     return luigi.contrib.s3.S3Target('s3://clean-data-assign2/labeled-data/')
















