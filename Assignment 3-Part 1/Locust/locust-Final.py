#Importing Libraries
import time
from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time=between(1,5)

#Endpoints
    @task
    def documentation_page(self):
        self.client.get(url="/documentation")

    @task
    def secure_endpoint_page(self):
        self.client.get(url="/secure_endpoint")

    @task
    def login_page(self):
        self.client.get(url="/login")

    @task
    def login_data_page(self):
        self.client.get(url="/login_data")

    @task
    def verification_details_page(self):
        self.client.get(url="/verification_details")

    @task
    def purpose_page(self):
        self.client.get(url="/purpose")

    @task
    def loan_amount_page(self):
        self.client.get(url="/loan_amount")

    @task
    def ownership_income_page(self):
        self.client.get(url="/ownership_income")

    @task
    def get_count_page(self):
        self.client.get(url="/get_count")

    @task
    def logout_page(self):
        self.client.get(url="/logout")




