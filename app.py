import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Safe Space Kenya",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
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
        line-height: 1.6;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Playfair Display', serif;
        color: var(--primary) !important;
        margin-top: 0.5rem !important;
        margin-bottom: 1rem !important;
    }
    
    .primary-btn {
        background-color: var(--primary) !important;
        color: white !important;
        border-radius: 30px !important;
        padding: 0.5rem 1.5rem !important;
        font-weight: 600 !important;
        border: none !important;
        transition: all 0.3s ease !important;
        cursor: pointer;
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
        cursor: pointer;
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
        margin-bottom: 1.5rem;
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
        margin-bottom: 1.5rem;
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
    
    .contact-form {
        background: white;
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .team-img {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        object-fit: cover;
        margin: 0 auto 1rem;
        border: 3px solid #4a9ca5;
        display: block;
    }
    
    .footer-link {
        text-decoration: none;
        color: #2a7a7c;
        transition: all 0.3s;
        display: block;
        padding: 5px 0;
        margin-bottom: 10px;
    }
    
    .footer-link:hover {
        color: #d4a373;
        transform: translateX(5px);
    }
    
    .social-icon {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: #e8f4f8;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.3s;
    }
    
    .social-icon:hover {
        background-color: var(--accent);
        color: white;
        transform: translateY(-3px);
    }
    
    .testimonial-card {
        border-radius: 10px;
        padding: 1.5rem;
        background: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        height: 300px;
    }
    
    .hero-section {
        background: linear-gradient(rgba(42, 122, 124, 0.85), rgba(42, 122, 124, 0.9)); 
        border-radius: 10px; 
        padding: 4rem 2rem; 
        text-align: center;
        color: white;
        margin-bottom: 3rem;
    }
    
    .about-section {
        display: flex; 
        gap: 2rem; 
        align-items: center; 
        margin-bottom: 3rem;
    }
    
    .about-image {
        background: linear-gradient(135deg, #4a9ca5 0%, #2a7a7c 100%); 
        border-radius: 10px; 
        height: 300px; 
        display: flex; 
        align-items: center; 
        justify-content: center; 
        color: white; 
        font-size: 3rem;
    }
    
    .footer-grid {
        display: grid; 
        grid-template-columns: repeat(4, 1fr); 
        gap: 2rem; 
        margin-bottom: 2rem;
    }
    
    .copyright {
        text-align: center; 
        padding-top: 1rem; 
        border-top: 1px solid #eee; 
        color: #777;
    }
</style>
""", unsafe_allow_html=True)

# Team data with image URLs
team_data = [
    {
        "name": "Jerim Owino", 
        "role": "Founder & CEO", 
        "bio": "Clinical psychologist specializing in trauma therapy with 12 years of experience. Jerim holds a PhD in Clinical Psychology from the University of Nairobi and has published several papers on trauma recovery.",
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Hamdi Roble", 
        "role": "Senior Therapist", 
        "bio": "Muslim therapist specializing in culturally-sensitive CBT for anxiety and depression. Hamdi integrates faith-based approaches with evidence-based therapies to support her clients' mental wellness.",
        "image": "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Yvone Orina", 
        "role": "Family Therapist", 
        "bio": "Specializes in family systems therapy and relationship counseling. Yvone helps families navigate challenges and build stronger connections through improved communication.",
        "image": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Brian Kiprop", 
        "role": "Art Therapist", 
        "bio": "Uses creative approaches to help clients express emotions. Brian's innovative methods help clients explore feelings through art, music, and movement therapy.",
        "image": "https://images.unsplash.com/photo-1560250097-0b93528c311a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=400&q=80"
    }
]

# Services data
services_data = [
    {"title": "Individual Counseling", "icon": "👤", "description": "Personalized one-on-one sessions addressing mental health concerns and personal growth. Tailored approaches for depression, anxiety, and life transitions."},
    {"title": "Group Therapy", "icon": "👥", "description": "Supportive group sessions fostering connection and shared healing. Topics include grief support, addiction recovery, and stress management."},
    {"title": "Family Counseling", "icon": "🏠", "description": "Strengthening family bonds and improving communication. Helping families navigate conflict, parenting challenges, and life transitions together."},
    {"title": "Workshops & Training", "icon": "🎓", "description": "Educational programs on mental wellness for organizations and communities. Customized sessions for schools, corporations, and community groups."},
    {"title": "Tele-therapy", "icon": "📱", "description": "Secure online counseling for convenient access. Professional support from the comfort of your home via video sessions."},
    {"title": "Trauma Support", "icon": "❤️", "description": "Specialized therapy for healing from traumatic experiences. Evidence-based approaches for PTSD and complex trauma recovery."}
]

# Testimonials
testimonials = [
    {
        "name": "Wanjiru M., Nairobi",
        "text": '"Safe Space Kenya provided me with the tools to manage my anxiety in a way that respected my cultural background. The therapists were understanding and professional."',
        "image": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80"
    },
    {
        "name": "David O., Mombasa",
        "text": '"The family counseling sessions helped us rebuild communication after a difficult period. Our family is stronger and more connected thanks to Safe Space Kenya."',
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80"
    },
    {
        "name": "Aisha K., Kisumu",
        "text": '"As a Muslim woman, I appreciated Hamdi\'s culturally sensitive approach. She helped me navigate anxiety while respecting my faith and values."',
        "image": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80"
    },
    {
        "name": "Samuel T., Nakuru",
        "text": '"After my accident, the trauma support program helped me process my experience and regain my confidence. I\'m forever grateful to the team at Safe Space Kenya."',
        "image": "https://images.unsplash.com/photo-1552058544-f2b08422138a?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80"
    }
]

# Session state for form submission
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Home Page
def home_page():
    # Hero Section
    st.markdown("""
    <div class="hero-section">
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
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div>
            <p>Founded in <strong>2023</strong>, Safe Space Kenya is dedicated to providing accessible mental health services to individuals and communities across Kenya.</p>
            <p>We believe that everyone deserves a safe, non-judgmental environment to explore their thoughts and emotions. Our mission is to break down barriers to mental healthcare and promote emotional wellbeing for all Kenyans.</p>
            <p>Our team of licensed therapists brings diverse expertise and a commitment to cultural sensitivity. We offer services in multiple languages and respect all cultural and religious backgrounds.</p>
            <button class="primary-btn">Meet Our Team</button>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="about-image">
            ❤️
        </div>
        """, unsafe_allow_html=True)
    
    # Services Section
    st.header("Our Therapeutic Services", anchor="services")
    st.markdown("We offer a range of evidence-based therapies tailored to meet your individual needs. All services are provided by licensed professionals in a confidential setting.")
    
    # Create columns for services
    cols = st.columns(3)
    for i, service in enumerate(services_data):
        with cols[i % 3]:
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
    
    # Team Section with images
    st.header("Our Professional Team")
    st.markdown("Meet our dedicated therapists committed to your mental wellness journey. Each team member brings unique expertise and a compassionate approach to care.")
    
    team_cols = st.columns(4)
    for i, member in enumerate(team_data):
        with team_cols[i]:
            st.markdown(f"""
            <div class="team-card">
                <img src="{member['image']}" class="team-img" alt="{member['name']}">
                <h3>{member['name']}</h3>
                <p style="color: #d4a373; font-weight: 600; font-style: italic;">{member['role']}</p>
                <p>{member['bio']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Testimonials
    st.header("Client Testimonials")
    st.markdown("Hear what others have to say about their healing journey with us.")
    
    testimonial_cols = st.columns(2)
    for i in range(0, len(testimonials), 2):
        with testimonial_cols[0]:
            testimonial = testimonials[i]
            st.markdown(f"""
            <div class="testimonial-card">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 1rem;">
                    <img src="{testimonial['image']}" 
                         style="width: 60px; height: 60px; border-radius: 50%; object-fit: cover;">
                    <div>
                        <h4 style="margin: 0;">{testimonial['name']}</h4>
                    </div>
                </div>
                <p style="font-style: italic;">{testimonial['text']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        if i+1 < len(testimonials):
            with testimonial_cols[1]:
                testimonial = testimonials[i+1]
                st.markdown(f"""
                <div class="testimonial-card">
                    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 1rem;">
                        <img src="{testimonial['image']}" 
                             style="width: 60px; height: 60px; border-radius: 50%; object-fit: cover;">
                        <div>
                            <h4 style="margin: 0;">{testimonial['name']}</h4>
                        </div>
                    </div>
                    <p style="font-style: italic;">{testimonial['text']}</p>
                </div>
                """, unsafe_allow_html=True)
    
    # Contact Section
    st.header("Contact Us", anchor="contact")
    st.markdown("Reach out to schedule an appointment or ask questions about our services. We're here to support you on your mental wellness journey.")
    
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
        with st.container():
            st.markdown('<div class="contact-form">', unsafe_allow_html=True)
            with st.form("appointment_form", clear_on_submit=True):
                st.subheader("Book an Appointment")
                name = st.text_input("Full Name", placeholder="Your full name", key="name")
                email = st.text_input("Email Address", placeholder="Your email", key="email")
                phone = st.text_input("Phone Number", placeholder="+254 XXX XXX XXX", key="phone")
                
                service_options = [
                    "Individual Counseling",
                    "Group Therapy",
                    "Family Counseling",
                    "Workshops & Training",
                    "Tele-therapy",
                    "Trauma Support"
                ]
                service = st.selectbox("Service Interested In", service_options, key="service")
                
                preferred_date = st.date_input("Preferred Date", min_value=datetime.today(), key="date")
                message = st.text_area("Your Message", placeholder="Briefly describe what you'd like to discuss", key="message")
                
                submitted = st.form_submit_button("Submit Appointment Request", type="primary")
                if submitted:
                    # Validate required fields
                    if not name or not email or not phone:
                        st.error("Please fill in all required fields")
                    else:
                        # Save form data to session state
                        st.session_state.submitted = True
                        st.session_state.form_data = {
                            "name": name,
                            "email": email,
                            "phone": phone,
                            "service": service,
                            "date": preferred_date,
                            "message": message
                        }
                        st.success("Thank you for your appointment request! We'll contact you within 24 hours to confirm your session.")
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div class="footer-grid">
        <div>
            <h4>Safe Space Kenya</h4>
            <p>Providing professional, confidential counseling and mental health services since 2023. Our mission is to make mental healthcare accessible to all Kenyans.</p>
            <div style="display: flex; gap: 15px; margin-top: 1rem;">
                <a href="https://facebook.com" target="_blank" style="text-decoration: none; color: inherit;">
                    <div class="social-icon">f</div>
                </a>
                <a href="https://twitter.com" target="_blank" style="text-decoration: none; color: inherit;">
                    <div class="social-icon">t</div>
                </a>
                <a href="https://linkedin.com" target="_blank" style="text-decoration: none; color: inherit;">
                    <div class="social-icon">in</div>
                </a>
            </div>
        </div>
        
        <div>
            <h4>Quick Links</h4>
            <a href="#" class="footer-link">Home</a>
            <a href="#services" class="footer-link">Services</a>
            <a href="#about" class="footer-link">About Us</a>
            <a href="#team" class="footer-link">Our Team</a>
            <a href="#contact" class="footer-link">Contact</a>
        </div>
        
        <div>
            <h4>Our Services</h4>
            <a href="#services" class="footer-link">Individual Counseling</a>
            <a href="#services" class="footer-link">Group Therapy</a>
            <a href="#services" class="footer-link">Family Counseling</a>
            <a href="#services" class="footer-link">Workshops & Training</a>
            <a href="#services" class="footer-link">Tele-therapy</a>
        </div>
        
        <div>
            <h4>Newsletter</h4>
            <p style="margin-bottom: 1rem;">Subscribe for mental health tips and updates</p>
            <div style="display: flex; margin-top: 1rem;">
                <input type="email" placeholder="Your email" 
                       style="padding: 0.5rem; border: 1px solid #ccc; border-radius: 4px 0 0 4px; flex: 1; outline: none;">
                <button class="primary-btn" 
                        style="border-radius: 0 4px 4px 0; padding: 0.5rem 1rem; cursor: pointer;">→</button>
            </div>
        </div>
    </div>
    
    <div class="copyright">
        <p>© 2023 Safe Space Kenya. All rights reserved. | Designed with ❤️ for Mental Wellness</p>
    </div>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    home_page()
