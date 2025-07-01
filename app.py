import streamlit as st
import requests
from datetime import date
from dotenv import load_dotenv

import os
import numpy as np
from scipy.io.wavfile import write

# Load .env variables
load_dotenv()



# Streamlit setup
st.set_page_config(page_title="NASA APOD Viewer", page_icon ="🚀", layout="wide")

# Beautiful header with logo in markdown
st.markdown("""
<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; margin-bottom: 2rem;">
    <img src="data:image/jpeg;base64,{}" width="80" style="margin-bottom: 1rem;">
    <h1 style="color: white; margin: 0; font-size: 3rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
        🌟🚀 NASA APOD Viewer
    </h1>
    <p style="color: #e0e6ff; margin: 0.5rem 0 0 0; font-size: 1.2rem;">
        Explore the cosmos with daily images from NASA
    </p>
</div>
""",unsafe_allow_html=True)

# Date range
today = date.today()
apod_start_date = date(1995, 6, 16)

selected_date = st.date_input(
    "Pick a date",
    value=today,
    min_value=apod_start_date,
    max_value=today
)
date_str = selected_date.strftime("%Y-%m-%d")
st.write(f"📅 Selected Date: {date_str}")

# Your n8n webhook URL
API_URL = "https://navyasribiruda009.app.n8n.cloud/webhook/https://api.nasa.gov/planetary/apod"  

try:
    # Fetch data from n8n
    response = requests.get(API_URL, params={"date": date_str})
    data = response.json()

    st.subheader(data.get("title", "No Title"))

    media_type = data.get("media_type")
    media_url = data.get("hdurl") or data.get("url")

    if media_type == "image" and media_url:
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.image(media_url, width=600)
        st.markdown("</div>", unsafe_allow_html=True)
    elif media_type == "video" and media_url:
        st.video(media_url)
    else:
        st.warning("No image or video available for this date.")

     # Explanation
    explanation_text = data.get("explanation", "")
    st.markdown(f"📅 **Date:** {data.get('date', '')}")
    st.markdown("### Explanation")
    st.write(explanation_text)

    
except Exception as e:
    st.error("Failed to load APOD data")
    st.code(str(e))

# Beautiful footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; margin-top: 2rem;">
    <p style="color: white; margin: 0; font-size: 1.1rem;">
        🌟 Powered by NASA APOD API • Built with n8n and streamlit.
    </p>
</div>
""", unsafe_allow_html=True)