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
    page_title="SafeSpace Organization",
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
    {
        "keywords": ["what is counseling", "what is counselling", "counseling mean"],
        "answer": "Counseling is a professional process where a trained therapist helps you address emotional, mental, or behavioral challenges in a safe, confidential space. At SafeSpace Organization, we offer counseling to manage issues like anxiety, depression, trauma, or relationship problems using evidence-based methods like CBT and EMDR. Sessions are tailored to your needs, helping you gain coping skills and improve wellbeing. Time: {time}."
    },
    {
        "keywords": ["how does counseling work", "what happens in counseling", "counseling session"],
        "answer": "In a counseling session, you’ll meet with a therapist to discuss your concerns, set goals, and explore solutions. Sessions last 50-90 minutes, starting with a 15-minute consultation to match you with the right therapist. Expect talk therapy, exercises (e.g., journaling), or techniques like mindfulness. Our therapists use CBT, EMDR, or DBT to guide you. Progress is tracked weekly, and 85% of clients report improvement after 8 sessions. Time: {time}."
    },
    {
        "keywords": ["what is cbt", "cognitive behavioral therapy", "cbt work"],
        "answer": "Cognitive Behavioral Therapy (CBT) is a therapy that helps you identify and change negative thought patterns affecting your emotions and behavior. It’s effective for anxiety, depression, and PTSD. At SafeSpace, CBT involves structured 50-minute sessions with exercises like thought records or relaxation techniques. Clients learn coping skills, with 80% seeing mood improvement after 6-8 sessions. Time: {time}."
    },
    {
        "keywords": ["what is emdr", "eye movement desensitization", "emdr therapy"],
        "answer": "Eye Movement Desensitization and Reprocessing (EMDR) is a therapy for trauma, helping you process distressing memories. It uses guided eye movements to reduce emotional triggers. At SafeSpace, 75-minute EMDR sessions are led by certified therapists for issues like abuse or accidents. 88% of clients report reduced triggers after 10 sessions. Time: {time}."
    },
    {
        "keywords": ["cost of counseling", "how much counseling", "counseling fees"],
        "answer": "Counseling at SafeSpace costs KSh 500-2,000 per session on a sliding scale based on income. Subsidies are available for low-income clients, and we offer free monthly workshops. Contact us at +254758943430 or info@safespaceorganization.org for payment options like M-Pesa or bank transfer. Time: {time}."
    },
    {
        "keywords": ["prepare for counseling", "get ready for session", "counseling preparation"],
        "answer": "To prepare for counseling, reflect on your goals (e.g., managing anxiety), bring any medical or mental health history, and arrive 5-10 minutes early. For online sessions, ensure a stable internet connection and a private space. Our therapists will guide you through the rest. Time: {time}."
    },
    {
        "keywords": ["therapist qualifications", "counselor credentials", "therapist trained"],
        "answer": "Our therapists at SafeSpace hold Master’s degrees or higher in psychology or counseling, with certifications in CBT, EMDR, DBT, and other therapies. They average 10+ years of experience and are registered with the Kenya Counseling and Psychological Association (KCPA). Time: {time}."
    },
    {
        "keywords": ["individual counseling", "one on one counseling", "personal therapy"],
        "answer": "Individual Counseling at SafeSpace offers 50-minute one-on-one sessions for issues like depression, anxiety, PTSD, or OCD. Using CBT, DBT, or ACT, therapists create personalized plans with weekly progress tracking. Available in-person or online. 85% of clients report better mood after 8 sessions. Book via our website or WhatsApp +254758943430. Time: {time}."
    },
    {
        "keywords": ["group therapy", "group counseling", "support group"],
        "answer": "Group Therapy involves 90-minute weekly sessions for 8-10 people, focusing on grief, addiction, or anxiety. Led by two counselors, it includes peer support and mindfulness exercises. Available in-person or online, with a 3-month commitment recommended. 80% of participants feel less isolated after 6 sessions. Register at #services or WhatsApp +254758943430. Time: {time}."
    },
    {
        "keywords": ["youth mentorship", "teen counseling", "youth program"],
        "answer": "Our Youth Mentorship Program supports ages 13-25 with 60-minute biweekly sessions addressing self-esteem, peer pressure, or academic stress. Using art therapy, CBT, and peer support, it includes group workshops and one-on-one mentoring. Available in-person or online. 95% of youth report increased confidence after 3 months. Contact us at +254758943430. Time: {time}."
    },
    {
        "keywords": ["confidential", "counseling privacy", "is counseling safe"],
        "answer": "Yes, counseling at SafeSpace is fully confidential. We use encrypted platforms for online sessions and follow strict privacy protocols. Your information is only shared with your consent or in emergencies, per KCPA guidelines. Time: {time}."
    },
    {
        "keywords": ["safespace organization", "about safespace", "who is safespace"],
        "answer": "SafeSpace Organization, founded in 2023 by Jerim Owino and Hamdi Roble, is a non-profit providing accessible mental health care in Kenya. We offer counseling for trauma, depression, and more, using CBT, EMDR, and mindfulness. Contact us at info@safespaceorganization.org. Time: {time}."
    },
    {
        "keywords": ["contact safespace", "reach safespace", "safespace phone"],
        "answer": "Contact SafeSpace at +254758943430 (8 AM-7 PM EAT, call or WhatsApp) or email info@safespaceorganization.org (24-hour response). Visit us at Greenhouse Plaza, Ngong Road, Nairobi. Time: {time}."
    },
    {
        "keywords": ["book appointment", "schedule counseling", "make appointment"],
        "answer": "Book a counseling session via the Book Appointment section on our website, call/WhatsApp +254758943430 (8 AM-7 PM EAT), or email info@safespaceorganization.org. Provide your name, email, phone, preferred date, time, and counseling type. We’ll confirm within 48 hours. Time: {time}."
    },
    {
        "keywords": [],
        "answer": "I’m sorry, I didn’t understand your question. Try asking about counseling, services, costs, preparation, or how to book an appointment. You can also contact us at +254758943430 or info@safespaceorganization.org. Time: {time}."
    }
]

# Function to get chatbot response
def get_chatbot_response(query):
    if not query or not isinstance(query, str):
        return knowledge_base[-1]["answer"].format(time=datetime.now().strftime("%I:%M %p EAT, %B %d, %Y"))
    
    query = query.lower().strip()
    for entry in knowledge_base[:-1]:  # Skip default response
        for keyword in entry["keywords"]:
            if keyword in query:
                return entry["answer"].format(time=datetime.now().strftime("%I:%M %p EAT, %B %d, %Y"))
    return knowledge_base[-1]["answer"].format(time=datetime.now().strftime("%I:%M %p EAT, %B %d, %Y"))

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
    <h1>SafeSpace Organization</h1>
    <p style='font-size: 1.2rem;'>Your Safe Haven for Mental Wellness Since 2023</p>
</div>
""", unsafe_allow_html=True)

# HERO SECTION
st.markdown("<div id='hero'></div>", unsafe_allow_html=True)
st.markdown("""
<div class='cta-banner'>
    <h1>Welcome to Your Journey of Healing</h1>
    <p style='font-size: 1.2rem; max-width: 800px; margin: 1rem auto;'>At SafeSpace Organization, we provide compassionate, professional counseling to support you through life’s challenges. Start your path to emotional wellness today in a safe, inclusive environment.</p>
    <img src='https://images.unsplash.com/photo-1588195539435-d6b5f19e1c24?auto=format&fit=crop&w=700&q=80' style='width: 100%; max-width: 700px; border-radius: 10px; margin: 1rem auto; box-shadow: 0 3px 6px rgba(0,0,0,0.2);' alt='Counseling session'/>
    <div style='display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;'>
        <a href='#book-appointment' class='primary-btn'>Start Your Journey</a>
        <a href='#services' class='primary-btn'>Explore Services</a>
        <a href='#contact' class='primary-btn'>Get in Touch</a>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Why Choose SafeSpace Organization?", expanded=False):
    st.markdown("""
    - **Mission**: We’re here to break mental health stigma and make care accessible to all.
    - **Impact**: Over 600 clients supported in 2025 with a 90% satisfaction rate.
    - **Accessibility**: Affordable sessions, online options, and support in multiple languages.
    - **Confidentiality**: Your privacy is our priority with secure, encrypted services.
    """)

# ABOUT SECTION
st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.markdown("## About SafeSpace Organization")
st.markdown("""
<div style='background: var(--white); padding: 1rem; border-radius: 10px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);'>
    <p style='font-size: 1.2rem;'>Founded in 2023 by Jerim Owino and Hamdi Roble, SafeSpace Organization is a non-profit committed to transforming mental health care in Kenya. Our team of 15 certified professionals serves Nairobi, Kisumu, Eldoret, and 20+ districts, addressing trauma, depression, anxiety, and family challenges with evidence-based therapies like CBT, EMDR, and mindfulness.</p>
    <p>We partner with NGOs, the Ministry of Health, and local communities to deliver inclusive, culturally sensitive care, ensuring everyone has access to a safe space for healing.</p>
    <div style='text-align: center; margin-top: 1rem;'>
        <a href='#services' class='primary-btn'>Discover Our Services</a>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Our Story and Impact", expanded=False):
    st.markdown("""
    - **Founded**: Launched after a 2022 pilot supporting 50 clients.
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
        <p>Jerim Owino, a licensed counselor with a Bachelor’s degree in Psychology from Maasai Mara University (2010), has over 12 years of experience in mental health care. Specializing in trauma and grief counseling, he is certified in Cognitive Behavioral Therapy (CBT) and Eye Movement Desensitization and Reprocessing (EMDR). Jerim founded SafeSpace Organization to address mental health challenges through accessible care. He has trained 50+ community health workers in psychological first aid, co-authored a trauma counseling guide, and leads SafeSpace’s clinical programs, ensuring evidence-based care. His vision is to make mental health support accessible to all.</p>
    </div>
    <div class='founder-card'>
        <h4>Hamdi Roble</h4>
        <p>Hamdi Roble, a human resource manager with 8 years of experience in organizational management, holds a Bachelor’s degree in Human Resource Management from the University of Nairobi (2015). She oversees SafeSpace Organization’s operations, including staff training, volunteer coordination, and program logistics. Hamdi developed a comprehensive training program for counselors and volunteers, enhancing service delivery. Her passion for mental health advocacy drives her work to create structured support systems. Hamdi’s goal is to build a sustainable, inclusive organization that empowers both clients and staff.</p>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("More About Our Founders", expanded=False):
    st.markdown("""
    - **Jerim Owino**: 
      - **Training**: Certified by the Kenya Counseling and Psychological Association (KCPA) in CBT (2014) and EMDR (2018).
      - **Achievements**: Led SafeSpace’s 2022 pilot, supporting 50 clients; received 2024 KCPA Innovation Award.
      - **Publications**: Co-authored “Trauma Recovery in Kenya” (2023).
      - **Vision**: Expand mental health access with mobile clinics by 2026.
    - **Hamdi Roble**: 
      - **Training**: Certified in HR Management (2016) and Non-Profit Management (2020).
      - **Achievements**: Coordinated outreach to 1,200+ clients in 2024; streamlined volunteer onboarding.
      - **Community Work**: Organized mental health awareness campaigns since 2017.
      - **Vision**: Create a national network of trained mental health advocates by 2027.
    """)

# SERVICES SECTION
st.markdown("<div id='services'></div>", unsafe_allow_html=True)
st.markdown("## Our Counseling Services")
st.markdown("""
<div style='background: var(--white); padding: 1rem; border-radius: 10px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);'>
    <p style='font-size: 1.2rem;'>Our team of 15 certified therapists, with over 75 years of combined experience, offers tailored counseling to address a wide range of mental health needs. Each service includes a free 15-minute consultation to ensure the right fit, with sessions available in-person in Nairobi, Kisumu, and Eldoret or online via secure platforms. Fees range from KSh 500-2,000 on a sliding scale, with subsidies for low-income clients.</p>
</div>
""", unsafe_allow_html=True)
services = [
    {
        "icon": "👤",
        "title": "Individual Counseling",
        "desc": "Personalized 50-minute sessions addressing chronic depression, anxiety, PTSD, OCD, or low self-esteem. Using Cognitive Behavioral Therapy (CBT), Dialectical Behavior Therapy (DBT), and Acceptance and Commitment Therapy (ACT), our therapists help you develop coping strategies and achieve emotional balance. Sessions include goal-setting, weekly progress tracking, and tailored exercises. Available in-person (Nairobi, Kisumu, Eldoret) or online, with evening/weekend slots. Outcomes: 85% of clients report improved mood after 8 sessions (2024 data). <em>“Individual counseling gave me tools to manage my anxiety.” – Sarah M., Nairobi, 2025</em>."
    },
    {
        "icon": "👥",
        "title": "Group Therapy",
        "desc": "90-minute weekly sessions for 8-10 participants, focusing on grief, addiction recovery, social anxiety, or stress management. Facilitated by two counselors using peer support, role-playing, and guided mindfulness, sessions foster connection and resilience. Expect monthly themes (e.g., coping with loss) and a 3-month commitment for optimal results. Available in-person or online. Outcomes: 80% of participants feel less isolated after 6 sessions (2024 survey). <em>“Group therapy helped me find my voice.” – Peter O., Kisumu, 2025</em>."
    },
    {
        "icon": "🏠",
        "title": "Family Counseling",
        "desc": "60-minute sessions to address parenting challenges, marital conflicts, or intergenerational trauma. Using systemic therapy, narrative therapy, and solution-focused techniques, our therapists improve communication and resolve conflicts. Expect a 6-session program with monthly check-ins, available in-person (Nairobi, Eldoret) or online, with home visits in select areas. Outcomes: 90% of families report stronger bonds after 6 sessions. <em>“We rebuilt trust as a family.” – Amina H., Eldoret, 2025</em>."
    },
    {
        "icon": "🧠",
        "title": "Trauma Recovery Therapy",
        "desc": "75-minute sessions for survivors of violence, abuse, accidents, or natural disasters. Using Eye Movement Desensitization and Reprocessing (EMDR), trauma-focused CBT, and somatic experiencing, our specialists help process trauma safely. Expect a 6-12 session program with ongoing support groups and priority for urgent cases. Available in Nairobi or via telehealth. Outcomes: 88% of clients report reduced triggers after 10 sessions. <em>“Trauma therapy gave me my life back.” – Jane K., Nairobi, 2025</em>."
    },
    {
        "icon": "💻",
        "title": "Online Counseling",
        "desc": "50-minute virtual sessions for anxiety, depression, stress, or relationship issues, using CBT, mindfulness, and solution-focused therapy. Delivered via encrypted Zoom or Google Meet with 24/7 scheduling flexibility. Expect a tailored treatment plan and access to digital resources. Outcomes: 92% client satisfaction for accessibility (2024 data). <em>“Online sessions fit my busy schedule perfectly.” – David W., Mombasa, 2025</em>."
    },
    {
        "icon": "🌟",
        "title": "Youth Mentorship Program",
        "desc": "60-minute biweekly sessions for ages 13-25, addressing self-esteem, peer pressure, academic stress, or identity issues. Combining group workshops and one-on-one mentoring, our program uses art therapy, CBT, and peer support. Expect a 4-month program with quarterly parent check-ins, available in Nairobi, Kisumu, or online. Outcomes: 95% of youth report increased confidence after 3 months. <em>“Mentorship helped me believe in myself.” – Esther N., Kisumu, 2025</em>."
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
    - **Therapist Credentials**: All therapists hold Master’s degrees or higher, certified in CBT, EMDR, DBT, and more, with 10+ years of experience on average.
    - **Affordability**: Sliding scale fees (KSh 500-2,000/session), subsidies for low-income clients, and free monthly workshops.
    - **Client Feedback**: 95% report improved wellbeing after 6 sessions (2024 survey).
    - **Innovation**: Piloting AI-assisted tools for rural access, launching Q4 2025.
    - **Preparation**: Bring any relevant history, reflect on goals, and expect a warm, confidential welcome.
    - **Customization**: Sessions tailored to cultural, linguistic, and personal needs.
    """)

# SUCCESS STORIES SECTION
st.markdown("<div id='success-stories'></div>", unsafe_allow_html=True)
st.markdown("## Success Stories")
st.markdown("""
<div style='background: var(--white); padding: 1rem; border-radius: 10px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);'>
    <p style='font-size: 1.2rem; text-align: center;'>Hear from clients who found hope and healing with SafeSpace Organization.</p>
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
    - **Support**: Email resources@safespaceorganization.org for custom requests.
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
    - **Engage**: Submit questions to blog@safespaceorganization.org.
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
        <li><strong>SafeSpace Crisis Line:</strong> +254758943430, 8 AM-7 PM EAT (Call or WhatsApp).</li>
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
    - **Support**: Email support@safespaceorganization.org for guidance.
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
    {"title": "Outreach Support", "desc": "Assist with 2-4 hour campaigns. Includes 10-hour training."},
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
        <p>July 30, 2025, 9 AM-1 PM, Nairobi Hall. Free, register at <a href='mailto:events@safespaceorganization.org'>events@safespaceorganization.org</a>.</p>
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
    <p style='font-size: 1.2rem;'>Collaborate with SafeSpace Organization to make mental health care accessible to all. Schools, businesses, and NGOs can support training, mobile clinics, or outreach programs.</p>
    <p><strong>Benefits:</strong> Enhance your CSR profile, access mental health resources, and impact communities.</p>
    <p>Contact us at <a href='mailto:partnership@safespaceorganization.org'>partnership@safespaceorganization.org</a> or register below.</p>
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
st.markdown("## Accessibility at SafeSpace Organization")
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
    - **Custom Support**: Request accommodations at info@safespaceorganization.org.
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
        <a href='https://wa.me/254758943430?text=Hello%20I%20would%20like%20to%20book%20a%20counseling%20appointment' class='primary-btn'>Book via WhatsApp</a>
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
    counseling_type = st.selectbox("Counseling Type", ["Individual Counseling", "Group Therapy", "Family Counseling", "Trauma Recovery Therapy", "Online Counseling", "Youth Mentorship"])
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
    - **Rescheduling**: Contact info@safespaceorganization.org or WhatsApp +254758943430.
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
    <p><strong>Q: How do I book?</strong> A: Use the Book Appointment form, call, or WhatsApp +254758943430.</p>
    <p><strong>Q: What should I bring to a session?</strong> A: Any medical/mental health history and your goals for therapy.</p>
    <p><strong>Q: Are therapists qualified?</strong> A: All hold Master’s degrees or higher, with certifications in CBT, EMDR, and more.</p>
</div>
""", unsafe_allow_html=True)
with st.expander("More FAQs", expanded=False):
    st.markdown("""
    - **Support**: Email faq@safespaceorganization.org for more questions.
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
    <p><strong>📞</strong> +254758943430, 8 AM-7 PM EAT (Call or WhatsApp).</p>
    <p><strong>✉️</strong> <a href='mailto:info@safespaceorganization.org'>info@safespaceorganization.org</a>, 24-hour response.</p>
    <p><strong>Hours:</strong> Mon-Fri 9 AM-5 PM, Sat 10 AM-2 PM.</p>
    <div style='display: flex; gap: 1rem; flex-wrap: wrap; justify-content: center;'>
        <a href='#book-appointment' class='primary-btn'>Book Appointment</a>
        <a href='https://wa.me/254758943430?text=Hello%20I%20have%20a%20question%20about%20SafeSpace%20services' class='primary-btn'>Contact via WhatsApp</a>
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

# CHATBOT SECTION
st.markdown("<div id='chatbot-section'></div>", unsafe_allow_html=True)
st.markdown("""
<button class='chatbot-toggle' id='chatbot-toggle'>💬</button>
<div class='chatbot-container' id='chatbot'>
    <h4>Ask SafeSpace Bot</h4>
    <div id='chat-messages' style='max-height: 350px; overflow-y: auto; margin-bottom: 0.5rem;'>
""", unsafe_allow_html=True)
# Display chat history
for sender, message in st.session_state.chat_history:
    st.markdown(f"<div class='chatbot-message {sender}'><p>{message}</p></div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
# Chatbot input form
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask a question...", placeholder="e.g., What is counseling? How do I book a session?", key=f"chat_input_{datetime.now().timestamp()}")
    submit = st.form_submit_button("Send")
    if submit and user_input:
        try:
            response = get_chatbot_response(user_input)
            st.session_state.chat_history.append(("user", user_input))
            st.session_state.chat_history.append(("bot", response))
            # Force rerender to show new messages
            st.rerun()
        except Exception as e:
            st.error(f"Error processing your request: {str(e)}. Please try again or contact support@safespaceorganization.org.")
st.markdown("</div>", unsafe_allow_html=True)

# WhatsApp Chat Widget
st.markdown("""
<button class='whatsapp-toggle' id='whatsapp-toggle'>📱</button>
<div class='whatsapp-widget-container' id='whatsapp-widget'>
    <h4>Chat with SafeSpace on WhatsApp</h4>
    <div id='whatsapp-chat'>
        <p>Click below to start a chat:</p>
        <a href='https://wa.me/254758943430?text=Hello%20I%20would%20like%20to%20book%20a%20counseling%20appointment' style='display: inline-block; padding: 0.5rem 1rem; border-radius: 20px; background: linear-gradient(135deg, #25D366, #128C7E); color: white; text-decoration: none; font-size: 0.9rem;'>Chat with Us</a>
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
    <p style='font-size: 1rem;'>© 2023-2025 SafeSpace Organization | Crafted with Care</p>
    <div style='display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;'>
        <a href='https://facebook.com/safespaceorganization' target='_blank' class='primary-btn'>Facebook</a>
        <a href='https://instagram.com/safespaceorganization' target='_blank' class='primary-btn'>Instagram</a>
        <a href='https://twitter.com/safespaceorganization' target='_blank' class='primary-btn'>Twitter</a>
        <a href='https://linkedin.com/company/safespaceorganization' target='_blank' class='primary-btn'>LinkedIn</a>
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
