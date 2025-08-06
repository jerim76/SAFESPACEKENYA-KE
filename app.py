import streamlit as st
import pandas as pd
from PIL import Image
import base64
import requests
from io import BytesIO

# Set page configuration
st.set_page_config(
    page_title="SafeSpace Organisation | Mental Health Support",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for a calming environment
st.markdown(f"""
<style>
/* Global styles */
:root {{
    --primary: #1E3A5F;
    --secondary: #26A69A;
    --accent: #FF6F61;
    --light: #E8F4F8;
    --lighter: #F5FBFD;
    --dark: #0D1C30;
    --text: #333333;
}}

* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

body {{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: var(--text);
    line-height: 1.7;
    background-color: var(--lighter);
}}

h1, h2, h3, h4, h5 {{
    color: var(--primary);
    font-weight: 700;
    line-height: 1.3;
}}

h1 {{
    font-size: 3.5rem;
    margin-bottom: 1.5rem;
}}

h2 {{
    font-size: 2.8rem;
    margin-bottom: 1.2rem;
}}

h3 {{
    font-size: 2rem;
    margin-bottom: 1rem;
}}

h4 {{
    font-size: 1.5rem;
    margin-bottom: 0.8rem;
}}

p {{
    margin-bottom: 1.2rem;
    font-size: 1.1rem;
}}

a {{
    color: var(--secondary);
    text-decoration: none;
    transition: all 0.3s ease;
}}

a:hover {{
    color: var(--primary);
    text-decoration: underline;
}}

.container {{
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}}

.section {{
    padding: 80px 0;
}}

.section-title {{
    text-align: center;
    margin-bottom: 50px;
}}

.section-title h2 {{
    position: relative;
    display: inline-block;
    padding-bottom: 15px;
}}

.section-title h2:after {{
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 80px;
    height: 4px;
    background: var(--secondary);
    border-radius: 2px;
}}

.divider {{
    width: 100px;
    height: 4px;
    background: var(--secondary);
    margin: 0 auto 30px;
    border-radius: 2px;
}}

.btn {{
    display: inline-block;
    padding: 14px 32px;
    background: var(--secondary);
    color: white;
    border-radius: 50px;
    text-decoration: none;
    font-weight: 600;
    font-size: 1.1rem;
    transition: all 0.3s ease;
    border: none;
    cursor: pointer;
    box-shadow: 0 4px 15px rgba(38, 166, 154, 0.3);
}}

.btn:hover {{
    background: var(--primary);
    transform: translateY(-3px);
    box-shadow: 0 7px 20px rgba(30, 58, 95, 0.3);
    text-decoration: none;
    color: white;
}}

.btn-emergency {{
    background: var(--accent);
    box-shadow: 0 4px 15px rgba(255, 111, 97, 0.3);
}}

.btn-emergency:hover {{
    background: #e05a50;
    box-shadow: 0 7px 20px rgba(224, 90, 80, 0.3);
}}

/* Navigation */
.navbar {{
    position: fixed;
    top: 0;
    width: 100%;
    background: rgba(255, 255, 255, 0.95);
    box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
    z-index: 1000;
    padding: 20px 0;
    backdrop-filter: blur(10px);
}}

.nav-container {{
    display: flex;
    justify-content: space-between;
    align-items: center;
}}

.logo {{
    display: flex;
    align-items: center;
}}

.logo h1 {{
    color: var(--secondary);
    font-size: 1.8rem;
    margin: 0;
    font-weight: 800;
}}

.nav-links {{
    display: flex;
    align-items: center;
}}

.nav-links a {{
    margin: 0 18px;
    text-decoration: none;
    color: var(--primary);
    font-weight: 600;
    font-size: 1.05rem;
    position: relative;
}}

.nav-links a:after {{
    content: '';
    position: absolute;
    bottom: -5px;
    left: 0;
    width: 0;
    height: 2px;
    background: var(--secondary);
    transition: width 0.3s ease;
}}

.nav-links a:hover:after {{
    width: 100%;
}}

.nav-btn {{
    margin-left: 15px;
}}

/* Hero Section */
.hero {{
    background: linear-gradient(135deg, rgba(30, 58, 95, 0.85) 0%, rgba(38, 166, 154, 0.8) 100%), 
                url('https://images.unsplash.com/photo-1506126613408-eca07ce68773?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1920&q=80');
    background-size: cover;
    background-position: center;
    color: white;
    padding: 180px 0 100px;
    text-align: center;
}}

.hero-content {{
    max-width: 850px;
    margin: 0 auto;
}}

.hero h1 {{
    color: white;
    font-size: 3.5rem;
    margin-bottom: 25px;
    text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}}

.hero p {{
    font-size: 1.4rem;
    margin: 0 auto 50px;
    max-width: 700px;
    text-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}}

.hero-btns {{
    display: flex;
    justify-content: center;
    gap: 20px;
    flex-wrap: wrap;
}}

/* Stats */
.stats {{
    background: white;
    padding: 30px 0;
    box-shadow: 0 5px 30px rgba(0, 0, 0, 0.05);
}}

.stats-container {{
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    gap: 20px;
}}

.stat-item {{
    text-align: center;
    padding: 20px;
    min-width: 200px;
}}

.stat-number {{
    font-size: 2.5rem;
    font-weight: 800;
    color: var(--secondary);
    margin-bottom: 10px;
    line-height: 1;
}}

.stat-label {{
    font-size: 1.1rem;
    color: #666;
    font-weight: 600;
}}

/* Card styles */
.card-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
    margin-top: 40px;
}}

.card {{
    background: white;
    border-radius: 16px;
    padding: 40px 30px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
    transition: all 0.4s ease;
    height: 100%;
    display: flex;
    flex-direction: column;
}}

.card:hover {{
    transform: translateY(-10px);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
}}

.card-icon {{
    font-size: 3.5rem;
    margin-bottom: 25px;
    color: var(--secondary);
}}

.card h3 {{
    margin-bottom: 20px;
    color: var(--primary);
}}

.card-content {{
    flex-grow: 1;
}}

/* Team section */
.team-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 40px;
    margin-top: 50px;
}}

.team-member {{
    text-align: center;
    background: white;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
    transition: all 0.3s ease;
}}

.team-member:hover {{
    transform: translateY(-10px);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
}}

.team-photo {{
    width: 100%;
    height: 280px;
    object-fit: cover;
    border-bottom: 4px solid var(--secondary);
}}

.team-info {{
    padding: 25px 20px;
}}

.team-info h3 {{
    margin-bottom: 5px;
    color: var(--primary);
}}

.team-role {{
    color: var(--secondary);
    font-weight: 600;
    margin-bottom: 15px;
    font-size: 1.1rem;
}}

/* Testimonials */
.testimonials-container {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 30px;
    margin-top: 50px;
}}

.testimonial {{
    background: white;
    padding: 40px;
    border-radius: 16px;
    position: relative;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
}}

.testimonial:before {{
    content: '"';
    font-size: 8rem;
    color: var(--light);
    position: absolute;
    top: 20px;
    left: 30px;
    font-family: serif;
    line-height: 1;
    z-index: 0;
}}

.testimonial-content {{
    position: relative;
    z-index: 2;
}}

.testimonial-text {{
    font-size: 1.1rem;
    font-style: italic;
    margin-bottom: 30px;
    color: var(--text);
    line-height: 1.8;
}}

.testimonial-author {{
    display: flex;
    align-items: center;
}}

.author-name {{
    font-weight: 700;
    color: var(--primary);
    font-size: 1.1rem;
}}

/* Contact section */
.contact-container {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 40px;
    margin-top: 50px;
}}

.contact-card {{
    background: white;
    padding: 40px;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
}}

.contact-card h3 {{
    margin-bottom: 25px;
    padding-bottom: 15px;
    border-bottom: 2px solid var(--light);
}}

.contact-info {{
    margin-bottom: 30px;
}}

.contact-item {{
    display: flex;
    margin-bottom: 20px;
}}

.contact-icon {{
    font-size: 1.5rem;
    color: var(--secondary);
    min-width: 40px;
    margin-top: 5px;
}}

.contact-details {{
    line-height: 1.6;
}}

.contact-details p {{
    margin: 0;
}}

.contact-btns {{
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    margin-top: 30px;
}}

.hours-list {{
    list-style: none;
    padding: 0;
}}

.hours-list li {{
    display: flex;
    justify-content: space-between;
    padding: 12px 0;
    border-bottom: 1px solid var(--light);
}}

.hours-list li:last-child {{
    border-bottom: none;
}}

.hours-list .day {{
    font-weight: 600;
}}

/* Map */
.map-container {{
    margin-top: 40px;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    height: 400px;
}}

/* Form */
.form-container {{
    background: white;
    padding: 40px;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
    margin-top: 50px;
}}

.form-grid {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 25px;
    margin-bottom: 25px;
}}

.form-group {{
    margin-bottom: 20px;
}}

.form-group label {{
    display: block;
    margin-bottom: 8px;
    font-weight: 600;
    color: var(--primary);
}}

.form-group input,
.form-group textarea,
.form-group select {{
    width: 100%;
    padding: 14px 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    font-size: 1rem;
    transition: all 0.3s ease;
}}

.form-group input:focus,
.form-group textarea:focus,
.form-group select:focus {{
    border-color: var(--secondary);
    outline: none;
    box-shadow: 0 0 0 3px rgba(38, 166, 154, 0.2);
}}

textarea {{
    min-height: 150px;
    resize: vertical;
}}

.submit-btn {{
    width: 100%;
    padding: 16px;
    font-size: 1.1rem;
}}

/* Footer */
.footer {{
    background: var(--dark);
    color: white;
    padding: 60px 0 30px;
}}

.footer-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 40px;
    margin-bottom: 50px;
}}

.footer-col h3 {{
    color: white;
    margin-bottom: 25px;
    font-size: 1.5rem;
}}

.footer-links {{
    list-style: none;
    padding: 0;
}}

.footer-links li {{
    margin-bottom: 12px;
}}

.footer-links a {{
    color: #b0c4de;
    transition: all 0.3s ease;
}}

.footer-links a:hover {{
    color: white;
    text-decoration: none;
}}

.contact-info p {{
    display: flex;
    align-items: flex-start;
    margin-bottom: 15px;
    color: #b0c4de;
}}

.contact-icon {{
    margin-right: 12px;
    color: var(--secondary);
    min-width: 20px;
    margin-top: 5px;
}}

.social-links {{
    display: flex;
    gap: 15px;
    margin-top: 20px;
}}

.social-icon {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 45px;
    height: 45px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 50%;
    color: white;
    font-size: 1.3rem;
    transition: all 0.3s ease;
}}

.social-icon:hover {{
    background: var(--secondary);
    transform: translateY(-5px);
}}

.copyright {{
    text-align: center;
    padding-top: 30px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    color: #b0c4de;
    font-size: 1rem;
}}
</style>
""", unsafe_allow_html=True)

# Navigation
st.markdown("""
<nav class="navbar">
    <div class="container nav-container">
        <div class="logo">
            <h1>SafeSpace</h1>
        </div>
        <div class="nav-links">
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#services">Services</a>
            <a href="#team">Team</a>
            <a href="#testimonials">Testimonials</a>
            <a href="#contact">Contact</a>
            <a href="#contact" class="btn nav-btn">Get Help</a>
        </div>
    </div>
</nav>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero" id="home">
    <div class="container hero-content">
        <h1>Your Journey to Wellness Begins Here</h1>
        <p>SafeSpace provides compassionate mental health support and counseling services for individuals and families in Kenya</p>
        <div class="hero-btns">
            <a href="#contact" class="btn">Book a Session</a>
            <a href="tel:+254781095919" class="btn btn-emergency">Emergency Help</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Stats Section
st.markdown("""
<div class="stats">
    <div class="container stats-container">
        <div class="stat-item">
            <div class="stat-number">1,200+</div>
            <div class="stat-label">Individuals Helped</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">8+</div>
            <div class="stat-label">Years of Service</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">15+</div>
            <div class="stat-label">Professional Staff</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">200+</div>
            <div class="stat-label">Community Workshops</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# About Section
st.markdown("""
<div class="section" id="about">
    <div class="container">
        <div class="section-title">
            <h2>About SafeSpace</h2>
        </div>
        
        <div class="about-content" style="display: flex; flex-wrap: wrap; gap: 50px; align-items: center;">
            <div style="flex: 1; min-width: 300px;">
                <h3>Creating a Safe Space for Healing</h3>
                <p>Founded in 2015, SafeSpace Organisation is a leading mental health provider in Nairobi, Kenya. We offer professional counseling services, support groups, and mental health education to individuals and communities facing life's challenges.</p>
                <p>Our mission is to break down the stigma surrounding mental health in Kenya and provide accessible, affordable care to all who need it.</p>
                <p>We believe that mental wellness is a fundamental human right and are committed to creating a safe, supportive environment where healing can begin.</p>
                <div style="margin-top: 40px;">
                    <a href="#services" class="btn">Our Services</a>
                </div>
            </div>
            <div style="flex: 1; min-width: 300px;">
                <div style="border-radius: 20px; overflow: hidden; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);">
                    <img src="https://images.unsplash.com/photo-1527613426441-4da17471b66d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80" 
                         style="width: 100%; height: 400px; object-fit: cover;" alt="SafeSpace Counseling">
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Services Section
st.markdown("""
<div class="section" id="services" style="background: #F5FBFD;">
    <div class="container">
        <div class="section-title">
            <h2>Our Services</h2>
            <p>Comprehensive mental health support tailored to your unique needs</p>
        </div>
        
        <div class="card-grid">
            <div class="card">
                <div class="card-icon">💬</div>
                <div class="card-content">
                    <h3>Individual Counseling</h3>
                    <p>One-on-one sessions with licensed therapists to address personal challenges, trauma, and mental health conditions.</p>
                </div>
            </div>
            
            <div class="card">
                <div class="card-icon">👨‍👩‍👧‍👦</div>
                <div class="card-content">
                    <h3>Family Therapy</h3>
                    <p>Support for families navigating relationship issues, communication challenges, and life transitions.</p>
                </div>
            </div>
            
            <div class="card">
                <div class="card-icon">👥</div>
                <div class="card-content">
                    <h3>Group Support</h3>
                    <p>Therapeutic groups for shared experiences including grief, addiction recovery, and anxiety management.</p>
                </div>
            </div>
            
            <div class="card">
                <div class="card-icon">🏥</div>
                <div class="card-content">
                    <h3>Crisis Intervention</h3>
                    <p>Immediate support for individuals experiencing mental health emergencies or acute distress.</p>
                </div>
            </div>
            
            <div class="card">
                <div class="card-icon">🏫</div>
                <div class="card-content">
                    <h3>Corporate Wellness</h3>
                    <p>Workshops and counseling services designed to support employee mental health in workplace settings.</p>
                </div>
            </div>
            
            <div class="card">
                <div class="card-icon">📚</div>
                <div class="card-content">
                    <h3>Educational Workshops</h3>
                    <p>Community programs focused on mental health awareness, stress management, and emotional resilience.</p>
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Team Section
st.markdown("""
<div class="section" id="team">
    <div class="container">
        <div class="section-title">
            <h2>Our Team</h2>
            <p>Meet our compassionate mental health professionals</p>
        </div>
        
        <div class="team-grid">
            <div class="team-member">
                <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=400&w=400" 
                     class="team-photo" alt="Dr. Amina Hassan">
                <div class="team-info">
                    <h3>Dr. Amina Hassan</h3>
                    <div class="team-role">Clinical Director</div>
                    <p>PhD in Clinical Psychology with 15+ years experience.</p>
                </div>
            </div>
            
            <div class="team-member">
                <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=400&w=400" 
                     class="team-photo" alt="James Omondi">
                <div class="team-info">
                    <h3>James Omondi</h3>
                    <div class="team-role">Senior Therapist</div>
                    <p>Specializes in trauma counseling and PTSD treatment.</p>
                </div>
            </div>
            
            <div class="team-member">
                <img src="https://images.unsplash.com/photo-1590086782792-42dd2350140d?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=400&w=400" 
                     class="team-photo" alt="Sarah Wanjiku">
                <div class="team-info">
                    <h3>Sarah Wanjiku</h3>
                    <div class="team-role">Family Therapist</div>
                    <p>Expert in family systems and relationship counseling.</p>
                </div>
            </div>
            
            <div class="team-member">
                <img src="https://images.unsplash.com/photo-1564564321837-a57b7070ac4f?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=400&w=400" 
                     class="team-photo" alt="David Kimani">
                <div class="team-info">
                    <h3>David Kimani</h3>
                    <div class="team-role">Crisis Counselor</div>
                    <p>Provides emergency support and intervention services.</p>
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Testimonials Section
st.markdown("""
<div class="section" id="testimonials" style="background: #F5FBFD;">
    <div class="container">
        <div class="section-title">
            <h2>Client Testimonials</h2>
            <p>Hear from those who have found hope and healing</p>
        </div>
        
        <div class="testimonials-container">
            <div class="testimonial">
                <div class="testimonial-content">
                    <div class="testimonial-text">
                        SafeSpace helped me through the darkest time of my life. The therapists showed incredible compassion and gave me tools to manage my anxiety that I still use every day.
                    </div>
                    <div class="testimonial-author">
                        <div class="author-name">Mariam K.</div>
                    </div>
                </div>
            </div>
            
            <div class="testimonial">
                <div class="testimonial-content">
                    <div class="testimonial-text">
                        After losing my job, I felt completely hopeless. The counseling I received at SafeSpace helped me rebuild my confidence and find a new career path.
                    </div>
                    <div class="testimonial-author">
                        <div class="author-name">John W.</div>
                    </div>
                </div>
            </div>
            
            <div class="testimonial">
                <div class="testimonial-content">
                    <div class="testimonial-text">
                        Family therapy saved our relationships. We learned how to communicate effectively and understand each other's perspectives.
                    </div>
                    <div class="testimonial-author">
                        <div class="author-name">The Ochieng Family</div>
                    </div>
                </div>
            </div>
            
            <div class="testimonial">
                <div class="testimonial-content">
                    <div class="testimonial-text">
                        The support group for anxiety was life-changing. Knowing I wasn't alone and having a safe space to share made all the difference.
                    </div>
                    <div class="testimonial-author">
                        <div class="author-name">Fatuma A.</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Contact Section
st.markdown("""
<div class="section" id="contact">
    <div class="container">
        <div class="section-title">
            <h2>Contact Us</h2>
            <p>Reach out to begin your journey to wellness</p>
        </div>
        
        <div class="contact-container">
            <div class="contact-card">
                <h3>Contact Information</h3>
                <div class="contact-info">
                    <div class="contact-item">
                        <div class="contact-icon">📍</div>
                        <div class="contact-details">
                            <p>Greenhouse Plaza, 3rd Floor</p>
                            <p>Ngong Road, Nairobi, Kenya</p>
                        </div>
                    </div>
                    
                    <div class="contact-item">
                        <div class="contact-icon">📞</div>
                        <div class="contact-details">
                            <p><a href="tel:+254781095919">+254 781 095 919</a></p>
                        </div>
                    </div>
                    
                    <div class="contact-item">
                        <div class="contact-icon">✉️</div>
                        <div class="contact-details">
                            <p><a href="mailto:info@safespaceorganisation.org">info@safespaceorganisation.org</a></p>
                        </div>
                    </div>
                    
                    <div class="contact-item">
                        <div class="contact-icon">🌐</div>
                        <div class="contact-details">
                            <p><a href="https://www.safespaceorganisation.org">www.safespaceorganisation.org</a></p>
                        </div>
                    </div>
                </div>
                
                <div class="contact-btns">
                    <a href="tel:+254781095919" class="btn">Call Now</a>
                    <a href="mailto:info@safespaceorganisation.org" class="btn">Email Us</a>
                </div>
            </div>
            
            <div class="contact-card">
                <h3>Operating Hours</h3>
                <ul class="hours-list">
                    <li>
                        <span class="day">Monday-Friday</span>
                        <span>9:00 AM - 6:00 PM</span>
                    </li>
                    <li>
                        <span class="day">Saturday</span>
                        <span>10:00 AM - 2:00 PM</span>
                    </li>
                    <li>
                        <span class="day">Sunday</span>
                        <span>Closed</span>
                    </li>
                </ul>
                
                <div style="margin-top: 30px; padding: 20px; background: rgba(255, 111, 97, 0.05); border-radius: 12px;">
                    <h4 style="color: var(--accent); margin-bottom: 15px;">Emergency Contact</h4>
                    <p style="font-size: 1.1rem; margin-bottom: 20px;">24/7 crisis support available</p>
                    <a href="tel:+254781095919" class="btn btn-emergency">Emergency Call</a>
                </div>
            </div>
        </div>
        
        <h3 style="color: var(--primary); margin-top: 60px; text-align: center;">Visit Our Center</h3>
        <p style="text-align: center; font-size: 1.2rem; margin-bottom: 30px;">Find us at Greenhouse Plaza, Ngong Road, Nairobi</p>
        
        <div class="map-container">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3988.818530728106!2d36.78262731475395!3d-1.2984995990625628!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x182f109997354b97%3A0xdeb9d6d8e3d7f5e8!2sGreenhouse%20Ngong%20Road!5e0!3m2!1sen!2ske!4v1651234567890!5m2!1sen!2ske" 
                    width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
        </div>
        
        <div class="form-container">
            <h3 style="text-align: center; margin-bottom: 40px;">Send Us a Message</h3>
            
            <form class="contact-form">
                <div class="form-grid">
                    <div class="form-group">
                        <label for="name">Full Name *</label>
                        <input type="text" id="name" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="email">Email Address *</label>
                        <input type="email" id="email" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="phone">Phone Number</label>
                        <input type="tel" id="phone">
                    </div>
                    
                    <div class="form-group">
                        <label for="subject">Subject</label>
                        <select id="subject">
                            <option>General Inquiry</option>
                            <option>Book Appointment</option>
                            <option>Group Program</option>
                            <option>Corporate Wellness</option>
                            <option>Other</option>
                        </select>
                    </div>
                </div>
                
                <div class="form-group">
                    <label for="message">Your Message *</label>
                    <textarea id="message" required></textarea>
                </div>
                
                <button type="submit" class="btn submit-btn">Send Message</button>
            </form>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <div class="container">
        <div class="footer-grid">
            <div class="footer-col">
                <h3>SafeSpace Organisation</h3>
                <p>Providing compassionate mental health support and counseling services to the Nairobi community since 2015.</p>
                <div class="social-links">
                    <a href="#"><span class="social-icon">f</span></a>
                    <a href="#"><span class="social-icon">t</span></a>
                    <a href="#"><span class="social-icon">in</span></a>
                    <a href="#"><span class="social-icon">ig</span></a>
                </div>
            </div>
            
            <div class="footer-col">
                <h3>Quick Links</h3>
                <ul class="footer-links">
                    <li><a href="#home">Home</a></li>
                    <li><a href="#about">About Us</a></li>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#team">Our Team</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </div>
            
            <div class="footer-col">
                <h3>Contact Info</h3>
                <div class="contact-info">
                    <p><span class="contact-icon">📍</span> Greenhouse Plaza, Ngong Road, Nairobi</p>
                    <p><span class="contact-icon">📞</span> +254 781 095 919</p>
                    <p><span class="contact-icon">✉️</span> info@safespaceorganisation.org</p>
                </div>
                <a href="#" class="btn" style="margin-top: 20px;">Make a Donation</a>
            </div>
        </div>
        
        <div class="copyright">
            <p>© 2023 SafeSpace Organisation. All rights reserved.</p>
            <p>Mental Health Support in Nairobi, Kenya</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
