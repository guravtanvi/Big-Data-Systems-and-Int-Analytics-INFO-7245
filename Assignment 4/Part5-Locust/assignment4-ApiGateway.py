#Importing Libraries
import time
from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time=between(1,5)

#End dpoints
    @task
    def access(self):
        self.client.post(url="/{bucket}?file={filetest}")

    @task
    def identifyentities(self):
        self.client.post(url="/identifyentities?uri={s3uri}&entitylist={entityList}&outputuri={outputuri}")

    @task
    def maskentities(self):
        self.client.get(url="/maskentities?s3uri={s3urimasking}&entitylist={entityList}&outputuri={outputuri}")



