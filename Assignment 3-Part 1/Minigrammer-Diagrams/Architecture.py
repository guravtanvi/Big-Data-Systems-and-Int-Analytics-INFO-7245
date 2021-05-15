from diagrams import Diagram
from diagrams.saas.analytics import Snowflake
from diagrams.aws.storage import S3
from diagrams.programming.framework import Fastapi, FastAPI
from diagrams.saas.identity import Auth0
from diagrams.custom import Custom

with Diagram("Event Processing", show=False):
    cc_csv = Custom("csv file", "./csv.png")
    source = S3("Upload csv to S3")
    download = S3("Download csv from S3")
    ingestion = Snowflake("Snowflake Database")
    api = FastAPI("API Endpoints")
    authentication = Auth0("API Auth")
    cc_test = Custom("Pytest", "./pytest.png")
    cc_locust = Custom("Locust", "./Locust.png")

    cc_csv >> source >> download >> ingestion >> api >> authentication >> cc_test >> cc_locust

