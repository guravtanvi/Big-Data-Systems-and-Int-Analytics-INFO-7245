import pytest
import logging
import requests
import json
from fake_useragent import UserAgent

ua = UserAgent()

logger = logging.getLogger(__name__)

# Replace the API Gateway URL with your own
# Deploy the API in /dev
API_GATEWAY_URL = "https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/dev/"

# Note: Make sure to include ?testing=true in the URL

# ---------------------------------------------------------------------------------------
# Blackbox Test 1: Endpoint /getaddress
# Context: Test the API gateway if empty filename is passed to get address from dynamodb
# ---------------------------------------------------------------------------------------
def test_api_gateway_getaddress_emptyfile():
    url_to_test = API_GATEWAY_URL + "getaddress?testing=true&filename="
    logger.info(f"url: {url_to_test}")
    response = requests.get(url_to_test, headers={"User-Agent": ua.chrome})
    logger.info(
        f"the response error code is {response.status_code}\n" f"the json of the response is {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 400
    assert response.json() == {'message': 'Missing required request parameters: [filename]'}
    assert response.json()["message"] == "Missing required request parameters: [filename]"


# ---------------------------------------------------------------------------------------
# Blackbox Test 2: Endpoint /getaddress
# Context: Test the API gateway if valid filename is passed to get address from dynamodb
# ---------------------------------------------------------------------------------------
def test_api_gateway_getaddress_validfile():
    url_to_test = API_GATEWAY_URL + "getaddress?testing=true&filename=b6e3b801-e652-49a0-9219-b4c94496199d_20210422T18_52_UTC"
    logger.info(f"url: {url_to_test}")
    response = requests.get(url_to_test, headers={"User-Agent": ua.chrome})
    logger.info(
        f"the response error code is {response.status_code}\n" f"the json of the response is {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200
    assert response.json()["body"]["Item"]["location"]["S"] == "29 Queensberry Street"


# ---------------------------------------------------------------------------------------
# Blackbox Test 3: Endpoint /jobstatus
# Context: Test the API gateway if empty jobname is passed to the job status
# ---------------------------------------------------------------------------------------
def test_api_gateway_jobstatus_emptyjob():
    url_to_test = API_GATEWAY_URL + "jobstatus?testing=true&jobname="
    logger.info(f"url: {url_to_test}")
    response = requests.get(url_to_test, headers={"User-Agent": ua.chrome})
    logger.info(
        f"the response error code is {response.status_code}\n" f"the json of the response is {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 400
    assert response.json() == {'message': 'Missing required request parameters: [jobname]'}
    assert response.json()["message"] == "Missing required request parameters: [jobname]"

# ---------------------------------------------------------------------------------------
# Blackbox Test 4: Endpoint /jobstatus
# Context: Test the API gateway if valid jobname is passed to get the job status
# ---------------------------------------------------------------------------------------
def test_api_gateway_jobstatus_validjob():
    url_to_test = API_GATEWAY_URL + "jobstatus?testing=true&jobname=b6e3b801-e652-49a0-9219-b4c94496199d_20210422T18_52_UTC"
    logger.info(f"url: {url_to_test}")
    response = requests.get(url_to_test, headers={"User-Agent": ua.chrome})
    logger.info(
        f"the response error code is {response.status_code}\n" f"the json of the response is {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200
    assert response.json() == {"body": "COMPLETED"}
    assert response.json()["body"] == "COMPLETED"


# ---------------------------------------------------------------------------------------
# Blackbox Test 5: Endpoint /jobstatus
# Context: Test the API gateway if non-existent jobname is passed to get the job status
# ---------------------------------------------------------------------------------------
def test_api_gateway_jobstatus_invalidjob():
    url_to_test = API_GATEWAY_URL + "jobstatus?testing=true&jobname=b6e3b801"
    logger.info(f"url: {url_to_test}")
    response = requests.get(url_to_test, headers={"User-Agent": ua.chrome})
    logger.info(
        f"the response error code is {response.status_code}\n" f"the json of the response is {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200
    assert response.json() == {"errorMessage": "An error occurred (BadRequestException) when calling the GetTranscriptionJob operation: The requested job couldn't be found. Check the job name and try your request again.", "errorType": "BadRequestException", "stackTrace": ["  File \"/var/task/lambda_function.py\", line 6, in lambda_handler\n    TranscriptionJobName=event['params']['querystring']['jobname']\n", "  File \"/var/runtime/botocore/client.py\", line 357, in _api_call\n    return self._make_api_call(operation_name, kwargs)\n", "  File \"/var/runtime/botocore/client.py\", line 676, in _make_api_call\n    raise error_class(parsed_response, operation_name)\n"]}
    assert response.json()["errorType"] == "BadRequestException"


# ---------------------------------------------------------------------------------------
# Blackbox Test 6: Endpoint /readdata
# Context: Test the API gateway if empty jobname is passed to read transcribed text
# ---------------------------------------------------------------------------------------
def test_api_gateway_readdata_emptyjob():
    url_to_test = API_GATEWAY_URL + "readdata?testing=true&jobname="
    logger.info(f"url: {url_to_test}")
    response = requests.get(url_to_test, headers={"User-Agent": ua.chrome})
    logger.info(
        f"the response error code is {response.status_code}\n" f"the json of the response is {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 400
    assert response.json() == {'message': 'Missing required request parameters: [jobname]'}
    assert response.json()["message"] == "Missing required request parameters: [jobname]"


# ---------------------------------------------------------------------------------------
# Blackbox Test 7: Endpoint /readdata
# Context: Test the API gateway if invalid jobname is passed to read transcribed text
# ---------------------------------------------------------------------------------------
def test_api_gateway_readdata_invalidjob():
    url_to_test = API_GATEWAY_URL + "readdata?testing=true&jobname=b6e3b801"
    logger.info(f"url: {url_to_test}")
    response = requests.get(url_to_test, headers={"User-Agent": ua.chrome})
    logger.info(
        f"the response error code is {response.status_code}\n" f"the json of the response is {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200
    assert response.json() == {"errorMessage": "local variable 'text' referenced before assignment", "errorType": "UnboundLocalError", "stackTrace": ["  File \"/var/task/lambda_function.py\", line 15, in lambda_handler\n    'body': text['results']['transcripts'][0]['transcript']\n"]}
    assert response.json()["errorMessage"] == "local variable 'text' referenced before assignment"


# ---------------------------------------------------------------------------------------
# Blackbox Test 8: Endpoint /readdata
# Context: Test the API gateway if valid jobname is passed to read transcribed text
# ---------------------------------------------------------------------------------------
def test_api_gateway_readdata_validjob():
    url_to_test = API_GATEWAY_URL + "readdata?testing=true&jobname=b6e3b801-e652-49a0-9219-b4c94496199d_20210422T18_52_UTC"
    logger.info(f"url: {url_to_test}")
    response = requests.get(url_to_test, headers={"User-Agent": ua.chrome})
    logger.info(
        f"the response error code is {response.status_code}\n" f"the json of the response is {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200
    assert response.json() == {"body": "Yeah. Hello, this is, this is uh there's an emergency. This is at uh 29 Queensberry Street. There's a medical emergency and we need an ambulance right now. Yeah."}


# ---------------------------------------------------------------------------------------
# Blackbox Test 9: Endpoint /triggertranscribe
# Context: Test the API gateway if valid jobname is passed to read transcribed text
# ---------------------------------------------------------------------------------------
def test_api_gateway_triggertranscribe_invalidparam():
    url_to_test = API_GATEWAY_URL + "triggertranscribe?testing=true&uri=&jobname="
    logger.info(f"url: {url_to_test}")
    response = requests.get(url_to_test, headers={"User-Agent": ua.chrome})
    logger.info(
        f"the response error code is {response.status_code}\n" f"the json of the response is {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 400
    assert response.json() == {'message': 'Missing required request parameters: [uri, jobname]'}
    assert response.json()["message"] == "Missing required request parameters: [uri, jobname]"


# ---------------------------------------------------------------------------------------
# Blackbox Test 10: Endpoint /triggertranscribe
# Context: Test the API gateway if valid method type is mentioned
# ---------------------------------------------------------------------------------------
def test_api_gateway_triggertranscribe_badreq():
    url_to_test = API_GATEWAY_URL + "triggertranscribe?testing=true&uri=&jobname="
    logger.info(f"url: {url_to_test}")
    response = requests.post(url_to_test, headers={"User-Agent": ua.chrome})
    logger.info(
        f"the response error code is {response.status_code}\n" f"the json of the response is {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 403
    assert response.json() == {"message":"Missing Authentication Token"}
    assert response.json()["message"] == "Missing Authentication Token"


# ---------------------------------------------------------------------------------------
# Blackbox Test 11: Endpoint /notification
# Context: Test the API gateway if valid method type is mentioned
# ---------------------------------------------------------------------------------------
def test_api_gateway_notification_badreq():
    url_to_test = API_GATEWAY_URL + "notification?testing=true&audiofile=&type="
    logger.info(f"url: {url_to_test}")
    response = requests.post(url_to_test, headers={"User-Agent": ua.chrome})
    logger.info(
        f"the response error code is {response.status_code}\n" f"the json of the response is {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 403
    assert response.json() == {"message":"Missing Authentication Token"}
    assert response.json()["message"] == "Missing Authentication Token"


# ---------------------------------------------------------------------------------------
# Blackbox Test 12: Endpoint /notification
# Context: Test the API gateway if empty parameters are send while sending out notification
# ---------------------------------------------------------------------------------------
def test_api_gateway_notification_invalidtype():
    url_to_test = API_GATEWAY_URL + "notification?testing=true&audiofile=&type="
    logger.info(f"url: {url_to_test}")
    response = requests.get(url_to_test, headers={"User-Agent": ua.chrome})
    logger.info(
        f"the response error code is {response.status_code}\n" f"the json of the response is {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 400
    assert response.json() == {"message": "Missing required request parameters: [type]"}
    assert response.json()["message"] == "Missing required request parameters: [type]"