import os
from dotenv import load_dotenv
import streamlit as st
import requests


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("Login Form")

    username=st.text_input("Enter username")
    password=st.text_input("Enter password")

    if st.button("Login"):
        if username == password and username != "":
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid credentials")

else:
    st.title("Weather App")

    city=st.text_input("Enter city name")


    if st.button("Get Weather"):
        if city:

            load_dotenv()

            API_KEY=os.getenv("API_KEY")
            url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response=requests.get(url)

            if response.status_code == 200:
                data = response.json()
                st.write("Temperature:",data["main"]["temp"], "°C")
                st.write("Humidity:",data["main"]["humidity"], "%")
                st.write("Condition:",data["weather"][0]["description"])
            else:
                st.error("City not found")
        else:
            st.warning("Enter a city name")

    if st.button("Logout"):
        st.session_state.logged_in=False
        st.success("Thanks for using the app")
        st.rerun()
