import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Safe Space Kenya",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Header section
st.markdown("""
<div style='text-align: center; padding: 4rem 2rem; background: linear-gradient(rgba(42,122,124,0.85), rgba(42,122,124,0.9)); border-radius: 10px; color: white;'>
    <h1 style='font-size: 3rem;'>Healing Minds, Restoring Lives</h1>
    <p style='font-size: 1.2rem; max-width: 800px; margin: auto;'>Safe Space Kenya provides professional, confidential counseling and mental health services in a supportive environment.</p>
</div>
""", unsafe_allow_html=True)

# About Section
st.header("About Safe Space Kenya")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    Founded in **2023**, Safe Space Kenya is dedicated to providing accessible mental health services to individuals and communities across Kenya.

    We believe that everyone deserves a safe, non-judgmental environment to explore their thoughts and emotions.

    Our mission is to break down barriers to mental healthcare and promote emotional wellbeing for all Kenyans.
    """)
    st.button("Meet Our Team")

with col2:
    st.markdown("""
    <div style='background:#2a7a7c; color:white; height:300px; border-radius:10px; display:flex; align-items:center; justify-content:center; font-size:4rem;'>❤️</div>
    """, unsafe_allow_html=True)

# Services Section
st.header("Our Therapeutic Services")
services = [
    ("👤", "Individual Counseling", "Personalized sessions addressing depression, anxiety, personal development, grief, and trauma."),
    ("👥", "Group Therapy", "Supportive group healing for grief, addiction, stress, and shared experiences."),
    ("🏠", "Family Counseling", "Improve communication, resolve conflicts, and strengthen family bonds."),
    ("🧒", "Child and Adolescent Therapy", "Helping young individuals navigate emotional and behavioral challenges."),
    ("🧕", "Faith-Sensitive Counseling", "Islamic and Christian-friendly counseling options that respect faith-based values."),
    ("🎓", "Workshops & Training", "Mental health awareness programs for schools, corporates, and community groups."),
    ("📱", "Tele-therapy", "Access therapy from anywhere via secure video sessions."),
    ("❤️", "Trauma & Crisis Support", "Immediate and long-term support for those dealing with traumatic events."),
    ("🧠", "Psychological Assessments", "Mental health evaluations, diagnostics, and wellness check-ins.")
]

cols = st.columns(3)
for i, (icon, title, desc) in enumerate(services):
    with cols[i % 3]:
        st.subheader(f"{icon} {title}")
        st.write(desc)

# Team Section
st.header("Meet Our Team")
teams = [
    {"name": "Jerim Owino", "role": "Founder & CEO", "bio": "Clinical psychologist specializing in trauma therapy. PhD holder from UoN.",
     "img": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80"},
    {"name": "Hamdi Roble", "role": "Senior Therapist", "bio": "Muslim therapist specializing in culturally-sensitive CBT for anxiety and depression.",
     "img": "https://images.unsplash.com/photo-1607746882042-944635dfe10e?auto=format&fit=crop&w=400&q=80"},
    {"name": "Yvone Orina", "role": "Family Therapist", "bio": "Focuses on family therapy and relationship counseling.",
     "img": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=400&q=80"},
    {"name": "Brian Kiprop", "role": "Art Therapist", "bio": "Helps clients express feelings through creative art and movement.",
     "img": "https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&w=400&q=80"}
]

cols = st.columns(4)
for i, member in enumerate(teams):
    with cols[i]:
        st.image(member["img"], width=150)
        st.markdown(f"**{member['name']}**\n\n*{member['role']}*")
        st.caption(member["bio"])

# Testimonials
st.header("Client Testimonials")
testimonials = [
    ("Wanjiru M., Nairobi", "Safe Space Kenya respected my cultural background. Very professional."),
    ("David O., Mombasa", "Family counseling helped us reconnect and improve communication."),
    ("Aisha K., Kisumu", "I appreciated the faith-sensitive approach to managing anxiety."),
    ("Samuel T., Nakuru", "Trauma support helped me rebuild after an accident.")
]
cols = st.columns(2)
for i, (name, quote) in enumerate(testimonials):
    with cols[i % 2]:
        st.markdown(f"**{name}**")
        st.info(f"_{quote}_")

# Contact Section
st.header("Contact Us")
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
        service = st.selectbox("Service", [s[1] for s in services])
        date = st.date_input("Preferred Date", min_value=datetime.today())
        message = st.text_area("Message")
        submit = st.form_submit_button("Submit")
        if submit:
            st.success(f"Thanks {name}, your request has been received!")

# Footer
st.markdown("---")
st.markdown("© 2023 Safe Space Kenya | Designed with ❤️ for mental wellness")
