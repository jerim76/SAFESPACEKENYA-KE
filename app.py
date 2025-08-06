import streamlit as st
import pandas as pd
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="SafeSpace Organisation",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
    <style>
    /* Global styles */
    body {
        font-family: 'Arial', sans-serif;
        color: #333;
        line-height: 1.6;
    }
    h1, h2, h3, h4 {
        color: #1E3A5F;
        font-weight: 600;
    }
    .section {
        padding: 60px 20px;
    }
    .section-title {
        text-align: center;
        margin-bottom: 50px;
    }
    .section-title h2 {
        font-size: 2.5rem;
        margin-bottom: 15px;
    }
    .divider {
        width: 100px;
        height: 4px;
        background: #26A69A;
        margin: 0 auto;
        border-radius: 2px;
    }
    .btn {
        display: inline-block;
        padding: 10px 20px;
        background: #26A69A;
        color: white;
        border-radius: 30px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
    }
    .btn:hover {
        background: #1E3A5F;
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    .btn-emergency {
        background: #FF6F61;
    }
    .btn-emergency:hover {
        background: #e05a50;
    }
    
    /* Hero section */
    .hero {
        background: linear-gradient(rgba(30, 58, 95, 0.8), rgba(30, 58, 95, 0.8)), url('https://images.unsplash.com/photo-1506126613408-eca07ce68773?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1200&q=80');
        background-size: cover;
        background-position: center;
        color: white;
        padding: 150px 20px;
        text-align: center;
    }
    .hero h1 {
        color: white;
        font-size: 3.5rem;
        margin-bottom: 20px;
    }
    .hero p {
        font-size: 1.5rem;
        max-width: 800px;
        margin: 0 auto 40px;
    }
    
    /* Card styles */
    .card {
        background: white;
        border-radius: 12px;
        padding: 30px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        height: 100%;
    }
    .card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.15);
    }
    .card-icon {
        font-size: 3rem;
        margin-bottom: 20px;
        color: #26A69A;
    }
    
    /* Team section */
    .team-member {
        text-align: center;
        margin-bottom: 30px;
    }
    .team-photo {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        object-fit: cover;
        margin: 0 auto 20px;
        border: 5px solid #E8F4F8;
    }
    
    /* Testimonial */
    .testimonial {
        background: #E8F4F8;
        padding: 30px;
        border-radius: 12px;
        position: relative;
        margin-bottom: 30px;
    }
    .testimonial:before {
        content: '"';
        font-size: 5rem;
        color: #26A69A;
        opacity: 0.2;
        position: absolute;
        top: 10px;
        left: 20px;
    }
    
    /* Contact section */
    .contact-info {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        margin-bottom: 30px;
    }
    .contact-card {
        flex: 1;
        min-width: 250px;
        background: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }
    
    /* Footer */
    .footer {
        background: #1E3A5F;
        color: white;
        padding: 50px 20px 20px;
    }
    .footer a {
        color: #26A69A;
        text-decoration: none;
    }
    .footer a:hover {
        color: white;
        text-decoration: underline;
    }
    .social-links {
        display: flex;
        gap: 15px;
        margin-top: 20px;
    }
    .social-icon {
        font-size: 1.5rem;
    }
    .copyright {
        text-align: center;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid rgba(255,255,255,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Navigation
st.markdown("""
    <nav style="position: fixed; top: 0; width: 100%; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.1); z-index: 1000; padding: 15px 0;">
        <div style="display: flex; justify-content: space-between; align-items: center; max-width: 1200px; margin: 0 auto; padding: 0 20px;">
            <div style="display: flex; align-items: center;">
                <h1 style="color: #26A69A; font-size: 1.8rem; margin: 0;">SafeSpace</h1>
            </div>
            <div>
                <a href="#home" style="margin: 0 15px; text-decoration: none; color: #1E3A5F; font-weight: 500;">Home</a>
                <a href="#about" style="margin: 0 15px; text-decoration: none; color: #1E3A5F; font-weight: 500;">About</a>
                <a href="#services" style="margin: 0 15px; text-decoration: none; color: #1E3A5F; font-weight: 500;">Services</a>
                <a href="#team" style="margin: 0 15px; text-decoration: none; color: #1E3A5F; font-weight: 500;">Team</a>
                <a href="#testimonials" style="margin: 0 15px; text-decoration: none; color: #1E3A5F; font-weight: 500;">Testimonials</a>
                <a href="#contact" style="margin: 0 15px; text-decoration: none; color: #1E3A5F; font-weight: 500;">Contact</a>
            </div>
            <a href="#contact" class="btn">Get Help</a>
        </div>
    </nav>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("<div id='home'></div>", unsafe_allow_html=True)
st.markdown("""
    <div class="hero">
        <h1>Your Mental Health Matters</h1>
        <p>SafeSpace provides compassionate mental health support and counseling services for individuals and families in Kenya</p>
        <div style="display: flex; justify-content: center; gap: 15px; flex-wrap: wrap;">
            <a href="#contact" class="btn" style="padding: 12px 30px; font-size: 1.1rem;">Book a Session</a>
            <a href="tel:+254781095919" class="btn btn-emergency" style="padding: 12px 30px; font-size: 1.1rem;">Emergency Help</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# About Section
st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'><h2>About SafeSpace</h2><div class='divider'></div></div>", unsafe_allow_html=True)

about_cols = st.columns(2)
with about_cols[0]:
    st.markdown("""
        <h3>Creating a Safe Space for Healing</h3>
        <p>Founded in 2015, SafeSpace Organisation is a leading mental health provider in Nairobi, Kenya. 
        We offer professional counseling services, support groups, and mental health education to individuals 
        and communities facing life's challenges.</p>
        <p>Our mission is to break down the stigma surrounding mental health in Kenya and provide accessible, 
        affordable care to all who need it.</p>
        <p>We believe that mental wellness is a fundamental human right and are committed to creating a safe, 
        supportive environment where healing can begin.</p>
        <div style="margin-top: 30px;">
            <a href="#services" class="btn">Our Services</a>
        </div>
    """, unsafe_allow_html=True)

with about_cols[1]:
    st.markdown("""
        <div style="display: flex; flex-wrap: wrap; gap: 15px;">
            <div style="flex: 1; min-width: 200px; background: #E8F4F8; padding: 20px; border-radius: 12px; text-align: center;">
                <h2 style="color: #26A69A; font-size: 2.5rem; margin: 0;">1,200+</h2>
                <p>Individuals Helped</p>
            </div>
            <div style="flex: 1; min-width: 200px; background: #E8F4F8; padding: 20px; border-radius: 12px; text-align: center;">
                <h2 style="color: #26A69A; font-size: 2.5rem; margin: 0;">8+</h2>
                <p>Years of Service</p>
            </div>
            <div style="flex: 1; min-width: 200px; background: #E8F4F8; padding: 20px; border-radius: 12px; text-align: center;">
                <h2 style="color: #26A69A; font-size: 2.5rem; margin: 0;">15+</h2>
                <p>Professional Staff</p>
            </div>
            <div style="flex: 1; min-width: 200px; background: #E8F4F8; padding: 20px; border-radius: 12px; text-align: center;">
                <h2 style="color: #26A69A; font-size: 2.5rem; margin: 0;">200+</h2>
                <p>Community Workshops</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Services Section
st.markdown("<div id='services'></div>", unsafe_allow_html=True)
st.markdown("<div class='section' style='background: #f8f9fa;'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'><h2>Our Services</h2><div class='divider'></div></div>", unsafe_allow_html=True)

services = st.columns(3)

services_content = [
    {
        "icon": "💬",
        "title": "Individual Counseling",
        "description": "One-on-one sessions with licensed therapists to address personal challenges, trauma, and mental health conditions."
    },
    {
        "icon": "👨‍👩‍👧‍👦",
        "title": "Family Therapy",
        "description": "Support for families navigating relationship issues, communication challenges, and life transitions."
    },
    {
        "icon": "👥",
        "title": "Group Support",
        "description": "Therapeutic groups for shared experiences including grief, addiction recovery, and anxiety management."
    },
    {
        "icon": "🏥",
        "title": "Crisis Intervention",
        "description": "Immediate support for individuals experiencing mental health emergencies or acute distress."
    },
    {
        "icon": "🏫",
        "title": "Corporate Wellness",
        "description": "Workshops and counseling services designed to support employee mental health in workplace settings."
    },
    {
        "icon": "📚",
        "title": "Educational Workshops",
        "description": "Community programs focused on mental health awareness, stress management, and emotional resilience."
    }
]

for i, col in enumerate(services):
    with col:
        service = services_content[i]
        st.markdown(f"""
            <div class="card">
                <div class="card-icon">{service['icon']}</div>
                <h3>{service['title']}</h3>
                <p>{service['description']}</p>
            </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Team Section
st.markdown("<div id='team'></div>", unsafe_allow_html=True)
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'><h2>Our Team</h2><div class='divider'></div></div>", unsafe_allow_html=True)

team = st.columns(4)

team_members = [
    {"name": "Dr. Amina Hassan", "role": "Clinical Director", "bio": "PhD in Clinical Psychology with 15+ years experience."},
    {"name": "James Omondi", "role": "Senior Therapist", "bio": "Specializes in trauma counseling and PTSD treatment."},
    {"name": "Sarah Wanjiku", "role": "Family Therapist", "bio": "Expert in family systems and relationship counseling."},
    {"name": "David Kimani", "role": "Crisis Counselor", "bio": "Provides emergency support and intervention services."}
]

for i, col in enumerate(team):
    with col:
        member = team_members[i]
        st.markdown(f"""
            <div class="team-member">
                <img src="https://randomuser.me/api/portraits/lego/{i+1}.jpg" class="team-photo">
                <h3>{member['name']}</h3>
                <p style="color: #26A69A; font-weight: 600;">{member['role']}</p>
                <p>{member['bio']}</p>
            </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Testimonials Section
st.markdown("<div id='testimonials'></div>", unsafe_allow_html=True)
st.markdown("<div class='section' style='background: #f8f9fa;'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'><h2>Client Testimonials</h2><div class='divider'></div></div>", unsafe_allow_html=True)

testimonials = st.columns(2)

testimonials_content = [
    {
        "name": "Mariam K.",
        "text": "SafeSpace helped me through the darkest time of my life. The therapists showed incredible compassion and gave me tools to manage my anxiety that I still use every day."
    },
    {
        "name": "John W.",
        "text": "After losing my job, I felt completely hopeless. The counseling I received at SafeSpace helped me rebuild my confidence and find a new career path."
    },
    {
        "name": "The Ochieng Family",
        "text": "Family therapy saved our relationships. We learned how to communicate effectively and understand each other's perspectives."
    },
    {
        "name": "Fatuma A.",
        "text": "The support group for anxiety was life-changing. Knowing I wasn't alone and having a safe space to share made all the difference."
    }
]

for i in range(0, 4, 2):
    with testimonials[0]:
        testimonial = testimonials_content[i]
        st.markdown(f"""
            <div class="testimonial">
                <p>{testimonial['text']}</p>
                <p style="font-weight: 600; margin-top: 20px;">— {testimonial['name']}</p>
            </div>
        """, unsafe_allow_html=True)
    
    with testimonials[1]:
        if i+1 < len(testimonials_content):
            testimonial = testimonials_content[i+1]
            st.markdown(f"""
                <div class="testimonial">
                    <p>{testimonial['text']}</p>
                    <p style="font-weight: 600; margin-top: 20px;">— {testimonial['name']}</p>
                </div>
            """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Contact Section
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'><h2>Contact Us</h2><div class='divider'></div></div>", unsafe_allow_html=True)

st.markdown("""
    <div class="contact-info">
        <div class="contact-card">
            <h3 style="color: #1E3A5F; margin-top: 0;">Contact Information</h3>
            <p style="font-size: 1rem; color: #333; line-height: 1.5;">
                📍 Greenhouse Plaza, 3rd Floor, Ngong Road, Nairobi, Kenya<br>
                📞 <a href='tel:+254781095919' style='color: #26A69A; text-decoration: none;'>+254 781 095 919</a><br>
                ✉️ <a href='mailto:info@safespaceorganisation.org' style='color: #26A69A; text-decoration: none;'>info@safespaceorganisation.org</a><br>
                🌐 <a href='https://www.safespaceorganisation.org' style='color: #26A69A; text-decoration: none;'>www.safespaceorganisation.org</a>
            </p>
            <div style="margin-top: 20px; display: flex; gap: 10px; flex-wrap: wrap;">
                <a href='tel:+254781095919' class="btn">Call Now</a>
                <a href='mailto:info@safespaceorganisation.org' class="btn">Email Us</a>
            </div>
        </div>
        
        <div class="contact-card">
            <h3 style="color: #1E3A5F; margin-top: 0;">Operating Hours</h3>
            <p style="font-size: 1rem; color: #333; line-height: 1.5;">
                Monday-Friday: 9:00 AM - 6:00 PM<br>
                Saturday: 10:00 AM - 2:00 PM<br>
                Sunday: Closed<br>
                <em style="color: #666;">Crisis support available 24/7</em>
            </p>
            <div style="margin-top: 20px;">
                <h4 style="color: #1E3A5F; margin-bottom: 10px;">Emergency Contact</h4>
                <p style="font-size: 1rem; color: #333;">📞 <a href='tel:+254781095919' style='color: #26A69A; text-decoration: none;'>+254 781 095 919</a> (24/7)</p>
                <a href='tel:+254781095919' class="btn btn-emergency">Emergency Call</a>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<h3 style='color: #1E3A5F;'>Visit Our Center</h3>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 1rem; color: #333; margin-bottom: 20px;'>Find us at Greenhouse Plaza, Ngong Road, Nairobi</p>", unsafe_allow_html=True)

# Map
try:
    map_data = pd.DataFrame({'lat': [-1.2985], 'lon': [36.7848]})
    st.map(map_data, zoom=14, use_container_width=True)
except Exception as e:
    st.error("Unable to display map. Please check your internet connection or visit our center at Greenhouse Plaza, Ngong Road, Nairobi.")

# Contact Form
st.markdown("<h3 style='color: #1E3A5F; margin-top: 40px;'>Send Us a Message</h3>", unsafe_allow_html=True)
contact_form = st.form("contact_form")
col1, col2 = contact_form.columns(2)

name = col1.text_input("Full Name")
email = col2.text_input("Email Address")
phone = col1.text_input("Phone Number")
subject = col2.selectbox("Subject", ["General Inquiry", "Book Appointment", "Group Program", "Corporate Wellness", "Other"])
message = contact_form.text_area("Your Message", height=150)

if contact_form.form_submit_button("Send Message"):
    if name and email and message:
        st.success("Thank you for your message! We'll get back to you within 24 hours.")
    else:
        st.warning("Please fill in all required fields")

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <div style="max-width: 1200px; margin: 0 auto; display: flex; flex-wrap: wrap; gap: 40px;">
            <div style="flex: 1; min-width: 300px;">
                <h2 style="color: white; font-size: 2rem; margin-top: 0;">SafeSpace Organisation</h2>
                <p>Providing compassionate mental health support and counseling services to the Nairobi community since 2015.</p>
                <div class="social-links">
                    <a href="#"><span class="social-icon">📱</span></a>
                    <a href="#"><span class="social-icon">📘</span></a>
                    <a href="#"><span class="social-icon">📸</span></a>
                    <a href="#"><span class="social-icon">🐦</span></a>
                </div>
            </div>
            
            <div style="flex: 1; min-width: 200px;">
                <h3 style="color: white;">Quick Links</h3>
                <p><a href="#home">Home</a></p>
                <p><a href="#about">About Us</a></p>
                <p><a href="#services">Services</a></p>
                <p><a href="#team">Our Team</a></p>
                <p><a href="#contact">Contact</a></p>
            </div>
            
            <div style="flex: 1; min-width: 250px;">
                <h3 style="color: white;">Contact Info</h3>
                <p>📍 Greenhouse Plaza, Ngong Road, Nairobi</p>
                <p>📞 +254 781 095 919</p>
                <p>✉️ info@safespaceorganisation.org</p>
                <p style="margin-top: 20px;">
                    <a href="#" class="btn" style="display: inline-block;">Donate</a>
                </p>
            </div>
        </div>
        <div class="copyright">
            <p>© 2023 SafeSpace Organisation. All rights reserved.</p>
            <p>Mental Health Support in Nairobi, Kenya</p>
        </div>
    </div>
""", unsafe_allow_html=True)
