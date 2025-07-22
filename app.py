import streamlit as st
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
    <img src='https://images.unsplash.com/photo-1593608306764-9698f90d29cb?auto=format&fit=crop&w=1200&q=80' style='width: 100%; border-radius: 10px; margin-top: 2rem;' />
</div>
""", unsafe_allow_html=True)

# About Section
st.markdown("## About Safe Space Kenya")
st.write("""
    Founded in **2023**, Safe Space Kenya is dedicated to providing accessible mental health services to individuals and communities across Kenya.

    We believe that everyone deserves a safe, non-judgmental environment to explore their thoughts and emotions.

    Our mission is to break down barriers to mental healthcare and promote emotional wellbeing for all Kenyans.
""")
st.button("Meet Our Team")

# Services Section with Learn More and Details
st.markdown("## Our Therapeutic Services")
services = [
    {
        "icon": "👤", 
        "title": "Individual Counseling", 
        "desc": "Personalized sessions addressing depression, anxiety, and personal growth.",
        "details": "One-on-one sessions tailored to each client’s emotional journey. Focus is placed on creating a supportive environment where clients can freely express their thoughts and develop coping strategies."
    },
    {
        "icon": "👥", 
        "title": "Group Therapy", 
        "desc": "Supportive group healing for grief, addiction, and stress.",
        "details": "Brings individuals with shared experiences together to encourage healing through community support. Led by a trained therapist who ensures a safe and respectful atmosphere."
    },
    {
        "icon": "🏠", 
        "title": "Family Counseling", 
        "desc": "Improve communication and resolve conflicts among family members.",
        "details": "Helps families navigate challenges, improve communication, and strengthen relationships. Focuses on joint problem solving and mutual understanding."
    },
    {
        "icon": "🎓", 
        "title": "Workshops & Training", 
        "desc": "Programs for schools, companies, and community organizations.",
        "details": "Includes stress management, conflict resolution, mental wellness in the workplace, parenting skills, and youth mentorship. Can be customized for different settings."
    },
    {
        "icon": "📱", 
        "title": "Tele-therapy", 
        "desc": "Online counseling via video sessions from the comfort of your home.",
        "details": "Offers flexibility for clients who prefer remote sessions due to time, privacy, or travel limitations. Delivered securely via encrypted platforms."
    },
    {
        "icon": "❤️", 
        "title": "Trauma Support", 
        "desc": "Therapy for PTSD and trauma recovery.",
        "details": "Tailored support for survivors of abuse, accidents, or loss. Focused on rebuilding trust, safety, and resilience through trauma-informed care."
    }
]

cols = st.columns(3)
for i, service in enumerate(services):
    with cols[i % 3]:
        st.markdown(f"### {service['icon']} {service['title']}")
        st.write(service["desc"])
        with st.expander("Learn More"):
            st.write(service["details"])

# Team Section with resized images
st.markdown("## Meet Our Team")
team = [
    {
        "name": "Jerim Owino",
        "role": "Founder & CEO",
        "bio": "Clinical psychologist specializing in trauma therapy. PhD holder from UoN.",
        "img": "https://images.unsplash.com/photo-1603415526960-f8f76b6b3d33?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Hamdi Roble",
        "role": "Senior Therapist",
        "bio": "Specialist in culturally-sensitive CBT for anxiety and depression.",
        "img": "https://images.unsplash.com/photo-1598970434795-0c54fe7c0642?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Yvone Orina",
        "role": "Family Therapist",
        "bio": "Focuses on family therapy and relationship counseling.",
        "img": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Brian Kiprop",
        "role": "Art Therapist",
        "bio": "Helps clients express feelings through creative art and movement.",
        "img": "https://images.unsplash.com/photo-1590080876652-9980f5a761c0?auto=format&fit=crop&w=400&q=80"
    }
]

cols = st.columns(4)
for i, member in enumerate(team):
    with cols[i]:
        st.image(member["img"], width=200)
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
