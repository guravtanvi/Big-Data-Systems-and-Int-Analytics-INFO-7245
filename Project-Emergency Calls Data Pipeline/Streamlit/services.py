import json

import boto3

import location as location_file
import streamlit as st
import os
import download_audio
from location import get_rand_lat_long
import config
import requests
import pandas as pd
import numpy as np
from boto.s3.connection import S3Connection
import time

global victim_name, location, r, emergency_type, description, resolved, longitude, lattitude
victim_name = ""
location = ""
r = ""
emergency_type = ""
description = ""
resolved = "No"
longitude = ""
path = ""
lattitude = ""

medical_list = ['medical', 'doctor', 'ambulance','hospital','health']
crime = ['police','crime','murder','shooting','gun','assault','harassment']
fire = ['fire','burning','fire alarm','smoke']


# Function to display the audio files
def audio_calls():
    # path = './data/'
    path_live = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'live_data'))
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'data'))
    for f in os.listdir(path):
        print(path+"\\"+f)
        os.remove(path+"/"+f)
    for f in os.listdir(path_live):
        os.remove(path_live+"/"+f)

    download_audio.download()
    download_audio.download_live()




    st.header(":phone: Live Calls")
    for filename in os.listdir(path_live):
        with st.beta_expander(filename):
            audio_file = open("./live_data/" + filename, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio / wav')

    def getitem(audiofile):
        dynamodb = boto3.client('dynamodb', aws_access_key_id=config.aws["secret_id"],
                                aws_secret_access_key=config.aws["access_key"],region_name=config.aws["region"])
        response = dynamodb.get_item(TableName='911emergencycalls', Key={'audiofile': {'S': audiofile}})
        print(response)
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

        st.code(
            "Caller's Name" + " - " + callername + '\n' + "Address" + " - " + address + '\n' + "Type of Emergency" + " - " + emergency + '\n' + "Contact Number" + " - " +
            response['Item']['contact']['S'] + '\n' + "Description" + " - " + desc + '\n' + "Resolved" + " - " +
            response['Item']['resolved']['S'] + '\n' + "Lattitude" + " - " + response['Item']['lattitude'][
                'S'] + '\n' + "Longitude" + " - " + response['Item']['longitude'][
                'S'] + '\n' + "audiofile" + " - " + response['Item']['audiofile']['S'])

        return response
    st.header(":phone: Historical Calls")

    for filename in os.listdir(path):
        with st.beta_expander(filename):
            #col1, col2 = st.beta_columns(2)
            audio_file = open("./data/" + filename, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio / wav')
            # st.button(getitem(filename))
            getitem(filename.split(".wav")[0])


    return


def location_services():
    df = pd.read_csv('911.csv')
    df_latlong = df[['lat', 'lng']]
    index = np.random.randint(0, 663522)
    latitude = df_latlong.loc[index].lat
    longitude = df_latlong.loc[index].lng
    key = config.google_maps_api["key"]
    response = requests.get(
        f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={key}")
    address = response.json()
    st.write(address["results"][0]["formatted_address"])
    return address["results"][0]["formatted_address"]


# Function to display menu once logged in
def login_menu():
    global victim_name, location, r, emergency_type, description, resolved, longitude, lattitude
    victim_name = ""
    location = ""
    r = ""
    emergency_type = ""
    description = ""
    resolved = "No"
    longitude = ""
    path = ""
    lattitude = ""

    medical_list = ['medical', 'doctor', 'emergency', 'ambulance']
    crime = ['police', 'crime', 'murder']
    fire = ['fire']

    st.sidebar.header(":gear:  Services")
    choice = st.sidebar.radio("Menu",
                              ["AWS Connect Calls", "Call Records Dashboard", "Call Transcripts", "Summarized Report",
                               "Notify Entities","Analytics Dashboard"])
    if choice == "AWS Connect Calls":
        st.header("Redirect to Virtual Call Center")
        st.write(
            "Login Here https://911emergencycallcenter.my.connect.aws/test-chat")


    elif choice == "Call Records Dashboard":
        audio_calls()

    elif choice == "Call Transcripts":
        uploaded_file = st.file_uploader("Choose a file",
                                         help="Upload a call recording (wav/mp3) to get the transcript")
        if uploaded_file is not None:
            audio_bytes = uploaded_file.read()
            st.audio(audio_bytes, format='audio / wav')
        conn = S3Connection(aws_access_key_id=config.aws["secret_id"],
                                    aws_secret_access_key=config.aws["access_key"])
        bucket = conn.get_bucket('amazon-connect-3c22ce0802db')

        drop = st.selectbox('Please select Audio for Transcribe',
                            options=[obj.key.split("/")[6] for obj in bucket.get_all_keys()])
        print(drop)
        if drop is not None:
            for obj in bucket.get_all_keys():
                if obj.key.split("/")[6] == drop:
                    path = 's3://amazon-connect-3c22ce0802db' + '/' + obj.key

            print(path)

            JobName = drop.split(".wav")[0]
            JobName=JobName.replace(":","_")

            if st.button('Convert Audio to text'):
                # api_gateway = boto3.client('apigateway', region_name='us-east-1')
                response = requests.get(
                    f"https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/dev/triggertranscribe?uri={path}&jobname={JobName}"
                )

                progress_bar = st.progress(0)
                status_text = st.empty()

                for i in range(100):
                    responsecheck = requests.get(
                        f"https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/dev/jobstatus?jobname={JobName}")
                    status = responsecheck.json()
                    print(status)
                    if status['body'] == "IN_PROGRESS":
                        progress_bar.progress(i + 1)
                        new_rows = np.random.randn(10, 2)
                        time.sleep(0.1)
                    elif status['body'] == "COMPLETED":
                        break

                st.success('Thanks for waiting Job execution is done!')

            st.info("Please click below button to see text data")
            if st.button("Text Data"):
                responsedata = requests.get(
                    f"https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/dev/readdata?jobname={JobName}")
                data = responsedata.json()
                st.success(data['body'])
        else:
            st.error("No new files")

    elif choice == "Summarized Report":
        conn = S3Connection(aws_access_key_id=config.aws["secret_id"],
                                    aws_secret_access_key=config.aws["access_key"])
        bucket = conn.get_bucket('transcribe-audiototext1')
        file = []

        for obj in bucket.get_all_keys():
            if obj.key != '.write_access_check_file.temp':
                file.append(obj.key)
        print(file)
        drop = st.selectbox('Please select Audio for Transcribe',
                            options=[obj for obj in file])
        jobname = drop
        print(drop)
        st.info("Please click on the below button for summarized call details")

        # function to save data in DynamoDB
        def putitem(victim_name, location, emergency_type, contact, description, resolved, lattitude, longitude,
                    audiofile):
            dynamodb = boto3.client('dynamodb', aws_access_key_id=config.aws["secret_id"],
                                    aws_secret_access_key=config.aws["access_key"],region_name=config.aws["region"])
            response = dynamodb.put_item(TableName='911emergencycalls',
                                         Item={
                                             'victim_name': {'S': victim_name},
                                             'location': {'S': location},
                                             'type': {'S': emergency_type},
                                             'contact': {'S': contact},
                                             'description': {'S': description},
                                             'resolved': {'S': resolved},
                                             'lattitude': {'S': lattitude},
                                             'longitude': {'S': longitude},
                                             'audiofile': {'S': audiofile}
                                         }

                                         )
            return response

        # function to pull data from DynamoDB
        def getitem(audiofile):
            dynamodb = boto3.client('dynamodb', aws_access_key_id=config.aws["secret_id"],
                                    aws_secret_access_key=config.aws["access_key"],region_name=config.aws["region"])
            response = dynamodb.get_item(TableName='911emergencycalls', Key={'audiofile': {'S': audiofile}})
            print(response)
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

            st.code(
                "Caller's Name" + " - " + callername + '\n' + "Address" + " - " + address + '\n' + "Type of Emergency" + " - " + emergency + '\n' + "Contact Number" + " - " +
                response['Item']['contact']['S'] + '\n' + "Description" + " - " + desc + '\n' + "Resolved" + " - " +
                response['Item']['resolved']['S'] + '\n' + "Lattitude" + " - " + response['Item']['lattitude'][
                    'S'] + '\n' + "Longitude" + " - " + response['Item']['longitude'][
                    'S'] + '\n' + "audiofile" + " - " + response['Item']['audiofile']['S'])

            return response

        # regular expression to check keywords for kind of emergency
        def emergencytype(search_list, Text):
            import re
            if re.compile('|'.join(search_list), re.IGNORECASE).search(Text):  # re.IGNORECASE is used to ignore case
                r = "Match"
            else:
                r = "Not Matched"
            return r

        if st.button("Summarized Call Details"):
            s3 = boto3.resource('s3', aws_access_key_id=config.aws["secret_id"],
                                aws_secret_access_key=config.aws["access_key"],region_name=config.aws["region"])
            bucket = s3.Bucket('transcribe-audiototext1')
            for obj in bucket.objects.all():
                if obj.key == jobname:
                    print(jobname)
                    key = obj.key
                    body = obj.get()['Body'].read()
                    test = json.loads(body)
                    test1 = test['results']['transcripts'][0]['transcript']

                    description = test1
                    print(test1)
                    audiofile = jobname.split(".json")[0]
                    if emergencytype(['medical', 'doctor', 'ambulance','hospital','health'], test1) == "Match":
                        emergency_type = "Medical"
                    if emergencytype(['police','crime','murder','shooting','gun','assault','harassment'], test1) == "Match":
                        emergency_type = "Crime"
                    if emergencytype(['fire','burning','fire alarm','smoke'], test1) == "Match":
                        emergency_type = "Fire"
                    print(emergency_type+"emergency_type")
                    client = boto3.client('comprehend', aws_access_key_id=config.aws["secret_id"],
                                          aws_secret_access_key=config.aws["access_key"],region_name=config.aws["region"])
                    response = client.detect_entities(
                        Text=test1,
                        LanguageCode='en'
                    )

                    for a in response['Entities']:
                        if a['Type'] == 'PERSON':
                            victim_name = a['Text']

                        if a['Type'] == 'LOCATION' and len(a['Text']) > 2:
                            location = a['Text']
                            print(location)

                            if location == "" or len(location) == 0:
                                lattitude, longitude, address_test = location_file.get_address()
                            else:
                                address = location.replace(" ", "+")
                                response = requests.get(
                                    f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key{config.google_maps_api["key"]}

                                response_json = response.json()
                                lattitude = str(response_json['results'][0]['geometry']['location']['lat'])

                                longitude = str(response_json['results'][0]['geometry']['location']['lng'])

                            if victim_name == "":
                                putitem("", location, emergency_type, "8577637852", description, resolved, lattitude,
                                        longitude, audiofile)
                            else:
                                putitem(victim_name, location, emergency_type, "8577637852", description, resolved,
                                        lattitude, longitude, audiofile)

                                print("Loaded in DynamoDB")

                            getitem(audiofile)




    elif choice == "Notify Entities":
        conn = S3Connection(aws_access_key_id=config.aws["secret_id"],
                                    aws_secret_access_key=config.aws["access_key"])
        bucket = conn.get_bucket('amazon-connect-3c22ce0802db')

        for obj in bucket.get_all_keys():
            filetonotify = obj.key.split("/")[6]
            filename=obj.key
            filetonotify = filetonotify.split(".wav")[0]
            print(filetonotify)
            filetonotify=filetonotify.replace(":","_")
            print(filetonotify)
        try:
            response = requests.get(f"https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/dev/getaddress?filename={filetonotify}")
            response_json = response.json()
            print(response_json)
            st.code("Caller's Address" +" - "+response_json['body']['Item']['location']['S']+'\n'+"EmergencyType" +" - "+response_json['body']['Item']['type']['S'])

            lattitude=response_json['body']['Item']['lattitude']['S']
            longitude=response_json['body']['Item']['longitude']['S']
            address=response_json['body']['Item']['location']['S']
            type=response_json['body']['Item']['type']['S']
            audiofile=response_json['body']['Item']['audiofile']['S']


            searchbox=[]
            if response_json['body']['Item']['type']['S']=="Medical":
                searchbox.append('Hospitals')
            elif response_json['body']['Item']['type']['S']=="Crime":
                searchbox.append('Police')
            elif response_json['body']['Item']['type']['S'] == "Fire":
                searchbox.append('Fire')

            choice = st.selectbox(label="Search", options=searchbox, index=0,
                                  help="Select to get Emergency Services nearby victim's location")

            if st.button("Search"):
                if choice == "Hospitals":
                    st.write("Showing list of near by Hospitals")
                    hospitals = location_file.get_hospitals(lattitude, longitude)
                    st.write(hospitals)
                    hospital = hospitals.iloc[0]
                    hosp_address = hospital["Address"]
                    st.markdown(
                        f""" <iframe width="1050" height="850" frameborder="0" style="border:0" src="https://www.google.com/maps/embed/v1/directions?key={config.google_maps_api["key"]}&origin={address}&destination={hosp_address.replace(" ", "+")}&zoom=7&maptype=satellite" allowfullscreen></iframe>
                                                            """, unsafe_allow_html=True)
            elif choice == "Police":
                st.write("Showing list of near by police stations")
                police_dept = location_file.get_police(lattitude, longitude)
                st.write(police_dept)
                police = police_dept.iloc[0]
                police_addr = police["Address"]
                st.markdown(
                    f""" <iframe width="1050" height="850" frameborder="0" style="border:0" src="https://www.google.com/maps/embed/v1/directions?key={config.google_maps_api["key"]}&origin={address}&destination={police_addr.replace(" ", "+")}&zoom=15&maptype=satellite" allowfullscreen></iframe>
                                                                        """, unsafe_allow_html=True)
            elif choice == "Fire":
                st.write("Showing list of near by fire departments")
                fire_dept = location_file.get_fire_dept(lattitude, longitude)
                st.write(fire_dept)
                fire_loc = fire_dept.iloc[0]
                fire_addr = fire_loc["Address"]
                st.markdown(
                    f""" <iframe width="1050" height="850" frameborder="0" style="border:0" src="https://www.google.com/maps/embed/v1/directions?key={config.google_maps_api["key"]}&origin={address}&destination={fire_addr.replace(" ", "+")}&zoom=15&maptype=satellite" allowfullscreen></iframe>
                                                                                   """, unsafe_allow_html=True)

            st.title("Sending Notification to the nearest help")
            if st.button("Send Notification"):
                response=requests.get(f"https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/dev/notification?audiofile={audiofile}&type={type}")
                response_json=response.json()
                print(response_json)
                st.success("Email Sent successfully")
                # filename=audiofile+".wav"

                print(filename)
                # code to move historical processed call to new bucket
                # response = requests.get(
                #     f"https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/dev/movefile?filename={filename}")
        except:
            st.error("No new calls to Notify")

    elif choice == "Analytics Dashboard":
        st.markdown("""
                            <iframe width="1000" height="600" src="https://app.powerbi.com/view?r=eyJrIjoiODgzZDQ5YzQtNTNmMS00OWE4LWIwMWMtZGM3MTM0NGI1MWEzIiwidCI6ImE4ZWVjMjgxLWFhYTMtNGRhZS1hYzliLTlhMzk4YjkyMTVlNyIsImMiOjN9" frameborder="0" style="border:0" allowfullscreen></iframe>
                            """, unsafe_allow_html=True)
        st.write(" ")
        st.markdown("""
            <iframe width="1000" height="600" src="https://app.powerbi.com/view?r=eyJrIjoiZDExNGU2NGYtZmU2MC00M2U3LWI4ODUtYmI4NmNiZGIxMWU5IiwidCI6ImE4ZWVjMjgxLWFhYTMtNGRhZS1hYzliLTlhMzk4YjkyMTVlNyIsImMiOjN9&pageName=ReportSection" frameborder="0" style="border:0" allowfullscreen></iframe>
            """, unsafe_allow_html=True)

    return
