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
        bottom: 10px;
        right: 10px;
        width: 90%;
        max-height: 250px;
        overflow-y: auto;
        z-index: 1000;
        background: white;
        padding: 0.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        display: none;
        left: 5%;
    }
    .chatbot-container.active {
        display: block;
    }
    .chatbot-message.user {
        background: #e8f4f8;
        text-align: right;
        color: var(--dark);
        padding: 0.3rem;
        margin: 0.3rem 0;
        border-radius: 6px;
        font-size: 0.9rem;
    }
    .chatbot-message.bot {
        background: white;
        text-align: left;
        color: var(--primary);
        padding: 0.3rem;
        margin: 0.3rem 0;
        border-radius: 6px;
        border-left: 3px solid var(--primary);
        font-size: 0.9rem;
    }
    .chatbot-input {
        width: 100%;
        padding: 0.3rem;
        border: 1px solid #e0e0e0;
        border-radius: 6px;
        margin-top: 0.3rem;
        font-size: 0.9rem;
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
            bottom: 5px;
            max-height: 200px;
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

# HEADER
st.markdown("""
<div style='text-align: center; padding: 0.8rem; background: var(--primary); color: white;'>
    <h1>SafeSpace Kenya</h1>
    <p>Empowering Minds, Nurturing Hope Since 2023 | Updated: 11:54 PM EAT, July 24, 2025</p>
</div>
""", unsafe_allow_html=True)

# HERO SECTION
st.markdown("<div id='hero'></div>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding: 0.8rem; background: linear-gradient(rgba(38,166,154,0.9), rgba(77,182,172,0.9)); border-radius: 8px; color: white;'>
    <h1>Healing Minds, Restoring Lives</h1>
    <p style='font-size: 1rem; max-width: 100%; margin: 0.5rem auto;'>SafeSpace Kenya offers professional, confidential counseling and mental health support in a culturally-sensitive environment, serving urban and rural communities across Kenya. Our mission is to break the stigma and provide accessible care to all.</p>
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
    - **Mission**: Break the stigma around mental health and provide affordable care to every Kenyan.
    - **Vision**: A mentally thriving Kenya where all have emotional support tools.
    - **Contact**: info@safespacekenya.org or +254 781 095 919 (until 7 PM EAT today).
    - **Impact**: Served 600+ clients in 2025, with a 90% satisfaction rate.
    """)

# ABOUT SECTION
st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.markdown("## About SafeSpace Kenya")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p><strong>SafeSpace Kenya</strong>, founded in 2023 by Jerim Owino and Hamdi Roble, is a non-profit dedicated to accessible, culturally-appropriate mental health care. With 15 licensed professionals, we serve urban hubs like Nairobi and rural areas like Kisumu and Eldoret, addressing trauma, depression, anxiety, and family issues via in-person, tele-counseling, and mobile outreach.</p>
    <p>We blend traditional Kenyan values (e.g., community support, storytelling) with modern therapies like CBT and mindfulness. Partnerships with NGOs, schools, and the Ministry of Health extend our reach to 20+ districts, focusing on inclusivity for youth, women, and marginalized groups.</p>
    <a href='#services' class='primary-btn'>Explore Our Services</a>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Our History", expanded=False):
    st.markdown("""
    - **Founding**: Launched after a 2022 Nakuru pilot aiding 50 individuals.
    - **Growth**: From 2 to 15 staff by mid-2025, aiming for 20 by year-end.
    - **Awards**: 2024 Kenya Health Federation Award, 2025 Global Mental Health Grant.
    - **Team**: Specialists in child psychology, trauma, and cultural therapy.
    """)

# FOUNDERS SECTION
st.markdown("<div id='founders'></div>", unsafe_allow_html=True)
st.markdown("## Our Founders")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <div class='founder-card'>
        <h4>Jerim Owino</h4>
        <p>Jerim, a clinical psychologist with 12 years of experience, co-founded SafeSpace to address rural mental health gaps. Holding a PhD from the University of Nairobi, he specializes in trauma recovery and has worked with refugee communities in Dadaab. His vision drives our mobile outreach programs.</p>
    </div>
    <div class='founder-card'>
        <h4>Hamdi Roble</h4>
        <p>Hamdi, a community health advocate with a Master’s in Public Health, brings 8 years of experience in cultural therapy. A Kisumu native, she integrates traditional practices like storytelling into modern counseling, leading our rural expansion efforts and partnerships with local elders.</p>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Our Founders", expanded=False):
    st.markdown("""
    - **Jerim’s Background**: Published 10+ papers on trauma, mentored 20 psychologists.
    - **Hamdi’s Impact**: Trained 100+ community leaders in mental health awareness.
    - **Collaboration**: Jointly developed SafeSpace’s cultural therapy model in 2023.
    - **Personal Touch**: Both offer occasional free workshops for underprivileged areas.
    """)

# SERVICES SECTION
st.markdown("<div id='services'></div>", unsafe_allow_html=True)
st.markdown("## Our Therapeutic Services")
st.markdown("A comprehensive suite of evidence-based therapies by 15 certified professionals with over 75 years of combined experience.")
services = [
    {
        "icon": "👤",
        "title": "Individual Counseling",
        "desc": "Personalized sessions for depression, anxiety, PTSD, and growth. Uses CBT, DBT, ACT, and MBSR by therapists with 5+ years’ experience. 50-minute sessions offered in-person (Nairobi), online, or via mobile units, with evening/weekend slots and a free 15-minute consultation. Includes progress reports."
    },
    {
        "icon": "👥",
        "title": "Group Therapy",
        "desc": "Support for grief, addiction, PTSD, and anxiety. 90-minute weekly sessions (max 10 participants) with role-playing, meditations, and monthly themes, led by two counselors. Available in-person and online, with a waiting list."
    },
    {
        "icon": "🏠",
        "title": "Family Counseling",
        "desc": "Enhances communication and resolves conflicts using systemic and narrative therapy. 60-minute sessions for parenting, marital issues, and trauma, with cultural techniques (proverbs, elder mediation). Offered in-person, online, or via home visits."
    },
    {
        "icon": "🧠",
        "title": "Trauma Recovery Therapy",
        "desc": "Intensive therapy for violence or disaster survivors using EMDR, trauma-focused CBT, and somatic experiencing. 75-minute sessions in a safe environment or telehealth, with a 6-session program and support groups, prioritizing refugees and gender-based violence victims."
    }
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
    - **Credentials**: Master’s or higher, certified in multiple modalities.
    - **Accessibility**: Sliding scale (KSh 500-2,000), subsidies, free workshops.
    - **Feedback**: 95% improved wellbeing, 85% continue therapy (2024 surveys).
    - **Innovation**: AI-assisted tools for rural areas, launching Q4 2025.
    """)

# TESTIMONIALS SECTION
st.markdown("<div id='testimonials'></div>", unsafe_allow_html=True)
st.markdown("## What Our Clients Say")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <div class='testimonial-card'>
        <p><em>'SafeSpace’s individual counseling helped me recover from anxiety post-accident. Life-changing!'</em> - Jane K., Nairobi, 2025</p>
    </div>
    <div class='testimonial-card'>
        <p><em>'Group therapy gave me a community during my grief journey. Highly recommend!'</em> - Peter O., Kisumu, 2025</p>
    </div>
    <div class='testimonial-card'>
        <p><em>'Family counseling resolved our conflicts with cultural wisdom. Amazing support!'</em> - Amina H., Eldoret, 2025</p>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Testimonials", expanded=False):
    st.markdown("""
    - **Verification**: Collected with consent from verified clients.
    - **Diversity**: Represents urban, rural, and various age groups.
    - **Impact**: 200+ testimonials in 2025, with a yearly report planned.
    """)

# MENTAL HEALTH BLOG SECTION
st.markdown("<div id='blog'></div>", unsafe_allow_html=True)
st.markdown("## Mental Health Blog")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Insightful articles by experts to support your wellbeing:</p>
""", unsafe_allow_html=True)
blogs = [
    {"title": "Coping with Economic Stress", "date": "July 20, 2025", "desc": "Strategies including budgeting and relaxation by Dr. Amina Hassan."},
    {"title": "Cultural Therapy in Kenya", "date": "July 15, 2025", "desc": "Integrating storytelling and remedies by Hamdi Roble."},
    {"title": "PTSD Survivor Guide", "date": "July 10, 2025", "desc": "Symptoms and recovery by Dr. James Otieno."}
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
    - **Updates**: Bi-weekly posts, youth series in August 2025.
    - **Panel**: Psychologists, cultural advisors, and a psychiatrist.
    - **Engagement**: Submit questions to blog@safespacekenya.org.
    - **Downloads**: Free PDFs under Resources.
    """)

# CRISIS RESOURCES SECTION
st.markdown("<div id='crisis'></div>", unsafe_allow_html=True)
st.markdown("## Crisis Resources")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Immediate support by trained professionals:</p>
    <ul>
        <li><strong>Befrienders Kenya:</strong> 1199, 24/7, 50+ trained volunteers.</li>
        <li><strong>SafeSpace Crisis Line:</strong> +254 781 095 919, 8 AM-7 PM EAT, 5 counselors.</li>
    </ul>
    <p>Emergency: Call 999 or visit a hospital. Ongoing support via sessions or groups.</p>
    <a href='#contact' class='primary-btn'>Get Help Now</a>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Crisis Support", expanded=False):
    st.markdown("""
    - **Training**: 40 hours annually for volunteers.
    - **Partnerships**: With Kenyatta Hospital for referrals.
    - **Confidentiality**: Encrypted calls, strict privacy.
    - **Resources**: Free crisis pamphlets at locations.
    """)

# PROGRESS TRACKER SECTION
st.markdown("<div id='tracker'></div>", unsafe_allow_html=True)
st.markdown("## Progress Tracker")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Track your mental health journey with interactive tools:</p>
    <div class='tracker-card'>
        <h4>Mood Tracker</h4>
        <p>Rate your mood (1-5) and add notes to track trends and share with your therapist.</p>
    </div>
""", unsafe_allow_html=True)
mood = st.slider("How do you feel? (1 = Low, 5 = High)", 1, 5, 3, key="mood_input")
note = st.text_input("Add a note (optional)", placeholder="e.g., Stressful day", key="mood_note")
if st.button("Log Mood"):
    st.session_state.mood_history.append({"date": datetime.now(), "mood": mood, "note": note})
    st.success(f"Mood logged at 11:54 PM EAT, July 24, 2025!")
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
    - **Features**: Export as CSV for records or therapy.
    - **Usage**: Log daily for 30 days, review weekly.
    - **Support**: Email support@safespacekenya.org.
    - **Privacy**: Secure, accessible only to you and therapist.
    """)

# VOLUNTEER OPPORTUNITIES SECTION
st.markdown("<div id='volunteer'></div>", unsafe_allow_html=True)
st.markdown("## Volunteer Opportunities")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Join our mission with flexible roles and training:</p>
""", unsafe_allow_html=True)
volunteer_roles = [
    {"title": "Outreach Support", "desc": "2-4 hour weekly campaigns in Nakuru/Mombasa, distributing materials, organizing talks. 10-hour online training."},
    {"title": "Event Volunteer", "desc": "4-6 hour support for July 30/August 15 events, setup, Q&A. On-site guidance."},
    {"title": "Crisis Line Assistant", "desc": "8 AM-7 PM shift support, 20-hour training in intervention skills."}
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
    name = st.text_input("Full Name", placeholder="Your full name")
    email = st.text_input("Email", placeholder="your.email@example.com")
    phone = st.text_input("Phone Number", placeholder="+254 XXX XXX XXX")
    experience = st.text_area("Relevant Experience", placeholder="e.g., counseling, event planning")
    role_preference = st.selectbox("Preferred Role", ["Outreach Support", "Event Volunteer", "Crisis Line Assistant", "Any"])
    submit = st.form_submit_button("Register")
    if submit:
        if not all([name, email, re.match(r"[^@]+@[^@]+\.[^@]+", email), phone, experience]):
            st.error("Please fill all fields.")
        else:
            st.session_state.outreach_form_data = {"name": name, "email": email, "phone": phone, "experience": experience, "role": role_preference}
            st.success(f"Thank you, {name}! Registered at 11:54 PM EAT, July 24, 2025. Contact at {email} within 48 hours.")
            st.session_state.outreach_form_data = {"name": "", "email": "", "phone": "", "experience": "", "role": "Any"}
st.markdown("""
<div style='text-align: center; margin-top: 0.5rem;'>
    <a href='#contact' class='primary-btn'>Contact Us 📞</a>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Volunteering", expanded=False):
    st.markdown("""
    - **Impact**: 1,200 reached in 2024, 2,000 target for 2025.
    - **Training**: 10-hour online, 5-hour in-person workshops.
    - **Recognition**: Certificates, Volunteer Day on December 15, 2025.
    - **Support**: Monthly check-ins with a coordinator.
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
        <p>August 15, 2025, 10 AM-2 PM, Kisumu Center. Ages 13-25, open entry.</p>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Events", expanded=False):
    st.markdown("""
    - **Registration**: Limit 50 per event, email required.
    - **Workshops**: Handouts, online Q&A follow-ups.
    - **Past**: June 2025 Trauma Day served 80.
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
        <p>Disaster response training since 2023, 10 regions.</p>
    </div>
    <div class='partnership-card'>
        <h4>Ministry of Health</h4>
        <p>Policy support and rural funding.</p>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Partnerships", expanded=False):
    st.markdown("""
    - **Goals**: Train 100 healthcare workers by 2026.
    - **Projects**: Mobile clinic pilot with Red Cross, 2025.
    - **Benefits**: Access to training modules and anonymized data.
    - **Expansion**: Seeking education and corporate partners.
    """)

# FAQ SECTION
st.markdown("<div id='faq'></div>", unsafe_allow_html=True)
st.markdown("## Frequently Asked Questions")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p><strong>Q: Ages served?</strong> A: All ages, with specialized programs.</p>
    <p><strong>Q: Confidentiality?</strong> A: Yes, encrypted, compliant with Kenyan laws.</p>
    <p><strong>Q: Payment?</strong> A: Cash, M-Pesa, bank; subsidies available.</p>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About FAQs", expanded=False):
    st.markdown("""
    - **Support**: Email faq@safespacekenya.org.
    - **Updates**: Reviewed quarterly, last July 2025.
    - **Resources**: Download FAQ PDF.
    """)

# CONTACT SECTION
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.markdown("## Contact Us")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p><strong>📍</strong> Greenhouse Plaza, Ngong Road, Nairobi, 5 min from bus stop.</p>
    <p><strong>📞</strong> +254 781 095 919, 8 AM-7 PM EAT, voicemail checked daily.</p>
    <p><strong>✉️</strong> <a href='mailto:info@safespacekenya.org'>info@safespacekenya.org</a>, 24-hour response.</p>
    <p><strong>Hours:</strong> Mon-Fri 9 AM-5 PM, Sat 10 AM-2 PM.</p>
    <a href='#' class='primary-btn'>Book Consultation</a>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Contacting Us", expanded=False):
    st.markdown("""
    - **Appointments**: Online or call, same-day slots until 3 PM.
    - **Accessibility**: Wheelchair, sign language, large print.
    - **Follow-Up**: Within one week, 80% opt-in.
    - **Map**: On our website.
    """)

# CHATBOT
st.markdown("""
<div class='chatbot-container' id='chatbot'>
    <h4>Ask SafeSpace Bot</h4>
    <div id='chat-messages' style='max-height: 200px; overflow-y: auto; margin-bottom: 0.5rem;'>
""", unsafe_allow_html=True)
for sender, message in st.session_state.chat_history:
    st.markdown(f"<div class='chatbot-message {sender}'><p>{message}</p></div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("", placeholder="Ask about services...", key="chat_input")
    submit = st.form_submit_button("Send")
    if submit and user_input:
        st.session_state.chat_history.append(("user", user_input))
        response = f"Assisting you! Visit Contact or call +254 781 095 919 (until 7 PM EAT). Time: 11:54 PM EAT, July 24, 2025."
        st.session_state.chat_history.append(("bot", response))
st.markdown("</div>", unsafe_allow_html=True)

# JavaScript to toggle chatbot
st.markdown("""
<script>
    document.addEventListener('DOMContentLoaded', function() {
        const toggleButton = document.createElement('button');
        toggleButton.textContent = 'Toggle Chatbot';
        toggleButton.className = 'primary-btn';
        toggleButton.style.position = 'fixed';
        toggleButton.style.bottom = '60px';
        toggleButton.style.right = '10px';
        toggleButton.style.zIndex = '1001';
        document.body.appendChild(toggleButton);
        const chatbot = document.getElementById('chatbot');
        if (chatbot) {
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
    <p style='font-size: 0.9rem;'>© 2023-2025 SafeSpace Kenya | Designed with ❤️ | Updated: 11:54 PM EAT, July 24, 2025</p>
    <div style='display: flex; justify-content: center; gap: 0.5rem; flex-wrap: wrap;'>
        <a href='https://facebook.com/safespacekenya' target='_blank' class='primary-btn'>Facebook</a>
        <a href='https://instagram.com/safespacekenya' target='_blank' class='primary-btn'>Instagram</a>
        <a href='https://twitter.com/safespacekenya' target='_blank' class='primary-btn'>Twitter</a>
        <a href='https://linkedin.com/company/safespacekenya' target='_blank' class='primary-btn'>LinkedIn</a>
    </div>
</div>
""", unsafe_allow_html=True)

knowledge_base = [
    {"section": "About", "answer": "Mental health care since 2023.", "keywords": ["about", "history"]},
    {"section": "Services", "answer": "Counseling, group, family, trauma therapy.", "keywords": ["services", "therapy"]},
]

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
