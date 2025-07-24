import streamlit as st
from datetime import datetime
import re
import base64
import pandas as pd

# Custom CSS for enhanced styling and mobile responsiveness
st.markdown("""
<style>
    :root {
        --primary: #26A69A;
        --accent: #FF6F61;
        --light: #e6f3f5;
        --dark: #2c3e50;
        --deep-blue: #1E3A8A;
    }
    .stApp {
        background-color: var(--light);
        background-image: url('https://www.transparenttextures.com/patterns/subtle-white-feathers.png');
        font-family: 'Inter', sans-serif;
        color: var(--dark);
        min-height: 100vh;
        width: 100%;
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    h1, h2, h3, h4 {
        font-family: 'Playfair Display', serif;
        color: var(--deep-blue) !important;
        text-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }
    h1 { font-size: 2.2rem; }
    h2 { font-size: 1.8rem; }
    h3 { font-size: 1.4rem; }
    h4 { font-size: 1.2rem; }
    .service-card, .testimonial-card, .event-card, .partnership-card, .blog-card, .tracker-card, .volunteer-card, .founder-card {
        background: white;
        padding: 0.8rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 0.5rem;
    }
    .primary-btn {
        background: linear-gradient(135deg, var(--primary), #4DB6AC);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        border: none;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
        font-size: 0.9rem;
    }
    .primary-btn:hover {
        background: linear-gradient(135deg, var(--accent), #FF8A80);
        transform: translateY(-2px);
    }
    .stButton > button {
        background: linear-gradient(135deg, var(--primary), #4DB6AC);
        color: white;
        border-radius: 20px;
        border: none;
        padding: 0.5rem 1rem;
        font-size: 0.9rem;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, var(--accent), #FF8A80);
    }
    .st-expander {
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        background: #f9f9f9;
        margin-bottom: 0.5rem;
    }
    .footer {
        text-align: center;
        padding: 1rem;
        background: #e8f4f8;
        border-top: 1px solid #ddd;
        margin-top: 1rem;
    }
    .cta-banner {
        background: linear-gradient(135deg, var(--primary), #4DB6AC);
        color: white;
        text-align: center;
        padding: 0.8rem;
    }
    .chatbot-container {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 300px;
        max-height: 400px;
        overflow-y: auto;
        z-index: 1000;
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        display: none;
    }
    .chatbot-container.active {
        display: block;
    }
    .chatbot-message.user {
        background: #e8f4f8;
        text-align: right;
        color: var(--dark);
        padding: 0.5rem;
        margin: 0.5rem 0;
        border-radius: 6px;
        font-size: 0.9rem;
    }
    .chatbot-message.bot {
        background: white;
        text-align: left;
        color: var(--primary);
        padding: 0.5rem;
        margin: 0.5rem 0;
        border-radius: 6px;
        border-left: 3px solid var(--primary);
        font-size: 0.9rem;
    }
    .chatbot-input {
        width: 100%;
        padding: 0.5rem;
        border: 1px solid #e0e0e0;
        border-radius: 6px;
        margin-top: 0.5rem;
        font-size: 0.9rem;
    }
    .chatbot-toggle {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 1001;
        background: linear-gradient(135deg, var(--primary), #4DB6AC);
        color: white;
        border: none;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        font-size: 1.2rem;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    .chatbot-toggle:hover {
        background: linear-gradient(135deg, var(--accent), #FF8A80);
    }
    html {
        scroll-behavior: smooth;
    }
    @media (max-width: 768px) {
        .stColumn {
            width: 100% !important;
            margin: 0 !important;
            padding: 0 !important;
        }
        .service-card, .testimonial-card, .event-card, .partnership-card, .blog-card, .tracker-card, .volunteer-card, .founder-card {
            margin: 0.3rem 0;
            width: 100% !important;
            padding: 0.5rem;
        }
        h1 { font-size: 1.6rem; }
        h2 { font-size: 1.4rem; }
        h3 { font-size: 1.2rem; }
        h4 { font-size: 1.0rem; }
        .chatbot-container {
            width: 90%;
            right: 5%;
            bottom: 70px;
            max-height: 300px;
        }
        .chatbot-toggle {
            bottom: 20px;
            right: 5%;
            width: 40px;
            height: 40px;
            font-size: 1rem;
        }
        img {
            max-width: 100% !important;
            height: auto !important;
        }
        .cta-banner {
            padding: 0.5rem;
        }
        .st-expander {
            margin: 0.3rem 0;
        }
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="SafeSpace Kenya",
    page_icon="🧠",
    layout="wide",
)

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "mood_history" not in st.session_state:
    st.session_state.mood_history = []
if "outreach_form_data" not in st.session_state:
    st.session_state.outreach_form_data = {"name": "", "email": "", "phone": "", "experience": "", "skills": [], "role": "Any"}
if "event_form_data" not in st.session_state:
    st.session_state.event_form_data = {"name": "", "email": "", "phone": "", "experience": "", "skills": []}

# Function to create download link
def get_download_link(file_content, file_name):
    b64 = base64.b64encode(file_content.encode()).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_name}" class="primary-btn" style="display: block; text-align: center; margin-top: 0.5rem;">Download</a>'
    return href

# Function to export mood history
def export_mood_history():
    df = pd.DataFrame(st.session_state.mood_history, columns=["Date", "Mood", "Note"])
    df["Date"] = df["Date"].apply(lambda x: x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime) else x)
    csv = df.to_csv(index=False)
    return csv

# Chatbot knowledge base
knowledge_base = [
    {"question": r"what is safespace kenya\??", "answer": "SafeSpace Kenya, founded in 2023 by Jerim Owino and Hamdi Roble, is a non-profit providing accessible, culturally-appropriate mental health care across Kenya, serving urban and rural areas with counseling, therapy, and outreach."},
    {"question": r"what services do you offer\??", "answer": "We offer Individual Counseling, Group Therapy, Family Counseling, and Trauma Recovery Therapy, using methods like CBT, EMDR, and mindfulness, available in-person, online, or via mobile units."},
    {"question": r"how can i contact you\??", "answer": "Contact us at +254 781 095 919 (8 AM-7 PM EAT) or info@safespacekenya.org (24-hour response). Visit Greenhouse Plaza, Ngong Road, Nairobi, or book online."},
    {"question": r"what are your hours\??", "answer": "Office hours are Mon-Fri 9 AM-5 PM, Sat 10 AM-2 PM, closed Sundays and holidays. Crisis line is 8 AM-7 PM EAT."},
    {"question": r"how much does it cost\??", "answer": "Fees range from KSh 500-2,000 per session on a sliding scale, with subsidies and free workshops for low-income clients."},
    {"question": r"who are the founders\??", "answer": "Our founders are Jerim Owino, a trauma specialist with a PhD, and Hamdi Roble, a cultural therapy expert with a Master’s in Public Health."},
    {"question": r"what events are coming up\??", "answer": "Upcoming events include a Stress Management Workshop on July 30, 2025, in Nairobi, and a Youth Mental Health Forum on August 15, 2025, in Kisumu. Register at events@safespacekenya.org."},
    {"question": r"how can i volunteer\??", "answer": "Volunteer roles include Outreach Support, Event Volunteer, and Crisis Line Assistant. Register via the Volunteer form on this page with your details and preferred role."},
    {"question": r"what is the crisis line\??", "answer": "Our Crisis Line is +254 781 095 919 (8 AM-7 PM EAT), with Befrienders Kenya at 1199 available 24/7 for emergencies."},
    {"default": "I'm sorry, I didn’t understand that. Please ask about our services, contact details, hours, costs, founders, events, volunteering, or crisis support, or visit the Contact section for more help. Current time: 12:00 AM EAT, July 25, 2025."}
]

# Function to get chatbot response
def get_chatbot_response(query):
    query = query.lower()
    for entry in knowledge_base:
        if "question" in entry and re.search(entry["question"], query):
            return entry["answer"]
    return knowledge_base[-1]["default"]

# HEADER
st.markdown("""
<div style='text-align: center; padding: 0.8rem; background: var(--primary); color: white;'>
    <h1>SafeSpace Kenya</h1>
    <p>Empowering Minds, Nurturing Hope Since 2023 | Updated: 12:00 AM EAT, July 25, 2025</p>
</div>
""", unsafe_allow_html=True)

# HERO SECTION
st.markdown("<div id='hero'></div>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding: 0.8rem; background: linear-gradient(rgba(38,166,154,0.9), rgba(77,182,172,0.9)); border-radius: 8px; color: white;'>
    <h1>Healing Minds, Restoring Lives</h1>
    <p style='font-size: 1rem; max-width: 100%; margin: 0.5rem auto;'>SafeSpace Kenya offers professional, confidential counseling in a culturally-sensitive environment, serving all Kenyan communities.</p>
    <img src='https://images.unsplash.com/photo-1588195539435-d6b5f19e1c24?auto=format&fit=crop&w=600&q=80' style='width: 100%; max-width: 600px; border-radius: 8px; margin: 0.5rem auto; box-shadow: 0 2px 4px rgba(0,0,0,0.2);' alt='Counseling outreach session'/>
    <div style='display: flex; justify-content: center; gap: 0.5rem; flex-wrap: wrap;'>
        <a href='#about' class='primary-btn'>About Us</a>
        <a href='#services' class='primary-btn'>Our Services</a>
        <a href='#events' class='primary-btn'>Upcoming Events</a>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Our Mission", expanded=False):
    st.markdown("""
    - **Mission**: Break mental health stigma and provide affordable care.
    - **Vision**: A thriving Kenya with emotional support for all.
    - **Contact**: info@safespacekenya.org or +254 781 095 919.
    - **Impact**: 600+ clients in 2025, 90% satisfaction.
    """)

# ABOUT SECTION
st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.markdown("## About SafeSpace Kenya")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p><strong>SafeSpace Kenya</strong>, founded in 2023 by Jerim Owino and Hamdi Roble, provides accessible mental health care. With 15 professionals, we serve Nairobi, Kisumu, Eldoret, and more, addressing trauma, depression, and family issues via multiple channels.</p>
    <p>We blend Kenyan traditions with modern therapies, partnering with NGOs and the Ministry of Health to reach 20+ districts, focusing on inclusivity.</p>
    <a href='#services' class='primary-btn'>Explore Our Services</a>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Our History", expanded=False):
    st.markdown("""
    - **Founding**: 2022 Nakuru pilot aided 50, leading to 2023 launch.
    - **Growth**: 2 to 15 staff, aiming for 20 by 2025 end.
    - **Awards**: 2024 Health Federation Award, 2025 Global Grant.
    - **Team**: Specialists in child, trauma, and cultural therapy.
    """)

# FOUNDERS SECTION
st.markdown("<div id='founders'></div>", unsafe_allow_html=True)
st.markdown("## Our Founders")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <div class='founder-card'>
        <h4>Jerim Owino</h4>
        <p>PhD holder with 12 years’ experience, specializes in trauma and refugee care, driving outreach programs.</p>
    </div>
    <div class='founder-card'>
        <h4>Hamdi Roble</h4>
        <p>Master’s in Public Health, 8 years’ experience, leads cultural therapy and rural expansion.</p>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Our Founders", expanded=False):
    st.markdown("""
    - **Jerim**: 10+ papers, mentored 20 psychologists.
    - **Hamdi**: Trained 100+ leaders, developed cultural model.
    - **Collaboration**: Jointly shaped SafeSpace’s approach.
    - **Workshops**: Offer free sessions in underprivileged areas.
    """)

# SERVICES SECTION
st.markdown("<div id='services'></div>", unsafe_allow_html=True)
st.markdown("## Our Therapeutic Services")
st.markdown("Therapies by 15 certified professionals with 75+ years’ experience.")
services = [
    {"icon": "👤", "title": "Individual Counseling", "desc": "Sessions for depression, anxiety, PTSD using CBT, DBT, ACT, MBSR. 50 mins, in-person/online/mobile, with free consultation."},
    {"icon": "👥", "title": "Group Therapy", "desc": "Support for grief, addiction, PTSD. 90 mins weekly, max 10, with role-playing and meditations."},
    {"icon": "🏠", "title": "Family Counseling", "desc": "Resolves conflicts with systemic therapy, cultural techniques. 60 mins, in-person/online/home visits."},
    {"icon": "🧠", "title": "Trauma Recovery Therapy", "desc": "For violence survivors using EMDR, CBT. 75 mins, 6-session program, prioritizes refugees."}
]
for service in services:
    st.markdown(f"""
    <div class='service-card'>
        <h3>{service['icon']} {service['title']}</h3>
        <p>{service['desc']}</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; margin-top: 0.5rem;'>
    <a href='#blog' class='primary-btn'>Explore Our Blog</a>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Our Services", expanded=False):
    st.markdown("""
    - **Credentials**: Master’s or higher, multi-modal certified.
    - **Accessibility**: KSh 500-2,000, subsidies, free workshops.
    - **Feedback**: 95% improved, 85% continue (2024).
    - **Innovation**: AI tools for rural areas, Q4 2025.
    """)

# TESTIMONIALS SECTION
st.markdown("<div id='testimonials'></div>", unsafe_allow_html=True)
st.markdown("## What Our Clients Say")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <div class='testimonial-card'><p><em>'Counseling changed my life post-accident!'</em> - Jane K., Nairobi, 2025</p></div>
    <div class='testimonial-card'><p><em>'Group therapy helped my grief!'</em> - Peter O., Kisumu, 2025</p></div>
    <div class='testimonial-card'><p><em>'Family counseling was amazing!'</em> - Amina H., Eldoret, 2025</p></div>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Testimonials", expanded=False):
    st.markdown("""
    - **Verification**: Consent-based, verified clients.
    - **Diversity**: Urban, rural, all ages.
    - **Impact**: 200+ in 2025, yearly report planned.
    """)

# MENTAL HEALTH BLOG SECTION
st.markdown("<div id='blog'></div>", unsafe_allow_html=True)
st.markdown("## Mental Health Blog")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Articles by experts for wellbeing:</p>
""", unsafe_allow_html=True)
blogs = [
    {"title": "Coping with Economic Stress", "date": "July 20, 2025", "desc": "By Dr. Amina Hassan."},
    {"title": "Cultural Therapy in Kenya", "date": "July 15, 2025", "desc": "By Hamdi Roble."},
    {"title": "PTSD Survivor Guide", "date": "July 10, 2025", "desc": "By Dr. James Otieno."}
]
for blog in blogs:
    st.markdown(f"""
    <div class='blog-card'>
        <h4>{blog['title']}</h4>
        <p><strong>Date:</strong> {blog['date']}</p>
        <p>{blog['desc']}</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; margin-top: 0.5rem;'>
    <a href='#crisis' class='primary-btn'>Crisis Support 💨</a>
    <a href='#tracker' class='primary-btn'>Tracker 📊</a>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Our Blog", expanded=False):
    st.markdown("""
    - **Updates**: Bi-weekly, youth series August 2025.
    - **Panel**: Experts and advisors.
    - **Engagement**: Submit to blog@safespacekenya.org.
    - **Downloads**: Free PDFs.
    """)

# CRISIS RESOURCES SECTION
st.markdown("<div id='crisis'></div>", unsafe_allow_html=True)
st.markdown("## Crisis Resources")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Immediate support:</p>
    <ul>
        <li><strong>Befrienders Kenya:</strong> 1199, 24/7.</li>
        <li><strong>SafeSpace Crisis:</strong> +254 781 095 919, 8 AM-7 PM EAT.</li>
    </ul>
    <p>Emergency: Call 999 or visit a hospital.</p>
    <a href='#contact' class='primary-btn'>Get Help Now</a>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Crisis Support", expanded=False):
    st.markdown("""
    - **Training**: 40 hours annually.
    - **Partnerships**: Kenyatta Hospital.
    - **Confidentiality**: Encrypted calls.
    - **Resources**: Free pamphlets.
    """)

# PROGRESS TRACKER SECTION
st.markdown("<div id='tracker'></div>", unsafe_allow_html=True)
st.markdown("## Progress Tracker")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Track your mental health:</p>
    <div class='tracker-card'>
        <h4>Mood Tracker</h4>
        <p>Rate mood (1-5) and add notes.</p>
    </div>
""", unsafe_allow_html=True)
mood = st.slider("How do you feel? (1 = Low, 5 = High)", 1, 5, 3, key="mood_input")
note = st.text_input("Add a note", placeholder="e.g., Stressful day", key="mood_note")
if st.button("Log Mood"):
    st.session_state.mood_history.append({"date": datetime.now(), "mood": mood, "note": note})
    st.success(f"Logged at 12:00 AM EAT, July 25, 2025!")
for entry in st.session_state.mood_history[-5:]:
    st.markdown(f"- {entry['date'].strftime('%Y-%m-%d %H:%M')}: Mood {entry['mood']}/5 {'(' + entry['note'] + ')' if entry['note'] else ''}")
if st.button("Export Mood History"):
    csv = export_mood_history()
    st.markdown(get_download_link(csv, "mood_history.csv"), unsafe_allow_html=True)
st.markdown("""
    <a href='#volunteer' class='primary-btn'>Next: Volunteer</a>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Tracking", expanded=False):
    st.markdown("""
    - **Features**: Export as CSV.
    - **Usage**: Log daily for 30 days.
    - **Support**: support@safespacekenya.org.
    - **Privacy**: Secure access.
    """)

# VOLUNTEER OPPORTUNITIES SECTION
st.markdown("<div id='volunteer'></div>", unsafe_allow_html=True)
st.markdown("## Volunteer Opportunities")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Join our mission with training:</p>
""", unsafe_allow_html=True)
volunteer_roles = [
    {"title": "Outreach Support", "desc": "2-4 hr campaigns in Nakuru/Mombasa, 10-hr training."},
    {"title": "Event Volunteer", "desc": "4-6 hr support for July 30/August 15 events."},
    {"title": "Crisis Line Assistant", "desc": "8 AM-7 PM shifts, 20-hr training."}
]
for role in volunteer_roles:
    st.markdown(f"""
    <div class='volunteer-card'>
        <h4>{role['title']}</h4>
        <p>{role['desc']}</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; margin-top: 0.5rem;'>
    <a href='#volunteer-form' class='primary-btn'>Register to Volunteer</a>
</div>
""", unsafe_allow_html=True)
st.markdown("<div id='volunteer-form'></div>", unsafe_allow_html=True)
with st.form("volunteer_form", clear_on_submit=True):
    name = st.text_input("Full Name")
    email = st.text_input("Email", placeholder="your.email@example.com")
    phone = st.text_input("Phone", placeholder="+254 XXX XXX XXX")
    experience = st.text_area("Experience", placeholder="e.g., counseling")
    role_preference = st.selectbox("Role", ["Outreach Support", "Event Volunteer", "Crisis Line Assistant", "Any"])
    submit = st.form_submit_button("Register")
    if submit:
        if not all([name, email, re.match(r"[^@]+@[^@]+\.[^@]+", email), phone, experience]):
            st.error("Fill all fields.")
        else:
            st.session_state.outreach_form_data = {"name": name, "email": email, "phone": phone, "experience": experience, "role": role_preference}
            st.success(f"Thank you, {name}! Registered at 12:00 AM EAT, July 25, 2025. Contact at {email} within 48 hours.")
            st.session_state.outreach_form_data = {"name": "", "email": "", "phone": "", "experience": "", "role": "Any"}
st.markdown("""
<div style='text-align: center; margin-top: 0.5rem;'>
    <a href='#contact' class='primary-btn'>Contact Us 📞</a>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Volunteering", expanded=False):
    st.markdown("""
    - **Impact**: 1,200 in 2024, 2,000 target 2025.
    - **Training**: 10-hr online, 5-hr in-person.
    - **Recognition**: Certificates, Volunteer Day Dec 15, 2025.
    - **Support**: Monthly check-ins.
    """)

# EVENTS SECTION
st.markdown("<div id='events'></div>", unsafe_allow_html=True)
st.markdown("## Upcoming Events")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <div class='event-card'>
        <h4>Stress Management Workshop</h4>
        <p>July 30, 2025, 9 AM-1 PM, Nairobi Hall. Free, register at events@safespacekenya.org.</p>
    </div>
    <div class='event-card'>
        <h4>Youth Mental Health Forum</h4>
        <p>August 15, 2025, 10 AM-2 PM, Kisumu Center. Ages 13-25.</p>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Events", expanded=False):
    st.markdown("""
    - **Registration**: 50 per event, email required.
    - **Workshops**: Handouts, online Q&A.
    - **Past**: June 2025 Trauma Day, 80 attendees.
    - **Accessibility**: Sign language, wheelchair access.
    """)

# PARTNERSHIPS SECTION
st.markdown("<div id='partnerships'></div>", unsafe_allow_html=True)
st.markdown("## Our Partnerships")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <div class='partnership-card'>
        <h4>Kenyatta National Hospital</h4>
        <p>Referrals and trauma programs since 2024.</p>
    </div>
    <div class='partnership-card'>
        <h4>Kenya Red Cross</h4>
        <p>Disaster response training since 2023.</p>
    </div>
    <div class='partnership-card'>
        <h4>Ministry of Health</h4>
        <p>Policy support and rural funding.</p>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Partnerships", expanded=False):
    st.markdown("""
    - **Goals**: Train 100 workers by 2026.
    - **Projects**: Mobile clinic pilot, 2025.
    - **Benefits**: Training access, data insights.
    - **Expansion**: Seeking new partners.
    """)

# FAQ SECTION
st.markdown("<div id='faq'></div>", unsafe_allow_html=True)
st.markdown("## Frequently Asked Questions")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p><strong>Q: Ages?</strong> A: All ages, specialized programs.</p>
    <p><strong>Q: Confidentiality?</strong> A: Yes, encrypted, compliant.</p>
    <p><strong>Q: Payment?</strong> A: Cash, M-Pesa, subsidies.</p>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About FAQs", expanded=False):
    st.markdown("""
    - **Support**: faq@safespacekenya.org.
    - **Updates**: Quarterly, last July 2025.
    - **Resources**: Download FAQ PDF.
    """)

# CONTACT SECTION
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.markdown("## Contact Us")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p><strong>📍</strong> Greenhouse Plaza, Ngong Road, Nairobi.</p>
    <p><strong>📞</strong> +254 781 095 919, 8 AM-7 PM EAT.</p>
    <p><strong>✉️</strong> <a href='mailto:info@safespacekenya.org'>info@safespacekenya.org</a>, 24-hr response.</p>
    <p><strong>Hours:</strong> Mon-Fri 9 AM-5 PM, Sat 10 AM-2 PM.</p>
    <a href='#' class='primary-btn'>Book Consultation</a>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Contacting Us", expanded=False):
    st.markdown("""
    - **Appointments**: Online or call, same-day slots.
    - **Accessibility**: Wheelchair, sign language.
    - **Follow-Up**: Within one week.
    - **Map**: On our website.
    """)

# CHATBOT
st.markdown("""
<button class='chatbot-toggle' id='chatbot-toggle'>💬</button>
<div class='chatbot-container' id='chatbot'>
    <h4>Ask SafeSpace Bot</h4>
    <div id='chat-messages' style='max-height: 300px; overflow-y: auto; margin-bottom: 0.5rem;'>
""", unsafe_allow_html=True)
for sender, message in st.session_state.chat_history:
    st.markdown(f"<div class='chatbot-message {sender}'><p>{message}</p></div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("", placeholder="Ask me anything...", key="chat_input")
    submit = st.form_submit_button("Send")
    if submit and user_input:
        response = get_chatbot_response(user_input)
        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("bot", response))
st.markdown("</div>", unsafe_allow_html=True)

# JavaScript to toggle chatbot
st.markdown("""
<script>
    document.addEventListener('DOMContentLoaded', function() {
        const toggleButton = document.getElementById('chatbot-toggle');
        const chatbot = document.getElementById('chatbot');
        if (toggleButton && chatbot) {
            toggleButton.addEventListener('click', function() {
                chatbot.classList.toggle('active');
            });
        }
    });
</script>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("---")
st.markdown("""
<div class='footer'>
    <p style='font-size: 0.9rem;'>© 2023-2025 SafeSpace Kenya | Designed with ❤️ | Updated: 12:00 AM EAT, July 25, 2025</p>
    <div style='display: flex; justify-content: center; gap: 0.5rem; flex-wrap: wrap;'>
        <a href='https://facebook.com/safespacekenya' target='_blank' class='primary-btn'>Facebook</a>
        <a href='https://instagram.com/safespacekenya' target='_blank' class='primary-btn'>Instagram</a>
        <a href='https://twitter.com/safespacekenya' target='_blank' class='primary-btn'>Twitter</a>
        <a href='https://linkedin.com/company/safespacekenya' target='_blank' class='primary-btn'>LinkedIn</a>
    </div>
</div>
""", unsafe_allow_html=True)

with st.form("newsletter_form", clear_on_submit=True):
    st.markdown("<div style='max-width: 300px; margin: 0.5rem auto; display: flex; gap: 0.3rem;'>", unsafe_allow_html=True)
    newsletter_email = st.text_input("", placeholder="Subscribe for tips...", key="newsletter_email")
    submit_newsletter = st.form_submit_button("Subscribe")
    st.markdown("</div>", unsafe_allow_html=True)
    if submit_newsletter:
        if not newsletter_email or not re.match(r"[^@]+@[^@]+\.[^@]+", newsletter_email):
            st.error("Valid email required.")
        else:
            st.success(f"Subscribed! Next newsletter: August 1, 2025, 9 AM EAT.")
