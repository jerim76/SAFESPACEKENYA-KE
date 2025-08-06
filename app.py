import streamlit as st
from datetime import datetime, timedelta
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
        .team-card {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            padding: 15px;
        }
        .team-img {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            object-fit: cover;
            margin-bottom: 15px;
            border: 3px solid var(--primary);
        }
        .service-card {
            padding: 20px;
            border-left: 4px solid var(--primary);
        }
        .appointment-card {
            background: linear-gradient(135deg, #e8f4f8, #d1e7ea);
            padding: 25px;
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

st.set_page_config(page_title="SafeSpace Organisation", page_icon="❤️", layout="wide")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "mood_history" not in st.session_state:
    st.session_state.mood_history = []
if "client_feedback" not in st.session_state:
    st.session_state.client_feedback = []
if "appointments" not in st.session_state:
    st.session_state.appointments = []
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
    st.markdown("<a href='#appointments' class='btn'>Book Appointment</a>", unsafe_allow_html=True)
with cols[1]:
    st.markdown("<a href='#services' class='btn'>Explore Services</a>", unsafe_allow_html=True)

# ABOUT SECTION
st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.markdown("## About Us")
st.markdown("""
<div class='card'>
    <p>Founded in 2023 by Jerim Owino and Hamdi Roble, SafeSpace Organisation is a Nairobi-based mental health 
    initiative committed to providing accessible, compassionate care to all Kenyans. With a team of 15 dedicated 
    professionals, we've supported over 2,500 clients through individual and community-based programs.</p>
    
    <h4>Our Mission</h4>
    <p>To create a stigma-free Kenya where mental health support is accessible to all, regardless of background 
    or financial means.</p>
    
    <h4>Our Approach</h4>
    <p>We combine evidence-based therapies with culturally sensitive approaches, focusing on:</p>
    <ul>
        <li>Trauma-informed care</li>
        <li>Holistic wellness</li>
        <li>Community empowerment</li>
        <li>Preventative mental health</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# FOUNDERS SECTION
st.markdown("<div id='founders'></div>", unsafe_allow_html=True)
st.markdown("## Meet Our Founders")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class='card team-card'>
        <div style='background-color:#ddd; width:120px; height:120px; border-radius:50%; margin:0 auto 15px; display:flex; align-items:center; justify-content:center;'>👨‍⚕️</div>
        <h4>Jerim Owino</h4>
        <p>Clinical Psychologist</p>
        <p>MA in Clinical Psychology, University of Nairobi</p>
        <p>12+ years specializing in trauma counseling for refugees and conflict survivors. Developed Kenya's 
        first community-based PTSD intervention program adopted by 7 counties.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card team-card'>
        <div style='background-color:#ddd; width:120px; height:120px; border-radius:50%; margin:0 auto 15px; display:flex; align-items:center; justify-content:center;'>👩‍⚕️</div>
        <h4>Hamdi Roble</h4>
        <p>Public Health Specialist</p>
        <p>MPH, Johns Hopkins University</p>
        <p>8+ years developing mental health integration programs in primary care settings. Led Kenya's 
        award-winning "Mind & Body" initiative reaching 50,000+ in rural communities.</p>
    </div>
    """, unsafe_allow_html=True)

# OUR TEAM SECTION
st.markdown("<div id='team'></div>", unsafe_allow_html=True)
st.markdown("## Our Caring Team")
st.markdown("<p class='support-text'>Meet some of our dedicated mental health professionals</p>", unsafe_allow_html=True)

team_cols = st.columns(3)
team_members = [
    {"name": "Dr. Aisha Mohamed", "role": "Clinical Director", "bio": "PhD in Counseling Psychology with 15 years experience in adolescent mental health."},
    {"name": "Peter Kiprop", "role": "Senior Therapist", "bio": "Specializes in CBT and addiction counseling. 10+ years in rehabilitation programs."},
    {"name": "Grace Mwende", "role": "Child Psychologist", "bio": "Developed Kenya's first school-based mental health screening program."}
]

for i, member in enumerate(team_members):
    with team_cols[i]:
        st.markdown(f"""
        <div class='card team-card'>
            <div style='background-color:#eee; width:100px; height:100px; border-radius:50%; margin:0 auto 15px; display:flex; align-items:center; justify-content:center;'>👤</div>
            <h4>{member['name']}</h4>
            <p><strong>{member['role']}</strong></p>
            <p>{member['bio']}</p>
        </div>
        """, unsafe_allow_html=True)

# EXPANDED SERVICES SECTION
st.markdown("<div id='services'></div>", unsafe_allow_html=True)
st.markdown("## Comprehensive Services for You")
st.markdown("<p class='support-text'>Tailored support for your mental wellness journey</p>", unsafe_allow_html=True)

services = [
    {"title": "Individual Counseling", 
     "desc": "One-on-one sessions with our licensed therapists",
     "details": """
        <ul>
            <li>50-minute personalized sessions</li>
            <li>Cognitive Behavioral Therapy (CBT)</li>
            <li>Solution-Focused Brief Therapy</li>
            <li>Trauma-focused interventions</li>
            <li>Anxiety and depression management</li>
        </ul>
        <p><strong>Duration:</strong> 6-12 sessions recommended</p>
        <p><strong>Cost:</strong> KSh 800-1,500/session</p>
     """},
     
    {"title": "Group Therapy", 
     "desc": "Healing in community with peer support",
     "details": """
        <ul>
            <li>Support groups (8-10 members)</li>
            <li>Thematic workshops: grief, anxiety, parenting</li>
            <li>Skills-building groups</li>
            <li>Process-oriented therapy</li>
        </ul>
        <p><strong>Schedule:</strong> Weekly 90-minute sessions</p>
        <p><strong>Cost:</strong> KSh 500/session</p>
     """},
     
    {"title": "Online Counseling", 
     "desc": "Professional support from anywhere",
     "details": """
        <ul>
            <li>Secure video sessions</li>
            <li>Flexible evening and weekend hours</li>
            <li>Chat-based support between sessions</li>
            <li>Digital resource library access</li>
        </ul>
        <p><strong>Platform:</strong> HIPAA-compliant secure portal</p>
        <p><strong>Cost:</strong> KSh 1,000-2,000/session</p>
     """},
     
    {"title": "Crisis Intervention", 
     "desc": "Immediate support when you need it most",
     "details": """
        <ul>
            <li>24/7 crisis hotline</li>
            <li>Emergency counseling sessions</li>
            <li>Safety planning</li>
            <li>Referrals to emergency services</li>
        </ul>
        <p><strong>Hotline:</strong> +254 781 095 919</p>
        <p><strong>Cost:</strong> Free for first 3 sessions</p>
     """},
     
    {"title": "Corporate Wellness", 
     "desc": "Mental health support for organizations",
     "details": """
        <ul>
            <li>Employee Assistance Programs</li>
            <li>Stress management workshops</li>
            <li>Leadership mental health training</li>
            <li>Organizational mental health audits</li>
        </ul>
        <p><strong>Custom packages</strong> available</p>
     """},
]

for service in services:
    with st.expander(f"{service['title']} - {service['desc']}"):
        st.markdown(f"""
        <div class='service-card'>
            {service['details']}
        </div>
        """, unsafe_allow_html=True)

# APPOINTMENT BOOKING SECTION
st.markdown("<div id='appointments'></div>", unsafe_allow_html=True)
st.markdown("## Book Your Appointment")
st.markdown("<p class='support-text'>Schedule a session with one of our specialists</p>", unsafe_allow_html=True)

with st.form("appointment_form", clear_on_submit=True):
    cols = st.columns(2)
    with cols[0]:
        name = st.text_input("Your Full Name")
        email = st.text_input("Your Email")
        phone = st.text_input("Your Phone")
        service_type = st.selectbox("Service Type", ["Individual Counseling", "Group Therapy", "Online Counseling", "Crisis Support"])
        
    with cols[1]:
        preferred_date = st.date_input("Preferred Date", min_value=datetime.today(), 
                                      max_value=datetime.today() + timedelta(days=60))
        preferred_time = st.selectbox("Preferred Time", ["9:00 AM", "11:00 AM", "1:00 PM", "3:00 PM", "5:00 PM"])
        therapist = st.selectbox("Preferred Therapist (Optional)", ["No preference", "Jerim Owino", "Hamdi Roble", "Dr. Aisha Mohamed", "Peter Kiprop"])
        concerns = st.text_area("Briefly share your concerns")
        
    submit = st.form_submit_button("Book Appointment")
    
    if submit:
        if name and email and phone and re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            appointment_data = {
                "name": name,
                "email": email,
                "phone": phone,
                "service": service_type,
                "date": preferred_date.strftime("%Y-%m-%d"),
                "time": preferred_time,
                "therapist": therapist,
                "timestamp": datetime.now()
            }
            st.session_state.appointments.append(appointment_data)
            st.success(f"Appointment booked for {preferred_date} at {preferred_time}! We've sent confirmation to {email}")
        else:
            st.error("Please provide valid name, email, and phone number")

# TESTIMONIALS SECTION
st.markdown("<div id='testimonials'></div>", unsafe_allow_html=True)
st.markdown("## Stories of Hope and Healing")
testimonials = [
    {"name": "Jane K.", "quote": "SafeSpace gave me hope when I needed it most. After losing my job, the counseling helped me rebuild my confidence and find new purpose."},
    {"name": "Michael T.", "quote": "The group therapy sessions helped me realize I wasn't alone in my anxiety. The coping strategies I learned are life-changing."},
    {"name": "Fatuma A.", "quote": "As a single mother, the affordable online sessions made it possible for me to get help without childcare worries."}
]

test_cols = st.columns(3)
for i, testimonial in enumerate(testimonials):
    with test_cols[i]:
        st.markdown(f"""
        <div class='card'>
            <p><em>"{testimonial['quote']}"</em></p>
            <p style='text-align:right;'><strong>- {testimonial['name']}</strong></p>
        </div>
        """, unsafe_allow_html=True)

# RESOURCES SECTION
st.markdown("<div id='resources'></div>", unsafe_allow_html=True)
st.markdown("## Mental Health Resources")
st.markdown("<p class='support-text'>Free tools and materials for your wellness journey</p>", unsafe_allow_html=True)

resources = [
    {"title": "Anxiety Management Guide", "desc": "Practical strategies for daily anxiety reduction", "type": "PDF"},
    {"title": "Mindfulness Meditation Series", "desc": "10 guided audio sessions for stress relief", "type": "Audio"},
    {"title": "Mental Health Self-Assessment", "desc": "Tool to track your emotional wellbeing", "type": "Interactive"},
    {"title": "Parenting During Stress", "desc": "Guide for maintaining family mental health", "type": "PDF"},
]

res_cols = st.columns(2)
for i in range(0, len(resources), 2):
    with res_cols[0]:
        if i < len(resources):
            st.markdown(f"""
            <div class='card'>
                <h4>{resources[i]['title']}</h4>
                <p>{resources[i]['desc']}</p>
                <p><strong>Format:</strong> {resources[i]['type']}</p>
                <button class='btn'>Download</button>
            </div>
            """, unsafe_allow_html=True)
    
    with res_cols[1]:
        if i+1 < len(resources):
            st.markdown(f"""
            <div class='card'>
                <h4>{resources[i+1]['title']}</h4>
                <p>{resources[i+1]['desc']}</p>
                <p><strong>Format:</strong> {resources[i+1]['type']}</p>
                <button class='btn'>Download</button>
            </div>
            """, unsafe_allow_html=True)

# MOOD TRACKER SECTION
st.markdown("<div id='tracker'></div>", unsafe_allow_html=True)
st.markdown("## Your Mood Journey")
st.markdown("<p class='support-text'>Track your emotional wellbeing over time</p>", unsafe_allow_html=True)

mood = st.slider("How are you feeling today? (1-5)", 1, 5, 3, help="1 = Very low, 5 = Excellent")
note = st.text_area("What's affecting your mood today?")
reflection = st.text_area("What might help improve how you feel?")
if st.button("Save Your Mood Entry"):
    st.session_state.mood_history.append({"Date": datetime.now(), "Mood": mood, "Note": note, "Reflection": reflection})
    st.success(f"Your mood entry saved successfully at {datetime.now().strftime('%I:%M %p')}")
    
if st.session_state.mood_history:
    st.markdown("### Your Recent Mood Entries")
    for entry in st.session_state.mood_history[-3:]:
        date_value = entry["Date"]
        date_str = date_value.strftime('%b %d, %Y %I:%M %p') if isinstance(date_value, datetime) else date_value
        mood_emoji = "😢" if entry["Mood"] <= 2 else "😐" if entry["Mood"] == 3 else "😊"
        st.markdown(f"""
        <div class='card'>
            <div style="display:flex; justify-content:space-between;">
                <div><strong>{date_str}</strong></div>
                <div>Mood: {entry['Mood']}/5 {mood_emoji}</div>
            </div>
            <p><strong>Notes:</strong> {entry['Note'] or 'No notes'}</p>
            <p><strong>Reflection:</strong> {entry['Reflection'] or 'No reflection'}</p>
        </div>
        """, unsafe_allow_html=True)
    
    if st.button("Download Full Mood History"):
        csv = export_mood_history()
        st.markdown(get_download_link(csv, "my_mood_journey.csv"), unsafe_allow_html=True)

# VOLUNTEER SECTION
st.markdown("<div id='volunteer'></div>", unsafe_allow_html=True)
st.markdown("## Join Our Movement")
st.markdown("<p class='support-text'>Make a difference in mental health awareness</p>", unsafe_allow_html=True)

with st.expander("Volunteer Opportunities"):
    st.markdown("""
    <div class='card'>
        <h4>Community Outreach Volunteer</h4>
        <p><strong>Commitment:</strong> 4-8 hours/month</p>
        <p>Help us bring mental health education to underserved communities through:</p>
        <ul>
            <li>Organizing community workshops</li>
            <li>Distributing educational materials</li>
            <li>Facilitating support groups</li>
        </ul>
        
        <h4>Professional Volunteer</h4>
        <p><strong>Commitment:</strong> Pro bono sessions (flexible)</p>
        <p>Licensed therapists can provide:</p>
        <ul>
            <li>Quarterly pro bono counseling</li>
            <li>Supervision for new counselors</li>
            <li>Specialized workshop facilitation</li>
        </ul>
        
        <h4>Administrative Support</h4>
        <p><strong>Commitment:</strong> Flexible remote hours</p>
        <p>Help with:</p>
        <ul>
            <li>Grant writing</li>
            <li>Social media management</li>
            <li>Event planning</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with st.form("volunteer_form", clear_on_submit=True):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    phone = st.text_input("Your Phone")
    role = st.selectbox("Area of Interest", ["Community Outreach", "Professional Counseling", "Administrative Support", "Fundraising"])
    experience = st.text_area("Relevant Experience")
    submit = st.form_submit_button("Apply to Volunteer")
    if submit and name and re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) and phone:
        st.session_state.volunteer_form_data = {"name": name, "email": email, "phone": phone, "role": role}
        st.success(f"Thank you, {name}! We'll contact you about volunteer opportunities.")
    elif submit:
        st.error("Please provide valid details: name, valid email, and phone number.")

# CONTACT SECTION
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.markdown("## We're Here for You")
st.markdown("""
<div class='card appointment-card'>
    <div style="display:flex; flex-wrap:wrap; gap:20px;">
        <div style="flex:1; min-width:250px;">
            <h4>Contact Information</h4>
            <p>📍 Greenhouse Plaza, 3rd Floor<br>Nairobi, Kenya</p>
            <p>📞 +254 781 095 919</p>
            <p>✉️ info@safespaceorganisation.org</p>
            <p>🌐 www.safespaceorganisation.org</p>
        </div>
        
        <div style="flex:1; min-width:250px;">
            <h4>Operating Hours</h4>
            <p>Monday-Friday: 9:00 AM - 6:00 PM</p>
            <p>Saturday: 10:00 AM - 2:00 PM</p>
            <p>Sunday: Closed</p>
            <p><em>Crisis support available 24/7</em></p>
        </div>
    </div>
    
    <div style="margin-top:20px;">
        <h4>Visit Our Center</h4>
        <div style="background:#eee; height:200px; display:flex; align-items:center; justify-content:center; border-radius:10px;">
            <p>📍 Map would appear here</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# CHATBOT SECTION
st.markdown("## Need Immediate Support?")
st.markdown("<p class='support-text'>Our virtual assistant is here to help</p>", unsafe_allow_html=True)

chat_container = st.container()
if st.session_state.chat_history:
    with chat_container:
        for msg in st.session_state.chat_history:
            if msg[0] == "user":
                st.markdown(f"<div style='background:var(--soft); padding:10px; border-radius:10px; margin-bottom:10px;'><strong>You:</strong> {msg[1]}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='background:var(--primary); color:white; padding:10px; border-radius:10px; margin-bottom:10px;'><strong>Friend:</strong> {msg[1]}</div>", unsafe_allow_html=True)

query = st.text_input("Type your message here...", key="chat_input")
if st.button("Send") and query:
    response = get_chatbot_response(query)
    st.session_state.chat_history.append(("user", query))
    st.session_state.chat_history.append(("bot", response))
    st.rerun()

# FOOTER
st.markdown("<hr style='border-color: var(--primary); opacity: 0.3;'>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; padding:20px;">
    <p>© 2023-2025 SafeSpace Organisation | Mental Health Support for Kenya</p>
    <div style="display:flex; justify-content:center; gap:15px; margin-top:10px;">
        <a href="#contact" style="color:var(--primary);">Contact</a> | 
        <a href="#privacy" style="color:var(--primary);">Privacy Policy</a> | 
        <a href="#terms" style="color:var(--primary);">Terms of Service</a> | 
        <a href="#donate" style="color:var(--primary);">Donate</a>
    </div>
    <div style="margin-top:15px;">
        <span style="font-size:1.5rem; margin:0 10px;">📱</span>
        <span style="font-size:1.5rem; margin:0 10px;">💬</span>
        <span style="font-size:1.5rem; margin:0 10px;">📸</span>
    </div>
</div>
""", unsafe_allow_html=True)
