import streamlit as st
from datetime import datetime
import re

# Custom CSS for enhanced styling
st.markdown("""
<style>
    :root {
        --primary: #2a7a7c;
        --accent: #d4a373;
        --light: #f8f9fa;
        --dark: #2c3e50;
    }
    .stApp {
        background-color: var(--light);
        background-image: url('https://www.transparenttextures.com/patterns/subtle-white-feathers.png');
        font-family: 'Inter', sans-serif;
        color: var(--dark);
    }
    h1, h2, h3, h4 {
        font-family: 'Playfair Display', serif;
        color: var(--primary) !important;
        text-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }
    h1 { font-size: 2.8rem; }
    h2 { font-size: 2.2rem; }
    h3 { font-size: 1.8rem; }
    .service-card, .team-card, .testimonial-card, .cta-banner, .insights-content {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-bottom: 1.5rem;
    }
    .service-card:hover, .team-card:hover, .testimonial-card:hover {
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
        background: linear-gradient(135deg, var(--primary), var(--accent));
        color: white;
        text-align: center;
        padding: 3rem;
    }
    html {
        scroll-behavior: smooth;
    }
    @media (max-width: 768px) {
        .stColumn {
            margin-bottom: 1rem;
        }
        .service-card, .team-card, .testimonial-card, .insights-content {
            margin: 0.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="SafeSpace Kenya",
    page_icon="🧠",
    layout="wide",
)

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
        "bio": "Founder and CEO with extensive experience in mental health advocacy and trauma therapy.",
        "img": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Hamdi Roble",
        "role": "Co-Founder",
        "bio": "Co-Founder passionate about culturally-sensitive mental health care and community outreach.",
        "img": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Yvone Orina",
        "role": "Family Therapist",
        "bio": "Focuses on family therapy and relationship counseling.",
        "img": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Brian Kiprop",
        "role": "Art Therapist",
        "bio": "Helps clients express feelings through creative art and movement.",
        "img": "https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&w=400&q=80"
    }
]

cols = st.columns(4)
for i, member in enumerate(team):
    with cols[i]:
        st.markdown(f"""
        <div class='team-card'>
            <img src='{member["img"]}' style='width: 100%; border-radius: 10px; margin-bottom: 1rem;' alt='{member["name"]}'>
            <h4>{member['name']}</h4>
            <p style='color: var(--accent); font-style: italic;'>{member['role']}</p>
            <p>{member['bio']}</p>
        </div>
        """, unsafe_allow_html=True)

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

# FAQ SECTION
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
        # Show service description when selected
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
