import json
import logging
import boto3


def lambda_handler(event, context):
    # TODO implement
    print(event)
    print(event['params']['querystring']["entitylist"])
    s3 = boto3.client('s3', aws_access_key_id='*****************************',
                      aws_secret_access_key='*********************************')
    comprehend = boto3.client("comprehend")

    try:
        s3.delete_object(Bucket='edgar-dataset', Key='AGEN.txt/.write_access_check_file.temp')
    except:
        print("file not exists")

    response = comprehend.start_pii_entities_detection_job(
        InputDataConfig={
            "S3Uri": event['params']['querystring']["s3uri"],
            "InputFormat": "ONE_DOC_PER_LINE"
        },
        OutputDataConfig={"S3Uri": event['params']['querystring']["outputuri"]},
        Mode="ONLY_REDACTION",
        RedactionConfig={
            "PiiEntityTypes": [event['params']['querystring']["entitylist"]],
            "MaskMode": "MASK",
            "MaskCharacter": "*"
        },
        JobName="assign-test-comprehend",
        LanguageCode="en",
        DataAccessRoleArn="arn:aws:iam::************:role/service-role/AmazonComprehendServiceRole-newcomprehend",
    )
    print("Uploaded in S3")
    return {
        'statusCode': 200,
        'body': json.dumps("Loading masked data in S3")
    }

