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
        background: rgba(255, 255, 255, 0.95);
        border-radius: 12px;
        padding: 1.8rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 1.8rem;
        border-left: 4px solid var(--primary);
    }
    .calming-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1.2rem 0;
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
        padding: 0.7rem 1.5rem;
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
    .mood-option {
        padding: 1rem;
        margin: 0.5rem;
        border-radius: 8px;
        cursor: pointer;
        text-align: center;
        background: #f8fbfa;
        transition: all 0.2s;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 130px;
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
        font-size: 2.2rem;
        margin-bottom: 0.5rem;
    }
    .confidential {
        font-size: 0.9rem;
        color: #5a6c75;
        margin-top: 1.2rem;
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 6px;
        border-left: 3px solid var(--primary);
        line-height: 1.6;
    }
    .testimonial {
        padding: 1.5rem;
        background: linear-gradient(to right, #f8fbfa, #e6f2f0);
        border-radius: 8px;
        margin: 1.2rem 0;
        border-left: 3px solid var(--accent);
        font-style: italic;
        position: relative;
    }
    .testimonial::before {
        content: "\\"";
        font-size: 3rem;
        position: absolute;
        top: -15px;
        left: 10px;
        color: var(--primary);
        opacity: 0.3;
    }
    .therapist-card {
        padding: 1.2rem;
        background: white;
        border-radius: 8px;
        box-shadow: 0 3px 8px rgba(0,0,0,0.06);
        text-align: center;
        margin: 0.7rem;
        height: 95%;
    }
    .therapy-method {
        background: #f0f7f5;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .symptom-guide {
        padding: 1rem;
        background: #f8fbfa;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 3px solid var(--accent);
    }
    @media (max-width: 768px) {
        .calming-card {
            padding: 1.2rem;
            margin: 1rem 0;
        }
        h1 { font-size: 2rem; }
        h2 { font-size: 1.7rem; }
        h3 { font-size: 1.4rem; }
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

# Therapist profiles
therapists = [
    {
        "name": "Dr. Amina Hassan",
        "specialty": "Trauma & PTSD Specialist",
        "approach": "EMDR, Somatic Therapy, CBT",
        "experience": "12 years",
        "bio": "Dr. Hassan specializes in trauma recovery with expertise in complex PTSD. Her approach integrates evidence-based therapies with cultural sensitivity, having worked with refugees and survivors of violence across East Africa.",
        "credentials": "PhD Clinical Psychology, Certified EMDR Therapist"
    },
    {
        "name": "Ben Ochieng",
        "specialty": "Relationships & Family Therapy",
        "approach": "Emotion-Focused Therapy, Gottman Method",
        "experience": "8 years",
        "bio": "Ben helps couples rebuild trust and communication using scientifically-backed methods. He leads our premarital counseling program and conducts workshops on healthy relationship dynamics.",
        "credentials": "MA Marriage & Family Therapy, EFT Certified"
    },
    {
        "name": "Grace Mwangi",
        "specialty": "Depression & Mood Disorders",
        "approach": "CBT, Positive Psychology, Behavioral Activation",
        "experience": "10 years",
        "bio": "Grace develops personalized treatment plans for depression that combine cognitive restructuring with practical behavioral changes. Her strength-based approach helps clients rediscover meaning and purpose.",
        "credentials": "MA Clinical Psychology, Certified CBT Practitioner"
    },
    {
        "name": "David Kimani",
        "specialty": "Youth & Adolescent Mental Health",
        "approach": "Play Therapy, Art Therapy, Family Systems",
        "experience": "7 years",
        "bio": "David creates safe spaces for young people to express themselves through creative modalities. He specializes in school-related anxiety, bullying recovery, and family reconciliation.",
        "credentials": "MS Child Psychology, Registered Play Therapist"
    }
]

# Therapeutic approaches
therapy_methods = [
    {
        "name": "Cognitive Behavioral Therapy (CBT)",
        "description": "Identifies and changes negative thought patterns and behaviors",
        "uses": "Effective for depression, anxiety, phobias, and eating disorders",
        "duration": "Typically 12-20 sessions"
    },
    {
        "name": "Eye Movement Desensitization & Reprocessing (EMDR)",
        "description": "Processes traumatic memories using bilateral stimulation",
        "uses": "PTSD, trauma, panic attacks, and phobias",
        "duration": "8-12 sessions for single trauma"
    },
    {
        "name": "Mindfulness-Based Stress Reduction (MBSR)",
        "description": "Cultivates present-moment awareness to reduce reactivity",
        "uses": "Stress, chronic pain, anxiety, and emotional regulation",
        "duration": "8-week program with daily practice"
    },
    {
        "name": "Dialectical Behavior Therapy (DBT)",
        "description": "Builds skills in emotional regulation and distress tolerance",
        "uses": "Borderline personality disorder, self-harm, and emotional dysregulation",
        "duration": "6-12 month comprehensive program"
    }
]

# Symptom guide
symptom_guide = {
    "Anxiety": {
        "physical": "Racing heart, sweating, trembling, dizziness, stomach issues",
        "emotional": "Excessive worry, fear of losing control, irritability, feeling on edge",
        "coping": "Deep breathing, grounding exercises, scheduled worry time, progressive muscle relaxation"
    },
    "Depression": {
        "physical": "Fatigue, sleep changes, appetite changes, unexplained aches",
        "emotional": "Persistent sadness, hopelessness, loss of interest, feelings of worthlessness",
        "coping": "Behavioral activation, light therapy, gratitude journaling, physical activity"
    },
    "PTSD": {
        "physical": "Hypervigilance, insomnia, exaggerated startle response, headaches",
        "emotional": "Flashbacks, nightmares, emotional numbness, avoidance of triggers",
        "coping": "Grounding techniques, EMDR, creating safety plans, trauma-focused CBT"
    }
}

# Testimonials
testimonials = [
    "SafeSpace gave me tools to manage my anxiety that I'll use for life. My therapist was incredibly patient and understanding.",
    "After just 6 sessions, I feel like a different person. The depression that felt permanent is finally lifting.",
    "The cultural sensitivity made all the difference. Finally a therapist who understands my background and experiences.",
    "The mood journal helped me see patterns I never noticed. My therapist used these insights to tailor our sessions perfectly."
]

# HERO SECTION
st.markdown("""
<div class='safe-container' style='text-align: center; background: linear-gradient(rgba(74,155,142,0.9), rgba(90,180,167,0.9)); color: white; padding: 2.5rem; border-radius: 12px;'>
    <h1 style='color: white; font-size: 2.8rem; margin-bottom: 1rem;'>SafeSpace Counseling</h1>
    <p style='font-size: 1.3rem; max-width: 800px; margin: 0 auto 2rem;'>Your Journey to Emotional Wellness Begins Here</p>
    <div style='display: flex; justify-content: center; gap: 1.5rem; flex-wrap: wrap; margin: 2rem 0;'>
        <a href='#services' class='primary-btn' style='background: white; color: var(--primary);'>Explore Services</a>
        <a href='#therapists' class='primary-btn' style='background: rgba(255,255,255,0.2); border: 1px solid white;'>Meet Our Therapists</a>
        <a href='#mood_tracker' class='primary-btn' style='background: rgba(255,255,255,0.2); border: 1px solid white;'>Mood Journal</a>
    </div>
</div>
""", unsafe_allow_html=True)

# THERAPEUTIC SERVICES
st.markdown("<div id='services'></div>", unsafe_allow_html=True)
st.markdown("## Comprehensive Therapeutic Services")
st.markdown("""
<div class='safe-container'>
    <p style='font-size: 1.1rem; line-height: 1.7;'>Our evidence-based therapies are delivered by licensed professionals with specialized training. 
    We customize treatment plans to address your unique needs and goals, providing compassionate care in a confidential setting.</p>
    
    <div class='calming-card'>
        <h3>Individual Therapy</h3>
        <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; align-items: center;'>
            <div>
                <p>One-on-one sessions focused on your personal growth and healing. Our therapists use various evidence-based approaches tailored to your specific concerns.</p>
                <ul style='margin: 1.2rem 0;'>
                    <li><strong>Duration:</strong> 50-minute weekly sessions</li>
                    <li><strong>Techniques:</strong> CBT, Mindfulness, Psychodynamic Therapy</li>
                    <li><strong>Focus Areas:</strong> Anxiety, depression, trauma, life transitions</li>
                    <li><strong>Outcomes:</strong> Improved coping skills, emotional regulation, self-awareness</li>
                </ul>
                <div class='primary-btn' style='display: inline-block; margin-top: 0.5rem;'>Learn More</div>
            </div>
            <div style='background: url(https://images.unsplash.com/photo-1591348131719-8c1a7b476f41?auto=format&fit=crop&w=600&q=80) center/cover; height: 280px; border-radius: 8px;'></div>
        </div>
    </div>
    
    <div class='calming-card'>
        <h3>Specialized Therapeutic Approaches</h3>
        <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.8rem; margin-top: 1.5rem;'>
""", unsafe_allow_html=True)

for method in therapy_methods:
    st.markdown(f"""
        <div class='therapy-method'>
            <h4 style='color: var(--primary); margin-bottom: 0.5rem;'>{method['name']}</h4>
            <p><strong>How it works:</strong> {method['description']}</p>
            <p><strong>Best for:</strong> {method['uses']}</p>
            <p><strong>Typical duration:</strong> {method['duration']}</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# SYMPTOM GUIDANCE
st.markdown("<div id='symptoms'></div>", unsafe_allow_html=True)
st.markdown("## Understanding Mental Health Symptoms")
st.markdown("""
<div class='safe-container'>
    <p style='font-size: 1.1rem; margin-bottom: 1.5rem;'>Recognizing symptoms is the first step toward healing. Here's a guide to common mental health experiences:</p>
    
    <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.8rem;'>
""", unsafe_allow_html=True)

for condition, info in symptom_guide.items():
    st.markdown(f"""
        <div class='symptom-guide'>
            <h4 style='color: var(--accent);'>{condition}</h4>
            <p><strong>Physical symptoms:</strong> {info['physical']}</p>
            <p><strong>Emotional symptoms:</strong> {info['emotional']}</p>
            <p><strong>Coping strategies:</strong> {info['coping']}</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# THERAPIST PROFILES
st.markdown("<div id='therapists'></div>", unsafe_allow_html=True)
st.markdown("## Our Therapeutic Team")
st.markdown("""
<div class='safe-container'>
    <p style='font-size: 1.1rem; margin-bottom: 1.8rem;'>Meet our licensed therapists who bring diverse expertise and compassionate care to your healing journey.</p>
    
    <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;'>
""", unsafe_allow_html=True)

colors = ["#4a9b8e", "#5ab4a7", "#6ac9bb", "#7ad8c9"]
for i, therapist in enumerate(therapists):
    st.markdown(f"""
        <div class='therapist-card'>
            <div style='background: {colors[i]}; width: 110px; height: 110px; border-radius: 50%; margin: 0 auto 1.2rem; display: flex; align-items: center; justify-content: center; font-size: 2.8rem; color: white;'>
                {therapist['name'][0]}
            </div>
            <h4>{therapist['name']}</h4>
            <p style='color: var(--primary); font-weight: 500;'>{therapist['specialty']}</p>
            <p style='font-size: 0.95rem;'><strong>Approach:</strong> {therapist['approach']}</p>
            <p style='font-size: 0.9rem; margin: 0.8rem 0;'>{therapist['bio']}</p>
            <div style='background: #f0f7f5; padding: 0.8rem; border-radius: 6px; margin: 1rem 0; font-size: 0.85rem;'>
                {therapist['credentials']}
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# TESTIMONIALS
st.markdown("## Client Experiences")
st.markdown("""
<div class='safe-container'>
    <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.8rem;'>
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
            <div style='display: flex; margin-top: 0.5rem; color: #ffc107;'>
                {'★'*5}
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# COUNSELING REGISTRATION
st.markdown("## Begin Your Healing Journey")
st.markdown("""
<div class='safe-container'>
    <p style='font-size: 1.1rem; margin-bottom: 1.5rem;'>Take the first step toward emotional wellness. Complete our confidential intake form and we'll match you with the right therapist.</p>
    
    <div style='background: #f8fbfa; padding: 1.5rem; border-radius: 10px;'>
        <h4 style='color: var(--primary); margin-bottom: 1.2rem;'>Personalized Matching Process</h4>
        <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; margin-bottom: 1.5rem;'>
            <div style='text-align: center;'>
                <div style='font-size: 2rem; background: #e6f2f0; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 0.8rem;'>1</div>
                <p>Complete intake form</p>
            </div>
            <div style='text-align: center;'>
                <div style='font-size: 2rem; background: #e6f2f0; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 0.8rem;'>2</div>
                <p>Therapist match within 24hrs</p>
            </div>
            <div style='text-align: center;'>
                <div style='font-size: 2rem; background: #e6f2f0; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 0.8rem;'>3</div>
                <p>Free 15-min consultation</p>
            </div>
            <div style='text-align: center;'>
                <div style='font-size: 2rem; background: #e6f2f0; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 0.8rem;'>4</div>
                <p>Begin your therapy journey</p>
            </div>
        </div>
        
        <div style='background: white; padding: 1.5rem; border-radius: 8px;'>
""", unsafe_allow_html=True)

with st.form("counseling_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your Full Name", placeholder="First and Last Name")
        email = st.text_input("Email Address", placeholder="you@example.com")
        phone = st.text_input("Phone Number", placeholder="+254 XXX XXX XXX")
        
    with col2:
        concern = st.selectbox("Primary Concern", 
                              ["Anxiety", "Depression", "Trauma/PTSD", "Relationship Issues", 
                               "Grief/Loss", "Stress Management", "Self-Esteem", "Life Transitions", "Other"])
        preference = st.radio("Session Preference", ["Online", "In-Person"])
        urgency = st.select_slider("Urgency Level", options=["Low", "Medium", "High"])
    
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
                "preference": preference,
                "urgency": urgency
            }
            st.success("Thank you for your request! A therapist will contact you within 24 hours to schedule your first session.")
            st.balloons()

st.markdown("""
        </div>
    </div>
    
    <div class='confidential'>
        <strong>Confidentiality Assurance:</strong> All information is protected under professional ethical guidelines (APA & KCPA). 
        We never share your details without explicit consent. Client-therapist confidentiality is strictly maintained, 
        with exceptions only as required by law regarding imminent safety concerns.
    </div>
</div>
""", unsafe_allow_html=True)

# MOOD TRACKER - FIXED SECTION
st.markdown("<div id='mood_tracker'></div>", unsafe_allow_html=True)
st.markdown("## Mood & Wellness Journal")
st.markdown("""
<div class='safe-container'>
    <p style='margin-bottom: 1.5rem;'>Track your emotional patterns between sessions. This private journal helps identify triggers and progress, providing valuable insights for your therapy.</p>
</div>
""", unsafe_allow_html=True)

# Mood selection with Streamlit components
mood_options = {
    "😊 Radiant": "Hopeful, joyful, energized",
    "😌 Calm": "Peaceful, centered, balanced",
    "😐 Neutral": "Steady, indifferent, stable",
    "😟 Anxious": "Worried, tense, overwhelmed",
    "😔 Sad": "Grieving, low, disconnected"
}

selected_mood = st.selectbox(
    "Select your current mood:", 
    ["Choose a mood"] + list(mood_options.keys()),
    key="mood_select"
)

if selected_mood != "Choose a mood":
    st.caption(mood_options[selected_mood])

note = st.text_area(
    "Journal your thoughts and experiences (optional)", 
    height=140, 
    placeholder="What thoughts, events, or physical sensations are you experiencing today? What coping strategies did you try? Your therapist will see this in your next session."
)

if st.button("Save Journal Entry", use_container_width=True):
    if selected_mood != "Choose a mood":
        entry = {
            "Date": datetime.now(),
            "Mood": selected_mood,
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
st.markdown("## Therapeutic Resources & Tools")
st.markdown("""
<div class='safe-container'>
    <div class='calming-card'>
        <h3>Crisis Support & Emergency Contacts</h3>
        <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;'>
            <div>
                <h4 style='color: var(--primary);'>Immediate Assistance</h4>
                <div style='background: #f0f7f5; padding: 1.2rem; border-radius: 8px; margin: 1rem 0;'>
                    <p style='font-size: 1.3rem; font-weight: bold; margin-bottom: 0.5rem;'>+254 781 095 919</p>
                    <p>SafeSpace 24/7 Crisis Line (Staffed by trained counselors)</p>
                </div>
                <div style='background: #f0f7f5; padding: 1.2rem; border-radius: 8px; margin: 1rem 0;'>
                    <p style='font-size: 1.3rem; font-weight: bold; margin-bottom: 0.5rem;'>1199</p>
                    <p>Befrienders Kenya Suicide Prevention Hotline</p>
                </div>
            </div>
            <div>
                <h4 style='color: var(--primary);'>Emergency Services</h4>
                <div style='background: #f0f7f5; padding: 1.2rem; border-radius: 8px; margin: 1rem 0;'>
                    <p style='font-size: 1.3rem; font-weight: bold; margin-bottom: 0.5rem;'>999</p>
                    <p>Kenya National Police Emergency</p>
                </div>
                <div style='background: #f0f7f5; padding: 1.2rem; border-radius: 8px; margin: 1rem 0;'>
                    <p style='font-size: 1.3rem; font-weight: bold; margin-bottom: 0.5rem;'>+254 20 272 6300</p>
                    <p>Nairobi Women's Hospital Gender Violence Recovery Centre</p>
                </div>
            </div>
        </div>
    </div>
    
    <div class='calming-card'>
        <h3>Evidence-Based Coping Strategies</h3>
        <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;'>
            <div>
                <h4 style='color: var(--primary); margin-bottom: 1rem;'>Grounding Techniques</h4>
                <p><strong>5-4-3-2-1 Sensory Awareness:</strong></p>
                <ol>
                    <li><strong>5 things</strong> you can see around you</li>
                    <li><strong>4 things</strong> you can touch right now</li>
                    <li><strong>3 things</strong> you can hear nearby</li>
                    <li><strong>2 things</strong> you can smell or like to smell</li>
                    <li><strong>1 thing</strong> you can taste or like to taste</li>
                </ol>
                
                <p style='margin-top: 1.5rem;'><strong>Container Exercise:</strong></p>
                <p>Visualize placing difficult thoughts/feelings in a container to be processed later with your therapist.</p>
            </div>
            <div>
                <h4 style='color: var(--primary); margin-bottom: 1rem;'>Breathing Exercises</h4>
                <p><strong>Box Breathing for Anxiety:</strong></p>
                <div style='display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.8rem; text-align: center; margin: 1.2rem 0;'>
                    <div style='background: #e6f2f0; padding: 1.2rem; border-radius: 8px;'>
                        <div style='font-size: 1.3rem; font-weight: bold;'>4s</div>
                        <div>Inhale</div>
                    </div>
                    <div style='background: #d1e7e3; padding: 1.2rem; border-radius: 8px;'>
                        <div style='font-size: 1.3rem; font-weight: bold;'>4s</div>
                        <div>Hold</div>
                    </div>
                    <div style='background: #bcddd7; padding: 1.2rem; border-radius: 8px;'>
                        <div style='font-size: 1.3rem; font-weight: bold;'>4s</div>
                        <div>Exhale</div>
                    </div>
                    <div style='background: #a7d3cb; padding: 1.2rem; border-radius: 8px;'>
                        <div style='font-size: 1.3rem; font-weight: bold;'>4s</div>
                        <div>Hold</div>
                    </div>
                </div>
                <p>Repeat for 5 minutes to activate parasympathetic nervous system</p>
                
                <p style='margin-top: 1.5rem;'><strong>4-7-8 Breathing for Sleep:</strong></p>
                <p>Inhale 4s → Hold 7s → Exhale 8s. Repeat 4 cycles before bedtime.</p>
            </div>
        </div>
    </div>
    
    <div class='calming-card'>
        <h3>Mental Health Resources</h3>
        <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem;'>
            <div>
                <h4 style='color: var(--primary);'>Recommended Reading</h4>
                <ul>
                    <li><strong>The Body Keeps the Score</strong> by Bessel van der Kolk (Trauma)</li>
                    <li><strong>Feeling Good</strong> by David D. Burns (Depression/CBT)</li>
                    <li><strong>The Anxiety and Phobia Workbook</strong> by Edmund Bourne</li>
                    <li><strong>Attached</strong> by Amir Levine (Relationships)</li>
                    <li><strong>Self-Compassion</strong> by Kristin Neff</li>
                </ul>
            </div>
            <div>
                <h4 style='color: var(--primary);'>Mobile Applications</h4>
                <ul>
                    <li><strong>Calm:</strong> Meditation & Sleep Stories</li>
                    <li><strong>MoodTools:</strong> Depression Aid & Safety Planning</li>
                    <li><strong>Daylio:</strong> Mood Tracking & Journaling</li>
                    <li><strong>Sanvello:</strong> CBT Techniques for Anxiety</li>
                    <li><strong>Insight Timer:</strong> Free Meditation Library</li>
                </ul>
            </div>
            <div>
                <h4 style='color: var(--primary);'>Online Resources</h4>
                <ul>
                    <li>Kenya Psychological Association (KPA)</li>
                    <li>Mental Health Kenya Directory</li>
                    <li>Anxiety and Depression Association of America</li>
                    <li>National Alliance on Mental Illness (NAMI)</li>
                    <li>Psychology Today Therapist Finder</li>
                </ul>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div style='margin-top: 3rem; padding: 2.5rem; text-align: center; background: #e8f4f8; border-top: 1px solid #d1e7e3;'>
    <div style='max-width: 900px; margin: 0 auto;'>
        <h3 style='color: var(--primary); margin-bottom: 1.2rem;'>SafeSpace Counseling</h3>
        <p style='margin-bottom: 1.8rem; font-size: 1.1rem;'>Professional, confidential mental health care for individuals, couples, and families</p>
        
        <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; margin-bottom: 2rem;'>
            <div>
                <h4>Contact Information</h4>
                <p>+254 781 095 919</p>
                <p>info@safespace.org</p>
                <p>contact@safespace.org</p>
            </div>
            <div>
                <h4>Operating Hours</h4>
                <p>Monday-Friday: 8am-8pm</p>
                <p>Saturday: 9am-4pm</p>
                <p>24/7 Crisis Line Available</p>
            </div>
            <div>
                <h4>Locations</h4>
                <p>Nairobi: Westlands Office Park</p>
                <p>Mombasa: Nyali Centre</p>
                <p>Kisumu: Mega Plaza</p>
                <p>Nakuru: Pinewood Mall</p>
            </div>
            <div>
                <h4>Quick Links</h4>
                <p><a href='#services' style='color: var(--primary); text-decoration: none;'>Services</a></p>
                <p><a href='#therapists' style='color: var(--primary); text-decoration: none;'>Therapists</a></p>
                <p><a href='#resources' style='color: var(--primary); text-decoration: none;'>Resources</a></p>
                <p><a href='#mood_tracker' style='color: var(--primary); text-decoration: none;'>Mood Journal</a></p>
            </div>
        </div>
        
        <div style='border-top: 1px solid #d1e7e3; padding-top: 1.2rem; font-size: 0.9rem; color: #6c757d;'>
            © 2023 SafeSpace Counseling. All rights reserved. 
            <div style='margin-top: 0.8rem;'>Licensed by Kenya Psychological Association • HIPAA-Compliant Platform • Confidential & Secure</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
