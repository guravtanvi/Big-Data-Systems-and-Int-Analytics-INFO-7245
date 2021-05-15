#Importing Libraries
import time
from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time=between(1,5)

#End dpoints
    @task
    def predict_page(self):
        self.client.get(url="/predict")






