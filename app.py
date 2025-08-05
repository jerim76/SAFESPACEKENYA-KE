import streamlit as st
from datetime import datetime
import re
import base64
import pandas as pd

# Custom CSS embedded directly
st.markdown("""
<style>
    :root {
        --primary: #2E7D32; /* Deep Green */
        --accent: #D81B60; /* Pink */
        --light: #F5F5F5;
        --dark: #212121;
        --deep-blue: #1E88E5;
        --shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    .stApp {
        background: linear-gradient(135deg, var(--light), #FFFFFF);
        font-family: 'Roboto', sans-serif;
        color: var(--dark);
        min-height: 100vh;
        width: 100%;
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    h1, h2, h3, h4 {
        font-family: 'Merriweather', serif;
        color: var(--deep-blue);
        text-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }
    h1 { font-size: 2.5rem; font-weight: 700; }
    h2 { font-size: 2rem; font-weight: 600; }
    h3 { font-size: 1.6rem; font-weight: 500; }
    h4 { font-size: 1.3rem; font-weight: 400; }
    .card {
        background: #FFFFFF;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: var(--shadow);
        margin-bottom: 1rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.15);
    }
    .primary-btn {
        background: linear-gradient(135deg, var(--primary), #388E3C);
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        border: none;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
        font-size: 1rem;
    }
    .primary-btn:hover {
        background: linear-gradient(135deg, var(--accent), #EC407A);
        transform: translateY(-2px);
    }
    .stButton > button {
        background: linear-gradient(135deg, var(--primary), #388E3C);
        color: white;
        border-radius: 25px;
        border: none;
        padding: 0.75rem 1.5rem;
        font-size: 1rem;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, var(--accent), #EC407A);
    }
    .st-expander {
        border: 1px solid #E0E6ED;
        border-radius: 12px;
        background: #F9FBFD;
        margin-bottom: 1rem;
    }
    .header {
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(135deg, var(--primary), #388E3C);
        color: white;
        border-radius: 0 0 12px 12px;
    }
    .subtitle {
        font-size: 1.1rem;
    }
    .hero {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, rgba(46, 125, 50, 0.9), rgba(56, 142, 60, 0.9));
        border-radius: 12px;
        color: white;
        margin: 1rem 0;
        box-shadow: var(--shadow);
    }
    .hero-text {
        font-size: 1.2rem;
        max-width: 80%;
        margin: 1rem auto;
    }
    .hero-image {
        width: 100%;
        max-width: 700px;
        border-radius: 12px;
        margin: 1rem auto;
        box-shadow: var(--shadow);
    }
    .hero-buttons {
        display: flex;
        justify-content: center;
        gap: 1rem;
        flex-wrap: wrap;
    }
    .footer {
        text-align: center;
        padding: 1.5rem;
        background: #E8ECEF;
        border-top: 1px solid #D3D8DE;
        margin-top: 2rem;
        font-size: 0.9rem;
    }
    .whatsapp-link {
        color: var(--accent);
        text-decoration: none;
        font-weight: 500;
    }
    .whatsapp-link:hover {
        text-decoration: underline;
    }
    .chatbot-container {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 320px;
        max-height: 450px;
        overflow-y: auto;
        z-index: 1000;
        background: #FFFFFF;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: var(--shadow);
        display: none;
    }
    .chatbot-container.active {
        display: block;
    }
    .chatbot-message.user {
        background: #E8ECEF;
        text-align: right;
        color: var(--dark);
        padding: 0.75rem;
        margin: 0.75rem 0;
        border-radius: 8px;
        font-size: 1rem;
    }
    .chatbot-message.bot {
        background: #F9FBFD;
        text-align: left;
        color: var(--primary);
        padding: 0.75rem;
        margin: 0.75rem 0;
        border-radius: 8px;
        border-left: 4px solid var(--primary);
        font-size: 1rem;
    }
    .chatbot-input {
        width: 100%;
        padding: 0.75rem;
        border: 1px solid #E0E6ED;
        border-radius: 8px;
        margin-top: 0.75rem;
        font-size: 1rem;
    }
    .chatbot-toggle {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 1001;
        background: linear-gradient(135deg, var(--primary), #388E3C);
        color: white;
        border: none;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        font-size: 1.5rem;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: var(--shadow);
    }
    .chatbot-toggle:hover {
        background: linear-gradient(135deg, var(--accent), #EC407A);
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
        .card {
            margin: 0.5rem 0;
            padding: 1rem;
        }
        h1 { font-size: 1.8rem; }
        h2 { font-size: 1.5rem; }
        h3 { font-size: 1.3rem; }
        h4 { font-size: 1.1rem; }
        .chatbot-container {
            width: 90%;
            right: 5%;
            bottom: 80px;
            max-height: 350px;
        }
        .chatbot-toggle {
            bottom: 20px;
            right: 5%;
            width: 50px;
            height: 50px;
            font-size: 1.2rem;
        }
        .hero-image {
            max-width: 100% !important;
            height: auto !important;
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
if "chatbot_active" not in st.session_state:
    st.session_state.chatbot_active = False
if "chat_input" not in st.session_state:
    st.session_state.chat_input = ""

# Function to create download link
def get_download_link(file_content, file_name):
    b64 = base64.b64encode(file_content.encode()).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_name}" class="primary-btn" style="display: block; text-align: center; margin-top: 0.75rem;">Download</a>'
    return href

# Function to export mood history
def export_mood_history():
    df = pd.DataFrame(st.session_state.mood_history, columns=["Date", "Mood", "Note"])
    df["Date"] = df["Date"].apply(lambda x: x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime) else x)
    csv = df.to_csv(index=False)
    return csv

# Chatbot knowledge base
knowledge_base = [
    {"question": r"what is safespace organisation\??", "answer": "SafeSpace Organisation, founded in 2023 by Jerim Owino and Hamdi Roble, is a non-profit providing accessible, culturally-appropriate mental health care across Kenya with branches in most counties and online services, addressing trauma, depression, and more with counseling and outreach."},
    {"question": r"what services do you offer\??", "answer": "We offer Individual Counseling, Group Therapy, Family Counseling, Trauma Recovery Therapy, and Online Counseling, using methods like CBT, EMDR, and mindfulness, tailored to diverse mental health needs. Register at the Services section."},
    {"question": r"how can i contact you\??", "answer": "Contact us at +254 781 095 919 (8 AM-7 PM EAT) or info@safespaceorganisation.org (24-hour response). Visit our branches across Kenya or access online services."},
    {"question": r"what are your hours\??", "answer": "Office hours are Mon-Fri 9 AM-5 PM, Sat 10 AM-2 PM, closed Sundays and holidays. Crisis line is 8 AM-7 PM EAT. Online services are available 24/7."},
    {"question": r"how much does it cost\??", "answer": "Fees range from KSh 500-2,000 per session on a sliding scale, with subsidies and free workshops for low-income clients."},
    {"question": r"who are the founders\??", "answer": "Our founders are Jerim Owino, a certified psychologist from Maasai Mara University, and Hamdi Roble, a cultural therapy expert with a Master’s in Public Health."},
    {"question": r"what events are coming up\??", "answer": "Upcoming events include a Stress Management Workshop on August 10, 2025, in Nairobi, and a Youth Mental Health Forum on August 20, 2025, in Mombasa. Register at events@safespaceorganisation.org."},
    {"question": r"how can i volunteer\??", "answer": "Volunteer roles include Outreach Support, Event Volunteer, and Crisis Line Assistant. Register via the Volunteer form with your details and preferred role."},
    {"question": r"what is the crisis line\??", "answer": "Our Crisis Line is +254 781 095 919 (8 AM-7 PM EAT), with Befrienders Kenya at 1199 available 24/7 for emergencies."},
    {"question": r"how can i partner with you\??", "answer": "You can partner with us by registering through the Partnership form on our Partnerships page, or donate via the Donor form."},
    {"question": r"where can i find resources\??", "answer": "Visit the Resources and Downloads section for guides, worksheets, and crisis hotlines in multiple languages. Available at all branches and online."},
    {"default": "I’m sorry, I didn’t understand. Ask about services, contact, hours, costs, founders, events, volunteering, crisis support, partnerships, or resources, or visit Contact. Time: 11:44 PM EAT, August 05, 2025."}
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
<div class='header'>
    <h1>SafeSpace Organisation</h1>
    <p class='subtitle'>Empowering Minds, Nurturing Hope Since 2023</p>
</div>
""", unsafe_allow_html=True)

# HERO SECTION
st.markdown("<div id='hero'></div>", unsafe_allow_html=True)
st.markdown("""
<div class='hero'>
    <h1>Healing Minds, Restoring Lives</h1>
    <p class='hero-text'>SafeSpace Organisation offers professional, confidential counseling in a culturally-sensitive environment for all communities.</p>
    <img src='https://images.unsplash.com/photo-1588195539435-d6b5f19e1c24?auto=format&fit=crop&w=700&q=80' alt='Counseling outreach session' class='hero-image'>
    <div class='hero-buttons'>
        <a href='#about' class='primary-btn'>About Us</a>
        <a href='#services' class='primary-btn'>Our Services</a>
        <a href='#appointments' class='primary-btn'>Book Appointment</a>
        <a href='#events' class='primary-btn'>Upcoming Events</a>
        <a href='#resources' class='primary-btn'>Resources</a>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Our Mission"):
    st.markdown("""
    - **Mission**: Break mental health stigma and provide affordable care.
    - **Vision**: A thriving Kenya with emotional support for all.
    - **Contact**: info@safespaceorganisation.org or +254 781 095 919.
    - **Impact**: 600+ clients in 2025, 90% satisfaction.
    """)

# ABOUT SECTION
st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.markdown("## About SafeSpace Organisation")
st.markdown("""
<div class='card'>
    <p><strong>SafeSpace Organisation</strong>, founded in 2023 by Jerim Owino and Hamdi Roble, provides accessible mental health care across Kenya, with branches in most counties and comprehensive online services. With 15 professionals, we address trauma, depression, and family issues through in-person and virtual channels, serving the entire nation.</p>
    <p>We blend traditions with modern therapies, partnering with NGOs and the Ministry of Health to reach communities nationwide, focusing on inclusivity and accessibility.</p>
    <a href='#services' class='primary-btn'>Explore Our Services</a>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Our History"):
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
<div class='card'>
    <div class='card'>
        <h4>Jerim Owino</h4>
        <p>Jerim is a certified psychologist from Maasai Mara University with over 12 years of experience in mental health. Raised in Narok among the Maasai community, he developed a deep understanding of cultural influences on trauma, particularly from his work with pastoralist communities affected by displacement and cattle raids. His expertise lies in trauma counseling and community-based interventions, shaping SafeSpace’s rural outreach programs.</p>
    </div>
    <div class='card'>
        <h4>Hamdi Roble</h4>
        <p>Hamdi holds a Master’s in Public Health from the University of Nairobi and brings 8 years of experience as a community health advocate. Born in Kisumu, she grew up immersed in Luo cultural practices, which inspired her to integrate storytelling and traditional healing into modern therapy. She has worked with women’s groups in rural Kenya, addressing gender-based violence, and leads SafeSpace’s efforts to expand services to underserved regions.</p>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Our Founders"):
    st.markdown("""
    - **Jerim**: Trained 50+ community health workers, co-authored a guide on trauma in pastoral communities.
    - **Hamdi**: Led 15 workshops on gender-based violence, secured funding from local NGOs for rural projects.
    - **Collaboration**: Developed SafeSpace’s culturally-sensitive therapy model after a 2022 pilot.
    - **Community Work**: Both volunteer monthly in low-income areas, offering free sessions.
    """)

# SERVICES SECTION
st.markdown("<div id='services'></div>", unsafe_allow_html=True)
st.markdown("## Our Therapeutic Services")
st.markdown("A comprehensive suite of evidence-based therapies by 15 certified professionals with over 75 years of combined experience, tailored to diverse mental health needs.")
services = [
    {
        "title": "Individual Counseling",
        "desc": "This service provides personalized, one-on-one therapy sessions targeting conditions such as chronic depression, generalized anxiety disorder, PTSD, and low self-esteem. Conducted by therapists with 5+ years of experience, sessions use CBT, DBT, ACT, and MBSR. Each 50-minute session is available in-person or via secure video conferencing with flexible scheduling and a free 15-minute initial consultation."
    },
    {
        "title": "Group Therapy",
        "desc": "Designed for individuals dealing with grief, addiction recovery, PTSD, and social anxiety. Facilitated by two counselors with 10+ years of group experience, these 90-minute weekly sessions accommodate up to 10 participants with role-playing, peer support, and guided meditations. Offered in-person and online with a 3-month commitment encouraged."
    },
    {
        "title": "Family Counseling",
        "desc": "Aims to improve family dynamics and resolve conflicts for parenting challenges, marital disputes, intergenerational trauma, and cultural clashes. Led by family therapists trained in systemic and narrative therapy, these 60-minute sessions incorporate culturally-sensitive practices and include a 6-session initial program."
    },
    {
        "title": "Trauma Recovery Therapy",
        "desc": "Targets individuals and families affected by severe trauma, including survivors of physical violence, sexual abuse, accidents, and natural disasters. Using EMDR, trauma-focused CBT, and somatic experiencing, our specialists provide 75-minute sessions with a 6-session initial phase and ongoing support groups."
    },
    {
        "title": "Online Counseling",
        "desc": "Offers virtual therapy sessions for individuals facing barriers to in-person care, addressing anxiety, depression, and stress. Delivered by licensed therapists via secure video platforms, each 50-minute session utilizes CBT, mindfulness, and teletherapy techniques, available 24/7 with a free 15-minute consultation."
    }
]
for service in services:
    st.markdown(f"""
    <div class='card'>
        <h3>{service['title']}</h3>
        <p style='color: var(--dark);'>{service['desc']}</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown("<div id='counseling-form'></div>", unsafe_allow_html=True)
with st.form("counseling_form", clear_on_submit=True):
    name = st.text_input("Full Name", key="counseling_name")
    email = st.text_input("Email", placeholder="your.email@example.com", key="counseling_email")
    phone = st.text_input("Phone", placeholder="+254 XXX XXX XXX", key="counseling_phone")
    counseling_type = st.selectbox("Counseling Type", ["Online", "In-Person"], key="counseling_type")
    submit = st.form_submit_button("Register")
    if submit:
        if not all([name, email, re.match(r"[^@]+@[^@]+\.[^@]+", email), phone]):
            st.error("Please fill all required fields.")
        else:
            st.session_state.counseling_form_data = {"name": name, "email": email, "phone": phone, "type": counseling_type}
            st.success(f"Thank you, {name}! Your {counseling_type} counseling registration at 11:44 PM EAT, August 05, 2025, has been received. We will contact you soon.")
with st.expander("Learn More About Our Services"):
    st.markdown("""
    - **Therapists**: 15 certified professionals with diverse expertise.
    - **Methods**: Blend of modern and traditional therapeutic approaches.
    - **Accessibility**: Available across Kenya and online 24/7.
    - **Support**: Free initial consultations and progress tracking.
    """)

# APPOINTMENT BOOKING SECTION
st.markdown("<div id='appointments'></div>", unsafe_allow_html=True)
st.markdown("## Book an Appointment")
st.markdown("""
<div class='card'>
    <p>Schedule a personalized counseling session with one of our experts. Choose your preferred date, time, and session type.</p>
</div>
""", unsafe_allow_html=True)
with st.form("appointment_form", clear_on_submit=True):
    name = st.text_input("Full Name", key="appointment_name")
    email = st.text_input("Email", placeholder="your.email@example.com", key="appointment_email")
    phone = st.text_input("Phone", placeholder="+254 XXX XXX XXX", key="appointment_phone")
    date = st.date_input("Date", min_value=datetime.now())
    time = st.time_input("Time", value=datetime.now().replace(hour=9, minute=0, second=0, microsecond=0))
    appointment_type = st.selectbox("Session Type", ["Online", "In-Person"], key="appointment_type")
    submit = st.form_submit_button("Book Appointment")
    if submit:
        if not all([name, email, re.match(r"[^@]+@[^@]+\.[^@]+", email), phone, date, time]):
            st.error("Please fill all required fields.")
        else:
            st.session_state.appointment_form_data = {"name": name, "email": email, "phone": phone, "date": date, "time": time, "type": appointment_type}
            st.success(f"Thank you, {name}! Your {appointment_type} appointment on {date.strftime('%Y-%m-%d')} at {time.strftime('%H:%M')} EAT has been booked at 11:44 PM EAT, August 05, 2025. We will confirm soon.")
with st.expander("Learn More About Appointments"):
    st.markdown("""
    - **Availability**: Book 24/7 with flexible slots.
    - **Confirmation**: Receive a confirmation via email or phone.
    - **Cancellation**: Free cancellation 24 hours prior.
    - **Support**: Contact +254 781 095 919 for assistance.
    """)

# TESTIMONIALS SECTION
st.markdown("<div id='testimonials'></div>", unsafe_allow_html=True)
st.markdown("## What Our Clients Say")
st.markdown("""
<div class='card'>
    <div class='card'>
        <h4>Jane K.</h4>
        <p>“The group therapy sessions helped me cope with my grief after losing my spouse. The support was invaluable. Highly recommend!” <a href='https://wa.me/254781095919' target='_blank' class='whatsapp-link'>WhatsApp Us</a></p>
    </div>
    <div class='card'>
        <h4>Peter O.</h4>
        <p>“Online counseling was convenient and effective. My therapist’s empathy made a huge difference in managing my anxiety.”</p>
    </div>
    <div class='card'>
        <h4>Amina H.</h4>
        <p>“Trauma recovery therapy gave me my life back after surviving violence. The safe space and guidance were life-changing.”</p>
    </div>
    <div class='card'>
        <h4>Mohammed S.</h4>
        <p>“The family counseling sessions resolved our conflicts and brought us closer. The cultural approach was perfect for us.”</p>
    </div>
    <div class='card'>
        <h4>Sarah L.</h4>
        <p>“The online sessions helped me overcome stress during a tough time. The flexibility and care were exceptional.”</p>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Testimonials"):
    st.markdown("""
    - **Verified**: All testimonials are from real clients, anonymized for privacy.
    - **Process**: Clients submit feedback post-session, reviewed by staff.
    - **Impact**: 90% report improved well-being after 5 sessions.
    - **Contact**: Share your story at info@safespaceorganisation.org or via WhatsApp.
    """)

# EVENTS SECTION
st.markdown("<div id='events'></div>", unsafe_allow_html=True)
st.markdown("## Upcoming Events")
st.markdown("""
<div class='card'>
    <div class='card'>
        <h4>Stress Management Workshop</h4>
        <p>Date: August 10, 2025 | Location: Nairobi | Register at events@safespaceorganisation.org</p>
    </div>
    <div class='card'>
        <h4>Youth Mental Health Forum</h4>
        <p>Date: August 20, 2025 | Location: Mombasa | Register at events@safespaceorganisation.org</p>
    </div>
    <div class='card'>
        <h4>Community Healing Day</h4>
        <p>Date: September 5, 2025 | Location: Nakuru | Register at events@safespaceorganisation.org</p>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Events"):
    st.markdown("""
    - **Purpose**: Educate and support community mental health.
    - **Format**: Workshops, forums, and community days.
    - **Cost**: Free with registration.
    - **Contact**: events@safespaceorganisation.org for details.
    """)

# RESOURCES AND DOWNLOADS SECTION
st.markdown("<div id='resources'></div>", unsafe_allow_html=True)
st.markdown("## Resources and Downloads")
st.markdown("""
<div class='card'>
    <h3>Available Resources</h3>
    <p>Download free guides, worksheets, and crisis hotlines to support your mental health journey.</p>
    <div class='card'>
        <h4>English</h4>
        <p><strong>Mental Health Guide</strong>: A comprehensive guide to managing stress and anxiety.</p>
        """ + get_download_link("This is a sample guide content.", "Mental_Health_Guide_English.pdf") + """
        <p><strong>Crisis Hotline List</strong>: Contact numbers for emergency support.</p>
        """ + get_download_link("This is a sample hotline list.", "Crisis_Hotline_English.pdf") + """
    </div>
    <div class='card'>
        <h4>Swahili (Kiswahili)</h4>
        <p><strong>Kiongozi wa Afya ya Akili</strong>: Mwongozo wa kumudu mkazo na wasiwasi.</p>
        """ + get_download_link("Hii ni maudhui ya sampuli ya kiongozi.", "Kiongozi_wa_Afya_ya_Akili.pdf") + """
        <p><strong>Orodha ya Namba za Dharura</strong>: Namba za msaada wa dharura.</p>
        """ + get_download_link("Hii ni orodha ya sampuli ya namba za dharura.", "Orodha_ya_Namba_za_Dharura.pdf") + """
    </div>
    <div class='card'>
        <h4>French</h4>
        <p><strong>Guide de Santé Mentale</strong>: Un guide pour gérer le stress et l'anxiété.</p>
        """ + get_download_link("Ceci est un contenu d'exemple de guide.", "Guide_de_Sante_Mentale.pdf") + """
        <p><strong>Liste des Numéros d'Urgence</strong>: Numéros pour un soutien d'urgence.</p>
        """ + get_download_link("Ceci est une liste d'exemple des numéros d'urgence.", "Liste_des_Numeros_dUrgence.pdf") + """
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Resources"):
    st.markdown("""
    - **Availability**: Free downloads available 24/7.
    - **Languages**: English, Swahili, and French.
    - **Purpose**: Support self-care and crisis response.
    - **Contact**: Request additional resources at info@safespaceorganisation.org.
    """)

# CHATBOT SECTION (FIXED)
st.markdown("## Chat with our Assistant")
st.markdown("Ask questions about our services, hours, or resources")

# Chatbot toggle button
if st.button("💬 Toggle Chatbot", key="chatbot_toggle"):
    st.session_state.chatbot_active = not st.session_state.chatbot_active

# Chatbot interface
if st.session_state.chatbot_active:
    # Display chat history
    for message in st.session_state.chat_history:
        role = "user" if message["role"] == "user" else "assistant"
        st.markdown(f"<div class='chatbot-message {role}'>{message['content']}</div>", unsafe_allow_html=True)
    
    # User input
    user_input = st.text_input("Type your message:", key="chat_input")
    
    if user_input:
        # Add user message to history
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Get bot response
        bot_response = get_chatbot_response(user_input)
        
        # Add bot response to history
        st.session_state.chat_history.append({"role": "assistant", "content": bot_response})
        
        # Clear input and rerun to show new messages
        st.session_state.chat_input = ""
        st.experimental_rerun()

# FOOTER
st.markdown("""
<div class='footer'>
    <p>© 2025 SafeSpace Organisation | +254 781 095 919 | info@safespaceorganisation.org</p>
    <p>Nairobi Headquarters: Ngong Road, Nairobi, Kenya | Mombasa Branch: Moi Avenue, Mombasa</p>
    <p>24/7 Crisis Support: Befrienders Kenya (1199) | Emergency Contacts: Nairobi Women's Hospital (0800 720 501)</p>
</div>
""", unsafe_allow_html=True)
