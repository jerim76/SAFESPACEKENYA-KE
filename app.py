import streamlit as st
from datetime import datetime
import re
import base64

# Custom CSS for enhanced styling
st.markdown("""
<style>
    :root {
        --primary: #2a7a7c;
        --accent: #d4a373;
        --light: #e6f3f5;
        --dark: #2c3e50;
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
        color: var(--primary) !important;
        text-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }
    h1 { font-size: 2.8rem; }
    h2 { font-size: 2.2rem; }
    h3 { font-size: 1.8rem; }
    .service-card, .team-card, .testimonial-card, .cta-banner, .insights-content, .chatbot-container, .resource-card, .story-card, .event-card, .partnership-card, .blog-card, .forum-card, .tracker-card, .volunteer-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
    }
    .service-card:hover, .team-card:hover, .testimonial-card:hover, .resource-card:hover, .story-card:hover, .event-card:hover, .partnership-card:hover, .blog-card:hover, .forum-card:hover, .tracker-card:hover, .volunteer-card:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 8px 16px rgba(0,0,0,0.15);
    }
    .primary-btn {
        background: linear-gradient(135deg, var(--primary), #4a9ca5);
        color: white;
        padding: 0.6rem 1.8rem;
        border-radius: 25px;
        border: none;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
    }
    .primary-btn:hover {
        background: linear-gradient(135deg, var(--accent), #e0b68a);
        transform: translateY(-3px);
    }
    .stButton > button {
        background: linear-gradient(135deg, var(--primary), #4a9ca5);
        color: white;
        border-radius: 25px;
        border: none;
        padding: 0.6rem 1.2rem;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, var(--accent), #e0b68a);
    }
    .st-expander {
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        background: #f9f9f9;
    }
    .footer {
        text-align: center;
        padding: 2.5rem 0;
        background: #e8f4f8;
        border-top: 1px solid #ddd;
        margin-top: 3rem;
    }
    .cta-banner {
        background: linear-gradient(135deg, var(--primary), #4a9ca5);
        color: white;
        text-align: center;
        padding: 3rem;
    }
    .chatbot-container {
        position: fixed;
        bottom: 20px;
        left: 20px;
        width: 350px;
        max-height: 400px;
        overflow-y: auto;
        z-index: 1000;
        background: white;
        padding: 1rem;
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.2);
    }
    .chatbot-message.user {
        background: #e8f4f8;
        text-align: right;
        color: var(--dark);
        padding: 0.5rem;
        margin: 0.5rem 0;
        border-radius: 8px;
    }
    .chatbot-message.bot {
        background: white;
        text-align: left;
        color: var(--primary);
        padding: 0.5rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        border-left: 4px solid var(--primary);
    }
    .chatbot-input {
        width: 100%;
        padding: 0.5rem;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        margin-top: 0.5rem;
    }
    html {
        scroll-behavior: smooth;
    }
    @media (max-width: 768px) {
        .stColumn {
            margin-bottom: 1rem;
        }
        .service-card, .team-card, .testimonial-card, .insights-content, .chatbot-container, .resource-card, .story-card, .event-card, .partnership-card, .blog-card, .forum-card, .tracker-card, .volunteer-card {
            margin: 0.5rem;
        }
        .chatbot-container {
            width: 90%;
            left: 5%;
        }
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="SafeSpace Kenya",
    page_icon="🧠",
    layout="wide",
)

# Initialize session state for chatbot and progress tracker
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "mood_history" not in st.session_state:
    st.session_state.mood_history = [{"date": datetime(2025, 7, 22).date(), "mood": 3}, {"date": datetime(2025, 7, 23).date(), "mood": 4}]

# Function to create download link
def get_download_link(file_content, file_name):
    b64 = base64.b64encode(file_content.encode()).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_name}" class="primary-btn" style="display: block; text-align: center; margin-top: 1rem;">Download</a>'
    return href

# TITLE BAR
st.title("SafeSpace Kenya")
st.subheader("Empowering Minds, Nurturing Hope")

# HERO SECTION
st.markdown("""
<div style='text-align: center; padding: 4rem 1rem; background: linear-gradient(rgba(42,122,124,0.9), rgba(74,156,165,0.9)); border-radius: 12px; color: white;'>
    <h1>Healing Minds, Restoring Lives</h1>
    <p style='font-size: 1.2rem; max-width: 900px; margin: 0 auto 2rem;'>SafeSpace Kenya provides professional, confidential counseling and mental health services in a supportive, culturally-sensitive environment.</p>
    <img src='https://images.unsplash.com/photo-1588195539435-d6b5f19e1c24?auto=format&fit=crop&w=1200&q=80' style='width: 90%; max-width: 1000px; border-radius: 12px; margin: 2rem auto; box-shadow: 0 4px 8px rgba(0,0,0,0.2);' alt='Safe counselling session'/>
    <div style='display: flex; justify-content: center; gap: 1.5rem;'>
        <a href='#contact' class='primary-btn'>Book a Free Consultation</a>
        <a href='#services' class='primary-btn'>Explore Services</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ABOUT SECTION
st.markdown("## About SafeSpace Kenya")
st.markdown("""
<div style='background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
    <p><strong>SafeSpace Kenya</strong>, founded in 2023, is dedicated to providing accessible, culturally-appropriate mental health care for all Kenyans. Our team of qualified professionals offers in-person and tele-counseling services, creating a safe, non-judgmental space for healing and growth.</p>
</div>
""", unsafe_allow_html=True)

# MISSION & VISION SECTION
st.markdown("## Our Mission & Vision")
st.markdown("""
<div style='background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
    <h3>Our Mission</h3>
    <p>To break down barriers to mental health care and promote emotional wellbeing for all Kenyans through compassionate, evidence-based services.</p>
    <h3>Our Vision</h3>
    <p>A Kenya where mental health is prioritized, stigma is eliminated, and everyone has access to supportive care in a safe environment.</p>
</div>
""", unsafe_allow_html=True)

# SERVICES SECTION
st.markdown("<div id='services'></div>", unsafe_allow_html=True)
st.markdown("## Our Therapeutic Services")
st.markdown("Discover our range of evidence-based therapies tailored to your needs.")
services = [
    {
        "icon": "👤",
        "title": "Individual Counseling",
        "desc": "Personalized sessions addressing depression, anxiety, and personal growth.",
        "info": """
        - **Approach**: Utilizes Cognitive Behavioral Therapy (CBT), Solution-Focused Brief Therapy (SFBT), and person-centered therapy tailored to individual needs.
        - **Duration**: 50-minute sessions, typically weekly or biweekly.
        - **Benefits**: Develop coping strategies, enhance self-awareness, and achieve personal goals.
        - **Target Audience**: Individuals facing anxiety, depression, life transitions, or seeking personal development.
        """
    },
    {
        "icon": "👥",
        "title": "Group Therapy",
        "desc": "Supportive group healing for grief, addiction, and stress.",
        "info": """
        - **Approach**: Facilitated by trained therapists using group dynamics and peer support, with themes like grief, addiction recovery, or stress management.
        - **Duration**: 90-minute sessions, weekly for 6-12 weeks.
        - **Benefits**: Build community, reduce isolation, and learn from shared experiences.
        - **Target Audience**: Individuals seeking peer support for specific challenges, such as loss or substance recovery.
        """
    },
    {
        "icon": "🏠",
        "title": "Family Counseling",
        "desc": "Improve communication and resolve conflicts among family members.",
        "info": """
        - **Approach**: Employs Family Systems Therapy and Structural Family Therapy to address relational dynamics.
        - **Duration**: 60-90 minute sessions, scheduled as needed.
        - **Benefits**: Strengthen family bonds, improve communication skills, and resolve conflicts collaboratively.
        - **Target Audience**: Families navigating marital issues, parenting challenges, or intergenerational conflicts.
        """
    },
    {
        "icon": "🎓",
        "title": "Workshops & Training",
        "desc": "Programs for schools, companies, and community organizations.",
        "info": """
        - **Approach**: Interactive sessions on mental wellness, stress management, and resilience, customized for each audience.
        - **Duration**: Half-day or full-day workshops, with follow-up sessions available.
        - **Benefits**: Equip participants with tools for mental health awareness and workplace or community wellbeing.
        - **Target Audience**: Schools, corporations, NGOs, and community groups seeking mental health education.
        """
    },
    {
        "icon": "📱",
        "title": "Tele-therapy",
        "desc": "Online counseling via video sessions from the comfort of your home.",
        "info": """
        - **Approach**: Secure, confidential sessions via Zoom or WhatsApp, using the same evidence-based therapies as in-person counseling.
        - **Duration**: 50-minute sessions, scheduled flexibly.
        - **Benefits**: Convenient access to therapy, ideal for remote or busy individuals.
        - **Target Audience**: Clients preferring virtual sessions or those unable to attend in-person due to location or mobility.
        """
    },
    {
        "icon": "❤️",
        "title": "Trauma Support",
        "desc": "Therapy for PTSD and trauma recovery.",
        "info": """
        - **Approach**: Uses Eye Movement Desensitization and Reprocessing (EMDR), Trauma-Focused CBT, and somatic therapy.
        - **Duration**: 60-minute sessions, with frequency based on individual needs.
        - **Benefits**: Process traumatic experiences, reduce PTSD symptoms, and regain emotional stability.
        - **Target Audience**: Survivors of physical, emotional, or psychological trauma, including abuse or accidents.
        """
    }
]

cols = st.columns(3)
for i, service in enumerate(services):
    with cols[i % 3]:
        st.markdown(f"""
        <div class='service-card'>
            <h3>{service['icon']} {service['title']}</h3>
            <p>{service['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        with st.expander(f"Learn More About {service['title']}", expanded=False):
            st.markdown(service["info"])

# CALL-TO-ACTION BANNER
st.markdown("""
<div class='cta-banner'>
    <h2>Start Your Healing Journey Today</h2>
    <p style='font-size: 1.2rem; margin-bottom: 2rem;'>Book a free consultation to discuss your needs with our caring team.</p>
    <a href='#contact' class='primary-btn'>Schedule Now</a>
</div>
""", unsafe_allow_html=True)

# TEAM SECTION
st.markdown("## Meet Our Team")
team = [
    {
        "name": "Jerim Owino",
        "role": "Founder & CEO",
        "bio": "As the Founder and CEO, Jerim Owino leads the strategic direction of SafeSpace Kenya, bringing over 10 years of experience in mental health advocacy. He specializes in trauma therapy, designing programs that address PTSD and emotional recovery using evidence-based methods like EMDR and Trauma-Focused CBT. Jerim is passionate about breaking mental health stigma in Kenya and oversees the development of culturally-sensitive counseling services."
    },
    {
        "name": "Hamdi Roble",
        "role": "Co-Founder",
        "bio": "As Co-Founder, Hamdi Roble focuses on community outreach and culturally-sensitive mental health care. With a background in social work, she develops initiatives that integrate local values and traditions into therapy, ensuring accessibility for diverse populations. Hamdi oversees tele-therapy services and faith-sensitive counseling, aiming to build a supportive network across rural and urban Kenya."
    }
]

cols = st.columns(2)
for i, member in enumerate(team):
    with cols[i]:
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
<div style='background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
    <p>Explore free tools to support your mental wellbeing:</p>
""", unsafe_allow_html=True)
resources = [
    {
        "title": "Breathing Exercise Guide",
        "desc": "A step-by-step guide to the 4-7-8 breathing technique for stress relief.",
        "content": "Follow these steps for the 4-7-8 breathing technique:\n1. Inhale through your nose for 4 seconds.\n2. Hold your breath for 7 seconds.\n3. Exhale slowly through your mouth for 8 seconds.\nRepeat 4-5 times daily for best results."
    },
    {
        "title": "Journaling Prompts",
        "desc": "Downloadable prompts to help you process emotions and reflect on your day.",
        "content": "Journaling Prompts:\n- What made me feel grateful today?\n- What challenged me, and how did I cope?\n- What are three goals for tomorrow?"
    },
    {
        "title": "Mindfulness Audio Script",
        "desc": "A short script for practicing mindfulness in daily life.",
        "content": "Mindfulness Script:\nClose your eyes. Focus on your breath. Notice the sounds around you. Let thoughts pass like clouds. Stay present for 5 minutes."
    }
]
cols = st.columns(3)
for i, resource in enumerate(resources):
    download_link = get_download_link(resource["content"], f"{resource['title'].lower().replace(' ', '_')}.txt")
    with cols[i % 3]:
        st.markdown(f"""
        <div class='resource-card'>
            <h4>{resource['title']}</h4>
            <p>{resource['desc']}</p>
            {download_link}
        </div>
        """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# SUCCESS STORIES OR CASE STUDIES SECTION
st.markdown("## Success Stories")
st.markdown("""
<div style='background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
    <p>Real stories of transformation from our clients (anonymized with consent):</p>
""", unsafe_allow_html=True)
stories = [
    {
        "title": "Overcoming Anxiety",
        "desc": "A client from Nairobi found relief from chronic anxiety through tailored CBT sessions, regaining confidence in daily life."
    },
    {
        "title": "Family Healing",
        "desc": "A Mombasa family resolved long-standing conflicts with Family Counseling, improving their communication and bond."
    }
]
cols = st.columns(2)
for i, story in enumerate(stories):
    with cols[i % 2]:
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
<div style='background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
    <p>Join us for upcoming mental health events:</p>
""", unsafe_allow_html=True)
events = [
    {
        "title": "Stress Management Workshop",
        "date": "July 30, 2025, 10:00 AM - 12:00 PM EAT",
        "desc": "Learn practical stress management techniques with our experts."
    },
    {
        "title": "Webinar: Understanding Trauma",
        "date": "August 5, 2025, 6:00 PM - 7:30 PM EAT",
        "desc": "Explore trauma recovery strategies in this live session."
    }
]
cols = st.columns(2)
for i, event in enumerate(events):
    with cols[i % 2]:
        st.markdown(f"""
        <div class='event-card'>
            <h4>{event['title']}</h4>
            <p><strong>Date:</strong> {event['date']}</p>
            <p>{event['desc']}</p>
            <a href='#contact' class='primary-btn' style='display: block; text-align: center; margin-top: 1rem;'>Register</a>
        </div>
        """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# PARTNERSHIPS AND COLLABORATIONS SECTION
st.markdown("## Partnerships and Collaborations")
st.markdown("""
<div style='background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
    <p>We partner with organizations to expand mental health support:</p>
""", unsafe_allow_html=True)
partnerships = [
    {
        "name": "Kenya Red Cross",
        "desc": "Collaborating on trauma support for disaster-affected communities."
    },
    {
        "name": "Nairobi County Education Department",
        "desc": "Providing workshops for student mental health in schools."
    }
]
cols = st.columns(2)
for i, partnership in enumerate(partnerships):
    with cols[i % 2]:
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
        "quote": "The individual counseling sessions at SafeSpace Kenya helped me manage my anxiety with culturally relevant techniques. The team’s warmth and professionalism made all the difference.",
        "img": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=100&q=80"
    },
    {
        "name": "David O., Mombasa",
        "quote": "Family counseling transformed our communication. We learned to listen and support each other, thanks to Yvone’s guidance in creating a safe space for us.",
        "img": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=100&q=80"
    },
    {
        "name": "Aisha K., Kisumu",
        "quote": "Hamdi’s faith-sensitive approach to therapy helped me address my depression while respecting my values. I felt truly understood and supported.",
        "img": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=100&q=80"
    },
    {
        "name": "Samuel T., Nakuru",
        "quote": "After a traumatic accident, the trauma support program gave me tools to rebuild my confidence. Brian’s art therapy sessions were a game-changer for me.",
        "img": "https://images.unsplash.com/photo-1552058544-f2b08422138a?auto=format&fit=crop&w=100&q=80"
    }
]

cols = st.columns(2)
for i, testimonial in enumerate(testimonials):
    with cols[i % 2]:
        st.markdown(f"""
        <div class='testimonial-card'>
            <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;'>
                <img src='{testimonial["img"]}' style='width: 50px; height: 50px; border-radius: 50%; object-fit: cover;'>
                <h4>{testimonial['name']}</h4>
            </div>
            <p style='font-style: italic;'>{testimonial['quote']}</p>
        </div>
        """, unsafe_allow_html=True)

# FAQ SECTION (Expanded)
st.markdown("## Frequently Asked Questions")
st.markdown("""
<div style='background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
    <h3>Common Questions</h3>
""", unsafe_allow_html=True)
faqs = [
    {
        "question": "How much do sessions cost?",
        "answer": "Costs vary by service. Individual sessions start at KES 3,000, with discounts for packages. Contact us for a detailed quote."
    },
    {
        "question": "Is my information confidential?",
        "answer": "Yes, we adhere to strict confidentiality policies to protect your privacy, except in cases required by law."
    },
    {
        "question": "What should I expect in my first session?",
        "answer": "Your first session involves discussing your goals and needs with a therapist to create a personalized plan."
    },
    {
        "question": "Do you offer services in languages other than English?",
        "answer": "Yes, our team provides counseling in English, Swahili, and other local languages upon request."
    },
    {
        "question": "How do I prepare for therapy?",
        "answer": "Reflect on your goals and bring any relevant notes or questions. Our team will guide you through the process."
    },
    {
        "question": "What should I do in a mental health crisis?",
        "answer": "Contact a trusted person or our helpline at +254 781 095 919. For emergencies, visit the nearest hospital."
    },
    {
        "question": "Do you accept insurance?",
        "answer": "Currently, we operate on a private pay basis. Contact us to discuss payment options."
    }
]
for faq in faqs:
    with st.expander(faq["question"]):
        st.markdown(faq["answer"])
st.markdown("</div>", unsafe_allow_html=True)

# CONTACT SECTION
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.markdown("## Contact Us")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div style='background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
        <p><strong>📍 Location</strong><br>Greenhouse Plaza, Ngong Road, Nairobi</p>
        <p><strong>📞 Phone</strong><br>+254 781 095 919 | +254 720 987 654</p>
        <p><strong>✉️ Email</strong><br>
            <a href='mailto:info@safespacekenya.org'>info@safespacekenya.org</a><br>
            <a href='mailto:owinojerim269@gmail.com'>owinojerim269@gmail.com (CEO)</a></p>
        <p><strong>🕒 Hours</strong><br>Mon-Fri: 8AM - 7PM | Sat: 9AM - 4PM</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.subheader("Book an Appointment")
    with st.form("appointment_form", clear_on_submit=True):
        name = st.text_input("Full Name", placeholder="Your full name")
        email = st.text_input("Email", placeholder="your.email@example.com")
        phone = st.text_input("Phone Number", placeholder="+254 XXX XXX XXX")
        service = st.selectbox("Service", [s["title"] for s in services], key="service")
        selected_service = next((s for s in services if s["title"] == service), None)
        if selected_service:
            st.markdown(f"<p>{selected_service['desc']}</p>", unsafe_allow_html=True)
        therapist = st.selectbox("Preferred Therapist", [t["name"] for t in team], key="therapist")
        time_slots = [
            "8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM",
            "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM", "6:00 PM"
        ] if datetime.today().weekday() < 5 else [
            "9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM"
        ]
        time = st.selectbox("Preferred Time", time_slots, key="time")
        date = st.date_input("Preferred Date", min_value=datetime.today())
        message = st.text_area("Message", placeholder="Tell us about your needs")
        submit = st.form_submit_button("Submit Request")
        if submit:
            if not name or not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                st.error("Please provide a valid name and email address.")
            elif not phone:
                st.error("Please provide a phone number.")
            else:
                st.success(f"Thank you, {name}! Your request for {service} with {therapist} on {date.strftime('%Y-%m-%d')} at {time} has been received. We'll contact you soon!")
                st.session_state.form_data = {
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "service": service,
                    "therapist": therapist,
                    "time": time,
                    "date": date,
                    "message": message
                }

# MENTAL HEALTH INSIGHTS SECTION
st.markdown("## Mental Health Insights")
st.markdown("""
<div style='background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
    <h3>Latest Tips & Articles</h3>
    <p>Explore our resources for mental wellness and self-care.</p>
    <div style='display: flex; gap: 1rem;'>
        <div style='flex: 1;'>
            <h4>5 Ways to Manage Stress</h4>
            <p>Learn practical techniques to reduce stress and improve your mental health.</p>
        </div>
        <div style='flex: 1;'>
            <h4>Understanding Anxiety</h4>
            <p>Discover the signs and coping strategies for anxiety disorders.</p>
        </div>
    </div>
    <a href='#insights-content' class='primary-btn' style='display: block; text-align: center; margin-top: 1rem;'>Read More</a>
</div>
""", unsafe_allow_html=True)

# Detailed Insights Content
st.markdown("<div id='insights-content'></div>", unsafe_allow_html=True)
st.markdown("""
<div class='insights-content'>
    <h3>5 Ways to Manage Stress</h3>
    <p>Stress is a common experience, especially in fast-paced environments like Nairobi or during challenging times such as economic pressures or family responsibilities. Here are five practical, evidence-based techniques to manage stress effectively:</p>
    <ul>
        <li><strong>Practice Deep Breathing</strong>: Take slow, deep breaths to calm your nervous system. Try the 4-7-8 technique: inhale for 4 seconds, hold for 7, exhale for 8. This can be done anywhere, like during a matatu ride or at work.</li>
        <li><strong>Engage in Physical Activity</strong>: Regular exercise, such as a brisk walk in Uhuru Park or dancing to your favorite bongo music, releases endorphins, reducing stress naturally.</li>
        <li><strong>Connect with Community</strong>: Share your feelings with trusted friends, family, or a chama group. In Kenyan culture, communal support is powerful for emotional relief.</li>
        <li><strong>Prioritize Self-Care</strong>: Set aside time for activities you enjoy, like cooking ugali, reading, or attending a local church or mosque for spiritual grounding.</li>
        <li><strong>Seek Professional Support</strong>: If stress feels overwhelming, our therapists at SafeSpace Kenya can guide you with tailored strategies like Cognitive Behavioral Therapy (CBT).</li>
    </ul>
    <h3>Understanding Anxiety</h3>
    <p>Anxiety disorders affect many Kenyans, often triggered by life transitions, work pressures, or personal challenges. Recognizing the signs and learning coping strategies can make a difference.</p>
    <p><strong>Common Signs of Anxiety</strong>:</p>
    <ul>
        <li>Persistent worry or fear, such as concerns about finances or family safety.</li>
        <li>Physical symptoms like a racing heart, sweating, or feeling shaky during stressful moments, like a job interview.</li>
        <li>Difficulty concentrating, perhaps while managing a business or studying for exams.</li>
        <li>Sleep disturbances, like trouble falling asleep before a big day.</li>
    </ul>
    <p><strong>Coping Strategies</strong>:</p>
    <ul>
        <li><strong>Mindfulness Practices</strong>: Try grounding techniques, like focusing on the smell of chai or the sound of birds, to stay present.</li>
        <li><strong>Journaling</strong>: Write down your thoughts to process worries, a practice that can be done privately at home.</li>
        <li><strong>Limit Stimulants</strong>: Reduce caffeine intake from tea or coffee, common in Kenyan diets, to lower anxiety levels.</li>
        <li><strong>Professional Help</strong>: Our tele-therapy and in-person sessions at SafeSpace Kenya offer culturally sensitive support, like trauma-focused CBT, to address anxiety.</li>
    </ul>
    <p>Contact us to learn more about managing stress and anxiety with our professional support.</p>
    <a href='#contact' class='primary-btn' style='display: block; text-align: center; margin-top: 1rem;'>Book a Session</a>
</div>
""", unsafe_allow_html=True)

# MENTAL HEALTH BLOG SECTION
st.markdown("## Mental Health Blog")
st.markdown("""
<div style='background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
    <p>Explore insightful articles and tips tailored for mental wellness in Kenya:</p>
""", unsafe_allow_html=True)
blogs = [
    {
        "title": "Coping with Stress During Economic Hardship",
        "date": "July 20, 2025",
        "desc": "This article offers practical strategies to manage stress during financial challenges, including budgeting tips and community support ideas rooted in Kenyan culture."
    },
    {
        "title": "Cultural Perspectives on Therapy",
        "date": "July 15, 2025",
        "desc": "Learn how integrating Kenyan traditions like storytelling and communal healing can enhance modern therapy practices."
    }
]
cols = st.columns(2)
for i, blog in enumerate(blogs):
    with cols[i % 2]:
        st.markdown(f"""
        <div class='blog-card'>
            <h4>{blog['title']}</h4>
            <p><strong>Date:</strong> {blog['date']}</p>
            <p>{blog['desc']}</p>
            <a href='#contact' class='primary-btn' style='display: block; text-align: center; margin-top: 1rem;'>Read More</a>
        </div>
        """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# CRISIS RESOURCES SECTION
st.markdown("## Crisis Resources")
st.markdown("""
<div style='background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
    <p>Immediate support for mental health crises:</p>
    <ul>
        <li><strong>Befrienders Kenya Helpline:</strong> 1199 (24/7 support for emotional distress)</li>
        <li><strong>SafeSpace Helpline:</strong> +254 781 095 919 (available 8 AM - 7 PM)</li>
        <li><strong>Emergency Steps:</strong> Call a trusted friend or family member, contact a helpline, or visit the nearest hospital if you’re in immediate danger.</li>
    </ul>
    <p><strong>Additional Note:</strong> If you feel overwhelmed, don’t hesitate to reach out—support is available.</p>
    <a href='#contact' class='primary-btn' style='display: block; text-align: center; margin-top: 1rem;'>Get Help Now</a>
</div>
""", unsafe_allow_html=True)

# COMMUNITY FORUM SECTION
st.markdown("## Community Forum")
st.markdown("""
<div style='background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
    <p>Join our moderated community to share experiences and support each other:</p>
    <div class='forum-card'>
        <h4>Upcoming Live Q&A</h4>
        <p><strong>Date:</strong> July 25, 2025, 6:00 PM - 7:00 PM EAT</p>
        <p>Topic: Coping with Grief - Hosted by Hamdi Roble. Share your story or ask questions in a safe space.</p>
        <p><strong>Recent Discussion:</strong> Members discussed stress management techniques last week, with over 50 participants.</p>
        <a href='#contact' class='primary-btn' style='display: block; text-align: center; margin-top: 1rem;'>Join Now</a>
    </div>
</div>
""", unsafe_allow_html=True)

# PROGRESS TRACKER SECTION
st.markdown("## Progress Tracker")
st.markdown("""
<div style='background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
    <p>Monitor your mental health journey with our simple tools:</p>
    <div class='tracker-card'>
        <h4>Mood Tracker</h4>
        <p>Rate your mood daily (1 = Low, 5 = High) and see your progress.</p>
    </div>
""", unsafe_allow_html=True)
mood = st.slider("How do you feel today?", 1, 5, 3, key="mood_input")
if st.button("Log Mood"):
    st.session_state.mood_history.append({"date": datetime.today().date(), "mood": mood})
    st.success("Mood logged successfully!")
st.markdown("<h4>Recent Mood History</h4>", unsafe_allow_html=True)
for entry in st.session_state.mood_history[-5:]:  # Show last 5 entries
    st.markdown(f"- {entry['date']}: Mood {entry['mood']}/5", unsafe_allow_html=True)
st.markdown("""
    <a href='#contact' class='primary-btn' style='display: block; text-align: center; margin-top: 1rem;'>View Full History</a>
</div>
""", unsafe_allow_html=True)

# VOLUNTEER OPPORTUNITIES SECTION
st.markdown("## Volunteer Opportunities")
st.markdown("""
<div style='background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
    <p>Contribute to mental health initiatives in your community:</p>
""", unsafe_allow_html=True)
volunteer_roles = [
    {
        "title": "Outreach Support",
        "desc": "Assist with community awareness programs in Nairobi. Training provided, 2-4 hours weekly."
    },
    {
        "title": "Event Volunteer",
        "desc": "Help organize the Stress Management Workshop on July 30, 2025. Roles include setup and participant support."
    }
]
cols = st.columns(2)
for i, role in enumerate(volunteer_roles):
    with cols[i % 2]:
        st.markdown(f"""
        <div class='volunteer-card'>
            <h4>{role['title']}</h4>
            <p>{role['desc']}</p>
            <a href='#contact' class='primary-btn' style='display: block; text-align: center; margin-top: 1rem;'>Apply</a>
        </div>
        """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Chatbot knowledge base and chatbot UI remain unchanged

# Chatbot knowledge base
knowledge_base = [
    {
        "section": "About",
        "answer": "SafeSpace Kenya, founded in 2023, is dedicated to providing accessible, culturally-appropriate mental health care for all Kenyans. Our team offers in-person and tele-counseling services in a safe, non-judgmental environment.",
        "keywords": ["about", "safespace", "founded", "mission", "who are you"]
    },
    {
        "section": "Mission",
        "answer": "Our mission is to break down barriers to mental health care and promote emotional wellbeing for all Kenyans through compassionate, evidence-based services.",
        "keywords": ["mission", "goal", "purpose"]
    },
    {
        "section": "Vision",
        "answer": "Our vision is a Kenya where mental health is prioritized, stigma is eliminated, and everyone has access to supportive care in a safe environment.",
        "keywords": ["vision", "future", "aim"]
    },
    {
        "section": "Services",
        "answer": "We offer Individual Counseling, Group Therapy, Family Counseling, Workshops & Training, Tele-therapy, and Trauma Support. Each service is tailored to your needs with evidence-based approaches like CBT, EMDR, and more.",
        "keywords": ["services", "counseling", "therapy", "offer", "programs"]
    },
    {
        "section": "Individual Counseling",
        "answer": "Individual Counseling provides personalized 50-minute sessions addressing depression, anxiety, and personal growth using Cognitive Behavioral Therapy (CBT) and other approaches.",
        "keywords": ["individual", "personal", "counseling", "cbt"]
    },
    {
        "section": "Group Therapy",
        "answer": "Group Therapy offers 90-minute sessions for 6-12 weeks, focusing on grief, addiction, or stress, fostering community and peer support.",
        "keywords": ["group", "therapy", "grief", "addiction", "stress"]
    },
    {
        "section": "Family Counseling",
        "answer": "Family Counseling uses Family Systems Therapy to improve communication and resolve conflicts in 60-90 minute sessions.",
        "keywords": ["family", "counseling", "communication", "conflict"]
    },
    {
        "section": "Workshops & Training",
        "answer": "Workshops & Training provide half-day or full-day sessions on mental wellness and resilience for schools, companies, and community groups.",
        "keywords": ["workshops", "training", "wellness", "resilience"]
    },
    {
        "section": "Tele-therapy",
        "answer": "Tele-therapy offers secure, confidential 50-minute video sessions via Zoom or WhatsApp, ideal for remote or busy individuals.",
        "keywords": ["tele-therapy", "online", "video", "zoom"]
    },
    {
        "section": "Trauma Support",
        "answer": "Trauma Support uses EMDR and Trauma-Focused CBT in 60-minute sessions to help survivors of trauma recover and regain stability.",
        "keywords": ["trauma", "ptsd", "emdr", "support"]
    },
    {
        "section": "Team",
        "answer": "Our team includes Jerim Owino (Founder & CEO, specializing in trauma therapy and program development) and Hamdi Roble (Co-Founder, focusing on community outreach and culturally-sensitive care).",
        "keywords": ["team", "therapist", "jerim", "hamdi", "founder"]
    },
    {
        "section": "Testimonials",
        "answer": "Clients like Wanjiru M. (Nairobi) praise our culturally relevant anxiety support, David O. (Mombasa) values family counseling, Aisha K. (Kisumu) appreciates faith-sensitive therapy, and Samuel T. (Nakuru) benefits from trauma support.",
        "keywords": ["testimonials", "reviews", "clients", "feedback"]
    },
    {
        "section": "Resources",
        "answer": "Access free downloadable resources like the Breathing Exercise Guide, Journaling Prompts, and Mindfulness Audio Script to support your mental wellbeing.",
        "keywords": ["resources", "tools", "self-help", "guide", "download"]
    },
    {
        "section": "Success Stories",
        "answer": "Read anonymized success stories, such as a Nairobi client overcoming anxiety with CBT or a Mombasa family healing through counseling.",
        "keywords": ["success", "stories", "case", "transformation"]
    },
    {
        "section": "Events",
        "answer": "Join our upcoming events like the Stress Management Workshop on July 30, 2025, or the Understanding Trauma Webinar on August 5, 2025.",
        "keywords": ["events", "webinar", "workshop", "register"]
    },
    {
        "section": "Partnerships",
        "answer": "We collaborate with Kenya Red Cross for trauma support and Nairobi County Education Department for school workshops.",
        "keywords": ["partnerships", "collaborations", "partners"]
    },
    {
        "section": "FAQ - Cost",
        "answer": "Costs vary by service. Individual sessions start at KES 3,000, with discounts for packages. Contact us for a detailed quote.",
        "keywords": ["cost", "price", "fee", "charge"]
    },
    {
        "section": "FAQ - Confidentiality",
        "answer": "Yes, we adhere to strict confidentiality policies to protect your privacy, except in cases required by law.",
        "keywords": ["confidential", "privacy", "private", "secure"]
    },
    {
        "section": "FAQ - First Session",
        "answer": "Your first session involves discussing your goals and needs with a therapist to create a personalized plan.",
        "keywords": ["first session", "expect", "initial", "start"]
    },
    {
        "section": "FAQ - Languages",
        "answer": "Yes, our team provides counseling in English, Swahili, and other local languages upon request.",
        "keywords": ["language", "swahili", "english", "local"]
    },
    {
        "section": "FAQ - Preparation",
        "answer": "Reflect on your goals and bring any relevant notes or questions. Our team will guide you through the process.",
        "keywords": ["prepare", "preparation", "ready"]
    },
    {
        "section": "FAQ - Crisis",
        "answer": "Contact a trusted person or our helpline at +254 781 095 919. For emergencies, visit the nearest hospital.",
        "keywords": ["crisis", "emergency", "help"]
    },
    {
        "section": "FAQ - Insurance",
        "answer": "Currently, we operate on a private pay basis. Contact us to discuss payment options.",
        "keywords": ["insurance", "payment", "cost"]
    },
    {
        "section": "Contact",
        "answer": "Visit us at Greenhouse Plaza, Ngong Road, Nairobi. Call +254 781 095 919 or +254 720 987 654. Email info@safespacekenya.org or owinojerim269@gmail.com (CEO). Hours: Mon-Fri 8AM-7PM, Sat 9AM-4PM.",
        "keywords": ["contact", "location", "phone", "email", "hours", "nairobi"]
    },
    {
        "section": "Stress Management",
        "answer": "Manage stress with deep breathing (4-7-8 technique), physical activity (e.g., walking in Uhuru Park), community connection (e.g., chama groups), self-care (e.g., cooking ugali), or professional support like CBT at SafeSpace Kenya.",
        "keywords": ["stress", "manage stress", "relax", "calm"]
    },
    {
        "section": "Anxiety",
        "answer": "Anxiety signs include persistent worry, racing heart, or sleep issues. Cope with mindfulness (e.g., focus on chai’s smell), journaling, limiting caffeine, or professional help like CBT at SafeSpace Kenya.",
        "keywords": ["anxiety", "worry", "nervous", "cope"]
    },
    {
        "section": "Blog",
        "answer": "Check out our Mental Health Blog for articles like 'Coping with Stress During Economic Hardship' and 'Cultural Perspectives on Therapy' to gain insights and tips.",
        "keywords": ["blog", "articles", "tips", "insights"]
    },
    {
        "section": "Crisis Resources",
        "answer": "For immediate help, call Befrienders Kenya at 1199 or our helpline at +254 781 095 919. Visit a hospital in emergencies.",
        "keywords": ["crisis", "emergency", "helpline", "resources"]
    },
    {
        "section": "Community Forum",
        "answer": "Join our Community Forum for peer support, including a live Q&A on July 25, 2025, about coping with grief.",
        "keywords": ["forum", "community", "support", "q&a"]
    },
    {
        "section": "Progress Tracker",
        "answer": "Use our Progress Tracker to log your daily mood (1-5) and review your mental health journey over time.",
        "keywords": ["progress", "tracker", "mood", "journey"]
    },
    {
        "section": "Volunteer Opportunities",
        "answer": "Volunteer with us in roles like Outreach Support or Event Volunteer to support mental health initiatives.",
        "keywords": ["volunteer", "opportunities", "support", "roles"]
    }
]

st.markdown("""
<div class='chatbot-container'>
    <h4 style='margin: 0 0 1rem;'>Ask SafeSpace Bot</h4>
    <div style='max-height: 300px; overflow-y: auto; margin-bottom: 1rem;'>
""", unsafe_allow_html=True)

for sender, message in st.session_state.chat_history:
    st.markdown(
        f"<div class='chatbot-message {sender}'><p>{message}</p></div>",
        unsafe_allow_html=True
    )

st.markdown("</div>", unsafe_allow_html=True)
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("", placeholder="Ask about our services, team, or tips...", key="chat_input")
    submit = st.form_submit_button("Send")
    if submit and user_input:
        st.session_state.chat_history.append(("user", user_input))
        user_input_lower = user_input.lower()
        response = "I'm sorry, I don't understand your question. Please try rephrasing or visit our <a href='#contact'>Contact section</a> for more help."
        for item in knowledge_base:
            if any(keyword in user_input_lower for keyword in item["keywords"]):
                response = item["answer"]
                break
        st.session_state.chat_history.append(("bot", response))
st.markdown("</div>", unsafe_allow_html=True)

# FOOTER
st.markdown("---")
st.markdown("""
<div class='footer'>
    <p style='font-size: 1rem;'>© 2023 SafeSpace Kenya | Designed with ❤️ for mental wellness</p>
    <div style='display: flex; justify-content: center; gap: 1.5rem; margin: 1.5rem 0;'>
        <a href='https://facebook.com' target='_blank' class='primary-btn'>🌐 Facebook</a>
        <a href='https://instagram.com' target='_blank' class='primary-btn'>📷 Instagram</a>
        <a href='https://twitter.com' target='_blank' class='primary-btn'>🐦 Twitter</a>
        <a href='https://linkedin.com' target='_blank' class='primary-btn'>💼 LinkedIn</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Newsletter Subscription Form
with st.form("newsletter_form", clear_on_submit=True):
    st.markdown("<div style='max-width: 500px; margin: 1rem auto; display: flex; gap: 0.5rem;'>", unsafe_allow_html=True)
    newsletter_email = st.text_input("", placeholder="Subscribe to our newsletter", key="newsletter_email")
    submit_newsletter = st.form_submit_button("Subscribe")
    st.markdown("</div>", unsafe_allow_html=True)
    if submit_newsletter:
        if not newsletter_email or not re.match(r"[^@]+@[^@]+\.[^@]+", newsletter_email):
            st.error("Please provide a valid email address.")
        else:
            st.session_state.newsletter_submitted = True
            st.success("Thank you for subscribing to our newsletter!")
