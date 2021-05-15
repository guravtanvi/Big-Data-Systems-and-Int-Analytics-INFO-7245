import streamlit as st
import requests
import flat_table
from pandas import json_normalize

# Code for loading main page


def main():

    st.title("Exploring Lending Club Analysis API")
    page = st.sidebar.radio("Select an option", ("", "Login", "Logout", "Fetch Data Without Login", "Visualize Lending Club Data"))

    if page == "":
        st.title("-----------------------------------------------------")

    elif page == 'Login':
        endpoint = 'login-streamlit'
        access_key = '1234567asdfgh'
        res = requests.get(f"http://localtest.me:8000/{endpoint}?access_token={access_key}")
        message = res.json()
        st.sidebar.success(message["message"])

        st.subheader("You now have access to the data")
        r = st.selectbox("Choose a page", ["--Select Data--", "Get All Data", "Get Data By Verification",
                                           "Get Data By Loan Status Count", "Get Data Based on Home Ownership & Annual Income"])

        if r == 'Get All Data':
            endpoint = 'all'
            access_key = '1234567asdfgh'
            res = requests.get(f"http://localtest.me:8000/{endpoint}?access_token={access_key}")
            st.write(res.json())

        elif r == 'Get Data By Verification':
            status = st.text_input("Enter the verification Status")
            if st.button("Get Data"):
                endpoint = 'verification_details'
                access_key = '1234567asdfgh'
                res = requests.get(f"http://localtest.me:8000/{endpoint}/{status}?access_token={access_key}")
                st.write(res.json())

        elif r == 'Get Data By Loan Status Count':
            endpoint = 'GET_COUNT'
            access_key = '1234567asdfgh'
            res = requests.get(f"http://localtest.me:8000/{endpoint}?access_token={access_key}")
            df = load_count(res.json())
            st.write(df)

        elif r == 'Get Data Based on Home Ownership & Annual Income':
            ownership = st.text_input("Enter Home Ownership")
            income = st.text_input("Enter Annual Income")
            if st.button("Get Data"):
                endpoint = 'ownership_income'
                access_key = '1234567asdfgh'
                res = requests.get(f"http://localtest.me:8000/{endpoint}/{ownership},{income}?access_token={access_key}")
                st.write(res.json())

    elif page == "Logout":
        if st.sidebar.button('Logout'):
            endpoint = 'logout-streamlit'
            res = requests.get(f"http://localtest.me:8000/{endpoint}")
            st.success(res.json()["message"])

    elif page == "Fetch Data Without Login":
        if st.button("Get Data"):
            endpoint = 'all'
            res = requests.get(f"http://localtest.me:8000/{endpoint}")
            message = res.json()
            st.error(message["detail"])

    elif page == "Visualize Lending Club Data":
        st.markdown("""
    <iframe width="1000" height="700" src="https://app.powerbi.com/reportEmbed?reportId=0402edc1-3333-462a-9a21-954581c88e1b&autoAuth=true&ctid=a8eec281-aaa3-4dae-ac9b-9a398b9215e7&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLXVzLW5vcnRoLWNlbnRyYWwtZi1wcmltYXJ5LXJlZGlyZWN0LmFuYWx5c2lzLndpbmRvd3MubmV0LyJ9" frameborder="0" style="border:0" allowfullscreen></iframe>
    """, unsafe_allow_html=True)


# Code for normalizing json to dataframe

@st.cache
def load_count(data):
    df = json_normalize(data)
    table = flat_table.normalize(df)
    table.drop(columns=['index'], inplace=True)
    return table

if __name__ == "__main__":
    main()