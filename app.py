import streamlit as st
from datetime import datetime
import re
import base64
import pandas as pd

# Custom CSS optimized for Streamlit deployment
st.markdown("""
    <style>
        :root {
            --primary: #26A69A;
            --accent: #FF6F61;
            --light: #F9F9F9;
            --soft: #E8F4F8;
            --dark: #1E3A5F;
            --shadow: rgba(0, 0, 0, 0.05);
        }
        .stApp {
            background: linear-gradient(135deg, var(--light), var(--soft));
            color: var(--dark);
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        h1, h2, h3, h4 {
            color: var(--dark);
            text-align: center;
            line-height: 1.4;
        }
        h1 { font-size: 2.8rem; font-weight: 700; margin-bottom: 10px; }
        h2 { font-size: 2.2rem; font-weight: 600; }
        h3 { font-size: 1.6rem; font-weight: 600; }
        h4 { font-size: 1.3rem; font-weight: 400; }
        .card {
            background: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 6px 12px var(--shadow);
            margin-bottom: 20px;
        }
        .btn {
            background: linear-gradient(45deg, var(--primary), #1E7D7A);
            color: white;
            padding: 10px 20px;
            border-radius: 30px;
            border: none;
            font-weight: 600;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
        }
        .btn:hover {
            background: linear-gradient(45deg, var(--accent), #FF8A80);
        }
        .stButton > button {
            background: linear-gradient(45deg, var(--primary), #1E7D7A);
            color: white;
            border-radius: 30px;
            border: none;
            padding: 10px 20px;
            font-weight: 600;
        }
        .stButton > button:hover {
            background: linear-gradient(45deg, var(--accent), #FF8A80);
        }
        .support-text {
            font-size: 1.1rem;
            color: var(--dark);
            text-align: center;
            margin: 10px 0;
        }
        @media (max-width: 768px) {
            h1 { font-size: 2.2rem; }
            h2 { font-size: 1.8rem; }
            h3 { font-size: 1.4rem; }
            h4 { font-size: 1.1rem; }
            .card { padding: 15px; margin-bottom: 15px; }
            .btn { padding: 8px 15px; }
        }
    </style>
""", unsafe_allow_html=True)

# Fixed syntax: removed trailing comma
st.set_page_config(page_title="SafeSpace Organisation", page_icon="❤️", layout="wide")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "mood_history" not in st.session_state:
    st.session_state.mood_history = []
if "client_feedback" not in st.session_state:
    st.session_state.client_feedback = []
if "counseling_form_data" not in st.session_state:
    st.session_state.counseling_form_data = {"name": "", "email": "", "phone": "", "type": "Online"}
if "volunteer_form_data" not in st.session_state:
    st.session_state.volunteer_form_data = {"name": "", "email": "", "phone": "", "role": "Any"}

# Utility functions
def get_download_link(file_content, file_name):
    b64 = base64.b64encode(file_content.encode()).decode()
    return f'<a href="data:application/octet-stream;base64,{b64}" download="{file_name}" class="btn">Download</a>'

def export_mood_history():
    df = pd.DataFrame(st.session_state.mood_history, columns=["Date", "Mood", "Note", "Reflection"])
    df["Date"] = df["Date"].apply(lambda x: x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime) else x)
    return df.to_csv(index=False)

# Chatbot knowledge base with client-centered responses
knowledge_base = [
    {"question": r"what is safespace organisation\??", "answer": "SafeSpace is here for you, offering mental health support since 2023 by Jerim Owino and Hamdi Roble."},
    {"question": r"what services do you offer\??", "answer": "We provide individual, group, and online counseling tailored to your needs. Register below to start your journey."},
    {"question": r"how can i contact you\??", "answer": "We’re here for you—call +254 781 095 919 or email info@safespaceorganisation.org anytime."},
    {"question": r"what are your hours\??", "answer": "We’re available Mon-Fri 9 AM-5 PM, Sat 10 AM-2 PM to support you."},
    {"question": r"how much does it cost\??", "answer": "Fees are flexible, ranging from KSh 500-2,000 per session, based on your situation."},
    {"question": r"who are the founders\??", "answer": "Jerim Owino, with 12 years in trauma counseling, and Hamdi Roble, with 8 years in community health, lead our mission to support you."},
    {"question": r"what events are coming up\??", "answer": "Join our Stress Management Workshop on August 10, 2025, in Nairobi—check below for details."},
    {"question": r"how can i volunteer\??", "answer": "Your help matters! Register below to volunteer with us."},
    {"question": r"what is the crisis line\??", "answer": "In crisis? Call +254 781 095 919 (8 AM-7 PM EAT) for immediate support."},
    {"question": r"how can i partner with us\??", "answer": "Partner with us to expand support—register below to collaborate."},
    {"default": f"We’re here to help. Ask about services, contact, hours, costs, founders, events, volunteering, crisis support, or partnerships. Time: 10:55 AM EAT, August 6, 2025."}
]

def get_chatbot_response(query):
    query = query.lower()
    for entry in knowledge_base:
        if "question" in entry and re.search(entry["question"], query):
            return entry["answer"]
    return knowledge_base[-1]["default"]

# HEADER
st.markdown("<h1 style='background: var(--primary); color: white; padding: 15px; border-radius: 15px;'>SafeSpace Organisation</h1>", unsafe_allow_html=True)
st.markdown("<p class='support-text'>Your Safe Haven for Mental Wellness Since 2023</p>", unsafe_allow_html=True)

# HERO SECTION
st.markdown("<div id='hero'></div>", unsafe_allow_html=True)
st.markdown("<h2 style='background: linear-gradient(135deg, var(--primary), #1E7D7A); color: white; padding: 25px; border-radius: 15px;'>You Are Not Alone</h2>", unsafe_allow_html=True)
st.markdown("<p class='support-text'>SafeSpace offers compassionate, confidential counseling tailored to you.</p>", unsafe_allow_html=True)
cols = st.columns(2)
with cols[0]:
    st.markdown("<a href='#services' class='btn'>Get Support</a>", unsafe_allow_html=True)
with cols[1]:
    st.markdown("<a href='#about' class='btn'>Learn More</a>", unsafe_allow_html=True)

# ABOUT SECTION
st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.markdown("## About Us")
st.markdown("<div class='card'><p>SafeSpace Organisation, founded in 2023 by Jerim Owino and Hamdi Roble, is committed to your mental health with a team of 15 dedicated professionals.</p></div>", unsafe_allow_html=True)
st.markdown("<div id='founders'></div>", unsafe_allow_html=True)
st.markdown("## Meet Our Founders")
st.markdown("<div class='card'><h4>Jerim Owino</h4><p>A certified psychologist with over 12 years of experience, specializing in trauma counseling to support your healing journey.</p></div>", unsafe_allow_html=True)
st.markdown("<div class='card'><h4>Hamdi Roble</h4><p>With a Master’s in Public Health and 8 years as a health advocate, Hamdi integrates holistic methods to empower your well-being.</p></div>", unsafe_allow_html=True)

# SERVICES SECTION
st.markdown("<div id='services'></div>", unsafe_allow_html=True)
st.markdown("## Services for You")
services = [
    {"title": "Individual Counseling", "desc": "Personalized sessions to support your unique needs."},
    {"title": "Group Therapy", "desc": "Connect with others in a safe, supportive environment."},
    {"title": "Online Counseling", "desc": "Convenient virtual support from anywhere."}
]
for service in services:
    st.markdown(f"<div class='card'><h3>{service['title']}</h3><p>{service['desc']}</p></div>", unsafe_allow_html=True)
with st.form("counseling_form", clear_on_submit=True):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    phone = st.text_input("Your Phone")
    preference = st.selectbox("Preferred Method", ["Online", "In-Person"])
    submit = st.form_submit_button("Start Your Journey")
    if submit and name and re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) and phone:
        st.session_state.counseling_form_data = {"name": name, "email": email, "phone": phone, "type": preference}
        st.success(f"Thank you, {name}! We’ll reach out at 10:55 AM EAT, August 6, 2025, via {email} to support you.")
    elif submit:
        st.error("Please provide valid details: name, valid email (user@example.com), and phone number.")

# TESTIMONIALS SECTION
st.markdown("<div id='testimonials'></div>", unsafe_allow_html=True)
st.markdown("## What Clients Say")
st.markdown("<div class='card'><p><em>'SafeSpace gave me hope when I needed it most.'</em> - Jane K.</p></div>", unsafe_allow_html=True)

# EVENTS SECTION
st.markdown("<div id='events'></div>", unsafe_allow_html=True)
st.markdown("## Events for Your Growth")
st.markdown("<div class='card'><h4>Stress Management Workshop</h4><p>August 10, 2025, Nairobi - Join us to learn coping strategies.</p></div>", unsafe_allow_html=True)

# MOOD TRACKER SECTION
st.markdown("<div id='tracker'></div>", unsafe_allow_html=True)
st.markdown("## Your Mood Journey")
mood = st.slider("How are you feeling today? (1-5)", 1, 5, 3, help="1 = Not good, 5 = Great")
note = st.text_area("Your Thoughts or Feelings")
reflection = st.text_area("What can help you today?")
if st.button("Save Your Moment"):
    st.session_state.mood_history.append({"Date": datetime.now(), "Mood": mood, "Note": note, "Reflection": reflection})
    st.success(f"Your moment is saved at 10:55 AM EAT, August 6, 2025. Take care!")
    
# Display mood history with proper date formatting
for entry in st.session_state.mood_history[-5:]:
    date_value = entry["Date"]
    date_str = date_value.strftime('%Y-%m-%d %H:%M') if isinstance(date_value, datetime) else date_value
    st.write(f"- {date_str}: Mood {entry['Mood']}/5 | {entry['Note'] or 'No note'} | {entry['Reflection'] or 'No reflection'}")
    
if st.button("Download Your Journey") and st.session_state.mood_history:
    csv = export_mood_history()
    st.markdown(get_download_link(csv, "my_mood_journey.csv"), unsafe_allow_html=True)

# VOLUNTEER SECTION
st.markdown("<div id='volunteer'></div>", unsafe_allow_html=True)
st.markdown("## Join Us to Support Others")
st.markdown("<div class='card'><h4>Outreach Support</h4><p>2-4 hour sessions to make a difference.</p></div>", unsafe_allow_html=True)
with st.form("volunteer_form", clear_on_submit=True):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    phone = st.text_input("Your Phone")
    role = st.selectbox("Role Preference", ["Any", "Counseling Support", "Outreach"])
    submit = st.form_submit_button("Contribute Today")
    if submit and name and re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) and phone:
        st.session_state.volunteer_form_data = {"name": name, "email": email, "phone": phone, "role": role}
        st.success(f"Thank you, {name}! We’ll contact you at 10:55 AM EAT, August 6, 2025, via {email}.")
    elif submit:
        st.error("Please provide valid details: name, valid email (user@example.com), and phone number.")

# CONTACT SECTION
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.markdown("## We’re Here for You")
st.markdown("<div class='card'><p>Reach out at Greenhouse Plaza, Nairobi, call +254 781 095 919, or email info@safespaceorganisation.org. You matter to us.</p></div>", unsafe_allow_html=True)

# CHATBOT SECTION
st.markdown("## Talk to a Friend")
chat_container = st.container()
if st.session_state.chat_history:
    with chat_container:
        for msg in st.session_state.chat_history:
            st.markdown(f"**{'You' if msg[0] == 'user' else 'Friend'}:** {msg[1]}")

query = st.text_input("Share what’s on your mind...", key="chat_input")
if st.button("Send") and query:
    response = get_chatbot_response(query)
    st.session_state.chat_history.append(("user", query))
    st.session_state.chat_history.append(("bot", response))
    st.rerun()

# FEEDBACK SECTION
st.markdown("## Your Voice Matters")
with st.form("feedback_form", clear_on_submit=True):
    feedback = st.text_area("How can we support you better?")
    submit = st.form_submit_button("Submit Feedback")
    if submit and feedback:
        st.session_state.client_feedback.append({"Date": datetime.now(), "Feedback": feedback})
        st.success(f"Thank you for your input at 10:55 AM EAT, August 6, 2025! We’re listening.")
    elif submit:
        st.warning("Please share your thoughts with us.")

# FOOTER
st.markdown("<hr style='border-color: var(--primary); opacity: 0.3;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size: 1rem; color: var(--dark);'>© 2023-2025 SafeSpace Organisation | <a href='#contact' style='color: var(--primary); text-decoration: none;'>Contact Us</a></p>", unsafe_allow_html=True)
