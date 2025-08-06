import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="SafeSpace Organisation | Mental Health Support",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for a client-friendly, calming design
st.markdown("""
<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Arial', sans-serif;
    color: #333333;
    line-height: 1.6;
    background-color: #F5FBFD;
}

h1, h2, h3, h4 {
    color: #1E3A5F;
    font-weight: 600;
}

h1 { font-size: 2.8rem; margin-bottom: 1rem; }
h2 { font-size: 2.2rem; margin-bottom: 1rem; }
h3 { font-size: 1.6rem; margin-bottom: 0.8rem; }
h4 { font-size: 1.3rem; margin-bottom: 0.6rem; }
p { margin-bottom: 1rem; font-size: 1rem; }

a {
    color: #26A69A;
    text-decoration: none;
}

a:hover {
    color: #1E3A5F;
    text-decoration: underline;
}

.container {
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 15px;
}

.section {
    padding: 50px 0;
}

.section-title {
    text-align: center;
    margin-bottom: 30px;
}

.section-title h2 {
    padding-bottom: 8px;
}

.section-title div {
    width: 60px;
    height: 3px;
    background: #26A69A;
    margin: 0 auto;
    border-radius: 2px;
}

.btn {
    display: inline-block;
    padding: 10px 25px;
    background: #26A69A;
    color: white;
    border-radius: 20px;
    font-weight: 600;
    font-size: 0.95rem;
    border: none;
    cursor: pointer;
    transition: background 0.3s ease;
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
    background: rgba(255, 255, 255, 0.97);
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
    z-index: 1000;
    padding: 12px 0;
}

.nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo h1 {
    color: #26A69A;
    font-size: 1.5rem;
    font-weight: 700;
}

.nav-links a {
    margin: 0 12px;
    color: #1E3A5F;
    font-weight: 600;
    font-size: 0.95rem;
}

.hero {
    background: linear-gradient(135deg, rgba(30, 58, 95, 0.8), rgba(38, 166, 154, 0.7));
    color: white;
    padding: 120px 0 60px;
    text-align: center;
}

.hero-content {
    max-width: 700px;
    margin: 0 auto;
}

.hero h1 {
    color: white;
    font-size: 2.8rem;
    margin-bottom: 15px;
}

.hero p {
    font-size: 1.2rem;
    margin: 0 auto 30px;
    max-width: 600px;
}

.hero-btns {
    display: flex;
    justify-content: center;
    gap: 12px;
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
    gap: 12px;
}

.stat-item {
    text-align: center;
    padding: 12px;
    min-width: 160px;
}

.stat-number {
    font-size: 2rem;
    font-weight: 700;
    color: #26A69A;
    margin-bottom: 6px;
}

.stat-label {
    font-size: 0.95rem;
    color: #666;
    font-weight: 600;
}

.service-container {
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    align-items: stretch;
}

.service-card {
    flex: 1;
    min-width: 260px;
    background: white;
    border-radius: 10px;
    padding: 25px;
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.05);
}

.service-card h3 {
    margin-bottom: 15px;
}

.service-card ul {
    list-style: none;
    padding: 0;
    margin-bottom: 20px;
}

.service-card li {
    font-size: 0.95rem;
    margin-bottom: 8px;
    color: #333;
}

.team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 25px;
    margin-top: 30px;
}

.team-member {
    text-align: center;
    background: white;
    border-radius: 10px;
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.05);
}

.team-photo {
    width: 100%;
    height: 220px;
    object-fit: cover;
    border-bottom: 2px solid #26A69A;
}

.team-info {
    padding: 15px;
}

.team-role {
    color: #26A69A;
    font-weight: 600;
    font-size: 0.95rem;
    margin-bottom: 8px;
}

.testimonials-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 20px;
    margin-top: 30px;
}

.testimonial {
    background: white;
    padding: 25px;
    border-radius: 10px;
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.05);
}

.testimonial-text {
    font-size: 0.95rem;
    font-style: italic;
    margin-bottom: 15px;
    color: #333;
}

.testimonial-author {
    display: flex;
    align-items: center;
}

.author-name {
    font-weight: 600;
    color: #1E3A5F;
    font-size: 0.95rem;
}

.contact-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 25px;
    margin-top: 30px;
}

.contact-card {
    background: white;
    padding: 25px;
    border-radius: 10px;
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.05);
}

.contact-info {
    margin-bottom: 15px;
}

.contact-item {
    display: flex;
    margin-bottom: 12px;
    align-items: flex-start;
}

.contact-icon {
    font-size: 1.3rem;
    color: #26A69A;
    min-width: 30px;
    margin-top: 4px;
}

.contact-details p {
    margin: 0;
    font-size: 0.95rem;
}

.contact-btns {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 15px;
}

.hours-list {
    list-style: none;
    padding: 0;
}

.hours-list li {
    display: flex;
    justify-content: space-between;
    padding: 8px 0;
    border-bottom: 1px solid #E8F4F8;
}

.hours-list li:last-child {
    border-bottom: none;
}

.hours-list .day {
    font-weight: 600;
}

.map-container {
    margin-top: 25px;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.05);
    height: 320px;
}

.form-container {
    background: white;
    padding: 25px;
    border-radius: 10px;
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.05);
    margin-top: 30px;
}

.form-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 15px;
    margin-bottom: 15px;
}

.form-group label {
    display: block;
    margin-bottom: 5px;
    font-weight: 600;
    color: #1E3A5F;
    font-size: 0.95rem;
}

.form-group input,
.form-group select,
.form-group textarea {
    width: 100%;
    padding: 10px 12px;
    border: 1px solid #ddd;
    border-radius: 6px;
    font-size: 0.95rem;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
    border-color: #26A69A;
    outline: none;
}

textarea {
    min-height: 100px;
    resize: vertical;
}

.submit-btn {
    width: 100%;
    padding: 12px;
    font-size: 0.95rem;
}

.resources-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 20px;
    margin-top: 25px;
}

.resource-card {
    background: white;
    border-radius: 10px;
    padding: 25px;
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.05);
}

.support-container {
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    align-items: stretch;
}

.support-card {
    flex: 1;
    min-width: 260px;
    background: white;
    border-radius: 10px;
    padding: 25px;
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.05);
}

.footer {
    background: #1E3A5F;
    color: white;
    padding: 40px 0 15px;
}

.footer-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 25px;
    margin-bottom: 30px;
}

.footer-col h3 {
    color: white;
    margin-bottom: 15px;
    font-size: 1.3rem;
}

.footer-links {
    list-style: none;
    padding: 0;
}

.footer-links li {
    margin-bottom: 8px;
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
    margin-bottom: 10px;
    color: #b0c4de;
    font-size: 0.95rem;
}

.social-links {
    display: flex;
    gap: 10px;
    margin-top: 12px;
}

.social-icon {
    width: 36px;
    height: 36px;
    background: rgba(255, 255, 255, 0.15);
    border-radius: 50%;
    color: white;
    font-size: 1.1rem;
    display: flex;
    align-items: center;
    justify-content: center;
}

.social-icon:hover {
    background: #26A69A;
}

.copyright {
    text-align: center;
    padding-top: 15px;
    border-top: 1px solid rgba(255, 255, 255, 0.15);
    color: #b0c4de;
    font-size: 0.9rem;
}

@media (max-width: 768px) {
    h1 { font-size: 2.2rem; }
    h2 { font-size: 1.8rem; }
    h3 { font-size: 1.4rem; }
    .hero { padding: 100px 0 50px; }
    .section { padding: 30px 0; }
    .btn { padding: 8px 20px; font-size: 0.9rem; }
    .map-container { height: 280px; }
    .container { padding: 0 10px; }
    .service-container, .support-container { flex-direction: column; }
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
            <a href="#about">About</a>
            <a href="#services">Services</a>
            <a href="#community">Community</a>
            <a href="#resources">Resources</a>
            <a href="#support">Support</a>
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
        <h1>Welcome to SafeSpace</h1>
        <p>Compassionate mental health support for you and your loved ones in Kenya.</p>
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
            <div class="stat-number">2,500+</div>
            <div class="stat-label">Clients Supported</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">15+</div>
            <div class="stat-label">Professional Staff</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">200+</div>
            <div class="stat-label">Workshops Held</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">24/7</div>
            <div class="stat-label">Crisis Support</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# About Section
st.markdown("""
<div class="section" id="about" style="background: #E8F4F8;">
    <div class="container">
        <div class="section-title">
            <h2>About SafeSpace</h2>
            <p>Founded by Jerim Owino and Hamdi Roble</p>
            <div></div>
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: 30px; align-items: center;">
            <div style="flex: 1; min-width: 260px; padding: 20px; background: white; border-radius: 10px; box-shadow: 0 6px 15px rgba(0, 0, 0, 0.05);">
                <h3>Our Mission</h3>
                <p>Founded in 2023 by Jerim Owino and Hamdi Roble, SafeSpace Organisation is committed to breaking the stigma around mental health in Kenya. We provide compassionate, accessible counseling to over 2,500 clients, creating a safe space for healing.</p>
                <p>Our vision is a Kenya where mental wellness is a priority for all, supported by culturally sensitive, evidence-based care.</p>
                <div style="margin-top: 20px;">
                    <a href="#services" class="btn">Discover Our Services</a>
                </div>
            </div>
            <div style="flex: 1; min-width: 260px;">
                <div style="border-radius: 10px; overflow: hidden; box-shadow: 0 6px 15px rgba(0, 0, 0, 0.05);">
                    <img src="https://images.unsplash.com/photo-1527613426441-4da17471b66d?crop=entropy&cs=tinysrgb&fit=crop&h=320&w=500" 
                         style="width: 100%; height: 320px; object-fit: cover;" alt="SafeSpace Counseling">
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Services Section
st.markdown("""
<div class="section" id="services">
    <div class="container">
        <div class="section-title">
            <h2>Our Services</h2>
            <p>Personalized mental health support tailored to your needs</p>
            <div></div>
        </div>
        <div class="service-container">
            <div class="service-card">
                <h3>Individual Counseling</h3>
                <p>One-on-one sessions with licensed therapists to address personal challenges such as anxiety, depression, or trauma.</p>
                <ul>
                    <li>Personalized therapy plans</li>
                    <li>CBT and other evidence-based methods</li>
                    <li>Confidential and supportive environment</li>
                </ul>
                <a href="#contact" class="btn">Book a Session</a>
            </div>
            <div class="service-card">
                <h3>Family Therapy</h3>
                <p>Support for families to improve communication, resolve conflicts, and navigate life transitions together.</p>
                <ul>
                    <li>Strengthen family bonds</li>
                    <li>Address relationship challenges</li>
                    <li>Flexible session formats</li>
                </ul>
                <a href="#contact" class="btn">Schedule Family Therapy</a>
            </div>
            <div class="service-card">
                <h3>Group Support</h3>
                <p>Join therapeutic groups to connect with others facing similar experiences, such as grief or addiction recovery.</p>
                <ul>
                    <li>Peer support and shared healing</li>
                    <li>Facilitated by trained professionals</li>
                    <li>Regular group sessions</li>
                </ul>
                <a href="#contact" class="btn">Join a Group</a>
            </div>
        </div>
        <div class="service-container" style="margin-top: 30px;">
            <div class="service-card">
                <h3>Crisis Intervention</h3>
                <p>Immediate support for individuals experiencing mental health emergencies or acute distress.</p>
                <ul>
                    <li>24/7 crisis hotline</li>
                    <li>Rapid response and stabilization</li>
                    <li>Follow-up care planning</li>
                </ul>
                <a href="tel:+254781095919" class="btn btn-emergency">Call Now</a>
            </div>
            <div class="service-card">
                <h3>Corporate Wellness</h3>
                <p>Workshops and counseling to promote employee mental health and workplace well-being.</p>
                <ul>
                    <li>Stress management workshops</li>
                    <li>Employee counseling programs</li>
                    <li>Customized corporate plans</li>
                </ul>
                <a href="#contact" class="btn">Contact for Corporate</a>
            </div>
            <div class="service-card">
                <h3>Educational Workshops</h3>
                <p>Community programs to raise mental health awareness and build emotional resilience.</p>
                <ul>
                    <li>Stress and coping skills training</li>
                    <li>Mental health education</li>
                    <li>Open to all community members</li>
                </ul>
                <a href="#contact" class="btn">Sign Up for Workshops</a>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Community Section
st.markdown("""
<div class="section" id="community" style="background: #E8F4F8;">
    <div class="container">
        <div class="section-title">
            <h2>Our Community</h2>
            <p>Building a stronger, healthier Kenya together</p>
            <div></div>
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: 30px; align-items: center;">
            <div style="flex: 1; min-width: 260px; padding: 20px; background: white; border-radius: 10px; box-shadow: 0 6px 15px rgba(0, 0, 0, 0.05);">
                <h3>Community Outreach</h3>
                <p>We partner with schools, churches, and community centers to offer free mental health workshops, screenings, and awareness campaigns across Nairobi.</p>
                <p>With over 200 workshops conducted, we’ve empowered thousands to prioritize mental wellness and reduce stigma.</p>
                <p>Join us as a volunteer, partner, or participant to make a difference in your community.</p>
                <div style="margin-top: 20px;">
                    <a href="#contact" class="btn">Get Involved</a>
                </div>
            </div>
            <div style="flex: 1; min-width: 260px;">
                <div style="border-radius: 10px; overflow: hidden; box-shadow: 0 6px 15px rgba(0, 0, 0, 0.05);">
                    <img src="https://images.unsplash.com/photo-1523240795612-9a054b0db644?crop=entropy&cs=tinysrgb&fit=crop&h=320&w=500" 
                         style="width: 100%; height: 320px; object-fit: cover;" alt="Community Workshop">
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Resources Section
st.markdown("""
<div class="section" id="resources">
    <div class="container">
        <div class="section-title">
            <h2>Resources</h2>
            <p>Tools and tips for your mental wellness journey</p>
            <div></div>
        </div>
        <div class="resources-container">
            <div class="resource-card">
                <h3>Self-Care Tips</h3>
                <p>Practice mindfulness, journaling, or breathing exercises to manage stress and boost emotional resilience.</p>
                <a href="#contact" class="btn">Request a Self-Care Guide</a>
            </div>
            <div class="resource-card">
                <h3>Mental Health Articles</h3>
                <p>Read our expert-written articles on anxiety, depression, and coping strategies tailored for Kenyans.</p>
                <a href="#contact" class="btn">Access Articles</a>
            </div>
            <div class="resource-card">
                <h3>External Support</h3>
                <p>Explore trusted mental health resources and hotlines available in Kenya for additional support.</p>
                <a href="#contact" class="btn">Learn More</a>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Support Options Section
st.markdown("""
<div class="section" id="support" style="background: #E8F4F8;">
    <div class="container">
        <div class="section-title">
            <h2>Support Options</h2>
            <p>Immediate help when you need it most</p>
            <div></div>
        </div>
        <div class="support-container">
            <div class="support-card">
                <h3>24/7 Crisis Hotline</h3>
                <p>Call our crisis hotline for immediate support during a mental health emergency.</p>
                <a href="tel:+254781095919" class="btn btn-emergency">Call +254 781 095 919</a>
            </div>
            <div class="support-card">
                <h3>Online Chat Support</h3>
                <p>Connect with a counselor via our secure online chat for quick, confidential support.</p>
                <a href="#contact" class="btn">Start a Chat</a>
            </div>
            <div class="support-card">
                <h3>In-Person Sessions</h3>
                <p>Visit our Nairobi center for face-to-face counseling with our experienced therapists.</p>
                <a href="#contact" class="btn">Book an Appointment</a>
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
            <p>Meet our dedicated mental health professionals</p>
            <div></div>
        </div>
        <div class="team-grid">
            <div class="team-member">
                <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?crop=entropy&cs=tinysrgb&fit=crop&h=300&w=300" 
                     class="team-photo" alt="Dr. Amina Hassan">
                <div class="team-info">
                    <h3>Dr. Amina Hassan</h3>
                    <div class="team-role">Clinical Director</div>
                    <p>PhD in Clinical Psychology with 15+ years experience.</p>
                </div>
            </div>
            <div class="team-member">
                <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?crop=entropy&cs=tinysrgb&fit=crop&h=300&w=300" 
                     class="team-photo" alt="James Omondi">
                <div class="team-info">
                    <h3>James Omondi</h3>
                    <div class="team-role">Senior Therapist</div>
                    <p>Specializes in trauma counseling and PTSD treatment.</p>
                </div>
            </div>
            <div class="team-member">
                <img src="https://images.unsplash.com/photo-1590086782792-42dd2350140d?crop=entropy&cs=tinysrgb&fit=crop&h=300&w=300" 
                     class="team-photo" alt="Sarah Wanjiku">
                <div class="team-info">
                    <h3>Sarah Wanjiku</h3>
                    <div class="team-role">Family Therapist</div>
                    <p>Expert in family systems and relationship counseling.</p>
                </div>
            </div>
            <div class="team-member">
                <img src="https://images.unsplash.com/photo-1564564321837-a57b7070ac4f?crop=entropy&cs=tinysrgb&fit=crop&h=300&w=300" 
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
<div class="section" id="testimonials" style="background: #E8F4F8;">
    <div class="container">
        <div class="section-title">
            <h2>Client Testimonials</h2>
            <p>Hear from those who have found hope and healing</p>
            <div></div>
        </div>
        <div class="testimonials-container">
            <div class="testimonial">
                <div class="testimonial-text">
                    SafeSpace helped me through the darkest time of my life. The therapists showed incredible compassion and gave me tools to manage my anxiety that I still use every day.
                </div>
                <div class="testimonial-author">
                    <div class="author-name">Mariam K.</div>
                </div>
            </div>
            <div class="testimonial">
                <div class="testimonial-text">
                    After losing my job, I felt completely hopeless. The counseling I received at SafeSpace helped me rebuild my confidence and find a new career path.
                </div>
                <div class="testimonial-author">
                    <div class="author-name">John W.</div>
                </div>
            </div>
            <div class="testimonial">
                <div class="testimonial-text">
                    Family therapy saved our relationships. We learned how to communicate effectively and understand each other's perspectives.
                </div>
                <div class="testimonial-author">
                    <div class="author-name">The Ochieng Family</div>
                </div>
            </div>
            <div class="testimonial">
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
""", unsafe_allow_html=True)

# Contact Section
st.markdown("""
<div class="section" id="contact">
    <div class="container">
        <div class="section-title">
            <h2>Connect With Us</h2>
            <p>We're here to support you every step of the way</p>
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
                <div style="margin-top: 20px; padding: 15px; background: rgba(255, 111, 97, 0.1); border-radius: 8px;">
                    <h4 style="color: #FF6F61; margin-bottom: 10px;">24/7 Emergency Support</h4>
                    <p style="font-size: 0.95rem; margin-bottom: 15px;">We're here for you anytime.</p>
                    <a href="tel:+254781095919" class="btn btn-emergency">Emergency Call</a>
                </div>
            </div>
        </div>
        <h3 style="color: #1E3A5F; margin-top: 40px; text-align: center;">Visit Our Center</h3>
        <p style="text-align: center; font-size: 1rem; margin-bottom: 20px;">Find us at Greenhouse Plaza, Ngong Road, Nairobi</p>
""", unsafe_allow_html=True)

# Map
try:
    map_data = pd.DataFrame({'lat': [-1.2985], 'lon': [36.7848]})
    st.map(map_data, zoom=14, use_container_width=True)
except Exception:
    st.markdown("<p style='color: #FF6F61; font-size: 0.95rem; text-align: center;'>Unable to display map. Visit us at Greenhouse Plaza, Ngong Road, Nairobi.</p>", unsafe_allow_html=True)

# Contact Form
st.markdown("""
<div class="form-container">
    <h3 style="text-align: center; margin-bottom: 25px;">Send Us a Message</h3>
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
    message = st.text_area("Your Message *", placeholder="How can we support you?")
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
                <p>Compassionate mental health support in Nairobi, Kenya, since 2023.</p>
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
                    <li><a href="#community">Community</a></li>
                    <li><a href="#resources">Resources</a></li>
                    <li><a href="#support">Support</a></li>
                    <li><a href="#team">Team</a></li>
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
                <a href="#" class="btn" style="margin-top: 12px;">Make a Donation</a>
            </div>
        </div>
        <div class="copyright">
            <p>© 2023-2025 SafeSpace Organisation. All rights reserved.</p>
            <p>Mental Health Support in Nairobi, Kenya</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
