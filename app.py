import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Safe Space Kenya",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hero Section
st.markdown("""
<div style='text-align: center; padding: 4rem 2rem; background: linear-gradient(rgba(42,122,124,0.85), rgba(42,122,124,0.9)); border-radius: 10px; color: white;'>
    <h1 style='font-size: 3rem;'>Healing Minds, Restoring Lives</h1>
    <p style='font-size: 1.2rem; max-width: 800px; margin: auto;'>Safe Space Kenya provides professional, confidential counseling and mental health services in a supportive environment.</p>
</div>
""", unsafe_allow_html=True)

# About Section
st.markdown("## About Safe Space Kenya")
col1, col2 = st.columns(2)
with col1:
    st.write("""
        Founded in **2023**, Safe Space Kenya is dedicated to providing accessible mental health services to individuals and communities across Kenya.

        We believe that everyone deserves a safe, non-judgmental environment to explore their thoughts and emotions.

        Our mission is to break down barriers to mental healthcare and promote emotional wellbeing for all Kenyans.
    """)
    st.button("Meet Our Team")

with col2:
    st.markdown("<div style='background:#2a7a7c; color:white; height:300px; border-radius:10px; display:flex; align-items:center; justify-content:center; font-size:4rem;'>❤️</div>", unsafe_allow_html=True)

# Services Section (with images + learn more)
st.markdown("## 🌿 Our Therapeutic Services")

services = [
    {
        "icon": "👤",
        "title": "Individual Counseling",
        "desc": "One-on-one sessions to support clients with anxiety, depression, trauma, or stress.",
        "img": "https://images.unsplash.com/photo-1611691547574-b4e0ceff6ec0?auto=format&fit=crop&w=400&q=80",
        "more": "We offer personal therapy for those facing life challenges, helping clients build resilience, self-awareness, and emotional wellness. Each session is private and tailored to your pace."
    },
    {
        "icon": "👥",
        "title": "Group Therapy",
        "desc": "Support groups for shared experiences like grief, addiction, or social anxiety.",
        "img": "https://images.unsplash.com/photo-1559027615-cdcbcb0f3c4c?auto=format&fit=crop&w=400&q=80",
        "more": "Group therapy promotes peer support, trust, and mutual healing. Ideal for people going through similar emotional experiences and looking to feel less isolated."
    },
    {
        "icon": "🏠",
        "title": "Family & Couples Counseling",
        "desc": "Therapy to improve communication, trust, and family relationships.",
        "img": "https://images.unsplash.com/photo-1607746882042-944635dfe10e?auto=format&fit=crop&w=400&q=80",
        "more": "We help families and couples resolve conflict, improve parenting, and strengthen connection. Sessions are respectful, neutral, and focused on healing."
    },
    {
        "icon": "🎓",
        "title": "Workshops & Training",
        "desc": "Programs for schools, companies, and organizations on emotional health.",
        "img": "https://images.unsplash.com/photo-1600880292089-90a7e086ee5a?auto=format&fit=crop&w=400&q=80",
        "more": "We offer interactive sessions on stress management, burnout prevention, youth empowerment, and mental health literacy. Perfect for staff wellness or student development."
    },
    {
        "icon": "📱",
        "title": "Tele-therapy",
        "desc": "Online sessions via video or phone for remote access and flexibility.",
        "img": "https://images.unsplash.com/photo-1581093588401-12f1c7b4c8b0?auto=format&fit=crop&w=400&q=80",
        "more": "Distance should not limit healing. Access our licensed counselors securely from home using your mobile, tablet, or computer—ideal for busy schedules or remote areas."
    },
    {
        "icon": "❤️",
        "title": "Trauma Recovery & Crisis Support",
        "desc": "Therapy for survivors of violence, abuse, loss, or accidents.",
        "img": "https://images.unsplash.com/photo-1610471800434-7481b90a3b5f?auto=format&fit=crop&w=400&q=80",
        "more": "We provide a safe space to process trauma and rebuild a sense of control. Our therapists are trained in trauma-informed care and crisis de-escalation."
    }
]

cols = st.columns(3)
for i, service in enumerate(services):
    with cols[i % 3]:
        st.image(service["img"], use_column_width=True)
        st.markdown(f"### {service['icon']} {service['title']}")
        st.write(service["desc"])
        with st.expander("Learn More"):
            st.write(service["more"])

# Team Section
st.markdown("## Meet Our Team")
team = [
    {
        "name": "Jerim Owino",
        "role": "Founder & CEO",
        "bio": "Clinical psychologist specializing in trauma therapy. PhD holder from UoN.",
        "img": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Hamdi Roble",
        "role": "Senior Therapist",
        "bio": "Specialist in culturally-sensitive CBT for anxiety and depression.",
        "img": "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7b?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Yvone Orina",
        "role": "Family Therapist",
        "bio": "Focuses on family therapy and relationship counseling.",
        "img": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Brian Kiprop",
        "role": "Art Therapist",
        "bio": "Helps clients express feelings through creative art and movement.",
        "img": "https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&w=400&q=80"
    }
]

cols = st.columns(4)
for i, member in enumerate(team):
    with cols[i]:
        st.image(member["img"], width=150)
        st.markdown(f"**{member['name']}**  \n*{member['role']}*")
        st.caption(member["bio"])

# Testimonials
st.markdown("## Client Testimonials")
testimonials = [
    ("Wanjiru M.", "Safe Space Kenya respected my cultural background. Very professional."),
    ("David O.", "Family counseling helped us reconnect and improve communication."),
    ("Aisha K.", "I appreciated the faith-sensitive approach to managing anxiety."),
    ("Samuel T.", "Trauma support helped me rebuild after an accident.")
]
cols = st.columns(2)
for i, (name, quote) in enumerate(testimonials):
    with cols[i % 2]:
        st.markdown(f"**{name}**")
        st.info(f"_{quote}_")

# Contact Section
st.markdown("## Contact Us")
col1, col2 = st.columns(2)
with col1:
    st.write("📍 Greenhouse Plaza, Ngong Road, Nairobi")
    st.write("📞 +254 781 095 919 | +254 720 987 654")
    st.write("✉️ info@safespacekenya.org")
    st.write("🕒 Mon-Fri: 8AM - 7PM | Sat: 9AM - 4PM")

with col2:
    st.subheader("Book an Appointment")
    with st.form("appointment_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        service = st.selectbox("Service", [s["title"] for s in services])
        date = st.date_input("Preferred Date", min_value=datetime.today())
        message = st.text_area("Message")
        submit = st.form_submit_button("Submit")
        if submit:
            st.success(f"Thanks {name}, your request has been received!")

# Footer
st.markdown("---")
st.markdown("© 2023 Safe Space Kenya | Designed with ❤️ for mental wellness", unsafe_allow_html=True)
