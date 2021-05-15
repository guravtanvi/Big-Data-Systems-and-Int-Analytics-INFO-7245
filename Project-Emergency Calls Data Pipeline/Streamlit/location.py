import pandas as pd
import numpy as np
import requests
from googleplaces import GooglePlaces, types
import streamlit as st


def get_rand_lat_long():
    df = pd.read_csv('911.csv')
    df_latlong = df[['lat', 'lng']]

    index = np.random.randint(0, 663522)
    lat = df_latlong.loc[index].lat
    long = df_latlong.loc[index].lng
    return lat, long


def get_address():
    df = pd.read_csv('911.csv')
    df_latlong = df[['lat', 'lng']]
    index = np.random.randint(0, 663522)
    latitude = df_latlong.loc[index].lat
    longitude = df_latlong.loc[index].lng
    key = "*********************************************"
    response = requests.get(
        f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={key}")
    address = response.json()
    return latitude, longitude, address["results"][0]["formatted_address"]


def get_hospitals(lat, lng):
    API_KEY = "*********************************************"
    google_places = GooglePlaces(API_KEY)
    query_result = google_places.nearby_search(

        lat_lng={'lat': lat, 'lng': lng},
        radius=5000,
        # types =[types.TYPE_HOSPITAL] or
        # [types.TYPE_CAFE] or [type.TYPE_BAR]
        # or [type.TYPE_CASINO])
        types=[types.TYPE_HOSPITAL])

    # If any attributions related with search results print them
    if query_result.has_attributions:
        st.write(query_result.html_attributions)

    hospital_list = []
    # Iterate over the search results
    for place in query_result.places:
        place.get_details()
        hospital_list.append(
            [place.name, place.formatted_address, place.international_phone_number, place.website, place.rating,
             place.geo_location['lat'], place.geo_location['lng']])

    hospitals = pd.DataFrame(hospital_list,
                             columns=["Hospital", "Address", "Contact", "Website", "Rating", "Latitude", "Longitude"])
    st.write(hospitals)


def get_police(lat, lng):
    API_KEY = "*********************************************"
    google_places = GooglePlaces(API_KEY)
    query_result = google_places.nearby_search(

        lat_lng={'lat': lat, 'lng': lng},
        radius=5000,
        types=[types.TYPE_POLICE])

    # If any attributions related with search results print them
    if query_result.has_attributions:
        st.write(query_result.html_attributions)

    hospital_list = []
    # Iterate over the search results
    for place in query_result.places:
        place.get_details()
        hospital_list.append(
            [place.name, place.formatted_address, place.international_phone_number, place.geo_location['lat'],
             place.geo_location['lng']])

    hospitals = pd.DataFrame(hospital_list, columns=["Police", "Address", "Contact", "Latitude", "Longitude"])
    st.write(hospitals)


def get_fire_dept(lat, lng):
    API_KEY = "*********************************************"
    google_places = GooglePlaces(API_KEY)
    query_result = google_places.nearby_search(

        lat_lng={'lat': lat, 'lng': lng},
        radius=5000,
        types=[types.TYPE_FIRE_STATION])

    # If any attributions related with search results print them
    if query_result.has_attributions:
        st.write(query_result.html_attributions)

    hospital_list = []
    # Iterate over the search results
    for place in query_result.places:
        place.get_details()
        hospital_list.append(
            [place.name, place.formatted_address, place.international_phone_number, place.geo_location['lat'],
             place.geo_location['lng']])

    hospitals = pd.DataFrame(hospital_list, columns=["Fire Station", "Address", "Contact", "Latitude", "Longitude"])
    st.write(hospitals)
