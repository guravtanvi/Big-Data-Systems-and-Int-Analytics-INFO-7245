import json
import boto3
def lambda_handler(event, context):
    transcribe = boto3.client('transcribe',aws_access_key_id ='' ,aws_secret_access_key = '' ,region_name = 'us-east-1')
    print(event)
    job_uri = event['params']['querystring']['uri']
    job_name = event['params']['querystring']['jobname']
    print(job_uri)

    response=transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={'MediaFileUri': job_uri},
    MediaFormat='wav',
    LanguageCode='en-US',
    OutputBucketName='transcribe-audiototext1')
    print(response)
    # TODO implement
    return {
    'statusCode': 200,
    'body': json.dumps("success")
    }
