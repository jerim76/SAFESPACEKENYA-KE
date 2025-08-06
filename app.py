import streamlit as st
import pandas as pd
from PIL import Image
import requests
from io import BytesIO

# Set page configuration
st.set_page_config(
    page_title="SafeSpace Organisation",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# FIX: Add Founder Info to About Section
st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'><h2>About SafeSpace</h2><div class='divider'></div></div>", unsafe_allow_html=True)

about_cols = st.columns(2)
with about_cols[0]:
    st.markdown("""
        <h3>Creating a Safe Space for Healing</h3>
        <p>Founded in 2015 by <strong>Jerim</strong>, SafeSpace Organisation is a leading mental health provider in Nairobi, Kenya.
        We offer professional counseling services, support groups, and mental health education to individuals
        and communities facing life's challenges.</p>
        <p>Our mission is to break down the stigma surrounding mental health in Kenya and provide accessible,
        affordable care to all who need it.</p>
        <p>We believe that mental wellness is a fundamental human right and are committed to creating a safe,
        supportive environment where healing can begin.</p>
        <div style="margin-top: 30px;">
            <a href="#services" class="btn">Our Services</a>
        </div>
    """, unsafe_allow_html=True)

# FIX: Add Location and Hours More Clearly in Contact Section
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'><h2>Contact Us</h2><div class='divider'></div></div>", unsafe_allow_html=True)

st.markdown("""
    <div class="contact-info">
        <div class="contact-card">
            <h3 style="color: #1E3A5F; margin-top: 0;">Location</h3>
            <p style="font-size: 1rem; color: #333; line-height: 1.5;">
                📍 Greenhouse Plaza, 3rd Floor,<br> Ngong Road, Nairobi, Kenya
            </p>
        </div>

        <div class="contact-card">
            <h3 style="color: #1E3A5F; margin-top: 0;">Operating Hours</h3>
            <p style="font-size: 1rem; color: #333; line-height: 1.5;">
                📝 Monday - Friday: 9:00 AM - 6:00 PM<br>
                📅 Saturday: 10:00 AM - 2:00 PM<br>
                🛌 Sunday: Closed<br>
                <em style="color: #666;">Crisis support available 24/7</em>
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)

# FIX: Add map section (if not already there)
try:
    map_data = pd.DataFrame({'lat': [-1.2985], 'lon': [36.7848]})
    st.map(map_data, zoom=14, use_container_width=True)
except Exception as e:
    st.error("Unable to display map. Please check your internet connection or visit our center at Greenhouse Plaza, Ngong Road, Nairobi.")

# FIX: Mention Jerim in Footer as Founder
st.markdown("""
    <div class="footer">
        <div style="max-width: 1200px; margin: 0 auto;">
            <p style="color: white; text-align: center;">Founded by Jerim | © 2023 SafeSpace Organisation. All rights reserved.</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Remaining sections (team, services, testimonials, etc.) remain unchanged
# You can paste them back after this code if needed
