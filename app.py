import streamlit as st
from datetime import datetime
import re
import base64
import pandas as pd
import random

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
        background-attachment: fixed;
    }
    h1, h2, h3, h4 {
        font-family: 'Merriweather', serif;
        color: var(--deep-blue);
        font-weight: 400;
    }
    .safe-container {
        background: rgba(255, 255, 255, 0.92);
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
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100px;
    }
    .mood-option:hover {
        background: #e6f2f0;
    }
    .mood-option.selected {
        background: var(--primary);
        color: white;
        font-weight: 500;
    }
    .mood-emoji {
        font-size: 2rem;
        margin-bottom: 0.5rem;
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
    .testimonial {
        padding: 1.2rem;
        background: linear-gradient(to right, #f8fbfa, #e6f2f0);
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 3px solid var(--accent);
        font-style: italic;
    }
    .therapist-card {
        padding: 1rem;
        background: white;
        border-radius: 8px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        text-align: center;
        margin: 0.5rem;
    }
    .therapist-img {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        object-fit: cover;
        margin: 0 auto 1rem;
        border: 3px solid var(--primary);
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

# Therapist profiles
therapists = [
    {
        "name": "Dr. Amina Hassan",
        "specialty": "Trauma & Anxiety",
        "approach": "EMDR, CBT, Mindfulness",
        "experience": "12 years",
        "quote": "Healing begins when we feel truly heard"
    },
    {
        "name": "Ben Ochieng",
        "specialty": "Relationship Counseling",
        "approach": "Narrative Therapy, EFT",
        "experience": "8 years",
        "quote": "Relationships flourish with understanding"
    },
    {
        "name": "Grace Mwangi",
        "specialty": "Depression & Self-Esteem",
        "approach": "CBT, Positive Psychology",
        "experience": "10 years",
        "quote": "Your worth is inherent, not earned"
    },
    {
        "name": "David Kimani",
        "specialty": "Youth & Family Therapy",
        "approach": "Play Therapy, Family Systems",
        "experience": "7 years",
        "quote": "Every family has its unique rhythm"
    }
]

# Testimonials
testimonials = [
    "SafeSpace gave me tools to manage my anxiety that I'll use for life. My therapist was incredibly patient and understanding.",
    "After just 6 sessions, I feel like a different person. The depression that felt permanent is finally lifting.",
    "The cultural sensitivity made all the difference. Finally a therapist who understands my background and experiences.",
    "The mood journal helped me see patterns I never noticed. My therapist used these insights to tailor our sessions perfectly."
]

# HERO SECTION
st.markdown("""
<div class='safe-container' style='text-align: center; background: linear-gradient(rgba(74,155,142,0.9), rgba(90,180,167,0.9)); color: white; padding: 2rem; border-radius: 12px;'>
    <h1 style='color: white; font-size: 2.5rem;'>SafeSpace Counseling</h1>
    <p style='font-size: 1.2rem; max-width: 700px; margin: 0.5rem auto 1.5rem;'>Your Journey to Emotional Wellness Begins Here</p>
    <div style='display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; margin: 1.5rem 0;'>
        <a href='#services' class='primary-btn' style='background: white; color: var(--primary);'>Start Healing</a>
        <a href='#mood_tracker' class='primary-btn' style='background: rgba(255,255,255,0.2); border: 1px solid white;'>Mood Tracker</a>
        <a href='#therapists' class='primary-btn' style='background: rgba(255,255,255,0.2); border: 1px solid white;'>Meet Our Therapists</a>
    </div>
</div>
""", unsafe_allow_html=True)

# THERAPEUTIC SERVICES
st.markdown("<div id='services'></div>", unsafe_allow_html=True)
st.markdown("## Personalized Counseling Services")
st.markdown("""
<div class='safe-container'>
    <p style='font-size: 1.1rem;'>Our licensed therapists provide evidence-based care in a safe, non-judgmental space. All services are completely confidential.</p>
    
    <div class='calming-card'>
        <div style='display: grid; grid-template-columns: 1fr 2fr; gap: 1.5rem; align-items: center;'>
            <div>
                <h3>Individual Therapy</h3>
                <p>One-on-one sessions tailored to your unique needs. Address anxiety, depression, trauma, and life transitions with compassionate support.</p>
                <ul>
                    <li>50-minute weekly sessions</li>
                    <li>Cognitive Behavioral Therapy (CBT)</li>
                    <li>Mindfulness-based approaches</li>
                    <li>Personalized treatment plans</li>
                </ul>
                <div class='primary-btn' style='display: inline-block; margin-top: 1rem;'>Learn More</div>
            </div>
            <div style='background: url(https://images.unsplash.com/photo-1591348131719-8c1a7b476f41?auto=format&fit=crop&w=600&q=80) center/cover; height: 250px; border-radius: 8px;'></div>
        </div>
    </div>
    
    <div class='calming-card'>
        <h3>Specialized Support</h3>
        <p style='margin-bottom: 1.5rem;'>Targeted approaches for specific challenges:</p>
        <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.5rem;'>
            <div style='background: #f0f7f5; padding: 1.2rem; border-radius: 8px;'>
                <h4 style='color: var(--primary);'>Trauma Recovery</h4>
                <p>EMDR therapy for processing past trauma</p>
                <div style='height: 120px; background: url(https://images.unsplash.com/photo-1527613426441-4da17471b66d?auto=format&fit=crop&w=400&q=80) center/cover; border-radius: 6px; margin-top: 1rem;'></div>
            </div>
            <div style='background: #f0f7f5; padding: 1.2rem; border-radius: 8px;'>
                <h4 style='color: var(--primary);'>Relationship Counseling</h4>
                <p>Improve communication and connection</p>
                <div style='height: 120px; background: url(https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=400&q=80) center/cover; border-radius: 6px; margin-top: 1rem;'></div>
            </div>
            <div style='background: #f0f7f5; padding: 1.2rem; border-radius: 8px;'>
                <h4 style='color: var(--primary);'>Stress Management</h4>
                <p>Coping strategies for daily challenges</p>
                <div style='height: 120px; background: url(https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=400&q=80) center/cover; border-radius: 6px; margin-top: 1rem;'></div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# THERAPIST PROFILES
st.markdown("<div id='therapists'></div>", unsafe_allow_html=True)
st.markdown("## Meet Our Therapists")
st.markdown("""
<div class='safe-container'>
    <p style='font-size: 1.1rem; margin-bottom: 1.5rem;'>Our team of licensed professionals brings diverse expertise and compassionate care to your healing journey.</p>
    
    <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem;'>
""", unsafe_allow_html=True)

for therapist in therapists:
    colors = ["#4a9b8e", "#5ab4a7", "#6ac9bb", "#7ad8c9"]
    st.markdown(f"""
        <div class='therapist-card'>
            <div style='background: {random.choice(colors)}; width: 100px; height: 100px; border-radius: 50%; margin: 0 auto 1rem; display: flex; align-items: center; justify-content: center; font-size: 2.5rem; color: white;'>
                {therapist['name'][0]}
            </div>
            <h4>{therapist['name']}</h4>
            <p><strong>{therapist['specialty']}</strong></p>
            <p style='font-size: 0.9rem;'>{therapist['approach']}</p>
            <p style='font-size: 0.85rem; color: #6c757d;'>{therapist['experience']} experience</p>
            <div style='border-top: 1px dashed #e0e0e0; margin: 0.8rem 0; padding-top: 0.8rem; font-style: italic;'>
                "{therapist['quote']}"
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# TESTIMONIALS
st.markdown("## Client Experiences")
st.markdown("""
<div class='safe-container'>
    <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;'>
""", unsafe_allow_html=True)

for testimonial in testimonials:
    st.markdown(f"""
        <div class='testimonial'>
            <div style='display: flex; align-items: center; margin-bottom: 0.5rem;'>
                <div style='background: var(--primary); width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 1.2rem; margin-right: 0.8rem;'>
                    {random.choice(["A", "B", "C", "D"])}
                </div>
                <div>
                    <strong>Anonymous Client</strong>
                    <div style='font-size: 0.8rem; color: #6c757d;'>5 sessions completed</div>
                </div>
            </div>
            <p>"{testimonial}"</p>
            <div style='display: flex; margin-top: 0.5rem;'>
                {'★'*5}
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# COUNSELING REGISTRATION
st.markdown("## Begin Your Healing Journey")
with st.form("counseling_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your Name", placeholder="First and Last Name")
        email = st.text_input("Email Address", placeholder="you@example.com")
        phone = st.text_input("Phone", placeholder="+254 XXX XXX XXX")
        
    with col2:
        concern = st.selectbox("Primary Concern", 
                              ["Anxiety", "Depression", "Trauma", "Relationship Issues", 
                               "Grief/Loss", "Stress Management", "Self-Esteem", "Other"])
        preference = st.radio("Session Preference", ["Online", "In-Person"])
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        submit = st.form_submit_button("Request Consultation", use_container_width=True)
    
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
    We never share your details without explicit consent. Your journey is safe with us.
</div>
""", unsafe_allow_html=True)

# MOOD TRACKER
st.markdown("<div id='mood_tracker'></div>", unsafe_allow_html=True)
st.markdown("## Mood & Wellness Journal")
st.markdown("""
<div class='safe-container'>
    <p style='margin-bottom: 1.5rem;'>Track your emotional patterns between sessions. This private journal helps you and your therapist understand your progress.</p>
    
    <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 1rem; margin: 1.5rem 0;'>
        <div class='mood-option' onclick='setMood("Radiant")'>
            <div class='mood-emoji'>😊</div>
            <div>Radiant</div>
            <div style='font-size: 0.8rem; color: #6c757d;'>Hopeful, joyful</div>
        </div>
        <div class='mood-option' onclick='setMood("Calm")'>
            <div class='mood-emoji'>😌</div>
            <div>Calm</div>
            <div style='font-size: 0.8rem; color: #6c757d;'>Peaceful, centered</div>
        </div>
        <div class='mood-option' onclick='setMood("Neutral")'>
            <div class='mood-emoji'>😐</div>
            <div>Neutral</div>
            <div style='font-size: 0.8rem; color: #6c757d;'>Balanced, steady</div>
        </div>
        <div class='mood-option' onclick='setMood("Anxious")'>
            <div class='mood-emoji'>😟</div>
            <div>Anxious</div>
            <div style='font-size: 0.8rem; color: #6c757d;'>Worried, tense</div>
        </div>
        <div class='mood-option' onclick='setMood("Sad")'>
            <div class='mood-emoji'>😔</div>
            <div>Sad</div>
            <div style='font-size: 0.8rem; color: #6c757d;'>Grieving, low</div>
        </div>
    </div>
    
    <script>
    function setMood(mood) {
        const options = document.querySelectorAll('.mood-option');
        options.forEach(opt => opt.classList.remove('selected'));
        event.target.closest('.mood-option').classList.add('selected');
        Streamlit.setComponentValue(mood);
    }
    </script>
    """, unsafe_allow_html=True)

mood = st.selectbox("How are you feeling today?", 
                   ["Select an option", "Radiant", "Calm", "Neutral", "Anxious", "Sad"],
                   key="mood_select")

note = st.text_area("Briefly note what's affecting your mood (optional)", 
                   height=120, 
                   placeholder="What thoughts, events, or sensations are you experiencing today? Your therapist will see this in your next session.")

if st.button("Save Journal Entry", use_container_width=True):
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
        <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;'>
            <div>
                <h4 style='color: var(--primary);'>24/7 Crisis Line</h4>
                <p style='font-size: 1.2rem; font-weight: bold;'>+254 781 095 919</p>
                <p>Available any time for urgent emotional support</p>
            </div>
            <div>
                <h4 style='color: var(--primary);'>Emergency Contact</h4>
                <p>If you're in immediate danger, please go to your nearest hospital or call:</p>
                <p style='font-size: 1.1rem; font-weight: bold;'>999 (Kenya Emergency Services)</p>
            </div>
        </div>
    </div>
    
    <div class='calming-card'>
        <h3>Self-Help Tools</h3>
        <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;'>
            <div>
                <h4 style='color: var(--primary);'>Grounding Exercise</h4>
                <p>Use this 5-4-3-2-1 technique when feeling overwhelmed:</p>
                <ol>
                    <li><strong>5 things</strong> you can see around you</li>
                    <li><strong>4 things</strong> you can touch right now</li>
                    <li><strong>3 things</strong> you can hear nearby</li>
                    <li><strong>2 things</strong> you can smell or like to smell</li>
                    <li><strong>1 thing</strong> you can taste or like to taste</li>
                </ol>
            </div>
            <div>
                <h4 style='color: var(--primary);'>Breathing Practice</h4>
                <p>Box Breathing for anxiety relief:</p>
                <div style='display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.5rem; text-align: center; margin: 1rem 0;'>
                    <div style='background: #e6f2f0; padding: 1rem; border-radius: 6px;'>
                        <div style='font-size: 1.2rem;'>4s</div>
                        <div>Inhale</div>
                    </div>
                    <div style='background: #d1e7e3; padding: 1rem; border-radius: 6px;'>
                        <div style='font-size: 1.2rem;'>4s</div>
                        <div>Hold</div>
                    </div>
                    <div style='background: #bcddd7; padding: 1rem; border-radius: 6px;'>
                        <div style='font-size: 1.2rem;'>4s</div>
                        <div>Exhale</div>
                    </div>
                    <div style='background: #a7d3cb; padding: 1rem; border-radius: 6px;'>
                        <div style='font-size: 1.2rem;'>4s</div>
                        <div>Hold</div>
                    </div>
                </div>
                <p>Repeat for 5 minutes to calm your nervous system</p>
            </div>
        </div>
    </div>
    
    <div class='calming-card'>
        <h3>Recommended Resources</h3>
        <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem;'>
            <div>
                <h4 style='color: var(--primary);'>Books</h4>
                <ul>
                    <li>The Body Keeps the Score</li>
                    <li>Feeling Good</li>
                    <li>Mindfulness for Beginners</li>
                    <li>The Anxiety Toolkit</li>
                </ul>
            </div>
            <div>
                <h4 style='color: var(--primary);'>Apps</h4>
                <ul>
                    <li>Calm - Meditation & Sleep</li>
                    <li>Headspace - Mindfulness</li>
                    <li>MoodTools - Depression Aid</li>
                    <li>Sanvello - Anxiety Relief</li>
                </ul>
            </div>
            <div>
                <h4 style='color: var(--primary);'>Online Courses</h4>
                <ul>
                    <li>CBT Techniques</li>
                    <li>Mindfulness Basics</li>
                    <li>Emotional Resilience</li>
                    <li>Communication Skills</li>
                </ul>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div style='margin-top: 3rem; padding: 2rem; text-align: center; background: #e8f4f8; border-top: 1px solid #d1e7e3;'>
    <div style='max-width: 800px; margin: 0 auto;'>
        <h3 style='color: var(--primary); margin-bottom: 1rem;'>SafeSpace Counseling</h3>
        <p style='margin-bottom: 1.5rem;'>Confidential support for your mental wellness journey</p>
        
        <div style='display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin-bottom: 1.5rem;'>
            <div>
                <h4>Contact</h4>
                <p>+254 781 095 919</p>
                <p>info@safespace.org</p>
            </div>
            <div>
                <h4>Hours</h4>
                <p>Mon-Fri: 8am-8pm</p>
                <p>Sat: 9am-4pm</p>
            </div>
            <div>
                <h4>Location</h4>
                <p>Nairobi • Mombasa</p>
                <p>Kisumu • Nakuru</p>
            </div>
        </div>
        
        <div style='border-top: 1px solid #d1e7e3; padding-top: 1rem; font-size: 0.9rem; color: #6c757d;'>
            © 2023 SafeSpace Counseling. All rights reserved. 
            <div style='margin-top: 0.5rem;'>Confidential & Secure • Professional Ethics • Inclusive Care</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
