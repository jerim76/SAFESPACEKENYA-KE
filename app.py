import streamlit as st
from datetime import datetime
import re
import pandas as pd

# --------------------
# PAGE CONFIG
# --------------------
st.set_page_config(
    page_title="SafeSpace Organisation",
    page_icon="❤️",
    layout="wide"
)

# --------------------
# CUSTOM CSS
# --------------------
st.markdown("""
    <style>
        :root {
            --primary: #26A69A;
            --accent: #FF6F61;
            --light: #F9F9F9;
            --soft: #E8F4F8;
            --dark: #1E3A5F;
            --shadow: rgba(0, 0, 0, 0.05);
        }
        .stApp {
            background: linear-gradient(135deg, var(--light), var(--soft));
            color: var(--dark);
            font-family: Arial, sans-serif;
            padding: 10px;
            max-width: 100%;
            overflow-x: hidden;
        }
        h1, h2, h3 {
            color: var(--primary);
        }
        .section {
            background-color: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 10px var(--shadow);
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# --------------------
# NAVIGATION MENU
# --------------------
menu = [
    "Home", 
    "Services", 
    "Resources", 
    "About Us", 
    "Founders", 
    "Contact", 
    "AI Chatbot", 
    "Mood Tracker"
]
choice = st.sidebar.radio("Navigate", menu)

# --------------------
# HOME
# --------------------
if choice == "Home":
    st.title("Welcome to SafeSpace ❤️")
    st.write("""
        At SafeSpace, we believe every individual deserves a place to be heard, supported,  
        and understood without judgment.  

        Our mission is to make mental health care accessible for everyone — regardless of  
        age, background, or financial situation.  

        ### What We Stand For:
        - **Confidentiality** – Your privacy is always protected.  
        - **Accessibility** – Services designed to reach anyone, anywhere.  
        - **Compassion** – Genuine care from trained professionals and volunteers.  
        - **Empowerment** – Tools to help you take charge of your mental health.  
    """)
    st.image(
        "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee", 
        caption="Your well-being matters", 
        use_column_width=True
    )

# --------------------
# SERVICES
# --------------------
elif choice == "Services":
    st.title("Our Services")
    st.markdown("""
    ### 🧠 Mental Health Counseling  
    Confidential one-on-one sessions with licensed therapists, tailored to your unique needs.  

    ### 📱 24/7 Crisis Helpline  
    Life doesn’t wait for office hours — and neither do we.  

    ### 📚 Mental Wellness Workshops  
    Topics include stress management, mindfulness, and self-esteem building.  

    ### 💬 Peer Support Groups  
    Safe, moderated spaces to connect and share experiences.  

    ### 🌐 Online Resources  
    Meditation tracks, guided exercises, and mood-tracking tools.
    """)

# --------------------
# RESOURCES
# --------------------
elif choice == "Resources":
    st.title("Helpful Resources")
    st.markdown("""
    #### 📲 Mental Health Apps  
    - Headspace – Guided meditation  
    - Calm – Sleep and relaxation  
    - Insight Timer – Free meditation library  

    #### ☎️ Crisis Numbers  
    - US: 988 Suicide Lifeline  
    - UK: 116 123 Samaritans  
    - Australia: 13 11 14 Lifeline  
    - More: https://findahelpline.com  

    #### 📚 Reading  
    - *The Happiness Trap* – Russ Harris  
    - *Lost Connections* – Johann Hari  
    - *Reasons to Stay Alive* – Matt Haig  

    #### 📝 Self-Care Tips  
    - Regular sleep  
    - Exercise  
    - Balanced diet  
    - Stay connected  
    - Practice gratitude
    """)

# --------------------
# ABOUT US
# --------------------
elif choice == "About Us":
    st.title("About SafeSpace")
    st.write("""
        Founded in 2023, SafeSpace is a non-profit focused on emotional well-being.  

        **Our Team**:
        - Licensed therapists  
        - Peer support volunteers  
        - Community advocates  

        **Our Goals**:
        - Affordable care  
        - Early intervention  
        - Mental health education
    """)

# --------------------
# FOUNDERS
# --------------------
elif choice == "Founders":
    st.title("Meet Our Founders")
    st.markdown("""
    **Dr. Maya Thompson** – Psychologist  
    - 15 years in trauma recovery and CBT.  

    **Alex Rivera** – Community Advocate  
    - Leads outreach and inclusion.  

    **Priya Sharma** – Mindfulness Coach  
    - Designs wellness workshops.
    """)

# --------------------
# CONTACT
# --------------------
elif choice == "Contact":
    st.title("Get in Touch")
    st.write("""
        📧 contact@safespace.org  
        📞 +1 (800) 555-1234  
        🏢 123 Hope Street, Mindville, USA  
    """)
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send")
        if submit:
            if name and re.match(r"[^@]+@[^@]+\.[^@]+", email) and message:
                st.success("Thank you! We'll get back to you soon.")
            else:
                st.error("Please fill all fields correctly.")

# --------------------
# AI CHATBOT
# --------------------
elif choice == "AI Chatbot":
    st.title("SafeSpace AI Chatbot 🤖❤️")
    st.write("This is a safe, private chatbot for emotional support and wellness tips.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("How are you feeling today?")
    if st.button("Send"):
        if user_input:
            # Simple keyword-based response
            if "sad" in user_input.lower() or "depressed" in user_input.lower():
                bot_reply = "I'm sorry you're feeling this way. Remember, your feelings are valid. Have you considered talking to a counselor or a trusted friend?"
            elif "happy" in user_input.lower():
                bot_reply = "That's wonderful to hear! Keep embracing the moments that bring you joy."
            elif "anxious" in user_input.lower():
                bot_reply = "Anxiety can be tough. Try taking a few deep breaths with me: Inhale for 4, hold for 4, exhale for 6."
            else:
                bot_reply = "Thank you for sharing. I'm here to listen and support you."

            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("SafeSpace Bot", bot_reply))

    for sender, msg in st.session_state.chat_history:
        st.write(f"**{sender}:** {msg}")

# --------------------
# MOOD TRACKER
# --------------------
elif choice == "Mood Tracker":
    st.title("Daily Mood Tracker 📊")
    st.write("Log your mood daily to monitor your emotional well-being over time.")

    if "mood_data" not in st.session_state:
        st.session_state.mood_data = []

    mood = st.selectbox("How do you feel today?", ["😊 Happy", "😐 Neutral", "😔 Sad", "😰 Anxious", "😡 Angry"])
    note = st.text_area("Any notes about your day?")
    if st.button("Save Entry"):
        st.session_state.mood_data.append({
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Mood": mood,
            "Note": note
        })
        st.success("Your mood has been recorded.")

    if st.session_state.mood_data:
        df = pd.DataFrame(st.session_state.mood_data)
        st.write("Mood History:")
        st.dataframe(df)
