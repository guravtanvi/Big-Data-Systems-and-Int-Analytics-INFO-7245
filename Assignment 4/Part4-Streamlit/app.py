import json,requests, random, time, streamlit as st, numpy as np, pandas as pd

import boto3


st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

chosenRadioButton = st.sidebar.radio(
    "Services Provided",
    ("Authentication","Load the Data","Anonymize Data","Masking","Sentiment Prediction")
)
global authValueFlag
authValueFlag = False
currentFunction =""

if chosenRadioButton == 'Authentication':
        usrname = st.text_input('Username')
        password = st.text_input('Password')
        email = st.text_input('Email')
        if st.button('Login'):

            f = open('AuthenticationValue.txt', 'a')
            f.truncate(0)

            current = open('Functionlocation.txt','a')
            current.truncate(0)

            try:
                aws_client = boto3.client('cognito-idp',
                                          region_name='us-east-1'
                                          )
                response = aws_client.admin_create_user(
                    UserPoolId='us-east-1_*********',
                    Username=usrname,
                    UserAttributes=[
                        {
                            'Name': "name",
                            'Value': usrname
                        },
                        {
                            'Name': "email",
                            'Value': email
                        }
                    ],
                    DesiredDeliveryMediums=['EMAIL']
                )
                st.info("user created")
                authValueFlag = True
                currentFunction="Authentication"
            except aws_client.exceptions.UsernameExistsException as e:
                st.info("Login successfully")
                st.balloons()
                authValueFlag = True
                currentFunction = "Authentication"

            f = open('AuthenticationValue.txt', 'a')
            f.truncate(0)
            f.write(str(authValueFlag))
            #f.write(currentFunction)
            f.close()

            current = open('Functionlocation.txt','a')
            current.truncate(0)
            current.write(str(currentFunction))
            current.close()


if chosenRadioButton == 'Load the Data':

    f = open("AuthenticationValue.txt", "a")
    f = open("AuthenticationValue.txt", "r")

    authValueFlag = (f.read())
    authValue = str(authValueFlag)
    print(authValue)

    f = open("Functionlocation.txt", "a")
    f = open("Functionlocation.txt", "r")

    currentFunction = (f.read())
    currentF = str(currentFunction)
    print(currentF)
    # currentF = authValueFlag[1]
    # print("currentFunction"+currentF)
    # print(authValueFlag)
    bucket = st.text_input("Bucket Name")
    filetest = st.text_input("File Name")
    if st.button('Get Data'):

        if authValue == "True" or currentF == "Load the Data":
            response = requests.get(f"https://**********.execute-api.us-east-1.amazonaws.com/prod/{bucket}?file={filetest}")
            data_list = response.json()
            st.success(data_list['body'])
            authValue = "False"
            currentF = "Load the Data"
        else:
            st.warning("Please authenticate yourself")
            authValue = "False"
            currentF = "Load the Data"


        f = open('AuthenticationValue.txt', 'a')
        f.truncate(0)
        f.write(authValue)
        #f.write(currentF)
        f.close()
        current = open('Functionlocation.txt', 'a')
        current.truncate(0)
        current.write(currentF)
        current.close()

if chosenRadioButton == 'Anonymize Data':
    s3uri = st.text_input("S3 URI")
    outputuri = st.text_input("outputuri")
    entityList = ""
    drop = st.selectbox('Please select Entities for Anonymization', ('ALL', 'Select'))
    st.write('You selected:', drop)
    entityList = ""
    if drop == 'ALL':
        ALL = st.checkbox("ALL", value=False, key=None)  # use ur brain bro make this a drop
        if ALL:
            entityList = "ALL"
            # entityList = '"'+entityList+'"'
    else:
        st.info('Please select the Entity List for Masking')  # use this info for the drop and select option
        # rest in the drop select
        CREDIT_DEBIT_NUMBER = st.checkbox("CREDIT_DEBIT_NUMBER", value=False, key=None)
        if CREDIT_DEBIT_NUMBER:
            entityList = entityList + "CREDIT_DEBIT_NUMBER" + ","
        AWS_ACCESS_KEY = st.checkbox("AWS_ACCESS_KEY", value=False, key=None)
        if AWS_ACCESS_KEY:
            entityList = entityList + "AWS_ACCESS_KEY" + ","
        BANK_ROUTING = st.checkbox("BANK_ROUTING", value=False, key=None)
        if BANK_ROUTING:
            entityList = entityList + "BANK_ROUTING" + ","
        MAC_ADDRESS = st.checkbox("MAC_ADDRESS", value=False, key=None)
        if MAC_ADDRESS:
            entityList = entityList + "MAC_ADDRESS" + ","
        DRIVER_ID = st.checkbox("DRIVER_ID", value=False, key=None)
        if DRIVER_ID:
            entityList = entityList + "DRIVER_ID" + ","
        CREDIT_DEBIT_CVV = st.checkbox("CREDIT_DEBIT_CVV", value=False, key=None)
        if CREDIT_DEBIT_CVV:
            entityList = entityList + "CREDIT_DEBIT_CVV" + ","
        IP_ADDRESS = st.checkbox("IP_ADDRESS", value=False, key=None)
        if IP_ADDRESS:
            entityList = entityList + "IP_ADDRESS" + ","
        ADDRESS = st.checkbox("ADDRESS", value=False, key=None)
        if ADDRESS:
            entityList = entityList + "ADDRESS" + ","
        NAME = st.checkbox("NAME", value=False, key=None)
        if NAME:
            entityList = entityList + "NAME"
        CREDIT_DEBIT_EXPIRY = st.checkbox("CREDIT_DEBIT_EXPIRY", value=False, key=None)
        if CREDIT_DEBIT_EXPIRY:
            entityList = entityList + "CREDIT_DEBIT_EXPIRY" + ","
        SSN = st.checkbox("SSN", value=False, key=None)
        if SSN:
            entityList = entityList + "SSN" + ","
        PHONE = st.checkbox("PHONE", value=False, key=None)
        if PHONE:
            entityList = entityList + "PHONE" + ","
        DATE_TIME = st.checkbox("DATE_TIME", value=False, key=None)
        if DATE_TIME:
            entityList = entityList + "DATE_TIME" + ","
        PIN = st.checkbox("PIN", value=False, key=None)
        if PIN:
            entityList = entityList + "PIN" + ","
        PASSPORT_NUMBER = st.checkbox("PASSPORT_NUMBER", value=False, key=None)
        if PASSPORT_NUMBER:
            entityList = entityList + "PASSPORT_NUMBER" + ","
        URL = st.checkbox("URL", value=False, key=None)
        if URL:
            entityList = entityList + "URL" + ","
        USERNAME = st.checkbox("USERNAME", value=False, key=None)
        if USERNAME:
            entityList = entityList + "USERNAME" + ","
        PASSWORD = st.checkbox("PASSWORD", value=False, key=None)
        if PASSWORD:
            entityList = entityList + "PASSWORD" + ","
        EMAIL = st.checkbox("EMAIL", value=False, key=None)
        if EMAIL:
            entityList = entityList + "EMAIL" + ","
        AWS_SECRET_KEY = st.checkbox("AWS_SECRET_KEY", value=False, key=None)
        if AWS_SECRET_KEY:
            entityList = entityList + "AWS_SECRET_KEY" + ","
        BANK_ACCOUNT_NUMBER = st.checkbox("BANK_ACCOUNT_NUMBER", value=False, key=None)
        if BANK_ACCOUNT_NUMBER:
            entityList = entityList + "BANK_ACCOUNT_NUMBER" + ","
        AGE = st.checkbox("AGE", value=False, key=None)
        if AGE:
            entityList = entityList + "AGE"

        print(entityList)

    if st.button('Load Anonymize data in S3'):
        api_gateway = boto3.client('apigateway', region_name='us-east-1')
        response = requests.get(f"https://**********.execute-api.us-east-1.amazonaws.com/prod/identifyentities?uri={s3uri}&entitylist={entityList}&outputuri={outputuri}")
        print(response)
        data_list = response.json()
        st.success(data_list)

    st.header('Custom Analysis')
    st.info('Please enter Input text for Analysis')
    text = st.text_area("text")
    if st.button('Real time Analysis'):
        client = boto3.client('comprehend','us-east-1')
        data = client.detect_pii_entities(
            Text=text,
            LanguageCode='en'
        )
        st.success(data['Entities'])



if chosenRadioButton == 'Masking':
        st.header('Mask Entities')
        st.info('Please enter S3 uri for masking job')
        s3urimasking = st.text_input("s3urimasking")
        outputuri = st.text_input("outputuri")
        drop = st.selectbox('Please select Entities for Masking', ('ALL', 'Select'))
        st.write('You selected:', drop)
        entityList = ""
        if drop == 'ALL':
            ALL = st.checkbox("ALL", value=False, key=None)  # use ur brain bro make this a drop
            if ALL:
                entityList = "ALL"
                # entityList = '"'+entityList+'"'
        else:
            st.info('Please select the Entity List for Masking')  # use this info for the drop and select option
            # rest in the drop select
            CREDIT_DEBIT_NUMBER = st.checkbox("CREDIT_DEBIT_NUMBER", value=False, key=None)
            if CREDIT_DEBIT_NUMBER:
                entityList = entityList + "CREDIT_DEBIT_NUMBER" + ","
            AWS_ACCESS_KEY = st.checkbox("AWS_ACCESS_KEY", value=False, key=None)
            if AWS_ACCESS_KEY:
                entityList = entityList + "AWS_ACCESS_KEY" + ","
            BANK_ROUTING = st.checkbox("BANK_ROUTING", value=False, key=None)
            if BANK_ROUTING:
                entityList = entityList + "BANK_ROUTING" + ","
            MAC_ADDRESS = st.checkbox("MAC_ADDRESS", value=False, key=None)
            if MAC_ADDRESS:
                entityList = entityList + "MAC_ADDRESS" + ","
            DRIVER_ID = st.checkbox("DRIVER_ID", value=False, key=None)
            if DRIVER_ID:
                entityList = entityList + "DRIVER_ID" + ","
            CREDIT_DEBIT_CVV = st.checkbox("CREDIT_DEBIT_CVV", value=False, key=None)
            if CREDIT_DEBIT_CVV:
                entityList = entityList + "CREDIT_DEBIT_CVV" + ","
            IP_ADDRESS = st.checkbox("IP_ADDRESS", value=False, key=None)
            if IP_ADDRESS:
                entityList = entityList + "IP_ADDRESS" + ","
            ADDRESS = st.checkbox("ADDRESS", value=False, key=None)
            if ADDRESS:
                entityList = entityList + "ADDRESS" + ","
            NAME = st.checkbox("NAME", value=False, key=None)
            if NAME:
                entityList = entityList + "NAME"
            CREDIT_DEBIT_EXPIRY = st.checkbox("CREDIT_DEBIT_EXPIRY", value=False, key=None)
            if CREDIT_DEBIT_EXPIRY:
                entityList = entityList + "CREDIT_DEBIT_EXPIRY" + ","
            SSN = st.checkbox("SSN", value=False, key=None)
            if SSN:
                entityList = entityList + "SSN" + ","
            PHONE = st.checkbox("PHONE", value=False, key=None)
            if PHONE:
                entityList = entityList + "PHONE" + ","
            DATE_TIME = st.checkbox("DATE_TIME", value=False, key=None)
            if DATE_TIME:
                entityList = entityList + "DATE_TIME" + ","
            PIN = st.checkbox("PIN", value=False, key=None)
            if PIN:
                entityList = entityList + "PIN" + ","
            PASSPORT_NUMBER = st.checkbox("PASSPORT_NUMBER", value=False, key=None)
            if PASSPORT_NUMBER:
                entityList = entityList + "PASSPORT_NUMBER" + ","
            URL = st.checkbox("URL", value=False, key=None)
            if URL:
                entityList = entityList + "URL" + ","
            USERNAME = st.checkbox("USERNAME", value=False, key=None)
            if USERNAME:
                entityList = entityList + "USERNAME" + ","
            PASSWORD = st.checkbox("PASSWORD", value=False, key=None)
            if PASSWORD:
                entityList = entityList + "PASSWORD" + ","
            EMAIL = st.checkbox("EMAIL", value=False, key=None)
            if EMAIL:
                entityList = entityList + "EMAIL" + ","
            AWS_SECRET_KEY = st.checkbox("AWS_SECRET_KEY", value=False, key=None)
            if AWS_SECRET_KEY:
                entityList = entityList + "AWS_SECRET_KEY" + ","
            BANK_ACCOUNT_NUMBER = st.checkbox("BANK_ACCOUNT_NUMBER", value=False, key=None)
            if BANK_ACCOUNT_NUMBER:
                entityList = entityList + "BANK_ACCOUNT_NUMBER" + ","
            AGE = st.checkbox("AGE", value=False, key=None)
            if AGE:
                entityList = entityList + "AGE"

            print(entityList)
        if st.button('Load Masked data in S3'):
            api_gateway = boto3.client('apigateway', region_name='us-east-1')
            response = requests.get(
                    f" https://**********.execute-api.us-east-1.amazonaws.com/prod/maskentities?s3uri={s3urimasking}&entitylist={entityList}&outputuri={outputuri}")
            print(response)
            data_list = response.json()
            st.success(data_list['body'])

if chosenRadioButton == 'Sentiment Prediction':
    st.header('Predict Sentiment on Custom Input')
    st.write('Enter text to get the sentiments:')
    text = st.text_input('Text')
    data = {"text": text}
    data = json.dumps(data)
    if st.button('Predict Sentiment'):
        response = requests.post(url="http://127.0.0.1:8000/predict", data=data)
        data_list = response.json()
        st.success("Sentiment is '" + data_list['sentiment'] + "' and the confidence score is '" + str(
            data_list['confidence']) + "'")

    st.header('Predict Sentiment on Anonymized EDGAR call transcripts')

    s3 = boto3.client('s3')
    st.subheader('Enter the S3 URI')
    S3Uri = st.text_input('S3 URI')

    if S3Uri.startswith('s3://'):
        S3Uri = S3Uri[5:]
    s3_components = S3Uri.split('/')
    bucket = s3_components[0]
    s3_key = ""
    if len(s3_components) > 1:
        s3_key = '/'.join(s3_components[1:])

    if st.button("Predict"):
        data = s3.get_object(Bucket=bucket, Key=s3_key)
        body = data['Body'].read().decode('utf-8')

        data = {"text": body}
        data = json.dumps(data)

        response = requests.post(url="http://127.0.0.1:8000/predict", data=data)
        data_list = response.json()
        st.success("Sentiment is '" + data_list['sentiment'] + "' and the confidence score is '" + str(
            data_list['confidence']) + "'")



