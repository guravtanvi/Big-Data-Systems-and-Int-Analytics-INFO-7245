import json
import boto3


def lambda_handler(event, context):
    sns = boto3.client("sns",region_name="us-east-1",aws_access_key_id="",aws_secret_access_key="")

    def getitem(audiofile):
        dynamodb = boto3.client('dynamodb', aws_access_key_id="",
                                    aws_secret_access_key="", region_name="us-east-1")
        response = dynamodb.get_item(TableName='911emergencycalls', Key={'audiofile': {'S': audiofile}})
        if response['Item']['victim_name']['S'] == "":
            callername = "Not Mentioned"
        else:
            callername = response['Item']['victim_name']['S']
        if response['Item']['location']['S'] == "":
            address = "Not Mentioned"
        else:
            address = response['Item']['location']['S']
        if response['Item']['type']['S'] == "":
            emergency = "Not Mentioned"
        else:
            emergency = response['Item']['type']['S']
        if response['Item']['description']['S'] == "":
            desc = "Not Mentioned"
        else:
            desc = response['Item']['description']['S']

            
        message="Help Needed" + '\n' + "Caller's Name" + " - " + callername + '\n' + "Address" + " - " + address + '\n' + "Type of Emergency" + " - " + emergency + '\n' + "Contact Number" + " - " +response['Item']['contact']['S'] + '\n' + "Description" + " - " + desc + '\n' + "Resolved" + " - " +response['Item']['resolved']['S'] + '\n' + "Lattitude" + " - " + response['Item']['lattitude']['S'] + '\n' + "Longitude" + " - " + response['Item']['longitude']['S']
        print(message)
        return  message
            
    # Publish to topic
    if event['params']['querystring']['type']=="Crime":
        response=sns.publish(TopicArn="arn:aws:sns:us-east-1:535502946823:emergency_calls_crime",
            Message=str(getitem(event['params']['querystring']['audiofile'])),
            Subject="Crime Emergency")

    if event['params']['querystring']['type']=="Medical":
        response=sns.publish(TopicArn="arn:aws:sns:us-east-1:535502946823:emergency_calls_medical",
            Message=str(getitem(event['params']['querystring']['audiofile'])),
            Subject="Medical Emergency")
            
    if event['params']['querystring']['type']=="Fire":
       sns.publish(TopicArn="arn:aws:sns:us-east-1:535502946823:emergency_calls_fire",
           Message=str(getitem(event['params']['querystring']['audiofile'])),
           Subject="Fire Emergency")

    #Send a single SMS
    sns.publish(PhoneNumber="+18573831137",
    Message=str(event['params']['querystring']['audiofile']),
    Subject="Hello")

    
    print("Email sent")    
    return {
        'statusCode': 200,
        'body': response
    }

