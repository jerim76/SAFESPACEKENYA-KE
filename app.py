import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Safe Space Kenya",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Title Section
st.markdown("<h1 style='text-align: center; color: #2A7A7C;'>Safe Space Kenya</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Empowering Minds, Nurturing Hope</h4>", unsafe_allow_html=True)

# About Section
st.markdown("## About Us")
st.write("""
At **Safe Space Kenya**, we are committed to breaking the stigma around mental health and providing inclusive, accessible, and compassionate counseling services to individuals, families, and communities.

We believe mental wellness is a human right. Our trained professionals create a safe, confidential environment where healing can begin.
""")

# Hero Section (counseling image)
st.markdown("""
<div style='text-align: center; padding: 3rem 1rem; background: linear-gradient(rgba(42,122,124,0.85), rgba(42,122,124,0.9)); border-radius: 10px; color: white;'>
    <h2 style='font-size: 2.5rem;'>Healing Minds, Restoring Lives</h2>
    <p style='font-size: 1.1rem; max-width: 800px; margin: auto;'>We offer professional and confidential therapy, both in-person and online, with cultural and spiritual sensitivity.</p>
    <img src='https://images.unsplash.com/photo-1593608306764-9698f90d29cb?auto=format&fit=crop&w=1200&q=80' style='width: 100%; border-radius: 10px; margin-top: 2rem;' />
</div>
""", unsafe_allow_html=True)

# Services Section
st.markdown("## Our Therapeutic Services")
services = [
    {"icon": "👤", "title": "Individual Counseling", "desc": "Personalized sessions addressing depression, anxiety, and personal growth.",
     "details": "Explore your thoughts and emotions in a safe one-on-one setting with a professional therapist."},
    {"icon": "👥", "title": "Group Therapy", "desc": "Supportive group healing for grief, addiction, and stress.",
     "details": "Join group discussions guided by therapists where you connect with others on similar journeys."},
    {"icon": "🏠", "title": "Family Counseling", "desc": "Improve communication and resolve conflicts among family members.",
     "details": "Build stronger relationships with your loved ones through open dialogue and expert guidance."},
    {"icon": "🎓", "title": "Workshops & Training", "desc": "Programs for schools, companies, and community organizations.",
     "details": "We offer customized training sessions on mental wellness, stress management, and leadership."},
    {"icon": "📱", "title": "Tele-therapy", "desc": "Online counseling via video sessions from the comfort of your home.",
     "details": "Flexible therapy options that fit your schedule, using secure video platforms."},
    {"icon": "❤️", "title": "Trauma Support", "desc": "Therapy for PTSD and trauma recovery.",
     "details": "Evidence-based care for those healing from emotional or physical trauma."}
]

cols = st.columns(3)
for i, service in enumerate(services):
    with cols[i % 3]:
        st.markdown(f"### {service['icon']} {service['title']}")
        st.write(service["desc"])
        with st.expander("Learn More"):
            st.write(service["details"])

# Team Section
st.markdown("## Meet Our Team")
team = [
    {"name": "Jerim Owino", "role": "Founder & CEO", "bio": "Clinical psychologist specializing in trauma therapy. PhD holder from UoN.",
     "img": "https://images.unsplash.com/photo-1603415526983-7c37e4c30e94?auto=format&fit=crop&w=400&q=80"},
    {"name": "Hamdi Roble", "role": "Senior Therapist", "bio": "Specialist in culturally-sensitive CBT for anxiety and depression.",
     "img": "https://images.unsplash.com/photo-1614285662404-b2d25d7602b4?auto=format&fit=crop&w=400&q=80"},
    {"name": "Yvone Orina", "role": "Family Therapist", "bio": "Focuses on family therapy and relationship counseling.",
     "img": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=400&q=80"},
    {"name": "Brian Kiprop", "role": "Art Therapist", "bio": "Helps clients express feelings through creative art and movement.",
     "img": "https://images.unsplash.com/photo-1573497019413-5644ffbbb03b?auto=format&fit=crop&w=400&q=80"}
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

# Contact Us
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

# Footer with Social Media
st.markdown("---")
st.markdown("### Connect With Us", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; font-size: 24px;'>
    <a href='https://www.facebook.com/' target='_blank'>🌐 Facebook</a> &nbsp;&nbsp;&nbsp;
    <a href='https://www.instagram.com/' target='_blank'>📸 Instagram</a> &nbsp;&nbsp;&nbsp;
    <a href='https://www.linkedin.com/' target='_blank'>💼 LinkedIn</a> &nbsp;&nbsp;&nbsp;
    <a href='https://twitter.com/' target='_blank'>🐦 Twitter</a>
</div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: gray;'>© 2023 Safe Space Kenya | Designed with ❤️ for mental wellness</p>", unsafe_allow_html=True)
