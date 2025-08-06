import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="SafeSpace Organisation | Mental Health Support",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with simplified styles for Streamlit compatibility
st.markdown("""
<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #333333;
    line-height: 1.7;
    background-color: #F5FBFD;
}

h1, h2, h3, h4, h5 {
    color: #1E3A5F;
    font-weight: 700;
    line-height: 1.3;
}

h1 { font-size: 3.2rem; margin-bottom: 1.5rem; }
h2 { font-size: 2.5rem; margin-bottom: 1.2rem; }
h3 { font-size: 1.8rem; margin-bottom: 1rem; }
h4 { font-size: 1.4rem; margin-bottom: 0.8rem; }
p { margin-bottom: 1.2rem; font-size: 1.1rem; }

a {
    color: #26A69A;
    text-decoration: none;
    transition: all 0.3s ease;
}

a:hover {
    color: #1E3A5F;
    text-decoration: underline;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 15px;
}

.section {
    padding: 60px 0;
}

.section-title {
    text-align: center;
    margin-bottom: 40px;
}

.section-title h2 {
    display: inline-block;
    padding-bottom: 10px;
}

.section-title div {
    width: 80px;
    height: 4px;
    background: #26A69A;
    margin: 0 auto;
    border-radius: 2px;
}

.btn {
    display: inline-block;
    padding: 12px 28px;
    background: #26A69A;
    color: white;
    border-radius: 25px;
    font-weight: 600;
    font-size: 1rem;
    transition: all 0.3s ease;
    border: none;
    cursor: pointer;
}

.btn:hover {
    background: #1E3A5F;
    color: white;
}

.btn-emergency {
    background: #FF6F61;
}

.btn-emergency:hover {
    background: #e05a50;
}

.navbar {
    position: fixed;
    top: 0;
    width: 100%;
    background: rgba(255, 255, 255, 0.95);
    box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
    z-index: 1000;
    padding: 15px 0;
}

.nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo h1 {
    color: #26A69A;
    font-size: 1.6rem;
    font-weight: 800;
}

.nav-links a {
    margin: 0 15px;
    color: #1E3A5F;
    font-weight: 600;
    font-size: 1rem;
}

.hero {
    background: linear-gradient(135deg, rgba(30, 58, 95, 0.85), rgba(38, 166, 154, 0.8));
    color: white;
    padding: 150px 0 80px;
    text-align: center;
}

.hero-content {
    max-width: 800px;
    margin: 0 auto;
}

.hero h1 {
    color: white;
    font-size: 3.2rem;
    margin-bottom: 20px;
}

.hero p {
    font-size: 1.3rem;
    margin: 0 auto 40px;
    max-width: 650px;
}

.hero-btns {
    display: flex;
    justify-content: center;
    gap: 15px;
    flex-wrap: wrap;
}

.stats {
    background: white;
    padding: 20px 0;
}

.stats-container {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    gap: 15px;
}

.stat-item {
    text-align: center;
    padding: 15px;
    min-width: 180px;
}

.stat-number {
    font-size: 2.2rem;
    font-weight: 800;
    color: #26A69A;
    margin-bottom: 8px;
}

.stat-label {
    font-size: 1rem;
    color: #666;
    font-weight: 600;
}

.card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 25px;
    margin-top: 30px;
}

.card {
    background: white;
    border-radius: 12px;
    padding: 30px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
}

.card-icon {
    font-size: 3rem;
    margin-bottom: 20px;
    color: #26A69A;
}

.card-content {
    flex-grow: 1;
}

.team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 30px;
    margin-top: 40px;
}

.team-member {
    text-align: center;
    background: white;
    border-radius: 12px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
}

.team-photo {
    width: 100%;
    height: 240px;
    object-fit: cover;
    border-bottom: 3px solid #26A69A;
}

.team-info {
    padding: 20px;
}

.team-role {
    color: #26A69A;
    font-weight: 600;
    font-size: 1rem;
    margin-bottom: 10px;
}

.testimonials-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
    gap: 25px;
    margin-top: 40px;
}

.testimonial {
    background: white;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
    position: relative;
}

.testimonial:before {
    content: '"';
    font-size: 6rem;
    color: #E8F4F8;
    position: absolute;
    top: 15px;
    left: 20px;
    font-family: serif;
}

.testimonial-text {
    font-size: 1rem;
    font-style: italic;
    margin-bottom: 20px;
    color: #333;
}

.testimonial-author {
    display: flex;
    align-items: center;
}

.author-name {
    font-weight: 700;
    color: #1E3A5F;
    font-size: 1rem;
}

.contact-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
    gap: 30px;
    margin-top: 40px;
}

.contact-card {
    background: white;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
}

.contact-info {
    margin-bottom: 20px;
}

.contact-item {
    display: flex;
    margin-bottom: 15px;
}

.contact-icon {
    font-size: 1.4rem;
    color: #26A69A;
    min-width: 35px;
    margin-top: 5px;
}

.contact-details p {
    margin: 0;
    font-size: 1rem;
}

.contact-btns {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 20px;
}

.hours-list {
    list-style: none;
    padding: 0;
}

.hours-list li {
    display: flex;
    justify-content: space-between;
    padding: 10px 0;
    border-bottom: 1px solid #E8F4F8;
}

.hours-list li:last-child {
    border-bottom: none;
}

.hours-list .day {
    font-weight: 600;
}

.map-container {
    margin-top: 30px;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
    height: 360px;
}

.form-container {
    background: white;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
    margin-top: 40px;
}

.form-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 20px;
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    margin-bottom: 6px;
    font-weight: 600;
    color: #1E3A5F;
}

.form-group input,
.form-group select,
.form-group textarea {
    width: 100%;
    padding: 12px 15px;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 1rem;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
    border-color: #26A69A;
    outline: none;
}

textarea {
    min-height: 120px;
    resize: vertical;
}

.submit-btn {
    width: 100%;
    padding: 14px;
    font-size: 1rem;
}

.footer {
    background: #0D1C30;
    color: white;
    padding: 50px 0 20px;
}

.footer-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 30px;
    margin-bottom: 40px;
}

.footer-col h3 {
    color: white;
    margin-bottom: 20px;
    font-size: 1.4rem;
}

.footer-links {
    list-style: none;
    padding: 0;
}

.footer-links li {
    margin-bottom: 10px;
}

.footer-links a {
    color: #b0c4de;
}

.footer-links a:hover {
    color: white;
}

.contact-info p {
    display: flex;
    align-items: flex-start;
    margin-bottom: 12px;
    color: #b0c4de;
}

.social-links {
    display: flex;
    gap: 12px;
    margin-top: 15px;
}

.social-icon {
    width: 40px;
    height: 40px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 50%;
    color: white;
    font-size: 1.2rem;
    display: flex;
    align-items: center;
    justify-content: center;
}

.social-icon:hover {
    background: #26A69A;
}

.copyright {
    text-align: center;
    padding-top: 20px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    color: #b0c4de;
    font-size: 0.9rem;
}

@media (max-width: 768px) {
    h1 { font-size: 2.5rem; }
    h2 { font-size: 2rem; }
    h3 { font-size: 1.6rem; }
    .hero { padding: 120px 0 60px; }
    .section { padding: 40px 0; }
    .btn { padding: 10px 20px; font-size: 0.9rem; }
    .map-container { height: 300px; }
}
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
            <a href="#about">with</a>
            <a href="#services">Services</a>
            <a href="#team">Team</a>
            <a href="#testimonials">Testimonials</a>
            <a href="#contact">Contact</a>
            <a href="#contact" class="btn">Get Help</a>
        </div>
    </div>
</nav>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero" id="home">
    <div class="container hero-content">
        <h1>Your Journey to Wellness Begins Here</h1>
        <p>SafeSpace provides compassionate mental health support and counseling services for individuals and families in Kenya.</p>
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
            <div></div>
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: 40px; align-items: center;">
            <div style="flex: 1; min-width: 280px;">
                <h3>Creating a Safe Space for Healing</h3>
                <p>Founded in 2023, SafeSpace Organisation is a leading mental health provider in Nairobi, Kenya. We offer professional counseling services, support groups, and mental health education to individuals and communities facing life's challenges.</p>
                <p>Our mission is to break down the stigma surrounding mental health in Kenya and provide accessible, affordable care to all who need it.</p>
                <p>We believe that mental wellness is a fundamental human right and are committed to creating a safe, supportive environment where healing can begin.</p>
                <div style="margin-top: 30px;">
                    <a href="#services" class="btn">Our Services</a>
                </div>
            </div>
            <div style="flex: 1; min-width: 280px;">
                <div style="border-radius: 15px; overflow: hidden; box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);">
                    <img src="https://images.unsplash.com/photo-1527613426441-4da17471b66d?crop=entropy&cs=tinysrgb&fit=crop&h=400&w=600" 
                         style="width: 100%; height: 360px; object-fit: cover;" alt="SafeSpace Counseling">
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
            < underlined>Our Services</h2>
            <p>Comprehensive mental health support tailored to your unique needs</p>
            <div></div>
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
 “

            <div class="team-grid">
                <div class="team-member">
                    <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?crop=entropy&cs=tinysrgb&fit=crop&h=360&w=360" 
                         class="team-photo" alt="Dr. Amina Hassan">
                    <div class="team-info">
                        <h3>Dr. Amina Hassan</h3>
                        <div class="team-role">Clinical Director</div>
                        <p>PhD in Clinical Psychology with 15+ years experience.</p>
                    </div>
                </div>
                <div class="team-member">
                    <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?crop=entropy&cs=tinysrgb&fit=crop&h=360&w=360" 
                         class="team-photo" alt="James Omondi">
                    <div class="team-info">
                        <h3>James Omondi</h3>
                        <div class="team-role">Senior Therapist</div>
                        <p>Specializes in trauma counseling and PTSD treatment.</p>
                    </div>
                </div>
                <div class="team-member">
                    <img src="https://images.unsplash.com/photo-1590086782792-42dd2350140d?crop=entropy&cs=tinysrgb&fit=crop&h=360&w=360" 
                         class="team-photo" alt="Sarah Wanjiku">
                    <div class="team-info">
                        <h3>Sarah Wanjiku</h3>
                        <div class="team-team">Family Therapist</div>
                        <p>Expert in family systems and relationship counseling.</p>
                    </div>
                </div>
                <div class="team-member">
                    <img src="https://images.unsplash.com/photo-1564564321837-a57b7070ac4f?crop=entropy&cs=tinysrgb&fit=crop&h=360&w=360" 
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
</div>
""", unsafe_allow_html=True)

# Testimonials Section
st.markdown("""
<div class="section" id="testimonials" style="background: #F5FBFD;">
    <div class="container">
        <div class="section-title">
            <h2>Client Testimonials</h2>
            <p>Hear from those who have found hope and healing</p>
            <div></div>
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
            <div></div>
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
                <div style="margin-top: 20px; padding: 15px; background: rgba(255, 111, 97, 0.05); border-radius: 10px;">
                    <h4 style="color: #FF6F61; margin-bottom: 10px;">Emergency Contact</h4>
                    <p style="font-size: 1rem; margin-bottom: 15px;">24/7 crisis support available</p>
                    <a href="tel:+254781095919" class="btn btn-emergency">Emergency Call</a>
                </div>
            </div>
        </div>
        <h3 style="color: #1E3A5F; margin-top: 50px; text-align: center;">Visit Our Center</h3>
        <p style="text-align: center; font-size: 1.1rem; margin-bottom: 20px;">Find us at Greenhouse Plaza, Ngong Road, Nairobi</p>
""", unsafe_allow_html=True)

# Map with Streamlit's native map component
try:
    map_data = pd.DataFrame({'lat': [-1.2985], 'lon': [36.7848]})
    st.map(map_data, zoom=14, use_container_width=True)
except Exception:
    st.markdown("<p style='color: #FF6F61; font-size: 1rem; text-align: center;'>Unable to display map. Visit us at Greenhouse Plaza, Ngong Road, Nairobi.</p>", unsafe_allow_html=True)

# Contact Form with Streamlit
st.markdown("""
<div class="form-container">
    <h3 style="text-align: center; margin-bottom: 30px;">Send Us a Message</h3>
""", unsafe_allow_html=True)

with st.form("contact_form", clear_on_submit=True):
    st.markdown('<div class="form-grid">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name *", placeholder="Enter your name")
        email = st.text_input("Email Address *", placeholder="Enter your email")
    with col2:
        phone = st.text_input("Phone Number", placeholder="Enter your phone number")
        subject = st.selectbox("Subject", ["General Inquiry", "Book Appointment", "Group Program", "Corporate Wellness", "Other"])
    st.markdown('</div>', unsafe_allow_html=True)
    message = st.text_area("Your Message *", placeholder="Type your message here")
    submit = st.form_submit_button("Send Message", use_container_width=True)
    if submit:
        if name and email and message and email.count('@') == 1:
            st.success(f"Thank you, {name}! Your message has been sent. We'll contact you soon.")
            st.balloons()
        else:
            st.error("Please provide a valid name, email, and message.")

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <div class="container">
        <div class="footer-grid">
            <div class="footer-col">
                <h3>SafeSpace Organisation</h3>
                <p>Providing compassionate mental health support and counseling services to the Nairobi community since 2023.</p>
                <div class="social-links">
                    <a href="#" class="social-icon">f</a>
                    <a href="#" class="social-icon">t</a>
                    <a href="#" class="social-icon">in</a>
                    <a href="#" class="social-icon">ig</a>
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
                <a href="#" class="btn" style="margin-top: 15px;">Make a Donation</a>
            </div>
        </div>
        <div class="copyright">
            <p>© 2023-2025 SafeSpace Organisation. All rights reserved.</p>
            <p>Mental Health Support in Nairobi, Kenya</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
