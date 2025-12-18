import os
from dotenv import load_dotenv
import streamlit as st
import requests
from langchain.chat_models import init_chat_model

load_dotenv()

llm=init_chat_model(
    model="llama-3.3-70b-versatile",
    model_provider="openai",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

st.title("Weather App with AI Explanation")

city=st.text_input("Enter city name")

if st.button("Get Weather"):
    if city:
        WEATHER_API_KEY=os.getenv("API_KEY")
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response=requests.get(url)

        if response.status_code==200:
            data=response.json()
            temp=data["main"]["temp"]
            humidity=data["main"]["humidity"]
            condition=data["weather"][0]["description"]

            st.subheader("Current Weather")
            st.write("Temperature:",temp,"°C")
            st.write("Humidity:",humidity,"%")
            st.write("Condition:",condition)

            llm_input=f"""
            Temperature:{temp}°C
            Humidity:{humidity}%
            Weather Condition:{condition}

            Instruction:
            Explain this weather in very simple English so that a beginner can understand.
            """

            result=llm.invoke(llm_input)

            st.subheader("AI Weather Explanation")
            st.write(result.content)

        else:
            st.error("City not found")
    else:
        st.warning("Please enter a city name")
