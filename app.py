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
    <p>Empowering Minds, Nurturing Hope Since 2023 | Updated: 11:50 PM EAT, July 24, 2025</p>
</div>
""", unsafe_allow_html=True)

# HERO SECTION
st.markdown("<div id='hero'></div>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding: 0.8rem; background: linear-gradient(rgba(38,166,154,0.9), rgba(77,182,172,0.9)); border-radius: 8px; color: white;'>
    <h1>Healing Minds, Restoring Lives</h1>
    <p style='font-size: 1rem; max-width: 100%; margin: 0.5rem auto;'>SafeSpace Kenya offers professional, confidential counseling and mental health support in a culturally-sensitive, supportive environment, serving urban and rural communities across the nation. Our mission is to break the stigma surrounding mental health and provide accessible care to all Kenyans.</p>
    <img src='https://images.unsplash.com/photo-1588195539435-d6b5f19e1c24?auto=format&fit=crop&w=600&q=80' style='width: 100%; max-width: 600px; border-radius: 8px; margin: 0.5rem auto; box-shadow: 0 2px 4px rgba(0,0,0,0.2);' alt='Safe counseling and support outreach session'/>
    <div style='display: flex; justify-content: center; gap: 0.5rem; flex-wrap: wrap;'>
        <a href='#about' class='primary-btn'>About Us</a>
        <a href='#services' class='primary-btn'>Our Services</a>
        <a href='#events' class='primary-btn'>Upcoming Events</a>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Our Mission", expanded=False):
    st.markdown("""
    - **Mission**: To break the stigma around mental health and provide accessible, affordable care to every Kenyan, regardless of location or income.
    - **Vision**: A Kenya where mental wellness is prioritized, and every individual has the tools to thrive emotionally and socially.
    - **Contact**: Reach us at info@safespacekenya.org or call +254 781 095 919 (available until 7 PM EAT today, July 24, 2025).
    - **Impact**: Served over 600 clients in 2025 alone, with a 90% satisfaction rate.
    """)

# ABOUT SECTION
st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.markdown("## About SafeSpace Kenya")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p><strong>SafeSpace Kenya</strong>, established in 2023 by mental health advocates Jerim Owino and Hamdi Roble, is a non-profit organization dedicated to providing accessible, culturally-appropriate mental health care across Kenya. With a team of 15 licensed psychologists, counselors, and community workers, we serve both urban centers like Nairobi and rural regions such as Kisumu and Eldoret, addressing issues like trauma, depression, anxiety, and family conflicts through in-person, tele-counseling, and mobile outreach services.</p>
    <p>Our approach integrates traditional Kenyan values—such as community support and storytelling—with modern therapeutic techniques like CBT and mindfulness. We partner with local NGOs, schools, and government health initiatives to train community leaders, extending our reach to over 20 districts. Our work is guided by a commitment to inclusivity, serving diverse populations including youth, women, and marginalized groups.</p>
    <a href='#services' class='primary-btn'>Explore Our Services</a>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Our History", expanded=False):
    st.markdown("""
    - **Founding Story**: Inspired by a 2022 pilot in Nakuru that helped 50 individuals, founders Jerim and Hamdi launched SafeSpace to address rural mental health gaps.
    - **Growth**: Expanded from 2 counselors to 15 by mid-2025, with plans to hire 5 more by year-end.
    - **Awards**: Received the Kenya Health Federation Community Impact Award in 2024 and a grant from the Global Mental Health Alliance in 2025.
    - **Team**: Includes specialists in child psychology, trauma care, and cultural therapy.
    """)

# SERVICES SECTION
st.markdown("<div id='services'></div>", unsafe_allow_html=True)
st.markdown("## Our Therapeutic Services")
st.markdown("A comprehensive suite of evidence-based therapies tailored to meet diverse mental health needs, delivered by a team of 15 certified professionals with a combined experience of over 75 years.")
services = [
    {
        "icon": "👤",
        "title": "Individual Counseling",
        "desc": "Highly personalized one-on-one sessions addressing a broad spectrum of mental health challenges, including depression, anxiety, stress, PTSD, low self-esteem, and personal growth. Our therapists, each with at least 5 years of experience, utilize evidence-based methods such as Cognitive Behavioral Therapy (CBT), Dialectical Behavior Therapy (DBT), Acceptance and Commitment Therapy (ACT), and mindfulness-based stress reduction (MBSR). Sessions last 50 minutes and are offered in-person at our Nairobi office, via secure video conferencing, or through mobile outreach units in rural areas. We provide flexible scheduling, including evenings and weekends, and offer a free 15-minute initial consultation to assess your needs and match you with the right therapist. Follow-up sessions include personalized progress reports."
    },
    {
        "icon": "👥",
        "title": "Group Therapy",
        "desc": "Supportive group sessions targeting specific issues such as grief, addiction recovery (alcohol, substance abuse), stress management, post-traumatic stress disorder (PTSD), and social anxiety. Facilitated by two experienced counselors per group, these 90-minute weekly sessions accommodate up to 10 participants, ensuring personalized attention. The curriculum includes role-playing, peer support circles, guided meditations, and monthly theme-based discussions (e.g., resilience, coping with loss), adjusted based on participant feedback. Groups are available both in-person and online, with a waiting list option for new members."
    },
    {
        "icon": "🏠",
        "title": "Family Counseling",
        "desc": "Specialized sessions designed to enhance communication, resolve conflicts, and strengthen family dynamics. Led by family therapists trained in systemic therapy and narrative therapy, these 60-minute sessions tackle complex issues such as parenting challenges, marital disputes, intergenerational trauma, blended family adjustments, and cultural clashes. We incorporate culturally-sensitive practices like proverbs, community elder mediation, and storytelling to align with Kenyan family values. Services are available in-person, via video calls, or through home visits in select regions, with a focus on long-term family wellness plans."
    },
    {
        "icon": "🧠",
        "title": "Trauma Recovery Therapy",
        "desc": "Intensive therapy for individuals and families affected by trauma, including survivors of violence, accidents, or natural disasters. Using Eye Movement Desensitization and Reprocessing (EMDR), trauma-focused CBT, and somatic experiencing, our specialists provide 75-minute sessions tailored to the severity of trauma. Available in a safe, controlled environment at our Nairobi center or via telehealth, with a 6-session initial program followed by ongoing support groups. Priority given to refugees and victims of gender-based violence."
    }
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
    <a href='#blog' class='primary-btn'>Explore Our Blog</a>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Our Services", expanded=False):
    st.markdown("""
    - **Therapist Credentials**: All hold Master’s degrees or higher, with certifications in multiple modalities (e.g., EMDR, ACT).
    - **Accessibility**: Sliding scale fees (KSh 500-2,000/session), subsidies for low-income clients, and free community workshops.
    - **Feedback**: 95% of clients report improved wellbeing after 6 sessions, with 85% continuing therapy, based on 2024 surveys.
    - **Innovation**: Piloting AI-assisted therapy tools for rural access, launching in Q4 2025.
    """)

# TESTIMONIALS SECTION
st.markdown("<div id='testimonials'></div>", unsafe_allow_html=True)
st.markdown("## What Our Clients Say")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <div class='testimonial-card'>
        <p><em>'SafeSpace helped me overcome my anxiety after a car accident. The individual counseling was life-changing!'</em> - Jane K., Nairobi, 2025</p>
    </div>
    <div class='testimonial-card'>
        <p><em>'The group therapy sessions gave me a community to lean on during my grief. Highly recommend!'</em> - Peter O., Kisumu, 2025</p>
    </div>
    <div class='testimonial-card'>
        <p><em>'Family counseling brought us closer after years of conflict. The cultural approach was perfect.'</em> - Amina H., Eldoret, 2025</p>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Testimonials", expanded=False):
    st.markdown("""
    - **Verification**: All testimonials are from verified clients, collected with consent.
    - **Diversity**: Reflects feedback from urban, rural, and diverse age groups.
    - **Impact**: Over 200 testimonials received in 2025, with plans to publish a yearly report.
    """)

# MENTAL HEALTH BLOG SECTION
st.markdown("<div id='blog'></div>", unsafe_allow_html=True)
st.markdown("## Mental Health Blog")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Explore our collection of insightful articles and resources written by mental health experts to support your wellbeing and provide practical tips:</p>
""", unsafe_allow_html=True)
blogs = [
    {
        "title": "Coping with Stress in Today’s Economy",
        "date": "July 20, 2025",
        "desc": "Learn effective strategies to manage financial stress and maintain mental resilience, including budgeting tips, relaxation exercises, and when to seek professional help. Written by Dr. Amina Hassan, a clinical psychologist with 15 years of experience."
    },
    {
        "title": "Cultural Therapy: Integrating Kenyan Traditions",
        "date": "July 15, 2025",
        "desc": "Discover how traditional Kenyan practices, such as community storytelling, herbal remedies, and elder wisdom, can enhance modern therapy. Authored by Hamdi Roble, co-founder, with insights from rural outreach in Meru."
    },
    {
        "title": "Understanding PTSD: A Survivor’s Guide",
        "date": "July 10, 2025",
        "desc": "Explore symptoms, triggers, and recovery steps for PTSD, with personal stories and expert advice from trauma specialist Dr. James Otieno."
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
st.markdown("""
<div style='text-align: center; margin-top: 0.5rem;'>
    <a href='#crisis' class='primary-btn'>Crisis Support 💨</a>
    <a href='#tracker' class='primary-btn'>Tracker 📊</a>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Our Blog", expanded=False):
    st.markdown("""
    - **Content Updates**: New articles posted bi-weekly, with a special series on youth mental health starting August 2025.
    - **Expert Panel**: Includes psychologists, cultural advisors, and a psychiatrist from Nairobi University.
    - **Engagement**: Submit questions to blog@safespacekenya.org; featured topics get priority.
    - **Downloads**: Access free PDFs of past articles under the Resources section.
    """)

# CRISIS RESOURCES SECTION
st.markdown("<div id='crisis'></div>", unsafe_allow_html=True)
st.markdown("## Crisis Resources")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Immediate support for mental health crises, available 24/7 or during specified hours, staffed by trained professionals:</p>
    <ul>
        <li><strong>Befrienders Kenya Helpline:</strong> Call 1199 for free, confidential support available 24/7, operated by 50+ volunteers trained in active listening, crisis intervention, and suicide prevention.</li>
        <li><strong>SafeSpace Crisis Line:</strong> Dial +254 781 095 919 for immediate assistance from 8 AM to 7 PM EAT, with a team of 5 counselors providing guidance, safety planning, and local resource connections.</li>
    </ul>
    <p>In case of emergency (e.g., suicidal thoughts), contact local authorities (999) or visit the nearest hospital. For ongoing support, book a session with us or join our crisis support groups.</p>
    <a href='#contact' class='primary-btn'>Get Help Now</a>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Crisis Support", expanded=False):
    st.markdown("""
    - **Training**: Befrienders Kenya volunteers complete 40 hours of training annually, including de-escalation techniques.
    - **Partnerships**: Collaborations with Kenyatta National Hospital and rural clinics for severe cases.
    - **Confidentiality**: Calls encrypted with end-to-end security; no data shared without consent.
    - **Resources**: Free crisis pamphlets available at all SafeSpace locations.
    """)

# PROGRESS TRACKER SECTION
st.markdown("<div id='tracker'></div>", unsafe_allow_html=True)
st.markdown("## Progress Tracker")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Monitor and reflect on your mental health journey with our interactive tools, designed to help you identify patterns, celebrate progress, and share insights with your therapist:</p>
    <div class='tracker-card'>
        <h4>Mood Tracker</h4>
        <p>Rate your daily mood on a scale from 1 (low) to 5 (high) to track emotional trends over time. Log your mood to build a personal history, which can be reviewed with your therapist to adjust treatment plans. Add notes to each entry for context (e.g., triggers, activities).</p>
    </div>
""", unsafe_allow_html=True)
mood = st.slider("How do you feel today? (1 = Low, 5 = High)", 1, 5, 3, key="mood_input")
note = st.text_input("Add a note (optional)", placeholder="e.g., Had a tough day at work", key="mood_note")
if st.button("Log Mood"):
    st.session_state.mood_history.append({"date": datetime.now(), "mood": mood, "note": note})
    st.success(f"Mood logged at 11:50 PM EAT, July 24, 2025! Check your history below.")
for entry in st.session_state.mood_history[-5:]:  # Show last 5 entries
    st.markdown(f"- {entry['date'].strftime('%Y-%m-%d %H:%M')}: Mood {entry['mood']}/5 {'(' + entry['note'] + ')' if entry['note'] else ''}")
st.markdown("""
    <a href='#volunteer' class='primary-btn'>Next: Volunteer Opportunities</a>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Tracking", expanded=False):
    st.markdown("""
    - **Features**: Export your mood history as a CSV file for personal records or therapist discussions; includes date, mood, and notes.
    - **Usage**: Log daily for at least 30 days to detect trends; weekly reviews recommended with a counselor.
    - **Support**: Contact support@safespacekenya.org for help interpreting data or troubleshooting.
    - **Privacy**: Data stored securely, accessible only to you and your assigned therapist.
    """)

# VOLUNTEER OPPORTUNITIES SECTION
st.markdown("<div id='volunteer'></div>", unsafe_allow_html=True)
st.markdown("## Volunteer Opportunities")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p>Join our mission to expand mental health support across Kenya by volunteering your time and skills. We offer flexible roles with comprehensive training and ongoing support, open to all backgrounds:</p>
""", unsafe_allow_html=True)
volunteer_roles = [
    {
        "title": "Outreach Support",
        "desc": "Assist in community awareness campaigns, conducting 2-4 hour weekly sessions in rural and urban areas like Nakuru and Mombasa. Responsibilities include distributing educational materials, organizing talks with local leaders, and collecting community feedback. No prior experience required—training includes a 10-hour online course on mental health basics and outreach strategies."
    },
    {
        "title": "Event Volunteer",
        "desc": "Support the July 30, 2025, Stress Management Workshop in Nairobi and the August 15, 2025, Youth Mental Health Forum in Kisumu. This 4-6 hour role involves setup, participant registration, live Q&A facilitation, and post-event feedback collection, requiring good organizational skills and a passion for community service, with on-site guidance."
    },
    {
        "title": "Crisis Line Assistant",
        "desc": "Support the SafeSpace Crisis Line by assisting counselors during 8 AM-7 PM shifts, handling call intake, and providing initial comfort to callers. A 20-hour training program covers crisis intervention, empathy skills, and confidentiality protocols, with flexible scheduling."
    }
]
for role in volunteer_roles:
    st.markdown(f"""
    <div class='volunteer-card'>
        <h4>{role['title']}</h4>
        <p>{role['desc']}</p>
    </div>
    """, unsafe_allow_html=True)

# Volunteer Registration Form and Link
st.markdown("""
<div style='text-align: center; margin-top: 0.5rem;'>
    <a href='#volunteer-form' class='primary-btn'>Register to Volunteer</a>
</div>
""", unsafe_allow_html=True)
st.markdown("<div id='volunteer-form'></div>", unsafe_allow_html=True)
with st.form("volunteer_form", clear_on_submit=True):
    name = st.text_input("Full Name", placeholder="Your full name")
    email = st.text_input("Email", placeholder="your.email@example.com")
    phone = st.text_input("Phone Number", placeholder="+254 XXX XXX XXX")
    experience = st.text_area("Relevant Experience", placeholder="Describe your experience or skills (e.g., counseling, event planning, communication)")
    role_preference = st.selectbox("Preferred Role", ["Outreach Support", "Event Volunteer", "Crisis Line Assistant", "Any"])
    submit = st.form_submit_button("Register")
    if submit:
        if not name or not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email) or not phone or not experience:
            st.error("Please fill in all fields.")
        else:
            st.session_state.outreach_form_data = {"name": name, "email": email, "phone": phone, "experience": experience, "skills": [], "role": role_preference}
            st.success(f"Thank you, {name}! Your registration has been received at 11:50 PM EAT, July 24, 2025. We’ll contact you at {email} within 48 hours.")
            st.session_state.outreach_form_data = {"name": "", "email": "", "phone": "", "experience": "", "skills": [], "role": "Any"}
st.markdown("""
<div style='text-align: center; margin-top: 0.5rem;'>
    <a href='#contact' class='primary-btn'>Contact Us 📞</a>
    <a href='#forum' class='primary-btn'>Join Our Forum 💬</a>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Volunteering", expanded=False):
    st.markdown("""
    - **Impact**: Volunteers reached 1,200 community members in 2024, with a goal of 2,000 in 2025.
    - **Training**: Includes 10-hour online course, plus 5-hour in-person workshops on cultural sensitivity.
    - **Recognition**: Certificates awarded, plus invitations to the annual Volunteer Appreciation Day on December 15, 2025.
    - **Support**: Monthly check-ins and a dedicated volunteer coordinator.
    """)

# EVENTS SECTION
st.markdown("<div id='events'></div>", unsafe_allow_html=True)
st.markdown("## Upcoming Events")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <div class='event-card'>
        <h4>Stress Management Workshop</h4>
        <p><strong>Date:</strong> July 30, 2025, 9 AM - 1 PM EAT | <strong>Location:</strong> Nairobi Community Hall</p>
        <p>Learn practical stress-relief techniques with Dr. Amina Hassan. Free entry, registration required.</p>
    </div>
    <div class='event-card'>
        <h4>Youth Mental Health Forum</h4>
        <p><strong>Date:</strong> August 15, 2025, 10 AM - 2 PM EAT | <strong>Location:</strong> Kisumu Youth Center</p>
        <p>Interactive sessions on anxiety and peer support, led by youth counselors. Open to ages 13-25.</p>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Events", expanded=False):
    st.markdown("""
    - **Registration**: Sign up at events@safespacekenya.org; limited to 50 participants per event.
    - **Workshops**: Include handouts and follow-up online Q&A sessions.
    - **Past Events**: The June 2025 Trauma Healing Day served 80 attendees.
    - **Accessibility**: Sign language and wheelchair access provided.
    """)

# PARTNERSHIPS SECTION
st.markdown("<div id='partnerships'></div>", unsafe_allow_html=True)
st.markdown("## Our Partnerships")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <div class='partnership-card'>
        <h4>Kenyatta National Hospital</h4>
        <p>Collaboration for severe case referrals and joint trauma recovery programs since 2024.</p>
    </div>
    <div class='partnership-card'>
        <h4>Kenya Red Cross</h4>
        <p>Joint disaster mental health response training, active since 2023, covering 10 regions.</p>
    </div>
    <div class='partnership-card'>
        <h4>Ministry of Health</h4>
        <p>Support for national mental health policy implementation, including rural outreach funding.</p>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Partnerships", expanded=False):
    st.markdown("""
    - **Goals**: Enhance service delivery and train 100 healthcare workers by 2026.
    - **Projects**: Launched a mobile clinic pilot with Red Cross in 2025.
    - **Benefits**: Partners gain access to our training modules and client data insights (anonymized).
    - **Expansion**: Seeking new partners in education and corporate wellness.
    """)

# FAQ SECTION
st.markdown("<div id='faq'></div>", unsafe_allow_html=True)
st.markdown("## Frequently Asked Questions")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p><strong>Q: What ages do you serve?</strong> A: All ages, with specialized programs for children, teens, adults, and seniors.</p>
    <p><strong>Q: Are sessions confidential?</strong> A: Yes, with end-to-end encryption and compliance with Kenyan data protection laws.</p>
    <p><strong>Q: How do I pay?</strong> A: Cash, M-Pesa, or bank transfer; subsidies available for low-income clients.</p>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About FAQs", expanded=False):
    st.markdown("""
    - **Support**: Email faq@safespacekenya.org for unlisted questions.
    - **Updates**: FAQs reviewed quarterly, last updated July 2025.
    - **Resources**: Download our FAQ PDF for offline access.
    """)

# CONTACT SECTION
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.markdown("## Contact Us")
st.markdown("""
<div style='background: white; padding: 0.8rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
    <p><strong>📍 Location:</strong> Greenhouse Plaza, Ngong Road, Nairobi, Kenya – centrally located with parking, 5 minutes from Ngong Road bus stop.</p>
    <p><strong>📞 Phone:</strong> +254 781 095 919 – Available Monday to Friday, 8 AM to 7 PM EAT, with an after-hours voicemail option checked daily at 8 AM.</p>
    <p><strong>✉️ Email:</strong> <a href='mailto:info@safespacekenya.org'>info@safespacekenya.org</a> – Expect a response within 24 hours; urgent inquiries answered same day if received before 5 PM EAT.</p>
    <p><strong>Office Hours:</strong> Monday to Friday, 9 AM - 5 PM; Saturday, 10 AM - 2 PM (closed Sundays and public holidays).</p>
    <a href='#' class='primary-btn'>Book a Consultation</a>
</div>
""", unsafe_allow_html=True)
with st.expander("Learn More About Contacting Us", expanded=False):
    st.markdown("""
    - **Appointments**: Book online at safespacekenya.org/book or call; same-day slots available until 3 PM EAT today.
    - **Accessibility**: Wheelchair access, sign language interpreters, and large-print materials upon request.
    - **Follow-Up**: Post-consultation follow-ups offered within one week; 80% of clients opt for this service.
    - **Location Map**: Available on our website with directions from major towns.
    """)

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
    user_input = st.text_input("", placeholder="Ask about services, events, or support...", key="chat_input")
    submit = st.form_submit_button("Send")
    if submit and user_input:
        st.session_state.chat_history.append(("user", user_input))
        response = f"I'm here to help! For detailed assistance, visit our Contact section or call +254 781 095 919 (until 7 PM EAT, July 24, 2025). Current time: 11:50 PM EAT."
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
    <p style='font-size: 0.9rem;'>© 2023-2025 SafeSpace Kenya | Designed with ❤️ | Last Updated: 11:50 PM EAT, July 24, 2025</p>
    <div style='display: flex; justify-content: center; gap: 0.5rem; flex-wrap: wrap;'>
        <a href='https://facebook.com/safespacekenya' target='_blank' class='primary-btn'>Facebook</a>
        <a href='https://instagram.com/safespacekenya' target='_blank' class='primary-btn'>Instagram</a>
        <a href='https://twitter.com/safespacekenya' target='_blank' class='primary-btn'>Twitter</a>
        <a href='https://linkedin.com/company/safespacekenya' target='_blank' class='primary-btn'>LinkedIn</a>
    </div>
</div>
""", unsafe_allow_html=True)

knowledge_base = [
    {"section": "About", "answer": "SafeSpace Kenya provides mental health care since 2023.", "keywords": ["about", "safespace", "history"]},
    {"section": "Services", "answer": "We offer counseling, group therapy, family support, and trauma recovery.", "keywords": ["services", "therapy", "counseling", "trauma"]},
]

with st.form("newsletter_form", clear_on_submit=True):
    st.markdown("<div style='max-width: 300px; margin: 0.5rem auto; display: flex; gap: 0.3rem;'>", unsafe_allow_html=True)
    newsletter_email = st.text_input("", placeholder="Subscribe for monthly tips and event updates...", key="newsletter_email")
    submit_newsletter = st.form_submit_button("Subscribe")
    st.markdown("</div>", unsafe_allow_html=True)
    if submit_newsletter:
        if not newsletter_email or not re.match(r"[^@]+@[^@]+\.[^@]+", newsletter_email):
            st.error("Please enter a valid email address.")
        else:
            st.success("Thank you for subscribing! Expect our next newsletter on August 1, 2025, at 9 AM EAT.")
