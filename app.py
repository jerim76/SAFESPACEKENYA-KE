import streamlit as st
from datetime import datetime
import re
import base64
import pandas as pd

# ... (all the CSS code remains the same) ...

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "mood_history" not in st.session_state:
    st.session_state.mood_history = []
if "outreach_form_data" not in st.session_state:
    st.session_state.outreach_form_data = {"name": "", "email": "", "phone": "", "experience": "", "skills": [], "role": "Any"}
if "event_form_data" not in st.session_state:
    st.session_state.event_form_data = {"name": "", "email": "", "phone": "", "experience": "", "skills": []}
if "partnership_form_data" not in st.session_state:
    st.session_state.partnership_form_data = {"name": "", "organization": "", "email": "", "phone": "", "type": "Partner"}
if "counseling_form_data" not in st.session_state:
    st.session_state.counseling_form_data = {"name": "", "email": "", "phone": "", "type": "Online"}

# ... (rest of the functions remain the same) ...

# SERVICES SECTION
st.markdown("<div id='services'></div>", unsafe_allow_html=True)
st.markdown("## Our Therapeutic Services")
st.markdown("A comprehensive suite of evidence-based therapies by 15 certified professionals with over 75 years of combined experience, tailored to diverse mental health needs.")
services = [
    # ... (service definitions remain the same) ...
]
for service in services:
    st.markdown(f"""
    <div class='service-card'>
        <h3>{service['title']}</h3>
        <p>{service['desc']}</p>
    </div>
    """, unsafe_allow_html=True)
    
st.markdown("<div id='counseling-form'></div>", unsafe_allow_html=True)
with st.form("counseling_form", clear_on_submit=True):
    name = st.text_input("Full Name")
    email = st.text_input("Email", placeholder="your.email@example.com")
    phone = st.text_input("Phone", placeholder="+254 XXX XXX XXX")
    counseling_type = st.selectbox("Counseling Type", ["Online", "In-Person"])
    submit = st.form_submit_button("Register")
    
    if submit:
        # Validate all fields are filled
        if not all([name, email, phone]):
            st.error("Please fill in all fields")
        # Validate email format
        elif not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            st.error("Please enter a valid email address")
        # Validate phone format (basic Kenya format)
        elif not re.match(r"^\+?254\d{9}$|^0\d{9}$", phone.replace(" ", "")):
            st.error("Please enter a valid Kenyan phone number (+254XXXXXXXXX or 07XXXXXXXX)")
        else:
            # Store form data
            st.session_state.counseling_form_data = {
                "name": name,
                "email": email,
                "phone": phone,
                "type": counseling_type
            }
            st.success("Thank you for registering! We will contact you within 24 hours to schedule your session")

# ... (rest of your app code continues here) ...
