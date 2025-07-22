import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="SafeSpace Kenya",
    page_icon="🧠",
    layout="wide",
)

# TITLE BAR
st.title("SafeSpace Kenya")
st.subheader("Empowering Minds, Nurturing Hope")

# HERO SECTION
st.markdown("""
<div style='text-align: center; padding: 3rem 1rem; background: linear-gradient(rgba(42,122,124,0.85), rgba(42,122,124,0.9)); border-radius: 10px; color: white;'>
    <h1>Healing Minds, Restoring Lives</h1>
    <p style='font-size: 1.1rem;'>SafeSpace Kenya provides professional, confidential counseling and mental health services in a supportive environment.</p>
    <img src='https://images.unsplash.com/photo-1616587892354-a1b3f2a4ba49?auto=format&fit=crop&w=1000&q=80' style='width: 90%; border-radius: 10px; margin-top: 2rem;'/>
</div>
""", unsafe_allow_html=True)

# ABOUT SECTION
st.markdown("## About SafeSpace Kenya")
st.write("""
**SafeSpace Kenya** is a mental health and wellness center founded in 2023 with the goal of offering culturally-appropriate, accessible mental health care for all Kenyans. 
We provide both in-person and tele-counseling services delivered by qualified mental health professionals.
""")

# SERVICES SECTION
st.markdown("## Our Therapeutic Services")
services = [
    {"icon": "👤", "title": "Individual Counseling", "desc": "Personalized sessions addressing depression, anxiety, and personal growth.", "info": "One-on-one counseling tailored to help you understand emotions, build coping strategies, and grow."},
    {"icon": "👥", "title": "Group Therapy", "desc": "Supportive group healing for grief, addiction, and stress.", "info": "Connect with others who share similar experiences in a safe and structured group."},
    {"icon": "🏠", "title": "Family Counseling", "desc": "Improve communication and resolve conflicts among family members.", "info": "Strengthen family bonds and resolve generational or marital issues collaboratively."},
    {"icon": "🎓", "title": "Workshops & Training", "desc": "Programs for schools, companies, and community organizations.", "info": "We offer workplace wellness sessions, student resilience training, and community empowerment workshops."},
    {"icon": "📱", "title": "Tele-therapy", "desc": "Online counseling via video sessions from the comfort of your home.", "info": "Confidential therapy from anywhere via Zoom or WhatsApp."},
    {"icon": "❤️", "title": "Trauma Support", "desc": "Therapy for PTSD and trauma recovery.", "info": "Guided therapy to heal from physical, emotional, or psychological trauma."}
]

cols = st.columns(3)
for i, service in enumerate(services):
    with cols[i % 3]:
        st.markdown(f"### {service['icon']} {service['title']}")
        st.write(service["desc"])
        with st.expander("Learn More"):
            st.write(service["info"])

# TEAM SECTION
st.markdown("## Meet Our Team")
team = [
    {
        "name": "Jerim Owino",
        "role": "Founder & CEO",
        "bio": "Clinical psychologist specializing in trauma therapy. PhD holder from UoN.",
        "img": "https://images.generated.photos/MaleBlack1.jpg"
    },
    {
        "name": "Hamdi Roble",
        "role": "Senior Therapist",
        "bio": "Specialist in culturally-sensitive CBT for anxiety and depression.",
        "img": "https://images.generated.photos/FemaleBlack1.jpg"
    },
    {
        "name": "Yvone Orina",
        "role": "Family Therapist",
        "bio": "Focuses on family therapy and relationship counseling.",
        "img": "https://images.unsplash.com/photo-1551836022-d5d88e9218df?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Brian Kiprop",
        "role": "Art Therapist",
        "bio": "Helps clients express feelings through creative art and movement.",
        "img": "https://images.generated.photos/MaleBlack2.jpg"
    }
]

cols = st.columns(4)
for i, member in enumerate(team):
    with cols[i]:
        st.image(member["img"], caption=member["name"], use_container_width=True)
        st.markdown(f"**{member['name']}**  \n*{member['role']}*")
        st.caption(member["bio"])

# TESTIMONIALS
st.markdown("## Client Testimonials")
testimonials = [
    ("Wanjiru M.", "SafeSpace Kenya respected my cultural background. Very professional."),
    ("David O.", "Family counseling helped us reconnect and improve communication."),
    ("Aisha K.", "I appreciated the faith-sensitive approach to managing anxiety."),
    ("Samuel T.", "Trauma support helped me rebuild after an accident.")
]
cols = st.columns(2)
for i, (name, quote) in enumerate(testimonials):
    with cols[i % 2]:
        st.markdown(f"**{name}**")
        st.info(f"_{quote}_")

# CONTACT SECTION
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

# FOOTER
st.markdown("---")
st.markdown("""
<div style='text-align: center; font-size: 0.9rem;'>
    <p>© 2023 SafeSpace Kenya | Designed with ❤️ for mental wellness</p>
    <a href='https://facebook.com' target='_blank'>🌐 Facebook</a> |
    <a href='https://instagram.com' target='_blank'>📷 Instagram</a> |
    <a href='https://twitter.com' target='_blank'>🐦 Twitter</a> |
    <a href='https://linkedin.com' target='_blank'>💼 LinkedIn</a>
</div>
""", unsafe_allow_html=True)
