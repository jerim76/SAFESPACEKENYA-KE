import streamlit as st
from streamlit_extras.card import card
from streamlit_extras.colored_header import colored_header
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Safe Space Kenya",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
<style>
    :root {
        --primary: #2a7a7c;
        --secondary: #4a9ca5;
        --accent: #d4a373;
        --light: #f8f9fa;
        --dark: #2c3e50;
    }
    
    .stApp {
        background-color: #fafafa;
        color: #333;
        font-family: 'Nunito', sans-serif;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Playfair Display', serif;
        color: var(--primary) !important;
    }
    
    .primary-btn {
        background-color: var(--primary) !important;
        color: white !important;
        border-radius: 30px !important;
        padding: 0.5rem 1.5rem !important;
        font-weight: 600 !important;
        border: none !important;
        transition: all 0.3s ease !important;
    }
    
    .primary-btn:hover {
        background-color: var(--accent) !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
    }
    
    .outline-btn {
        background-color: transparent !important;
        border: 2px solid var(--primary) !important;
        color: var(--primary) !important;
        border-radius: 30px !important;
        padding: 0.5rem 1.5rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    
    .outline-btn:hover {
        background-color: var(--primary) !important;
        color: white !important;
    }
    
    .service-card {
        border-radius: 10px;
        padding: 1.5rem;
        background: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        border-top: 4px solid var(--secondary);
        height: 100%;
    }
    
    .service-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    
    .team-card {
        border-radius: 10px;
        padding: 1.5rem;
        background: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        position: relative;
        overflow: hidden;
        height: 100%;
    }
    
    .team-card::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 5px;
        background-color: var(--accent);
    }
    
    .contact-item {
        display: flex;
        gap: 15px;
        align-items: flex-start;
        margin-bottom: 1.5rem;
    }
    
    .contact-icon {
        background: #e8f4f8;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--primary);
        font-size: 1.2rem;
        flex-shrink: 0;
    }
</style>
""", unsafe_allow_html=True)

# Team data
team_data = [
    {"name": "Jerim Owino", "role": "Founder & CEO", "bio": "Clinical psychologist specializing in trauma therapy with 12 years of experience."},
    {"name": "Hamdi Roble", "role": "Senior Therapist", "bio": "Expert in cognitive behavioral therapy with focus on anxiety and depression."},
    {"name": "Yvone Orina", "role": "Family Therapist", "bio": "Specializes in family systems therapy and relationship counseling."},
    {"name": "Brian Kiprop", "role": "Art Therapist", "bio": "Uses creative approaches to help clients express emotions."}
]

# Services data
services_data = [
    {"title": "Individual Counseling", "icon": "👤", "description": "Personalized sessions addressing mental health concerns and personal growth."},
    {"title": "Group Therapy", "icon": "👥", "description": "Supportive group sessions fostering connection and shared healing."},
    {"title": "Family Counseling", "icon": "🏠", "description": "Strengthening family bonds and improving communication."},
    {"title": "Workshops & Training", "icon": "🎓", "description": "Educational programs on mental wellness for organizations."},
    {"title": "Tele-therapy", "icon": "📱", "description": "Secure online counseling for convenient access."},
    {"title": "Trauma Support", "icon": "❤️", "description": "Specialized therapy for healing from traumatic experiences."}
]

# Home Page
def home_page():
    colored_header(
        label="",
        description="",
        color_name="blue-70"
    )
    
    # Hero Section
    st.markdown("""
    <div style="background: linear-gradient(rgba(42, 122, 124, 0.85), rgba(42, 122, 124, 0.9)); 
                border-radius: 10px; 
                padding: 4rem 2rem; 
                text-align: center;
                color: white;
                margin-bottom: 3rem;">
        <h1 style="color: white !important; font-size: 3rem;">Healing Minds, Restoring Lives</h1>
        <p style="font-size: 1.2rem; max-width: 800px; margin: 0 auto 2rem;">
            Safe Space Kenya provides professional, confidential counseling and mental health services in a supportive environment.
        </p>
        <div style="display: flex; justify-content: center; gap: 20px; margin-top: 2rem;">
            <a href="#contact" class="primary-btn" style="text-decoration: none;">Book a Session</a>
            <a href="#services" class="outline-btn" style="text-decoration: none;">Our Services</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # About Section
    st.header("About Safe Space Kenya")
    st.markdown("""
    <div style="display: flex; gap: 2rem; align-items: center; margin-bottom: 3rem;">
        <div style="flex: 1;">
            <p>Founded in <strong>2023</strong>, Safe Space Kenya is dedicated to providing accessible mental health services to individuals and communities across Kenya.</p>
            <p>We believe that everyone deserves a safe, non-judgmental environment to explore their thoughts and emotions.</p>
            <p>Our team of licensed therapists brings diverse expertise and a commitment to cultural sensitivity.</p>
            <button class="primary-btn">Meet Our Team</button>
        </div>
        <div style="flex: 1; background: linear-gradient(135deg, #4a9ca5 0%, #2a7a7c 100%); 
                    border-radius: 10px; height: 300px; display: flex; 
                    align-items: center; justify-content: center; color: white; font-size: 3rem;">
            ❤️
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Services Section
    st.header("Our Therapeutic Services", anchor="services")
    st.markdown("We offer a range of evidence-based therapies tailored to meet your individual needs.")
    
    # Create columns for services
    cols = st.columns(3)
    for i, service in enumerate(services_data):
        with cols[i % 3]:
            with st.expander(f"{service['icon']} {service['title']}", expanded=True):
                st.markdown(f"""
                <div class="service-card">
                    <div style="font-size: 3rem; text-align: center; margin-bottom: 1rem;">
                        {service['icon']}
                    </div>
                    <h3>{service['title']}</h3>
                    <p>{service['description']}</p>
                    <button class="outline-btn" style="margin-top: 1rem;">Learn More</button>
                </div>
                """, unsafe_allow_html=True)
    
    # Team Section
    st.header("Our Professional Team")
    st.markdown("Meet our dedicated therapists committed to your mental wellness journey.")
    
    team_cols = st.columns(4)
    for i, member in enumerate(team_data):
        with team_cols[i]:
            st.markdown(f"""
            <div class="team-card">
                <div style="background-color: #e8f4f8; width: 120px; height: 120px; border-radius: 50%; 
                            margin: 0 auto 1rem; display: flex; align-items: center; justify-content: center; 
                            font-size: 2rem; color: #2a7a7c; border: 3px solid #4a9ca5;">
                    👤
                </div>
                <h3>{member['name']}</h3>
                <p style="color: #d4a373; font-weight: 600; font-style: italic;">{member['role']}</p>
                <p>{member['bio']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Testimonials
    st.header("Client Testimonials")
    st.markdown("Hear what others have to say about their healing journey with us.")
    
    testimonial_cols = st.columns(2)
    with testimonial_cols[0]:
        card(
            title="Wanjiru M., Nairobi",
            text='"Safe Space Kenya provided me with the tools to manage my anxiety in a way that respected my cultural background."',
            image="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80",
            styles={
                "card": {
                    "width": "100%",
                    "height": "300px",
                    "border-radius": "10px",
                    "box-shadow": "0 4px 6px rgba(0,0,0,0.1)"
                }
            }
        )
    
    with testimonial_cols[1]:
        card(
            title="David O., Mombasa",
            text='"The family counseling sessions helped us rebuild communication after a difficult period. Our family is stronger now."',
            image="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80",
            styles={
                "card": {
                    "width": "100%",
                    "height": "300px",
                    "border-radius": "10px",
                    "box-shadow": "0 4px 6px rgba(0,0,0,0.1)"
                }
            }
        )
    
    # Contact Section
    st.header("Contact Us", anchor="contact")
    st.markdown("Reach out to schedule an appointment or ask questions about our services.")
    
    contact_cols = st.columns(2)
    with contact_cols[0]:
        st.markdown("""
        <div>
            <div class="contact-item">
                <div class="contact-icon">
                    📍
                </div>
                <div>
                    <h4>Our Location</h4>
                    <p>Greenhouse Plaza, 3rd Floor<br>Ngong Road, Nairobi, Kenya</p>
                </div>
            </div>
            
            <div class="contact-item">
                <div class="contact-icon">
                    📞
                </div>
                <div>
                    <h4>Phone Number</h4>
                    <p>+254 781 095 919<br>+254 720 987 654</p>
                </div>
            </div>
            
            <div class="contact-item">
                <div class="contact-icon">
                    ✉️
                </div>
                <div>
                    <h4>Email Address</h4>
                    <p>info@safespacekenya.org<br>jerimowino679@gmail.com (CEO)</p>
                </div>
            </div>
            
            <div class="contact-item">
                <div class="contact-icon">
                    🕒
                </div>
                <div>
                    <h4>Working Hours</h4>
                    <p>Monday - Friday: 8:00 AM - 7:00 PM<br>Saturday: 9:00 AM - 4:00 PM</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with contact_cols[1]:
        with st.form("appointment_form"):
            st.subheader("Book an Appointment")
            name = st.text_input("Full Name", placeholder="Your full name")
            email = st.text_input("Email Address", placeholder="Your email")
            phone = st.text_input("Phone Number", placeholder="+254 XXX XXX XXX")
            
            service_options = [
                "Individual Counseling",
                "Group Therapy",
                "Family Counseling",
                "Workshops & Training",
                "Tele-therapy",
                "Trauma Support"
            ]
            service = st.selectbox("Service Interested In", service_options)
            
            preferred_date = st.date_input("Preferred Date", min_value=datetime.today())
            message = st.text_area("Your Message", placeholder="Briefly describe what you'd like to discuss")
            
            submitted = st.form_submit_button("Submit Appointment Request", type="primary")
            if submitted:
                st.success("Thank you for your appointment request! We'll contact you shortly to confirm your session.")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; margin-bottom: 2rem;">
        <div>
            <h4>Safe Space Kenya</h4>
            <p>Providing professional, confidential counseling and mental health services since 2023.</p>
            <div style="display: flex; gap: 15px; margin-top: 1rem;">
                <div style="width: 40px; height: 40px; border-radius: 50%; background: #e8f4f8; display: flex; align-items: center; justify-content: center;">f</div>
                <div style="width: 40px; height: 40px; border-radius: 50%; background: #e8f4f8; display: flex; align-items: center; justify-content: center;">t</div>
                <div style="width: 40px; height: 40px; border-radius: 50%; background: #e8f4f8; display: flex; align-items: center; justify-content: center;">in</div>
            </div>
        </div>
        
        <div>
            <h4>Quick Links</h4>
            <p>Home</p>
            <p>Services</p>
            <p>About Us</p>
            <p>Our Team</p>
            <p>Contact</p>
        </div>
        
        <div>
            <h4>Our Services</h4>
            <p>Individual Counseling</p>
            <p>Group Therapy</p>
            <p>Family Counseling</p>
            <p>Workshops & Training</p>
            <p>Tele-therapy</p>
        </div>
        
        <div>
            <h4>Newsletter</h4>
            <p>Subscribe for mental health tips and updates</p>
            <div style="display: flex; margin-top: 1rem;">
                <input type="email" placeholder="Your email" style="padding: 0.5rem; border: 1px solid #ccc; border-radius: 4px 0 0 4px; flex: 1;">
                <button class="primary-btn" style="border-radius: 0 4px 4px 0; padding: 0.5rem 1rem;">→</button>
            </div>
        </div>
    </div>
    
    <div style="text-align: center; padding-top: 1rem; border-top: 1px solid #eee; color: #777;">
        <p>© 2023 Safe Space Kenya. All rights reserved. | Designed with ❤️ for Mental Wellness</p>
    </div>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    home_page()
