import streamlit as st
from datetime import datetime
import re
import base64

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
    .service-card, .team-card, .testimonial-card, .cta-banner, .insights-content, .resource-card, .story-card, .event-card, .partnership-card, .blog-card, .forum-card, .tracker-card, .volunteer-card {
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
        .service-card, .team-card, .testimonial-card, .insights-content, .chatbot-container, .resource-card, .story-card, .event-card, .partnership-card, .blog-card, .forum-card, .tracker-card, .volunteer-card {
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
        .cta-banner, .insights-content {
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
    st.session_state.mood_history = [{"date": datetime(2025, 7, 22).date(), "mood": 3}, {"date": datetime(2025, 7, 23).date(), "mood": 4}]
if "outreach_form_data" not in st.session_state:
    st.session_state.outreach_form_data = {"name": "", "email": "", "phone": "", "experience": "", "skills": []}
if "event_form_data" not in st.session_state:
    st.session_state.event_form_data = {"name": "", "email": "", "phone": "", "experience": "", "skills": []}

# Function to create download link
def get_download_link(file_content, file_name):
    b64 = base64.b64encode(file_content.encode()).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_name}" class="primary-btn" style="display: block; text-align: center; margin-top: 0.5rem;">Download</a>'
    return href

# HEADER
st.markdown("""
<div style='text-align: center; padding: 0.8rem; background: var(--primary); color: white;'>
    <h1>SafeSpace Kenya</h1>
    <p>Empowering Minds, Nurturing Hope</p>
</div>
""", unsafe_allow_html=True)

# HERO SECTION
st.markdown("<div id='hero'></div>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding: 0.8rem; background: linear-gradient(rgba(38,166,154,0.9), rgba(77,182,172,0.9)); border-radius: 8px; color: white;'>
    <h1>Healing Minds, Restoring Lives</h1>
    <p style='font-size: 1rem; max-width: 100%; margin: 0.5rem auto;'>SafeSpace Kenya provides professional counseling in a supportive environment.</p>
    <img src='https://images.unsplash.com/photo-1588195539435-d6b5f19e1c24?auto=format&fit=crop&w=600&q=80' style='width: 100%; max-width: 600px; border-radius: 8px; margin: 0.5rem auto; box-shadow: 0 2px 4px rgba(0,0,0,0.2);' alt='Safe counselling session'/>
    <div style='display: flex; justify-content: center; gap: 0.5rem; flex-wrap: wrap;'>
        <a href='#about' class='primary-btn'>About</a>
        <a href='#services' class='primary-btn'>Services</a>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Read More", expanded=False):
    st.markdown("- Purpose: Accessible mental health care. - Contact: info@safespacekenya.org.")

# ABOUT SECTION
st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.markdown("## About SafeSpace Kenya")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p><strong>SafeSpace Kenya</strong>, founded in 2023, offers accessible mental health care for all Kenyans.</p>
    <a href='#services' class='primary-btn'>Learn More</a>
</div>
""", unsafe_allow_html=True)

# SERVICES SECTION
st.markdown("<div id='services'></div>", unsafe_allow_html=True)
st.markdown("## Our Therapeutic Services")
st.markdown("Tailored therapies for your needs.")
services = [
    {"icon": "👤", "title": "Individual Counseling", "desc": "Sessions for depression and anxiety."},
    {"icon": "👥", "title": "Group Therapy", "desc": "Support for grief and stress."},
    {"icon": "🏠", "title": "Family Counseling", "desc": "Resolve family conflicts."}
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
    <a href='#blog' class='primary-btn'>Next Section</a>
</div>
""", unsafe_allow_html=True)

# MENTAL HEALTH BLOG SECTION
st.markdown("<div id='blog'></div>", unsafe_allow_html=True)
st.markdown("## Mental Health Blog")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Articles for mental wellness:</p>
""", unsafe_allow_html=True)
blogs = [
    {"title": "Coping with Stress", "date": "July 20, 2025", "desc": "Manage financial stress."},
    {"title": "Cultural Therapy", "date": "July 15, 2025", "desc": "Kenyan traditions in therapy."}
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

# CRISIS RESOURCES SECTION
st.markdown("<div id='crisis'></div>", unsafe_allow_html=True)
st.markdown("## Crisis Resources")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Immediate support:</p>
    <ul>
        <li><strong>Befrienders Kenya:</strong> 1199 (24/7)</li>
        <li><strong>SafeSpace:</strong> +254 781 095 919 (8 AM - 7 PM)</li>
    </ul>
    <a href='#contact' class='primary-btn'>Get Help</a>
</div>
""", unsafe_allow_html=True)

# PROGRESS TRACKER SECTION
st.markdown("<div id='tracker'></div>", unsafe_allow_html=True)
st.markdown("## Progress Tracker")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Track your journey:</p>
    <div class='tracker-card'>
        <h4>Mood Tracker</h4>
        <p>Rate your mood (1-5).</p>
    </div>
""", unsafe_allow_html=True)
mood = st.slider("How do you feel?", 1, 5, 3, key="mood_input")
if st.button("Log Mood"):
    st.session_state.mood_history.append({"date": datetime.today().date(), "mood": mood})
    st.success("Logged!")
for entry in st.session_state.mood_history[-3:]:
    st.markdown(f"- {entry['date']}: {entry['mood']}/5")
st.markdown("""
    <a href='#volunteer' class='primary-btn'>Next Section</a>
</div>
""", unsafe_allow_html=True)

# VOLUNTEER OPPORTUNITIES SECTION
st.markdown("<div id='volunteer'></div>", unsafe_allow_html=True)
st.markdown("## Volunteer Opportunities")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Contribute to our work:</p>
""", unsafe_allow_html=True)
volunteer_roles = [
    {"title": "Outreach Support", "desc": "Assist awareness, 2-4 hours weekly."},
    {"title": "Event Volunteer", "desc": "Help with July 30 workshop."}
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
    <a href='#contact' class='primary-btn'>Contact Us 📞</a>
    <a href='#forum' class='primary-btn'>Forum 💬</a>
</div>
""", unsafe_allow_html=True)

# CONTACT SECTION
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.markdown("## Contact Us")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p><strong>📍</strong> Greenhouse Plaza, Ngong Road, Nairobi</p>
    <p><strong>📞</strong> +254 781 095 919</p>
    <p><strong>✉️</strong> <a href='mailto:info@safespacekenya.org'>info@safespacekenya.org</a></p>
    <a href='#' class='primary-btn'>Book Now</a>
</div>
""", unsafe_allow_html=True)

# CHATBOT
st.markdown("""
<div class='chatbot-container' id='chatbot'>
    <h4>Ask SafeSpace Bot</h4>
    <div style='max-height: 200px; overflow-y: auto; margin-bottom: 0.5rem;'>
""", unsafe_allow_html=True)
for sender, message in st.session_state.chat_history:
    st.markdown(
        f"<div class='chatbot-message {sender}'><p>{message}</p></div>",
        unsafe_allow_html=True
    )
st.markdown("</div>", unsafe_allow_html=True)
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("", placeholder="Ask about services...", key="chat_input")
    submit = st.form_submit_button("Send")
    if submit and user_input:
        st.session_state.chat_history.append(("user", user_input))
        response = "I'm sorry, I don't understand. Visit Contact for help."
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
    <p style='font-size: 0.9rem;'>© 2023 SafeSpace Kenya | Designed with ❤️</p>
    <div style='display: flex; justify-content: center; gap: 0.5rem; flex-wrap: wrap;'>
        <a href='https://facebook.com' target='_blank' class='primary-btn'>Facebook</a>
        <a href='https://instagram.com' target='_blank' class='primary-btn'>Instagram</a>
    </div>
</div>
""", unsafe_allow_html=True)

knowledge_base = [
    {"section": "About", "answer": "SafeSpace Kenya provides mental health care.", "keywords": ["about", "safespace"]},
    {"section": "Services", "answer": "We offer counseling and workshops.", "keywords": ["services", "therapy"]},
]

with st.form("newsletter_form", clear_on_submit=True):
    st.markdown("<div style='max-width: 300px; margin: 0.5rem auto; display: flex; gap: 0.3rem;'>", unsafe_allow_html=True)
    newsletter_email = st.text_input("", placeholder="Subscribe...", key="newsletter_email")
    submit_newsletter = st.form_submit_button("Subscribe")
    st.markdown("</div>", unsafe_allow_html=True)
    if submit_newsletter:
        if not newsletter_email or not re.match(r"[^@]+@[^@]+\.[^@]+", newsletter_email):
            st.error("Valid email required.")
        else:
            st.success("Subscribed!")
