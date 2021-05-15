import streamlit as st
import altair as alt
import s3fs
import h5py # needs conda/pip install h5py
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import cv2
import tempfile
import os


def h5_img(img_typ,year,event_type, start_date, end_date):
    s3 = s3fs.S3FileSystem()
    img_typ_cap = img_typ.upper()
    file_index = 0

    try:
        with h5py.File(s3.open('sevir/data/' + img_typ + '/' + year + '/SEVIR_'+ img_typ_cap +'_'+ event_type +'_'+ year +'_'+start_date+'_'+end_date+'.h5'),"r") as hf:
            event_id = hf['id'][file_index]
            vil = hf[img_typ][file_index]
            st.write(event_id)
            fig, axs = plt.subplots(1, 4, figsize=(10, 4))
            axs[0].imshow(vil[:, :, 1])
            axs[1].imshow(vil[:, :, 2])
            axs[2].imshow(vil[:, :, 3])
            axs[3].imshow(vil[:, :, 4])
            st.pyplot(plt)

    except FileNotFoundError:
        st.error('Oops! File not found.')

#    Code for converting image to video

#    if st.button('Get Video for 4 hour'):
#        image_fil = [vil[:, :, i] for i in range(49)]
#        size = image_fil[0].shape
#        out = cv2.VideoWriter('project_new.avi', cv2.VideoWriter_fourcc(*'XVID'), 1, size, isColor=False)
#        for i in range(len(image_fil)):
#            out.write(image_fil[i])
        #out.release()
#        video_file = open(out.release(), 'rb')
#        video_bytes = video_file.read()
#        st.video(video_bytes, format='video/avi')



def main():
    page = st.sidebar.selectbox("Choose a page", ["--Select Data--", "Storm Data", "Sevir Data"])
    st.title("Exploring Storm EVent ImageRy (SEVIR)")

    if page == "--Select Data--":
        st.header("Select a page on the left")

    elif page == "Storm Data":
        st.title("Data Exploration for Strom dataset - 2018")
        df = load_data()
        st.write(df)
        x_axis = st.selectbox("Choose a variable for the x-axis", df.columns, index=3)
        y_axis = st.selectbox("Choose a variable for the y-axis", df.columns, index=4)

        try:
            if st.button("Visualize Data"):
                visualize_data(df, x_axis, y_axis)
        except ValueError:
            st.error('Oops! Unable to visualize')

    elif page == "Sevir Data":
        st.title("Data Exploration for SEVIR dataset")

        img_typ = st.selectbox("Choose a img_typ", ["vil", "vis", "ir069", "ir107"])
        year = st.selectbox("Choose a year", ["2017", "2018", "2019"])
        event_type = st.selectbox("Choose a event type", ["STORMEVENTS", "RANDOMEVENTS"])
        start_date = st.selectbox("Choose a start date (MMDD)", ["0101", "0901", "0701", "0501"])
        end_date = st.selectbox("Choose a end date (MMDD)", ["0630", "1231", "0440", "0831"])

        if st.button('Get SEVIR-Image Sample') is not None:
            h5_img(img_typ,year,event_type,start_date,end_date)


@st.cache
def load_data():
    df = pd.read_csv('D:\InformationSystem\CSYE-BDS\MainDataset\StormEvents_fatalities_2019.csv')
    df.drop(columns=['FAT_TIME', 'EVENT_YEARMONTH', 'FATALITY_DATE'], inplace=True)
    return df

def visualize_data(df, x_axis, y_axis):
    graph = alt.Chart(df).mark_circle().encode(
        x=x_axis,
        y=y_axis,
        color=y_axis,
    ).interactive()

    st.write(graph)

if __name__ == "__main__":
    main()