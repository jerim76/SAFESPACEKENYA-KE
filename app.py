<app.py>
import streamlit as st
import pandas as pd
import re
from datetime import datetime

# Custom CSS styling
st.markdown(
    """
    <style>
    :root {
        --primary: #26A69A;
        --accent: #FF6F61;
    }
    
    .header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, var(--primary), #1b7a71);
        color: white;
        border-radius: 0 0 20px 20px;
        margin-bottom: 2rem;
    }
    
    .hero {
        text-align: center;
        padding: 3rem 2rem;
        margin: 2rem 0;
        background: linear-gradient(rgba(255,255,255,0.8), rgba(255,255,255,0.8)), 
                    url('https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=1200');
        background-size: cover;
        border-radius: 15px;
    }
    
    .section {
        padding: 2rem;
        margin: 2rem 0;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-left: 5px solid var(--primary);
    }
    
    .testimonial-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid var(--accent);
        margin: 1rem 0;
    }
    
    .btn {
        background-color: var(--primary);
        color: white !important;
        padding: 0.5rem 1rem;
        text-align: center;
        border-radius: 30px;
        display: inline-block;
        margin: 0.5rem;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
    }
    
    .btn:hover {
        background-color: var(--accent);
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    .form-container {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        margin-top: 1rem;
    }
    
    footer {
        text-align: center;
        padding: 2rem;
        margin-top: 3rem;
        background-color: var(--primary);
        color: white;
        border-radius: 20px 20px 0 0;
    }
    
    .chat-container {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 1rem;
        max-height: 400px;
        overflow-y: auto;
        margin-bottom: 1rem;
    }
    
    .user-msg {
        background-color: #e3f2fd;
        padding: 0.5rem 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        text-align: right;
    }
    
    .bot-msg {
        background-color: #f5f5f5;
        padding: 0.5rem 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Header
st.markdown(
    """
    <div class="header">
        <h1>SafeSpace Organisation</h1>
        <p>Empowering Minds, Nurturing Hope Since 2023</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Hero Section
st.markdown(
    """
    <div class="hero">
        <h2>Healing Minds, Restoring Lives</h2>
        <div>
            <a href="#about-section" class="btn">About Us</a>
            <a href="#services-section" class="btn">Our Services</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# About Section
st.markdown('<a name="about-section"></a>', unsafe_allow_html=True)
with st.container():
    st.subheader("About SafeSpace")
    st.write("""
    SafeSpace Organisation was founded in 2023 by Jerim Owino and Hamdi Roble with a mission to provide accessible 
    mental health care to communities across Kenya. We believe in creating a supportive environment where individuals 
    can heal, grow, and find hope through professional counseling and community support.
    """)
    st.write("""
    Our founders bring together decades of experience in clinical psychology and community health initiatives, 
    creating a unique approach that combines evidence-based therapies with culturally sensitive care.
    """)

# Services Section
st.markdown('<a name="services-section"></a>', unsafe_allow_html=True)
with st.container():
    st.subheader("Our Services")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Individual Counseling**")
        st.write("One-on-one sessions with licensed therapists")
    
    with col2:
        st.markdown("**Group Therapy**")
        st.write("Support groups for shared experiences")
    
    with col3:
        st.markdown("**Online Counseling**")
        st.write("Virtual sessions for remote access")
    
    with st.expander("Register for Services"):
        with st.form("service_registration"):
            name = st.text_input("Full Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone Number")
            service = st.selectbox("Interested In", 
                                   ["Individual Counseling", "Group Therapy", "Online Counseling"])
            submitted = st.form_submit_button("Submit")
            
            if submitted:
                if not all([name, email, phone]):
                    st.error("Please fill all fields")
                elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    st.error("Please enter a valid email address")
                else:
                    st.success(f"Thank you {name}! We'll contact you by August 7, 2025 to schedule your {service}")

# Testimonials
with st.container():
    st.subheader("Client Experiences")
    st.markdown(
        """
        <div class="testimonial-card">
            <p>"SafeSpace helped me regain control of my life during a difficult divorce. 
            My counselor provided tools that I still use daily."</p>
            <p><strong>- Wanjiku M., Nairobi</strong></p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Events
with st.container():
    st.subheader("Upcoming Events")
    event_col1, event_col2 = st.columns([1, 3])
    with event_col1:
        st.markdown("**Aug 10, 2025**")
    with event_col2:
        st.markdown("**Stress Management Workshop**")
        st.caption("10:00 AM - 12:00 PM | Community Hall, Greenhouse Plaza")
        st.markdown("[Register Here](#events-section)")

# Partnerships
with st.container():
    st.subheader("Our Partners")
    st.write("We collaborate with leading institutions to expand mental health access:")
    st.markdown("- Kenyatta National Hospital")
    st.markdown("- Ministry of Health Mental Health Unit")
    st.markdown("- University of Nairobi Psychology Department")
    
    with st.expander("Partner With Us"):
        with st.form("partner_form"):
            p_name = st.text_input("Organization Name")
            p_contact = st.text_input("Contact Person")
            p_email = st.text_input("Email")
            p_phone = st.text_input("Phone")
            submitted = st.form_submit_button("Submit Inquiry")
            
            if submitted:
                if not all([p_name, p_contact, p_email, p_phone]):
                    st.error("Please fill all fields")
                elif not re.match(r"[^@]+@[^@]+\.[^@]+", p_email):
                    st.error("Please enter a valid email address")
                else:
                    st.success("Thank you for your interest! Our partnership team will contact you by August 8, 2025")

# Blog
with st.container():
    st.subheader("Mental Health Resources")
    with st.expander("Coping with Stress - by Dr. Amina"):
        st.write("""
        Stress is a natural response to life's challenges, but chronic stress can impact both physical and mental health. 
        Here are evidence-based techniques to manage stress:
        
        1. **Mindful Breathing**: Practice 5-5-7 breathing (inhale 5s, hold 5s, exhale 7s)
        2. **Physical Activity**: 30 minutes of daily movement reduces cortisol
        3. **Structured Problem Solving**: Break challenges into manageable steps
        4. **Social Connection**: Reach out to trusted friends or support groups
        
        Remember that seeking professional help is a sign of strength, not weakness. Our counselors are available for 
        confidential consultations.
        """)

# Mood Tracker
with st.container():
    st.subheader("Mood Tracker")
    st.write("Monitor your emotional wellbeing over time")
    
    with st.form("mood_form"):
        date = st.date_input("Date", datetime(2025, 8, 6))
        mood = st.slider("Mood Rating (1 = Low, 5 = High)", 1, 5, 3)
        notes = st.text_area("Notes")
        submitted = st.form_submit_button("Save Entry")
        
        if submitted:
            new_entry = pd.DataFrame({
                "Date": [date],
                "Mood": [mood],
                "Notes": [notes]
            })
            
            try:
                # Initialize session state for entries
                if "mood_data" not in st.session_state:
                    st.session_state.mood_data = pd.DataFrame(columns=["Date", "Mood", "Notes"])
                
                # Add new entry
                st.session_state.mood_data = pd.concat([st.session_state.mood_data, new_entry], ignore_index=True)
                st.success("Entry saved successfully!")
            except Exception as e:
                st.error(f"Error saving entry: {str(e)}")
    
    if "mood_data" in st.session_state and not st.session_state.mood_data.empty:
        st.line_chart(st.session_state.mood_data.set_index("Date")["Mood"])
        
        # Export functionality
        if st.button("Export to CSV"):
            try:
                csv = st.session_state.mood_data.to_csv(index=False)
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name="mood_tracker.csv",
                    mime="text/csv"
                )
            except Exception as e:
                st.error(f"Export error: {str(e)}")

# Volunteer
with st.container():
    st.subheader("Volunteer Opportunities")
    st.markdown("**Outreach Support Volunteer**")
    st.write("Help us bring mental health resources to underserved communities in Nairobi")
    
    with st.expander("Apply to Volunteer"):
        with st.form("volunteer_form"):
            v_name = st.text_input("Full Name")
            v_email = st.text_input("Email")
            v_phone = st.text_input("Phone")
            skills = st.text_area("Relevant Skills/Experience")
            submitted = st.form_submit_button("Apply")
            
            if submitted:
                if not all([v_name, v_email, v_phone]):
                    st.error("Please fill all required fields")
                elif not re.match(r"[^@]+@[^@]+\.[^@]+", v_email):
                    st.error("Please enter a valid email address")
                else:
                    st.success("Application received! Our volunteer coordinator will contact you by August 9, 2025")

# Contact Section
with st.container():
    st.subheader("Contact Us")
    st.markdown("📍 **Address**: Greenhouse Plaza, 3rd Floor, Nairobi")
    st.markdown("📞 **Phone**: +254 781 095 919")
    st.markdown("✉️ **Email**: info@safespaceorganisation.org")
    st.markdown("🕒 **Hours**: Monday-Friday 8:00 AM - 6:00 PM")

# Chatbot
with st.container():
    st.subheader("Mental Health Assistant")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [{
            "role": "assistant", 
            "content": "Hello! I'm SafeSpace virtual assistant. Ask me about our services, "
                       "events, or mental health resources. Last updated: 01:28 AM EAT, August 06, 2025"
        }]
    
    # Display chat messages
    for msg in st.session_state.messages:
        st.markdown(
            f'<div class="{"user-msg" if msg["role"]=="user" else "bot-msg"}">{msg["content"]}</div>', 
            unsafe_allow_html=True
        )
    
    # Knowledge base
    knowledge_base = {
        "services": "We offer: 1) Individual Counseling, 2) Group Therapy, 3) Online Counseling. Sessions cost KES 2,000 or subsidized based on need.",
        "hours": "Open Monday-Friday 8:00 AM - 6:00 PM, Saturday 9:00 AM - 1:00 PM",
        "founders": "Founded in 2023 by Jerim Owino (Clinical Psychologist) and Hamdi Roble (Community Mental Health Specialist)",
        "events": "Next event: Stress Management Workshop on August 10, 2025 at Community Hall",
        "volunteer": "Apply through our volunteer form! Current need: Outreach Support Volunteers",
        "crisis": "For immediate help: Call +254 781 095 919 (24/7 crisis line) or visit Nairobi Hospital ER",
        "partners": "Key partners: Kenyatta National Hospital, Ministry of Health, University of Nairobi",
        "cost": "Standard session: KES 2,000. Sliding scale available based on income verification",
        "contact": "📍 Greenhouse Plaza, Nairobi 📞 +254 781 095 919 ✉️ info@safespaceorganisation.org"
    }
    
    # Handle user input
    user_input = st.text_input("Ask a question:", key="chat_input")
    
    if user_input:
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Generate response
        response = "I'm sorry, I didn't understand. Could you rephrase? Try asking about: services, hours, costs, events, or contact info."
        input_lower = user_input.lower()
        
        for key, value in knowledge_base.items():
            if key in input_lower:
                response = value
                break
        
        # Add assistant response to history
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Rerun to update chat display
        st.experimental_rerun()

# Footer
st.markdown(
    """
    <footer>
        <p>© 2023-2025 SafeSpace Organisation. All rights reserved.</p>
        <p>Empowering Minds, Nurturing Hope</p>
    </footer>
    """,
    unsafe_allow_html=True
)
</app.py>
