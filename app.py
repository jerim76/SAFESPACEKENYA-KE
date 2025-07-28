import streamlit as st
from datetime import datetime
import re
import base64
import pandas as pd

# Custom CSS for client-friendly design
st.markdown("""
<style>
    :root {
        --primary: #26A69A;
        --accent: #FF6F61;
        --light: #e6f3f5;
        --dark: #2c3e50;
        --deep-blue: #1E3A8A;
        --white: #FFFFFF;
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
    h1 { font-size: 2.8rem; font-weight: 700; }
    h2 { font-size: 2.2rem; font-weight: 600; }
    h3 { font-size: 1.6rem; font-weight: 500; }
    h4 { font-size: 1.3rem; font-weight: 500; }
    p, li { font-size: 1.1rem; line-height: 1.6; color: var(--dark); }
    .service-card, .testimonial-card, .event-card, .partnership-card, .blog-card, .tracker-card, .volunteer-card, .founder-card, .appointment-card, .resource-card {
        background: var(--white);
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 3px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        transition: transform 0.2s ease;
    }
    .service-card:hover, .testimonial-card:hover, .event-card:hover, .partnership-card:hover, .blog-card:hover, .tracker-card:hover, .volunteer-card:hover, .founder-card:hover, .appointment-card:hover, .resource-card:hover {
        transform: translateY(-5px);
    }
    .primary-btn {
        background: linear-gradient(135deg, var(--primary), #4DB6AC);
        color: var(--white);
        padding: 0.8rem 1.5rem;
        border-radius: 25px;
        border: none;
        font-weight: 600;
        font-size: 1.1rem;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    .primary-btn:hover {
        background: linear-gradient(135deg, var(--accent), #FF8A80);
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }
    .stButton > button {
        background: linear-gradient(135deg, var(--primary), #4DB6AC);
        color: var(--white);
        border-radius: 25px;
        border: none;
        padding: 0.8rem 1.5rem;
        font-size: 1.1rem;
        font-weight: 600;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, var(--accent), #FF8A80);
    }
    .st-expander {
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        background: #f9f9f9;
        margin-bottom: 1rem;
    }
    .footer {
        text-align: center;
        padding: 1.5rem;
        background: #e8f4f8;
        border-top: 1px solid #ddd;
        margin-top: 2rem;
    }
    .cta-banner {
        background: linear-gradient(135deg, var(--primary), #4DB6AC);
        color: var(--white);
        text-align: center;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .chatbot-container, .whatsapp-widget-container {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 320px;
        max-height: 450px;
        overflow-y: auto;
        z-index: 1000;
        background: var(--white);
        padding: 1.2rem;
        border-radius: 10px;
        box-shadow: 0 3px 6px rgba(0,0,0,0.2);
        display: none;
    }
    .chatbot-container.active, .whatsapp-widget-container.active {
        display: block;
    }
    .chatbot-message.user {
        background: #e8f4f8;
        text-align: right;
        color: var(--dark);
        padding: 0.6rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        font-size: 1rem;
    }
    .chatbot-message.bot {
        background: var(--white);
        text-align: left;
        color: var(--primary);
        padding: 0.6rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        border-left: 4px solid var(--primary);
        font-size: 1rem;
    }
    .chatbot-input {
        width: 100%;
        padding: 0.6rem;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        margin-top: 0.5rem;
        font-size: 1rem;
    }
    .chatbot-toggle, .whatsapp-toggle {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 1001;
        background: linear-gradient(135deg, var(--primary), #4DB6AC);
        color: var(--white);
        border: none;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        font-size: 1.5rem;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 3px 6px rgba(0,0,0,0.2);
    }
    .whatsapp-toggle {
        bottom: 90px;
        background: linear-gradient(135deg, #25D366, #128C7E);
    }
    .chatbot-toggle:hover, .whatsapp-toggle:hover {
        background: linear-gradient(135deg, var(--accent), #FF8A80);
    }
    .whatsapp-toggle:hover {
        background: linear-gradient(135deg, #128C7E, #25D366);
    }
    .nav-bar {
        position: sticky;
        top: 0;
        z-index: 1002;
        background: var(--white);
        padding: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        display: flex;
        justify-content: center;
        gap: 1rem;
        flex-wrap: wrap;
    }
    .nav-link {
        color: var(--deep-blue);
        text-decoration: none;
        font-size: 1.1rem;
        font-weight: 500;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        transition: background 0.3s ease;
    }
    .nav-link:hover {
        background: var(--light);
        color: var(--primary);
    }
    .success-story {
        background: var(--white);
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 3px 6px rgba(0,0,0,0.1);
        margin: 0.5rem;
        text-align: center;
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
        .service-card, .testimonial-card, .event-card, .partnership-card, .blog-card, .tracker-card, .volunteer-card, .founder-card, .appointment-card, .resource-card {
            margin: 0.5rem 0;
            padding: 0.8rem;
        }
        h1 { font-size: 2rem; }
        h2 { font-size: 1.6rem; }
        h3 { font-size: 1.4rem; }
        h4 { font-size: 1.1rem; }
        p, li { font-size: 1rem; }
        .primary-btn {
            padding: 0.6rem 1.2rem;
            font-size: 1rem;
        }
        .chatbot-container, .whatsapp-widget-container {
            width: 95%;
            right: 2.5%;
            bottom: 80px;
            max-height: 350px;
        }
        .chatbot-toggle, .whatsapp-toggle {
            bottom: 20px;
            right: 2.5%;
            width: 50px;
            height: 50px;
            font-size: 1.2rem;
        }
        .whatsapp-toggle {
            bottom: 80px;
        }
        .nav-bar {
            padding: 0.5rem;
            gap: 0.5rem;
        }
        .nav-link {
            font-size: 0.9rem;
            padding: 0.4rem 0.8rem;
        }
        img {
            max-width: 100% !important;
            height: auto !important;
        }
        .cta-banner {
            padding: 0.8rem;
        }
        .st-expander {
            margin: 0.5rem 0;
        }
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="SafeSpace Organisation",
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
if "partnership_form_data" not in st.session_state:
    st.session_state.partnership_form_data = {"name": "", "organization": "", "email": "", "phone": "", "type": "Partner"}
if "counseling_form_data" not in st.session_state:
    st.session_state.counseling_form_data = {"name": "", "email": "", "phone": "", "type": "Online"}
if "appointment_form_data" not in st.session_state:
    st.session_state.appointment_form_data = {"name": "", "email": "", "phone": "", "date": "", "time": "", "type": "Online"}

# Function to create download link
def get_download_link(file_content, file_name):
    b64 = base64.b64encode(file_content.encode()).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_name}" class="primary-btn" style="display: block; text-align: center; margin-top: 0.5rem;">Download {file_name}</a>'
    return href

# Function to export mood history
def export_mood_history():
    df = pd.DataFrame(st.session_state.mood_history, columns=["Date", "Mood", "Note"])
    df["Date"] = df["Date"].apply(lambda x: x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime) else x)
    csv = df.to_csv(index=False)
    return csv

# Chatbot knowledge base
knowledge_base = [
    {"question": r"what is safespace organisation\??", "answer": "SafeSpace Organisation, founded in 2023 by Jerim Owino and Hamdi Roble, is a non-profit dedicated to accessible mental health care, offering counseling for trauma, depression, and more, with a focus on inclusivity and support."},
    {"question": r"what services do you offer\??", "answer": "We provide Individual Counseling, Group Therapy, Family Counseling, Trauma Recovery Therapy, and Online Counseling, using evidence-based methods like CBT, EMDR, and mindfulness. Register in the Services section or WhatsApp us."},
    {"question": r"how can i contact you\??", "answer": "Reach us at +254 781 095 919 (8 AM-7 PM EAT) via call or WhatsApp, or email info@safespaceorganisation.org (24-hour response). Visit us at Greenhouse Plaza, Ngong Road, Nairobi."},
    {"question": r"what are your hours\??", "answer": "Office hours are Mon-Fri 9 AM-5 PM, Sat 10 AM-2 PM, closed Sundays and holidays. Crisis line is available 8 AM-7 PM EAT."},
    {"question": r"how much does it cost\??", "answer": "Sessions cost KSh 500-2,000 on a sliding scale, with subsidies and free workshops for low-income clients. Contact us for details."},
    {"question": r"who are the founders\??", "answer": "Jerim Owino, a counselor with a psychology degree from Maasai Mara University, and Hamdi Roble, a human resource manager with 8 years of experience in organizational management."},
    {"question": r"what events are coming up\??", "answer": "Join our Stress Management Workshop on July 30, 2025, in Nairobi, or Youth Mental Health Forum on August 15, 2025, in Kisumu. Register at events@safespaceorganisation.org."},
    {"question": r"how can i volunteer\??", "answer": "Volunteer as an Outreach Support, Event Volunteer, or Crisis Line Assistant. Register via the Volunteer form or WhatsApp +254 781 095 919."},
    {"question": r"what is the crisis line\??", "answer": "Our Crisis Line is +254 781 095 919 (8 AM-7 PM EAT). For 24/7 support, call Befrienders Kenya at 1199."},
    {"question": r"how can i partner with you\??", "answer": "Register as a Partner or Donor via the Partnerships form or contact partnership@safespaceorganisation.org."},
    {"question": r"how can i book an appointment\??", "answer": "Use the Book Appointment section, call, or WhatsApp +254 781 095 919 (8 AM-7 PM EAT) with your name, email, phone, preferred date, time, and counseling type."},
    {"question": r"how can i contact you via whatsapp\??", "answer": "Click the WhatsApp button on our website or message +254 781 095 919 (8 AM-7 PM EAT)."},
    {"question": r"how do i prepare for a session\??", "answer": "Bring any relevant medical or mental health history, reflect on your goals, and arrive 5-10 minutes early. Online sessions require a stable internet connection."},
    {"question": r"what qualifications do your therapists have\??", "answer": "Our therapists hold Master’s degrees or higher in psychology or counseling, with certifications in CBT, EMDR, and other modalities, averaging 10+ years of experience."},
    {"default": f"I’m sorry, I didn’t understand. Ask about services, contact, hours, costs, founders, events, volunteering, crisis support, appointments, WhatsApp, or preparation. Time: {datetime.now().strftime('%I:%M %p EAT, %B %d, %Y')}."}
]

# Function to get chatbot response
def get_chatbot_response(query):
    query = query.lower()
    for entry in knowledge_base:
        if "question" in entry and re.search(entry["question"], query):
            return entry["answer"]
    return knowledge_base[-1]["default"]

# Navigation Bar
st.markdown("""
<div class='nav-bar'>
    <a href='#hero' class='nav-link'>Home</a>
    <a href='#services' class='nav-link'>Services</a>
    <a href='#book-appointment' class='nav-link'>Book Appointment</a>
    <a href='#resources' class='nav-link'>Resources</a>
    <a href='#contact' class='nav-link'>Contact</a>
    <a href='#about' class='nav-link'>About</a>
</div>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
<div style='text-align: center; padding: 1rem; background: var(--primary); color: var(--white);'>
    <h1>SafeSpace Organisation</h1>
    <p style='font-size: 1.2rem;'>Your Safe Haven for Mental Wellness Since 2023</p>
</div>
""", unsafe_allow_html=True)

# HERO SECTION
st.markdown("<div id='hero'></div>", unsafe_allow_html=True)
st.markdown("""
<div class='cta-banner'>
    <h1>Welcome to Your Journey of Healing</h1>
    <p style='font-size: 1.2rem; max-width: 800px; margin: 1rem auto;'>At SafeSpace, we provide compassionate, professional counseling to support you through life’s challenges. Start your path to emotional wellness today in a safe, inclusive environment.</p>
    <img src='https://images.unsplash.com/photo-1588195539435-d6b5f19e1c24?auto=format&fit=crop&w=700&q=80' style='width: 100%; max-width: 700px; border-radius: 10px; margin: 1rem auto; box-shadow: 0 3px 6px rgba(0,0,0,0.2);' alt='Counseling session'/>
    <div style='display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;'>
        <a href='#book-appointment' class='primary-btn'>Start Your Journey</a>
        <a href='#services' class='primary-btn'>Explore Services</a>
        <a href='#contact' class='primary-btn'>Get in Touch</a>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Why Choose SafeSpace?", expanded=False):
    st.markdown("""
    - **Mission**: We’re here to break mental health stigma and make care accessible to all.
    - **Impact**: Over 600 clients supported in 2025 with a 90% satisfaction rate.
    - **Accessibility**: Affordable sessions, online options, and support in multiple languages.
    - **Confidentiality**: Your privacy is our priority with secure, encrypted services.
    """)

# ABOUT SECTION
st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.markdown("## About SafeSpace")
st.markdown("""
<div style='background: var(--white); padding: 1rem; border-radius: 10px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);'>
    <p style='font-size: 1.2rem;'>Founded in 2023 by Jerim Owino and Hamdi Roble, SafeSpace Organisation is dedicated to empowering individuals through professional mental health care. Our team of 15 certified professionals serves Nairobi, Kisumu, Eldoret, and beyond, helping clients overcome trauma, depression, anxiety, and family challenges.</p>
    <p>We use evidence-based therapies like CBT and EMDR, partnering with NGOs and the Ministry of Health to reach over 20 districts. Our goal is to create a supportive, inclusive space where everyone feels heard and valued.</p>
    <div style='text-align: center; margin-top: 1rem;'>
        <a href='#services' class='primary-btn'>Discover Our Services</a>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Our Story and Impact", expanded=False):
    st.markdown("""
    - **Founded**: Started with a 2022 pilot in Nakuru, helping 50 clients, leading to our 2023 launch.
    - **Growth**: Expanded from 2 to 15 staff, with plans for 20 by end of 2025.
    - **Awards**: 2024 Health Federation Award, 2025 Global Grant for mental health innovation.
    - **Reach**: Serving diverse communities with a focus on accessibility and inclusivity.
    """)

# FOUNDERS SECTION
st.markdown("<div id='founders'></div>", unsafe_allow_html=True)
st.markdown("## Meet Our Founders")
st.markdown("""
<div style='background: var(--white); padding: 1rem; border-radius: 10px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);'>
    <div class='founder-card'>
        <h4>Jerim Owino</h4>
        <p>Jerim, a counselor with a psychology degree from Maasai Mara University, brings over 12 years of experience in mental health. Specializing in trauma counseling, he uses Cognitive Behavioral Therapy (CBT) and Eye Movement Desensitization and Reprocessing (EMDR) to guide SafeSpace’s programs.</p>
    </div>
    <div class='founder-card'>
        <h4>Hamdi Roble</h4>
        <p>Hamdi, a human resource manager with 8 years of experience, oversees staff training and program coordination, ensuring seamless delivery of mental health services at SafeSpace.</p>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("More About Our Founders", expanded=False):
    st.markdown("""
    - **Jerim**: Trained 50+ community health workers in psychological first aid and co-authored a trauma counseling guide.
    - **Hamdi**: Developed training programs for mental health service delivery, enhancing staff readiness.
    - **Collaboration**: Built SafeSpace’s evidence-based therapy model post-2022 pilot.
    - **Commitment**: Both lead program development for high-quality, client-focused care.
    """)

# SERVICES SECTION
st.markdown("<div id='services'></div>", unsafe_allow_html=True)
st.markdown("## Our Counseling Services")
st.markdown("""
<div style='background: var(--white); padding: 1rem; border-radius: 10px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);'>
    <p style='font-size: 1.2rem;'>Our 15 certified therapists, with over 75 years of combined experience, offer tailored, evidence-based counseling to help you navigate life’s challenges. Each service is designed to support your unique needs with compassion and professionalism.</p>
</div>
""", unsafe_allow_html=True)
services = [
    {
        "icon": "👤",
        "title": "Individual Counseling",
        "desc": "One-on-one sessions (50 minutes) to address chronic depression, anxiety, PTSD, or low self-esteem. Using CBT, DBT, ACT, and mindfulness, our therapists help you develop coping strategies. Expect a safe, confidential space with a free 15-minute consultation to match you with the right therapist. Available in-person in Nairobi or online, with evening/weekend slots. Benefits include improved emotional regulation and personalized progress plans."
    },
    {
        "icon": "👥",
        "title": "Group Therapy",
        "desc": "90-minute weekly sessions for up to 10 participants, focusing on grief, addiction recovery, PTSD, or social anxiety. Led by two experienced counselors, sessions include peer support, role-playing, and guided meditations. Expect a supportive community and monthly themes (e.g., resilience). Available in-person or online, with a 3-month commitment recommended for lasting impact. Benefits include reduced isolation and shared coping skills."
    },
    {
        "icon": "🏠",
        "title": "Family Counseling",
        "desc": "60-minute sessions to resolve parenting challenges, marital disputes, or intergenerational trauma. Using systemic and narrative therapy, our therapists foster communication and healing. Expect a 6-session program with monthly check-ins, available in-person, online, or via home visits in select areas. Benefits include stronger family bonds and conflict resolution skills."
    },
    {
        "icon": "🧠",
        "title": "Trauma Recovery Therapy",
        "desc": "75-minute sessions for survivors of violence, abuse, accidents, or disasters. Using EMDR, trauma-focused CBT, and somatic experiencing, our specialists help you process trauma safely. Expect a 6-session initial phase with ongoing support groups. Available in Nairobi or via telehealth, prioritizing urgent cases. Benefits include reduced triggers and restored sense of safety."
    },
    {
        "icon": "💻",
        "title": "Online Counseling",
        "desc": "50-minute virtual sessions for anxiety, depression, or stress, using CBT and mindfulness. Delivered via secure video platforms with 24/7 scheduling flexibility and a free 15-minute consultation. Expect encrypted, private sessions tailored to your needs. Benefits include accessibility from anywhere and convenience for busy schedules."
    }
]
for service in services:
    st.markdown(f"""
    <div class='service-card'>
        <h3>{service['icon']} {service['title']}</h3>
        <p>{service['desc']}</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown("<div id='counseling-form'></div>", unsafe_allow_html=True)
with st.form("counseling_form", clear_on_submit=True):
    st.markdown("### Register for Counseling")
    name = st.text_input("Full Name")
    email = st.text_input("Email", placeholder="your.email@example.com")
    phone = st.text_input("Phone", placeholder="+254 XXX XXX XXX")
    counseling_type = st.selectbox("Counseling Type", ["Online", "In-Person"])
    submit = st.form_submit_button("Register Now")
    if submit:
        if not all([name, email, re.match(r"[^@]+@[^@]+\.[^@]+", email), phone]):
            st.error("Please fill all required fields with valid information.")
        else:
            st.session_state.counseling_form_data = {"name": name, "email": email, "phone": phone, "type": counseling_type}
            st.success(f"Thank you, {name}! Your {counseling_type} counseling registration at {datetime.now().strftime('%I:%M %p EAT, %B %d, %Y')} is received. We’ll contact you at {email} within 48 hours.")
            st.session_state.counseling_form_data = {"name": "", "email": "", "phone": "", "type": "Online"}
st.markdown("""
<div style='text-align: center; margin-top: 1rem;'>
    <a href='#book-appointment' class='primary-btn'>Book a Session</a>
    <a href='#resources' class='primary-btn'>Explore Resources</a>
</div>
""", unsafe_allow_html=True)
with st.expander("What to Expect from Our Services", expanded=False):
    st.markdown("""
    - **Therapist Credentials**: All therapists hold Master’s degrees or higher, certified in CBT, EMDR, and more, with 10+ years of experience on average.
    - **Affordability**: Sliding scale fees (KSh 500-2,000/session), subsidies for low-income clients, and free monthly workshops.
    - **Client Feedback**: 95% report improved wellbeing after 6 sessions (2024 survey).
    - **Innovation**: Piloting AI-assisted tools for rural access, launching Q4 2025.
    - **Preparation**: Bring any relevant history, reflect on goals, and expect a warm, confidential welcome.
    """)

# SUCCESS STORIES SECTION
st.markdown("<div id='success-stories'></div>", unsafe_allow_html=True)
st.markdown("## Success Stories")
st.markdown("""
<div style='background: var(--white); padding: 1rem; border-radius: 10px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);'>
    <p style='font-size: 1.2rem; text-align: center;'>Hear from clients who found hope and healing with SafeSpace.</p>
    <div style='display: flex; overflow-x: auto; gap: 1rem; padding: 1rem 0;'>
        <div class='success-story' style='flex: 0 0 auto; width: 250px;'>
            <p><em>“SafeSpace helped me overcome my anxiety after a car accident. I feel in control again!”</em></p>
            <p><strong>Jane K., Nairobi, 2025</strong></p>
        </div>
        <div class='success-story' style='flex: 0 0 auto; width: 250px;'>
            <p><em>“Group therapy gave me a sense of belonging during my grief.”</em></p>
            <p><strong>Peter O., Kisumu, 2025</strong></p>
        </div>
        <div class='success-story' style='flex: 0 0 auto; width: 250px;'>
            <p><em>“Family counseling rebuilt our communication and trust.”</em></p>
            <p><strong>Amina H., Eldoret, 2025</strong></p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("More About Our Impact", expanded=False):
    st.markdown("""
    - **Verified Stories**: Collected with consent from real clients.
    - **Diversity**: Stories from urban and rural clients, all ages.
    - **Impact**: Over 200 clients shared positive outcomes in 2025.
    - **Privacy**: All stories are anonymized to protect client confidentiality.
    """)

# COUNSELING SESSIONS SECTION
st.markdown("<div id='counseling-sessions'></div>", unsafe_allow_html=True)
st.markdown("## Counseling in Action")
st.markdown("""
<div style='background: var(--white); padding: 1rem; border-radius: 10px; box-shadow: 0 3px 6px rgba(0,0,0,0.1); text-align: center;'>
    <p style='font-size: 1.2rem;'>See how our compassionate counselors support clients across Kenya.</p>
    <div style='margin-bottom: 1rem;'>
        <img src='https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=500&q=80' style='width: 100%; max-width: 500px; border-radius: 10px; box-shadow: 0 3px 6px rgba(0,0,0,0.2);' alt='Group therapy session'/>
        <p>Group therapy session fostering connection in Nairobi.</p>
    </div>
    <div>
        <img src='https://images.unsplash.com/photo-1573496359142-b8d87734a5a4?auto=format&fit=crop&w=500&q=80' style='width: 100%; max-width: 500px; border-radius: 10px; box-shadow: 0 3px 6px rgba(0,0,0,0.2);' alt='One-on-one counseling'/>
        <p>One-on-one counseling session in Kisumu.</p>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Our Sessions", expanded=False):
    st.markdown("""
    - **Settings**: Urban centers, telehealth, and select home visits.
    - **Clients**: Youth, adults, and families from diverse backgrounds.
    - **Safety**: Strict confidentiality with encrypted platforms.
    - **Impact**: Reached 600+ clients in 2025 with tailored support.
    """)

# RESOURCES SECTION
st.markdown("<div id='resources'></div>", unsafe_allow_html=True)
st.markdown("## Mental Health Resources")
st.markdown("""
<div style='background: var(--white); padding: 1rem; border-radius: 10px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);'>
    <p style='font-size: 1.2rem;'>Access free resources to support your mental wellness journey.</p>
    <div class='resource-card'>
        <h4>Coping with Anxiety Guide</h4>
        <p>Practical tips for managing anxiety, including breathing exercises and journaling prompts.</p>
        """, unsafe_allow_html=True)
st.markdown(get_download_link("""
# Coping with Anxiety
1. **Deep Breathing**: Inhale for 4 seconds, hold for 4, exhale for 4.
2. **Journaling**: Write three things you’re grateful for daily.
3. **Grounding**: Name 5 things you see, 4 you feel, 3 you hear, 2 you smell, 1 you taste.
""", "anxiety_guide.txt"), unsafe_allow_html=True)
st.markdown("""
    </div>
    <div class='resource-card'>
        <h4>Stress Management Toolkit</h4>
        <p>Strategies for reducing stress, including mindfulness and time management tips.</p>
        """, unsafe_allow_html=True)
st.markdown(get_download_link("""
# Stress Management Toolkit
1. **Mindfulness**: Practice 5-minute daily meditation.
2. **Time Management**: Prioritize tasks with a to-do list.
3. **Physical Activity**: Take a 10-minute walk to clear your mind.
""", "stress_toolkit.txt"), unsafe_allow_html=True)
st.markdown("""
    </div>
    <div class='resource-card'>
        <h4>External Support Links</h4>
        <p>
            <a href='https://www.befrienders.org' target='_blank'>Befrienders Worldwide</a>: Global suicide prevention.<br>
            <a href='https://www.who.int/mental_health' target='_blank'>WHO Mental Health</a>: Reliable mental health information.
        </p>
    </div>
    <div style='text-align: center; margin-top: 1rem;'>
        <a href='#book-appointment' class='primary-btn'>Book a Session</a>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("More About Our Resources", expanded=False):
    st.markdown("""
    - **Free Access**: Downloadable guides available to all.
    - **Updates**: New resources added monthly, next update August 2025.
    - **Support**: Email resources@safespaceorganisation.org for custom requests.
    - **Community**: Share resources at our workshops or via WhatsApp.
    """)

# MENTAL HEALTH BLOG SECTION
st.markdown("<div id='blog'></div>", unsafe_allow_html=True)
st.markdown("## Our Blog")
st.markdown("""
<div style='background: var(--white); padding: 1rem; border-radius: 10px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);'>
    <p style='font-size: 1.2rem;'>Read expert insights to support your mental health journey.</p>
""", unsafe_allow_html=True)
blogs = [
    {"title": "Coping with Economic Stress", "date": "July 20, 2025", "desc": "Learn budgeting and relaxation techniques to manage financial stress, by Dr. Amina Hassan."},
    {"title": "Therapeutic Approaches in Mental Health", "date": "July 15, 2025", "desc": "Explore evidence-based therapies like CBT and EMDR, by Hamdi Roble."},
    {"title": "PTSD Survivor Guide", "date": "July 10, 2025", "desc": "Understand PTSD symptoms and recovery steps, by Dr. James Otieno."}
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
<div style='text-align: center; margin-top: 1rem;'>
    <a href='#crisis' class='primary-btn'>Crisis Support</a>
    <a href='#tracker' class='primary-btn'>Track Your Mood</a>
</div>
""", unsafe_allow_html=True)
with st.expander("More About Our Blog", expanded=False):
    st.markdown("""
    - **Updates**: New posts every two weeks, youth series in August 2025.
    - **Authors**: Psychologists, counselors, and guest experts.
    - **Engage**: Submit questions to blog@safespaceorganisation.org.
    - **Access**: Free PDFs available for all articles.
    """)

# CRISIS RESOURCES SECTION
st.markdown("<div id='crisis'></div>", unsafe_allow_html=True)
st.markdown("## Crisis Support")
st.markdown("""
<div style='background: var(--white); padding: 1rem; border-radius: 10px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);'>
    <p style='font-size: 1.2rem;'>We’re here for you in times of crisis. Reach out for immediate support.</p>
    <ul>
        <li><strong>Befrienders Kenya:</strong> Call 1199, available 24/7.</li>
        <li><strong>SafeSpace Crisis Line:</strong> +254 781 095 919, 8 AM-7 PM EAT (Call or WhatsApp).</li>
        <li><strong>Emergency Services:</strong> Call 999 or visit a hospital.</li>
    </ul>
    <div style='text-align: center; margin-top: 1rem;'>
        <a href='#contact' class='primary-btn'>Get Help Now</a>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("More About Crisis Support", expanded=False):
    st.markdown("""
    - **Training**: 40+ hours of annual training for crisis volunteers.
    - **Partnerships**: Collaborations with Kenyatta Hospital for referrals.
    - **Confidentiality**: Encrypted calls and strict privacy protocols.
    - **Resources**: Free crisis guides available in the Resources section.
    """)

# PROGRESS TRACKER SECTION
st.markdown("<div id='tracker'></div>", unsafe_allow_html=True)
st.markdown("## Mood Tracker")
st.markdown("""
<div style='background: var(--white); padding: 1rem; border-radius: 10px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);'>
    <p style='font-size: 1.2rem;'>Track your emotional wellbeing to better understand your journey.</p>
    <div class='tracker-card'>
        <h4>Log Your Mood</h4>
        <p>Rate your mood (1-5) and add optional notes to monitor your progress.</p>
    </div>
""", unsafe_allow_html=True)
mood = st.slider("How do you feel today? (1 = Low, 5 = High)", 1, 5, 3, key="mood_input")
note = st.text_input("Add a note (optional)", placeholder="e.g., Feeling hopeful today", key="mood_note")
if st.button("Log Mood"):
    st.session_state.mood_history.append({"date": datetime.now(), "mood": mood, "note": note})
    st.success(f"Mood logged at {datetime.now().strftime('%I:%M %p EAT, %B %d, %Y')}!")
for entry in st.session_state.mood_history[-5:]:
    st.markdown(f"- {entry['date'].strftime('%Y-%m-%d %H:%M')}: Mood {entry['mood']}/5 {'(' + entry['note'] + ')' if entry['note'] else ''}")
if st.button("Export Mood History"):
    csv = export_mood_history()
    st.markdown(get_download_link(csv, "mood_history.csv"), unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; margin-top: 1rem;'>
    <a href='#volunteer' class='primary-btn'>Volunteer With Us</a>
</div>
""", unsafe_allow_html=True)
with st.expander("More About Mood Tracking", expanded=False):
    st.markdown("""
    - **Features**: Export your mood history as a CSV file.
    - **Usage**: Log daily for 30 days to identify patterns.
    - **Support**: Email support@safespaceorganisation.org for guidance.
    - **Privacy**: Your data is securely stored and private.
    """)

# VOLUNTEER OPPORTUNITIES SECTION
st.markdown("<div id='volunteer'></div>", unsafe_allow_html=True)
st.markdown("## Volunteer With Us")
st.markdown("""
<div style='background: var(--white); padding: 1rem; border-radius: 10px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);'>
    <p style='font-size: 1.2rem;'>Join our mission to make mental health care accessible to all.</p>
""", unsafe_allow_html=True)
volunteer_roles = [
    {"title": "Outreach Support", "desc": "Assist with 2-4 hour campaigns in Nakuru or Mombasa. Includes 10-hour training."},
    {"title": "Event Volunteer", "desc": "Support events like our July 30 or August 15, 2025, workshops. 4-6 hours per event."},
    {"title": "Crisis Line Assistant", "desc": "Answer calls during 8 AM-7 PM shifts. Requires 20-hour training."}
]
for role in volunteer_roles:
    st.markdown(f"""
    <div class='volunteer-card'>
        <h4>{role['title']}</h4>
        <p>{role['desc']}</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; margin-top: 1rem;'>
    <a href='#volunteer-form' class='primary-btn'>Join as a Volunteer</a>
</div>
""", unsafe_allow_html=True)
st.markdown("<div id='volunteer-form'></div>", unsafe_allow_html=True)
with st.form("volunteer_form", clear_on_submit=True):
    st.markdown("### Volunteer Registration")
    name = st.text_input("Full Name")
    email = st.text_input("Email", placeholder="your.email@example.com")
    phone = st.text_input("Phone", placeholder="+254 XXX XXX XXX")
    experience = st.text_area("Experience", placeholder="e.g., Previous counseling or community work")
    role_preference = st.selectbox("Preferred Role", ["Outreach Support", "Event Volunteer", "Crisis Line Assistant", "Any"])
    submit = st.form_submit_button("Register Now")
    if submit:
        if not all([name, email, re.match(r"[^@]+@[^@]+\.[^@]+", email), phone, experience]):
            st.error("Please fill all fields with valid information.")
        else:
            st.session_state.outreach_form_data = {"name": name, "email": email, "phone": phone, "experience": experience, "role": role_preference}
            st.success(f"Thank you, {name}! Your registration for {role_preference} at {datetime.now().strftime('%I:%M %p EAT, %B %d, %Y')} is received. We’ll contact you at {email} within 48 hours.")
            st.session_state.outreach_form_data = {"name": "", "email": "", "phone": "", "experience": "", "role": "Any"}
st.markdown("""
<div style='text-align: center; margin-top: 1rem;'>
    <a href='#contact' class='primary-btn'>Contact Us</a>
</div>
""", unsafe_allow_html=True)
with st.expander("More About Volunteering", expanded=False):
    st.markdown("""
    - **Impact**: Supported 1,200 people in 2024, targeting 2,000 in 2025.
    - **Training**: 10-hour online and 5-hour in-person sessions.
    - **Recognition**: Certificates and Volunteer Day on Dec 15, 2025.
    - **Support**: Monthly check-ins with our team.
    """)

# EVENTS SECTION
st.markdown("<div id='events'></div>", unsafe_allow_html=True)
st.markdown("## Upcoming Events")
st.markdown("""
<div style='background: var(--white); padding: 1rem; border-radius: 10px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);'>
    <p style='font-size: 1.2rem;'>Join our free workshops to learn and connect with others.</p>
    <div class='event-card'>
        <h4>Stress Management Workshop</h4>
        <p>July 30, 2025, 9 AM-1 PM, Nairobi Hall. Free, register at <a href='mailto:events@safespaceorganisation.org'>events@safespaceorganisation.org</a>.</p>
    </div>
    <div class='event-card'>
        <h4>Youth Mental Health Forum</h4>
        <p>August 15, 2025, 10 AM-2 PM, Kisumu Center. For ages 13-25.</p>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("More About Events", expanded=False):
    st.markdown("""
    - **Registration**: Limited to 50 attendees, email required.
    - **Materials**: Free handouts and online Q&A sessions.
    - **Past Events**: June 2025 Trauma Day with 80 attendees.
    - **Accessibility**: Sign language interpreters and wheelchair access.
    """)

# PARTNERSHIPS SECTION
st.markdown("<div id='partnerships'></div>", unsafe_allow_html=True)
st.markdown("## Our Partners")
st.markdown("""
<div style='background: var(--white); padding: 1rem; border-radius: 10px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);'>
    <p style='font-size: 1.2rem;'>We collaborate with leading organizations to expand mental health access.</p>
    <div class='partnership-card'>
        <h4>Kenyatta National Hospital</h4>
        <p>Supporting trauma programs and referrals since 2024.</p>
    </div>
    <div class='partnership-card'>
        <h4>Kenya Red Cross</h4>
        <p>Training for disaster response since 2023.</p>
    </div>
    <div class='partnership-card'>
        <h4>Ministry of Health</h4>
        <p>Policy support and funding for rural outreach.</p>
    </div>
    <div style='text-align: center; margin-top: 1rem;'>
        <a href='#partnership-form' class='primary-btn'>Become a Partner</a>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown("<div id='partnership-form'></div>", unsafe_allow_html=True)
with st.form("partnership_form", clear_on_submit=True):
    st.markdown("### Partner or Donate")
    name = st.text_input("Full Name")
    organization = st.text_input("Organization Name (if applicable)")
    email = st.text_input("Email", placeholder="your.email@example.com")
    phone = st.text_input("Phone", placeholder="+254 XXX XXX XXX")
    partnership_type = st.selectbox("Register As", ["Partner", "Donor"])
    submit = st.form_submit_button("Submit")
    if submit:
        if not all([name, email, re.match(r"[^@]+@[^@]+\.[^@]+", email), phone]):
            st.error("Please fill all required fields.")
        else:
            st.session_state.partnership_form_data = {"name": name, "organization": organization, "email": email, "phone": phone, "type": partnership_type}
            st.success(f"Thank you, {name}! Your {partnership_type} registration at {datetime.now().strftime('%I:%M %p EAT, %B %d, %Y')} is received. We’ll contact you at {email} within 48 hours.")
            st.session_state.partnership_form_data = {"name": "", "organization": "", "email": "", "phone": "", "type": "Partner"}

# PARTNER WITH US SECTION
st.markdown("<div id='partner-with-us'></div>", unsafe_allow_html=True)
st.markdown("## Partner With Us")
st.markdown("""
<div style='background: var(--white); padding: 1rem; border-radius: 10px; box-shadow: 0 3px 6px rgba(0,0,0,0.1); text-align: center;'>
    <p style='font-size: 1.2rem;'>Collaborate with us to make mental health care accessible to all. Schools, businesses, and NGOs can support training, mobile clinics, or outreach programs.</p>
    <p><strong>Benefits:</strong> Enhance your CSR profile, access mental health resources, and impact communities.</p>
    <p>Contact us at <a href='mailto:partnership@safespaceorganisation.org'>partnership@safespaceorganisation.org</a> or register below.</p>
    <a href='#partnership-form' class='primary-btn'>Get Started</a>
</div>
""", unsafe_allow_html=True)
with st.expander("More About Partnerships", expanded=False):
    st.markdown("""
    - **Opportunities**: Joint workshops, funding, or research collaborations.
    - **Impact**: Reach 2,000+ clients by 2026 with new partners.
    - **Process**: Consultation within 72 hours of contact.
    - **Examples**: Partnerships with health NGOs and schools.
    """)

# ACCESSIBILITY SECTION
st.markdown("<div id='accessibility'></div>", unsafe_allow_html=True)
st.markdown("## Accessibility at SafeSpace")
st.markdown("""
<div style='background: var(--white); padding: 1rem; border-radius: 10px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);'>
    <p style='font-size: 1.2rem;'>We’re committed to making our services accessible to everyone.</p>
    <ul>
        <li><strong>Physical Access</strong>: Wheelchair-friendly facilities at our Nairobi office.</li>
        <li><strong>Language Support</strong>: Sign language interpreters and multilingual therapists.</li>
        <li><strong>Online Options</strong>: Secure telehealth for remote or mobility-limited clients.</li>
        <li><strong>Financial Aid</strong>: Sliding scale fees and subsidies for low-income clients.</li>
    </ul>
    <div style='text-align: center; margin-top: 1rem;'>
        <a href='#contact' class='primary-btn'>Learn More</a>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("More About Accessibility", expanded=False):
    st.markdown("""
    - **Custom Support**: Request accommodations at info@safespaceorganisation.org.
    - **Events**: All workshops include accessibility features.
    - **Technology**: Encrypted platforms for secure online sessions.
    - **Feedback**: Share suggestions to improve access.
    """)

# BOOK APPOINTMENT SECTION
st.markdown("<div id='book-appointment'></div>", unsafe_allow_html=True)
st.markdown("## Book Your Appointment")
st.markdown("""
<div style='background: var(--white); padding: 1rem; border-radius: 10px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);'>
    <p style='font-size: 1.2rem;'>Take the first step toward healing. Schedule a counseling session with our compassionate team.</p>
    <div class='appointment-card'>
        <h4>Appointment Booking Form</h4>
        <p>Fill in your details below or contact us via WhatsApp. We’ll confirm within 48 hours.</p>
    </div>
    <div style='text-align: center; margin-top: 1rem;'>
        <a href='https://wa.me/254781095919?text=Hello%20I%20would%20like%20to%20book%20a%20counseling%20appointment' class='primary-btn'>Book via WhatsApp</a>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown("<div id='appointment-form'></div>", unsafe_allow_html=True)
with st.form("appointment_form", clear_on_submit=True):
    name = st.text_input("Full Name")
    email = st.text_input("Email", placeholder="your.email@example.com")
    phone = st.text_input("Phone", placeholder="+254 XXX XXX XXX")
    preferred_date = st.date_input("Preferred Date", min_value=datetime.now().date())
    preferred_time = st.time_input("Preferred Time")
    counseling_type = st.selectbox("Counseling Type", ["Individual Counseling", "Group Therapy", "Family Counseling", "Trauma Recovery Therapy", "Online Counseling"])
    submit = st.form_submit_button("Book Now")
    if submit:
        if not all([name, email, re.match(r"[^@]+@[^@]+\.[^@]+", email), phone, preferred_date, preferred_time]):
            st.error("Please fill all required fields with valid information.")
        else:
            st.session_state.appointment_form_data = {
                "name": name,
                "email": email,
                "phone": phone,
                "date": preferred_date.strftime("%Y-%m-%d"),
                "time": preferred_time.strftime("%I:%M %p"),
                "type": counseling_type
            }
            st.success(f"Thank you, {name}! Your {counseling_type} appointment request for {preferred_date.strftime('%B %d, %Y')} at {preferred_time.strftime('%I:%M %p')} has been received at {datetime.now().strftime('%I:%M %p EAT, %B %d, %Y')}. We’ll contact you at {email} within 48 hours to confirm.")
            st.session_state.appointment_form_data = {"name": "", "email": "", "phone": "", "date": "", "time": "", "type": "Online"}
with st.expander("What to Expect When Booking", expanded=False):
    st.markdown("""
    - **Availability**: Sessions available Mon-Fri 9 AM-5 PM, Sat 10 AM-2 PM.
    - **Confirmation**: Via email, phone, or WhatsApp within 48 hours.
    - **Rescheduling**: Contact info@safespaceorganisation.org or WhatsApp +254 781 095 919.
    - **First Session**: Includes a 15-minute consultation to discuss goals and match with a therapist.
    - **Tips**: Reflect on your needs and bring any relevant history to your session.
    """)

# FAQ SECTION
st.markdown("<div id='faq'></div>", unsafe_allow_html=True)
st.markdown("## Frequently Asked Questions")
st.markdown("""
<div style='background: var(--white); padding: 1rem; border-radius: 10px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);'>
    <p style='font-size: 1.2rem;'>Find answers to common questions about our services.</p>
    <p><strong>Q: Who can access services?</strong> A: All ages, with specialized programs for youth, adults, and families.</p>
    <p><strong>Q: Is it confidential?</strong> A: Yes, we use encrypted platforms and strict privacy protocols.</p>
    <p><strong>Q: How do I pay?</strong> A: Cash, M-Pesa, or bank transfer; subsidies available.</p>
    <p><strong>Q: How do I book?</strong> A: Use the Book Appointment form, call, or WhatsApp +254 781 095 919.</p>
    <p><strong>Q: What should I bring to a session?</strong> A: Any medical/mental health history and your goals for therapy.</p>
    <p><strong>Q: Are therapists qualified?</strong> A: All hold Master’s degrees or higher, with certifications in CBT, EMDR, and more.</p>
</div>
""", unsafe_allow_html=True)
with st.expander("More FAQs", expanded=False):
    st.markdown("""
    - **Support**: Email faq@safespaceorganisation.org for more questions.
    - **Updates**: FAQs updated quarterly, last in July 2025.
    - **Resources**: Download our full FAQ guide in the Resources section.
    """)

# CONTACT SECTION
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.markdown("## Get in Touch")
st.markdown("""
<div style='background: var(--white); padding: 1rem; border-radius: 10px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);'>
    <p style='font-size: 1.2rem;'>We’re here to support you. Reach out today!</p>
    <p><strong>📍</strong> Greenhouse Plaza, Ngong Road, Nairobi.</p>
    <p><strong>📞</strong> +254 781 095 919, 8 AM-7 PM EAT (Call or WhatsApp).</p>
    <p><strong>✉️</strong> <a href='mailto:info@safespaceorganisation.org'>info@safespaceorganisation.org</a>, 24-hour response.</p>
    <p><strong>Hours:</strong> Mon-Fri 9 AM-5 PM, Sat 10 AM-2 PM.</p>
    <div style='display: flex; gap: 1rem; flex-wrap: wrap; justify-content: center;'>
        <a href='#book-appointment' class='primary-btn'>Book Appointment</a>
        <a href='https://wa.me/254781095919?text=Hello%20I%20have%20a%20question%20about%20SafeSpace%20services' class='primary-btn'>Contact via WhatsApp</a>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("More About Contacting Us", expanded=False):
    st.markdown("""
    - **Appointments**: Book online, call, or WhatsApp for same-day slots.
    - **Accessibility**: Wheelchair access, sign language interpreters.
    - **Response Time**: Within 24 hours for emails, 48 hours for bookings.
    - **Location**: View our office map on our website.
    """)

# CHATBOT
st.markdown("""
<button class='chatbot-toggle' id='chatbot-toggle'>💬</button>
<div class='chatbot-container' id='chatbot'>
    <h4>Ask SafeSpace Bot</h4>
    <div id='chat-messages' style='max-height: 350px; overflow-y: auto; margin-bottom: 0.5rem;'>
""", unsafe_allow_html=True)
for sender, message in st.session_state.chat_history:
    st.markdown(f"<div class='chatbot-message {sender}'><p>{message}</p></div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("", placeholder="Ask about services, bookings, or support...", key="chat_input")
    submit = st.form_submit_button("Send")
    if submit and user_input:
        response = get_chatbot_response(user_input)
        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("bot", response))
st.markdown("</div>", unsafe_allow_html=True)

# WhatsApp Chat Widget
st.markdown("""
<button class='whatsapp-toggle' id='whatsapp-toggle'>📱</button>
<div class='whatsapp-widget-container' id='whatsapp-widget'>
    <h4>Chat with SafeSpace on WhatsApp</h4>
    <div id='whatsapp-chat'>
        <p>Click below to start a chat:</p>
        <a href='https://wa.me/254781095સ
        <a href='https://wa.me/254781095919?text=Hello%20I%20would%20like%20to%20book%20a%20counseling%20appointment' style='display: inline-block; padding: 0.5rem 1rem; border-radius: 20px; background: linear-gradient(135deg, #25D366, #128C7E); color: white; text-decoration: none; font-size: 0.9rem;'>Chat with Us</a>
    </div>
</div>
<script>
    document.addEventListener('DOMContentLoaded', function() {
        const chatbotToggle = document.getElementById('chatbot-toggle');
        const whatsappToggle = document.getElementById('whatsapp-toggle');
        const chatbot = document.getElementById('chatbot');
        const whatsappWidget = document.getElementById('whatsapp-widget');
        if (chatbotToggle && chatbot) {
            chatbotToggle.addEventListener('click', function() {
                chatbot.classList.toggle('active');
                whatsappWidget.classList.remove('active');
            });
        }
        if (whatsappToggle && whatsappWidget) {
            whatsappToggle.addEventListener('click', function() {
                whatsappWidget.classList.toggle('active');
                chatbot.classList.remove('active');
            });
        }
    });
</script>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("---")
st.markdown("""
<div class='footer'>
    <p style='font-size: 1rem;'>© 2023-2025 SafeSpace Organisation | Crafted with Care</p>
    <div style='display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;'>
        <a href='https://facebook.com/safespaceorganisation' target='_blank' class='primary-btn'>Facebook</a>
        <a href='https://instagram.com/safespaceorganisation' target='_blank' class='primary-btn'>Instagram</a>
        <a href='https://twitter.com/safespaceorganisation' target='_blank' class='primary-btn'>Twitter</a>
        <a href='https://linkedin.com/company/safespaceorganisation' target='_blank' class='primary-btn'>LinkedIn</a>
    </div>
</div>
""", unsafe_allow_html=True)

with st.form("newsletter_form", clear_on_submit=True):
    st.markdown("<div style='max-width: 400px; margin: 1rem auto; display: flex; gap: 0.5rem;'>", unsafe_allow_html=True)
    newsletter_email = st.text_input("", placeholder="Get monthly mental health tips...", key="newsletter_email")
    submit_newsletter = st.form_submit_button("Subscribe")
    st.markdown("</div>", unsafe_allow_html=True)
    if submit_newsletter:
        if not newsletter_email or not re.match(r"[^@]+@[^@]+\.[^@]+", newsletter_email):
            st.error("Please provide a valid email.")
        else:
            st.success(f"Subscribed! Next newsletter: August 1, 2025, 9 AM EAT.")
