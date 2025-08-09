import streamlit as st
from datetime import datetime
import re
import base64
import pandas as pd

# Custom CSS for therapeutic environment
st.markdown("""
<style>
    :root {
        --primary: #4a9b8e;
        --accent: #ff9a8b;
        --light: #f0f7f5;
        --dark: #2c3e50;
        --deep-blue: #1E3A8A;
    }
    .stApp {
        background-color: var(--light);
        font-family: 'Inter', sans-serif;
        color: var(--dark);
        min-height: 100vh;
        background-image: url('https://www.transparenttextures.com/patterns/soft-wallpaper.png');
    }
    h1, h2, h3, h4 {
        font-family: 'Merriweather', serif;
        color: var(--deep-blue);
        font-weight: 400;
    }
    .safe-container {
        background: rgba(255, 255, 255, 0.85);
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 1.5rem;
        border-left: 4px solid var(--primary);
    }
    .calming-card {
        background: white;
        border-radius: 10px;
        padding: 1.2rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
        border: 1px solid #e6f2f0;
        transition: all 0.3s ease;
    }
    .calming-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 12px rgba(74, 155, 142, 0.15);
    }
    .primary-btn {
        background: linear-gradient(135deg, var(--primary), #5ab4a7);
        color: white;
        padding: 0.6rem 1.2rem;
        border-radius: 8px;
        border: none;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
        font-size: 1rem;
        margin: 0.5rem 0;
    }
    .primary-btn:hover {
        background: linear-gradient(135deg, var(--accent), #ffab9f);
        transform: translateY(-2px);
        color: white;
    }
    .stButton > button {
        background: linear-gradient(135deg, var(--primary), #5ab4a7);
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.6rem 1.2rem;
        font-size: 1rem;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, var(--accent), #ffab9f);
        color: white;
    }
    .mood-option {
        padding: 0.8rem;
        margin: 0.3rem;
        border-radius: 8px;
        cursor: pointer;
        text-align: center;
        background: #f8fbfa;
        transition: all 0.2s;
    }
    .mood-option:hover {
        background: #e6f2f0;
    }
    .mood-option.selected {
        background: var(--primary);
        color: white;
        font-weight: 500;
    }
    .confidential {
        font-size: 0.85rem;
        color: #6c757d;
        margin-top: 1rem;
        padding: 0.8rem;
        background: #f8f9fa;
        border-radius: 6px;
        border-left: 3px solid var(--primary);
    }
    @media (max-width: 768px) {
        .stColumn {
            width: 100% !important;
        }
        .calming-card {
            padding: 1rem;
            margin: 0.8rem 0;
        }
        h1 { font-size: 1.8rem; }
        h2 { font-size: 1.5rem; }
        h3 { font-size: 1.3rem; }
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="SafeSpace Counseling",
    page_icon="🧠",
    layout="wide",
)

# Initialize session state
if "current_view" not in st.session_state:
    st.session_state.current_view = "home"
if "mood_history" not in st.session_state:
    st.session_state.mood_history = []
if "counseling_form_data" not in st.session_state:
    st.session_state.counseling_form_data = {"name": "", "email": "", "phone": "", "concern": "Anxiety", "preference": "Online"}

# Function to create download link
def get_download_link(file_content, file_name):
    b64 = base64.b64encode(file_content.encode()).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_name}" class="primary-btn" style="display: block; text-align: center; margin-top: 0.5rem;">Download Journal</a>'
    return href

# Function to export mood history
def export_mood_history():
    df = pd.DataFrame(st.session_state.mood_history, columns=["Date", "Mood", "Note"])
    df["Date"] = df["Date"].apply(lambda x: x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime) else x)
    csv = df.to_csv(index=False)
    return csv

# Chatbot knowledge base
knowledge_base = [
    {"question": r"how do i start counseling\??", "answer": "You can begin by completing our brief registration form. We'll match you with a specialized therapist based on your needs. All information is confidential."},
    {"question": r"what can i expect in my first session\??", "answer": "Your first session is about building comfort and understanding your needs. Your therapist will listen without judgment and help create a personalized care plan."},
    {"question": r"is this confidential\??", "answer": "Absolutely. All sessions and records are protected under professional confidentiality standards. We never share information without your explicit consent."},
    {"question": r"what if i need urgent help\??", "answer": "For immediate crisis support, call our 24/7 helpline: +254 781 095 919. For life-threatening emergencies, please go to your nearest hospital."},
    {"question": r"can i change therapists\??", "answer": "Yes, at any time. Your comfort is paramount. Contact our support team to discuss finding a better match."},
    {"default": "I'm here to listen. You can ask about starting counseling, what to expect, confidentiality, or urgent support. If you're in crisis, call +254 781 095 919 now."}
]

# Main App Navigation
if st.session_state.current_view == "home":
    # HERO SECTION
    st.markdown("""
    <div class='safe-container' style='text-align: center; background: linear-gradient(rgba(74,155,142,0.9), rgba(90,180,167,0.9)); color: white;'>
        <h1>SafeSpace Counseling</h1>
        <p style='font-size: 1.1rem;'>Your Journey to Emotional Wellness Begins Here</p>
        <div style='display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; margin: 1.5rem 0;'>
            <button onclick="window.location.href='#start_healing'" class='primary-btn'>Start Healing</button>
            <button onclick="window.location.href='#mood_tracker'" class='primary-btn'>Mood Tracker</button>
            <button onclick="window.location.href='#resources'" class='primary-btn'>Resources</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # THERAPEUTIC SERVICES
    st.markdown("<div id='start_healing'></div>", unsafe_allow_html=True)
    st.markdown("## Personalized Counseling Services")
    st.markdown("""
    <div class='safe-container'>
        <p>Our licensed therapists provide evidence-based care in a safe, non-judgmental space. All services are completely confidential.</p>
        
        <div class='calming-card'>
            <h3>Individual Therapy</h3>
            <p>One-on-one sessions tailored to your unique needs. Address anxiety, depression, trauma, and life transitions with compassionate support.</p>
            <ul>
                <li>50-minute weekly sessions</li>
                <li>Cognitive Behavioral Therapy (CBT)</li>
                <li>Mindfulness-based approaches</li>
                <li>Personalized treatment plans</li>
            </ul>
        </div>
        
        <div class='calming-card'>
            <h3>Specialized Support</h3>
            <p>Targeted approaches for specific challenges:</p>
            <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin: 1rem 0;'>
                <div style='background: #f0f7f5; padding: 1rem; border-radius: 8px;'>
                    <h4>Trauma Recovery</h4>
                    <p>EMDR therapy for processing past trauma</p>
                </div>
                <div style='background: #f0f7f5; padding: 1rem; border-radius: 8px;'>
                    <h4>Relationship Counseling</h4>
                    <p>Improve communication and connection</p>
                </div>
                <div style='background: #f0f7f5; padding: 1rem; border-radius: 8px;'>
                    <h4>Stress Management</h4>
                    <p>Coping strategies for daily challenges</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # COUNSELING REGISTRATION
    with st.form("counseling_form", clear_on_submit=True):
        st.markdown("### Begin Your Healing Journey")
        name = st.text_input("Your Name", placeholder="First and Last Name")
        email = st.text_input("Email Address", placeholder="you@example.com")
        phone = st.text_input("Phone", placeholder="+254 XXX XXX XXX")
        concern = st.selectbox("Primary Concern", 
                              ["Anxiety", "Depression", "Trauma", "Relationship Issues", 
                               "Grief/Loss", "Stress Management", "Self-Esteem", "Other"])
        preference = st.radio("Session Preference", ["Online", "In-Person"])
        submit = st.form_submit_button("Request Consultation")
        
        if submit:
            if not all([name, email, phone]):
                st.error("Please complete all required fields")
            elif not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
                st.error("Please enter a valid email address")
            elif not re.match(r"^\+?254\d{9}$|^0\d{9}$", phone.replace(" ", "")):
                st.error("Please enter a valid Kenyan phone number")
            else:
                st.session_state.counseling_form_data = {
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "concern": concern,
                    "preference": preference
                }
                st.success("Thank you for your request! A therapist will contact you within 24 hours to schedule your first session.")
                st.balloons()

    st.markdown("""
    <div class='confidential'>
        <strong>Confidentiality Assurance:</strong> All information shared is protected under professional ethical guidelines. 
        We never share your details without explicit consent.
    </div>
    """, unsafe_allow_html=True)

    # MOOD TRACKER
    st.markdown("<div id='mood_tracker'></div>", unsafe_allow_html=True)
    st.markdown("## Mood & Wellness Journal")
    st.markdown("""
    <div class='safe-container'>
        <p>Track your emotional patterns between sessions. This private journal helps you and your therapist understand your progress.</p>
        
        <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 0.5rem; margin: 1rem 0;'>
            <div class='mood-option' onclick='setMood("Radiant")'>😊 Radiant</div>
            <div class='mood-option' onclick='setMood("Calm")'>😌 Calm</div>
            <div class='mood-option' onclick='setMood("Neutral")'>😐 Neutral</div>
            <div class='mood-option' onclick='setMood("Anxious")'>😟 Anxious</div>
            <div class='mood-option' onclick='setMood("Sad")'>😔 Sad</div>
        </div>
        
        <script>
        function setMood(mood) {
            const options = document.querySelectorAll('.mood-option');
            options.forEach(opt => opt.classList.remove('selected'));
            event.target.classList.add('selected');
            Streamlit.setComponentValue(mood);
        }
        </script>
        """, unsafe_allow_html=True)
    
    mood = st.selectbox("How are you feeling today?", 
                       ["Select an option", "Radiant", "Calm", "Neutral", "Anxious", "Sad"],
                       key="mood_select")
    
    note = st.text_area("Briefly note what's affecting your mood (optional)", 
                       height=100, 
                       placeholder="What thoughts, events, or sensations are you experiencing?")
    
    if st.button("Save Journal Entry"):
        if mood != "Select an option":
            entry = {
                "Date": datetime.now(),
                "Mood": mood,
                "Note": note
            }
            st.session_state.mood_history.append(entry)
            st.success("Journal entry saved. This information can help your therapist support you better.")
        else:
            st.warning("Please select a mood before saving")
    
    if st.session_state.mood_history:
        st.markdown("### Your Mood History")
        mood_df = pd.DataFrame(st.session_state.mood_history)
        mood_df["Date"] = mood_df["Date"].dt.strftime("%b %d, %Y %I:%M %p")
        st.dataframe(mood_df[["Date", "Mood", "Note"]], hide_index=True)
        
        csv = export_mood_history()
        st.markdown(get_download_link(csv, "mood_journal.csv"), unsafe_allow_html=True)
    
    # RESOURCES SECTION
    st.markdown("<div id='resources'></div>", unsafe_allow_html=True)
    st.markdown("## Therapeutic Resources")
    st.markdown("""
    <div class='safe-container'>
        <div class='calming-card'>
            <h3>Immediate Support</h3>
            <p><strong>24/7 Crisis Line:</strong> +254 781 095 919</p>
            <p><strong>Emergency Contact:</strong> If you're in immediate danger, please go to your nearest hospital</p>
        </div>
        
        <div class='calming-card'>
            <h3>Self-Help Tools</h3>
            <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;'>
                <div>
                    <h4>Grounding Exercise</h4>
                    <p>5-4-3-2-1 Technique: Notice 5 things you see, 4 things you touch, 3 things you hear, 2 things you smell, 1 thing you taste</p>
                </div>
                <div>
                    <h4>Breathing Practice</h4>
                    <p>Box Breathing: Inhale 4s → Hold 4s → Exhale 4s → Hold 4s. Repeat for 5 minutes</p>
                </div>
            </div>
        </div>
        
        <div class='calming-card'>
            <h3>Recommended Reading</h3>
            <ul>
                <li>The Body Keeps the Score by Bessel van der Kolk</li>
                <li>Feeling Good by David D. Burns</li>
                <li>Mindfulness for Beginners by Jon Kabat-Zinn</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class='footer' style='margin-top: 3rem; padding: 1.5rem; text-align: center; background: #e8f4f8; border-top: 1px solid #d1e7e3;'>
    <p>SafeSpace Counseling • +254 781 095 919 • info@safespace.org</p>
    <p style='font-size: 0.9rem; color: #6c757d;'>Confidential support for your mental wellness journey</p>
</div>
""", unsafe_allow_html=True)
