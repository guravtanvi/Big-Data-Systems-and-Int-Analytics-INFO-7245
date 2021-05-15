#Importing Libraries

import time
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time=between(1,5)

#End dpoints
    @task
    def triggertranscribe(self):
        self.client.get(url="/triggertranscribe?uri={path}&jobname={JobName}")

    @task
    def transcribejobstatus(self):
        self.client.get(url="/jobstatus?jobname={JobName}")

    @task
    def fetchingaddressfromdynamodb(self):
        self.client.get(url="/getaddress?filename={filetonotify}")

    @task
    def sendingnotifications(self):
        self.client.get(url="/notification?audiofile={audiofile}&type={type}")

    @task
    def googleapi(self):
        self.client.get(url="/json?address={address}&key=AIzaSyBWyJXeBhUSMuu9dB7YlMIXFlY0zlr37vg")

    @task
    def readingdatafroms3(self):
        self.client.get(url="/readdata?jobname={JobName}")

    @task
    def geographiclocation(self):
        self.client.get(url="/json?latlng={latitude},{longitude}&key={key}")