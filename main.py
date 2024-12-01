import streamlit as st
import requests
import time
import os
from dotenv import load_dotenv
load_dotenv()

today = time.strftime("%Y-%m-%d")

api_key = os.getenv("MY_KEY")
url= "https://api.nasa.gov/planetary/apod?"\
     f"&date={today}"\
     f"&api_key={api_key}"

response1 = requests.get(url)
data = response1.json()

title = data['title']
explanation = data['explanation']
image_url = data['hdurl']
response2 = requests.get(image_url)

st.title(title)
st.image(image_url, caption=f"{title}")
st.write(explanation)
st.info(f"{image_url}")





