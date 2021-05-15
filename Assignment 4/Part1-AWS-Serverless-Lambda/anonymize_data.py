import json
import logging
import boto3


def lambda_handler(event, context):
    # TODO implement
    print(event)
    print(event['params']['querystring']["entitylist"])
    s3 = boto3.client('s3', aws_access_key_id='****************************',
                      aws_secret_access_key='********************************')
    comprehend = boto3.client("comprehend")

    response = comprehend.start_pii_entities_detection_job(
        InputDataConfig={
            "S3Uri": event['params']['querystring']["uri"],
            "InputFormat": "ONE_DOC_PER_LINE"
        },
        OutputDataConfig={"S3Uri": event['params']['querystring']["outputuri"]},
        Mode="ONLY_REDACTION",
        RedactionConfig={
            "PiiEntityTypes": [event['params']['querystring']["entitylist"]],
        },
        JobName="assign-test-comprehend",
        LanguageCode="en",
        DataAccessRoleArn="arn:aws:iam::************:role/service-role/AmazonComprehendServiceRole-newcomprehend",
    )
    print("Uploaded in S3")
    return {
        'statusCode': 200,
        'body': json.dumps("Data loading in S3")
    }
