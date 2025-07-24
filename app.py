import streamlit as st
from datetime import datetime
import re
import base64

# Custom CSS for enhanced styling including fixed icons and mobile responsiveness
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
    .service-card, .team-card, .testimonial-card, .cta-banner, .insights-content, .chatbot-container, .resource-card, .story-card, .event-card, .partnership-card, .blog-card, .forum-card, .tracker-card, .volunteer-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .service-card:hover, .team-card:hover, .testimonial-card:hover, .resource-card:hover, .story-card:hover, .event-card:hover, .partnership-card:hover, .blog-card:hover, .forum-card:hover, .tracker-card:hover, .volunteer-card:hover {
        transform: translateY(-3px) scale(1.01);
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
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
        margin-bottom: 1rem;
    }
    .footer {
        text-align: center;
        padding: 1.5rem 0;
        background: #e8f4f8;
        border-top: 1px solid #ddd;
        margin-top: 1rem;
    }
    .cta-banner {
        background: linear-gradient(135deg, var(--primary), #4DB6AC);
        color: white;
        text-align: center;
        padding: 1.5rem;
    }
    .chatbot-container {
        position: fixed;
        bottom: 10px;
        right: 10px;
        width: 90%;
        max-height: 300px;
        overflow-y: auto;
        z-index: 1000;
        background: white;
        padding: 0.5rem;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
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
    /* Fixed icons bar at the bottom */
    .fixed-icons {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: rgba(38, 166, 154, 0.95);
        display: flex;
        justify-content: space-around;
        padding: 0.3rem 0;
        z-index: 1001;
        box-shadow: 0 -1px 5px rgba(0,0,0,0.2);
    }
    .fixed-icons a {
        color: white;
        text-decoration: none;
        font-size: 1.1rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 0.2rem;
    }
    .fixed-icons a span {
        font-size: 0.6rem;
        margin-top: 0.1rem;
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
            max-height: 250px;
        }
        .fixed-icons {
            padding: 0.2rem 0;
        }
        .fixed-icons a {
            font-size: 1.0rem;
        }
        .fixed-icons a span {
            font-size: 0.5rem;
        }
        #about, #services, #blog, #crisis, #forum, #tracker, #volunteer, #contact {
            display: block !important;
            width: 100% !important;
            padding: 0 !important;
            margin: 0 !important;
        }
        .stColumns > div {
            width: 100% !important;
            padding: 0 !important;
        }
        img {
            max-width: 100% !important;
            height: auto !important;
        }
        .cta-banner, .insights-content {
            padding: 0.8rem;
        }
        .st-expander {
            margin: 0.5rem 0;
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
if "workshop_form_data" not in st.session_state:
    st.session_state.workshop_form_data = {"name": "", "email": "", "phone": ""}
if "webinar_form_data" not in st.session_state:
    st.session_state.webinar_form_data = {"name": "", "email": "", "phone": ""}

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
    <div style='display: flex; justify-content: center; gap: 0.5rem; margin-top: 0.5rem; flex-wrap: wrap;'>
        <a href='#about' class='primary-btn'>About</a>
        <a href='#services' class='primary-btn'>Services</a>
        <a href='#blog' class='primary-btn'>Blog</a>
        <a href='#tracker' class='primary-btn'>Tracker</a>
        <a href='#volunteer' class='primary-btn'>Volunteer</a>
        <a href='#contact' class='primary-btn'>Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# HERO SECTION
st.markdown("<div id='hero'></div>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding: 1.5rem; background: linear-gradient(rgba(38,166,154,0.9), rgba(77,182,172,0.9)); border-radius: 8px; color: white;'>
    <h1>Healing Minds, Restoring Lives</h1>
    <p style='font-size: 1rem; max-width: 100%; margin: 0.5rem auto;'>SafeSpace Kenya provides professional, confidential counseling and mental health services in a supportive, culturally-sensitive environment.</p>
    <img src='https://images.unsplash.com/photo-1588195539435-d6b5f19e1c24?auto=format&fit=crop&w=600&q=80' style='width: 100%; max-width: 600px; border-radius: 8px; margin: 0.5rem auto; box-shadow: 0 2px 4px rgba(0,0,0,0.2);' alt='Safe counselling session'/>
    <div style='display: flex; justify-content: center; gap: 0.5rem; flex-wrap: wrap;'>
        <a href='#contact' class='primary-btn'>Book a Free Consultation</a>
        <a href='#services' class='primary-btn'>Explore Services</a>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Read More About Hero Section", expanded=False):
    st.markdown("""
    - **Purpose**: Highlights our mission to provide accessible mental health care.
    - **Image**: Represents a safe counseling environment.
    - **Contact**: Reach out at info@safespacekenya.org for more details.
    """)

# ABOUT SECTION
st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.markdown("## About SafeSpace Kenya")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p><strong>SafeSpace Kenya</strong>, founded in 2023, is dedicated to providing accessible, culturally-appropriate mental health care for all Kenyans. Our team of qualified professionals offers in-person and tele-counseling services, creating a safe, non-judgmental space for healing and growth.</p>
</div>
""", unsafe_allow_html=True)
with st.expander("Read More About SafeSpace Kenya", expanded=False):
    st.markdown("""
    - **History**: Established to address mental health stigma in Kenya.
    - **Reach**: Serves urban and rural communities across the country.
    - **Contact**: Email history@safespacekenya.org for more background.
    """)

# SERVICES SECTION
st.markdown("<div id='services'></div>", unsafe_allow_html=True)
st.markdown("## Our Therapeutic Services")
st.markdown("Discover our range of evidence-based therapies tailored to your needs.")
services = [
    {
        "icon": "👤",
        "title": "Individual Counseling",
        "desc": "Personalized sessions addressing depression, anxiety, and personal growth."
    },
    {
        "icon": "👥",
        "title": "Group Therapy",
        "desc": "Supportive group healing for grief, addiction, and stress."
    },
    {
        "icon": "🏠",
        "title": "Family Counseling",
        "desc": "Improve communication and resolve conflicts among family members."
    },
    {
        "icon": "🎓",
        "title": "Workshops & Training",
        "desc": "Programs for schools, companies, and community organizations."
    },
    {
        "icon": "📱",
        "title": "Tele-therapy",
        "desc": "Online counseling via video sessions from your home."
    },
    {
        "icon": "❤️",
        "title": "Trauma Support",
        "desc": "Therapy for PTSD and trauma recovery."
    }
]

for service in services:
    st.markdown(f"""
    <div class='service-card'>
        <h3>{service['icon']} {service['title']}</h3>
        <p>{service['desc']}</p>
    </div>
    """, unsafe_allow_html=True)

# TEAM SECTION
st.markdown("## Meet Our Team")
team = [
    {
        "name": "Jerim Owino",
        "role": "Founder & CEO",
        "bio": "Jerim leads SafeSpace Kenya with 10+ years in mental health advocacy, specializing in trauma therapy."
    },
    {
        "name": "Hamdi Roble",
        "role": "Co-Founder",
        "bio": "Hamdi focuses on community outreach and culturally-sensitive mental health care."
    }
]

for member in team:
    st.markdown(f"""
    <div class='team-card'>
        <h4>{member['name']}</h4>
        <p style='color: var(--accent); font-style: italic;'>{member['role']}</p>
        <p>{member['bio']}</p>
    </div>
    """, unsafe_allow_html=True)

# RESOURCES AND SELF-HELP TOOLS SECTION
st.markdown("## Resources and Self-Help Tools")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Explore free tools to support your mental wellbeing:</p>
""", unsafe_allow_html=True)
resources = [
    {
        "title": "Breathing Exercise Guide",
        "desc": "Step-by-step guide to the 4-7-8 breathing technique."
    },
    {
        "title": "Journaling Prompts",
        "desc": "Prompts to process emotions and reflect daily."
    },
    {
        "title": "Mindfulness Audio Script",
        "desc": "Short script for practicing mindfulness."
    }
]
for resource in resources:
    download_link = get_download_link(f"{resource['title']}: {resource['desc']}", f"{resource['title'].lower().replace(' ', '_')}.txt")
    st.markdown(f"""
    <div class='resource-card'>
        <h4>{resource['title']}</h4>
        <p>{resource['desc']}</p>
        {download_link}
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# CRISIS RESOURCES SECTION
st.markdown("<div id='crisis'></div>", unsafe_allow_html=True)
st.markdown("## Crisis Resources")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Immediate support for mental health crises:</p>
    <ul>
        <li><strong>Befrienders Kenya Helpline:</strong> 1199 (24/7)</li>
        <li><strong>SafeSpace Helpline:</strong> +254 781 095 919 (8 AM - 7 PM)</li>
    </ul>
    <a href='#contact' class='primary-btn' style='display: block; text-align: center; margin-top: 0.5rem;'>Get Help Now</a>
</div>
""", unsafe_allow_html=True)

# MENTAL HEALTH BLOG SECTION
st.markdown("<div id='blog'></div>", unsafe_allow_html=True)
st.markdown("## Mental Health Blog")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Insightful articles and tips for mental wellness:</p>
""", unsafe_allow_html=True)
blogs = [
    {
        "title": "Coping with Stress",
        "date": "July 20, 2025",
        "desc": "Strategies to manage stress during financial challenges."
    },
    {
        "title": "Cultural Therapy",
        "date": "July 15, 2025",
        "desc": "Integrating Kenyan traditions into therapy."
    }
]
for blog in blogs:
    st.markdown(f"""
    <div class='blog-card'>
        <h4>{blog['title']}</h4>
        <p><strong>Date:</strong> {blog['date']}</p>
        <p>{blog['desc']}</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# SUCCESS STORIES OR CASE STUDIES SECTION
st.markdown("## Success Stories")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Real transformation stories (anonymized):</p>
""", unsafe_allow_html=True)
stories = [
    {
        "title": "Overcoming Anxiety",
        "desc": "A Nairobi client regained confidence with CBT."
    },
    {
        "title": "Family Healing",
        "desc": "A Mombasa family improved communication."
    }
]
for story in stories:
    st.markdown(f"""
    <div class='story-card'>
        <h4>{story['title']}</h4>
        <p>{story['desc']}</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# EVENTS AND WEBINARS SECTION
st.markdown("## Events and Webinars")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Join our upcoming mental health events:</p>
""", unsafe_allow_html=True)
events = [
    {
        "title": "Stress Management Workshop",
        "date": "July 30, 2025, 10:00 AM - 12:00 PM EAT",
        "desc": "Learn stress management techniques."
    },
    {
        "title": "Understanding Trauma Webinar",
        "date": "August 5, 2025, 6:00 PM - 7:30 PM EAT",
        "desc": "Explore trauma recovery strategies."
    }
]
for i, event in enumerate(events):
    with st.form(f"event_form_{i}", clear_on_submit=True):
        st.session_state[f"event_form_data_{i}"] = st.session_state.get(f"event_form_data_{i}", {"name": "", "email": "", "phone": ""})
        name = st.text_input("Full Name", value=st.session_state[f"event_form_data_{i}"]["name"], placeholder="Your full name", key=f"name_{i}")
        email = st.text_input("Email", value=st.session_state[f"event_form_data_{i}"]["email"], placeholder="your.email@example.com", key=f"email_{i}")
        phone = st.text_input("Phone Number", value=st.session_state[f"event_form_data_{i}"]["phone"], placeholder="+254 XXX XXX XXX", key=f"phone_{i}")
        submit = st.form_submit_button("Register")
        if submit:
            if not name or not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email) or not phone:
                st.error("Please fill in all required fields.")
            else:
                st.session_state[f"event_form_data_{i}"] = {"name": name, "email": email, "phone": phone}
                st.success(f"Thank you, {name}! Your registration for {event['title']} has been received.")
                st.session_state[f"event_form_data_{i}"] = {"name": "", "email": "", "phone": ""}
    st.markdown(f"""
    <div class='event-card'>
        <h4>{event['title']}</h4>
        <p><strong>Date:</strong> {event['date']}</p>
        <p>{event['desc']}</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# PARTNERSHIPS AND COLLABORATIONS SECTION
st.markdown("## Partnerships and Collaborations")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>We partner with organizations to expand support:</p>
""", unsafe_allow_html=True)
partnerships = [
    {
        "name": "Kenya Red Cross",
        "desc": "Collaborating on trauma support."
    },
    {
        "name": "Nairobi County Education",
        "desc": "Workshops for student mental health."
    }
]
for partnership in partnerships:
    st.markdown(f"""
    <div class='partnership-card'>
        <h4>{partnership['name']}</h4>
        <p>{partnership['desc']}</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# TESTIMONIALS SECTION
st.markdown("## Client Testimonials")
testimonials = [
    {
        "name": "Wanjiru M., Nairobi",
        "quote": "Counseling helped me manage anxiety with cultural techniques."
    },
    {
        "name": "David O., Mombasa",
        "quote": "Family counseling improved our communication."
    }
]
for testimonial in testimonials:
    st.markdown(f"""
    <div class='testimonial-card'>
        <h4>{testimonial['name']}</h4>
        <p style='font-style: italic;'>{testimonial['quote']}</p>
    </div>
    """, unsafe_allow_html=True)

# FAQ SECTION
st.markdown("## Frequently Asked Questions")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <h3>Common Questions</h3>
""", unsafe_allow_html=True)
faqs = [
    {
        "question": "How much do sessions cost?",
        "answer": "Sessions start at KES 3,000 with discounts for packages."
    },
    {
        "question": "Is my information confidential?",
        "answer": "Yes, we adhere to strict confidentiality policies."
    }
]
for faq in faqs:
    with st.expander(faq["question"]):
        st.markdown(faq["answer"])
st.markdown("</div>", unsafe_allow_html=True)

# CONTACT SECTION
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.markdown("## Contact Us")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p><strong>📍 Location</strong><br>Greenhouse Plaza, Ngong Road, Nairobi</p>
    <p><strong>📞 Phone</strong><br>+254 781 095 919</p>
    <p><strong>✉️ Email</strong><br><a href='mailto:info@safespacekenya.org'>info@safespacekenya.org</a></p>
    <a href='#' class='primary-btn' style='display: block; text-align: center; margin-top: 0.5rem;'>Book Now</a>
</div>
""", unsafe_allow_html=True)

# MENTAL HEALTH INSIGHTS SECTION
st.markdown("## Mental Health Insights")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <h3>Latest Tips</h3>
    <div style='display: flex; flex-direction: column; gap: 0.5rem;'>
        <div>
            <h4>5 Ways to Manage Stress</h4>
            <p>Learn techniques to reduce stress.</p>
        </div>
        <div>
            <h4>Understanding Anxiety</h4>
            <p>Discover signs and coping strategies.</p>
        </div>
    </div>
    <a href='#' class='primary-btn' style='display: block; text-align: center; margin-top: 0.5rem;'>Read More</a>
</div>
""", unsafe_allow_html=True)

# COMMUNITY FORUM SECTION
st.markdown("<div id='forum'></div>", unsafe_allow_html=True)
st.markdown("## Community Forum")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Join our forum to share experiences:</p>
    <div class='forum-card'>
        <h4>Live Q&A</h4>
        <p>Date: July 25, 2025, 6:00 PM EAT</p>
        <p>Topic: Coping with Grief</p>
    </div>
    <a href='#contact' class='primary-btn' style='display: block; text-align: center; margin-top: 0.5rem;'>Join Now</a>
</div>
""", unsafe_allow_html=True)

# PROGRESS TRACKER SECTION
st.markdown("<div id='tracker'></div>", unsafe_allow_html=True)
st.markdown("## Progress Tracker")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Track your mental health journey:</p>
    <div class='tracker-card'>
        <h4>Mood Tracker</h4>
        <p>Rate your mood (1-5).</p>
    </div>
""", unsafe_allow_html=True)
mood = st.slider("How do you feel today?", 1, 5, 3, key="mood_input")
if st.button("Log Mood"):
    st.session_state.mood_history.append({"date": datetime.today().date(), "mood": mood})
    st.success("Mood logged!")
for entry in st.session_state.mood_history[-3:]:
    st.markdown(f"- {entry['date']}: Mood {entry['mood']}/5")
st.markdown("""
    <a href='#contact' class='primary-btn' style='display: block; text-align: center; margin-top: 0.5rem;'>View History</a>
</div>
""", unsafe_allow_html=True)

# VOLUNTEER OPPORTUNITIES SECTION
st.markdown("<div id='volunteer'></div>", unsafe_allow_html=True)
st.markdown("## Volunteer Opportunities")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Contribute to our initiatives:</p>
""", unsafe_allow_html=True)
volunteer_roles = [
    {
        "title": "Outreach Support",
        "desc": "Assist with awareness programs, 2-4 hours weekly."
    },
    {
        "title": "Event Volunteer",
        "desc": "Help with the July 30 workshop."
    }
]
for role in volunteer_roles:
    st.markdown(f"""
    <div class='volunteer-card'>
        <h4>{role['title']}</h4>
        <p>{role['desc']}</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

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
        response = "I'm sorry, I don't understand. Visit our Contact section for help."
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

# Fixed Icons Bar
st.markdown("""
<div class='fixed-icons'>
    <a href='#forum'><span>Forum</span>💬</a>
    <a href='#crisis'><span>Crisis</span>🚨</a>
</div>
""", unsafe_allow_html=True)

knowledge_base = [
    {"section": "About", "answer": "SafeSpace Kenya provides accessible mental health care.", "keywords": ["about", "safespace"]},
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
