import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather Forecast")
place=st.text_input("Place:")
days=st.slider("Forecast Days",min_value=1,max_value=5,help="Select the number of Forecast days")
option=st.selectbox("Select data to view",("Temperatures","Sky"))
st.subheader(f"{option} for next {days} days in {place}")

if place:
    try:
        filtered_data = get_data(place,days)
        if option=="Temperatures":
             temperatures=[dict["main"]["temp"]/10 for dict in filtered_data]
             dates=[dict["dt_txt"] for dict in filtered_data]
             figure=px.line(x=dates,y=temperatures,labels={"x":"Date","y":"Temperatures(C)"})
             st.plotly_chart(figure)



        if option=="Sky":
            images = {"Clear": "images/sun.png", "Clouds": "images/cloudy.png","Rain": "images/storm.png", "Snow": "images/snow.png"}
            sky_conditions=[dict["weather"][0]["main"]for dict in filtered_data]
            image_paths=[images[condition] for condition in sky_conditions]
            print(sky_conditions)
            st.image(image_paths,width=50)

    except KeyError:
        st.write("Not exit")