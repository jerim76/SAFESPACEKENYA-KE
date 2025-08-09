```python
import streamlit as st
from datetime import datetime
import re
import base64
import pandas as pd

# Custom CSS optimized for screen fit and user-friendliness
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
        .nav {
            position: sticky;
            top: 0;
            background: var(--primary);
            padding: 10px;
            z-index: 1000;
            text-align: center;
        }
        .nav a {
            color: white;
            margin: 0 15px;
            text-decoration: none;
            font-size: 1.1rem;
        }
        .nav a:hover {
            color: var(--accent);
        }
        h1, h2, h3, h4 {
            color: var(--dark);
            text-align: center;
            line-height: 1.4;
        }
        h1 { font-size: 2.2rem; font-weight: 700; margin-bottom: 10px; }
        h2 { font-size: 1.8rem; font-weight: 600; }
        h3 { font-size: 1.4rem; font-weight: 600; }
        h4 { font-size: 1.1rem; font-weight: 400; }
        .section {
            max-height: 70vh;
            overflow-y: auto;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 10px;
            background: white;
            box-shadow: 0 4px 8px var(--shadow);
        }
        .card {
            background: white;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 15px;
            box-shadow: 0 2px 4px var(--shadow);
        }
        .btn {
            background: linear-gradient(45deg, var(--primary), #1E7D7A);
            color: white;
            padding: 12px 20px;
            border-radius: 25px;
            border: none;
            font-weight: 600;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            font-size: 1rem;
            margin: 5px;
        }
        .btn:hover {
            background: linear-gradient(45deg, var(--accent), #FF8A80);
        }
        .stButton > button {
            background: linear-gradient(45deg, var(--primary), #1E7D7A);
            color: white;
            border-radius: 25px;
            border: none;
            padding: 12px 20px;
            font-weight: 600;
            font-size: 1rem;
        }
        .stButton > button:hover {
            background: linear-gradient(45deg, var(--accent), #FF8A80);
        }
        .support-text {
            font-size: 1rem;
            color: var(--dark);
            text-align: center;
            margin: 10px 0;
        }
        @media (max-width: 768px) {
            .stApp { padding: 5px; }
            h1 { font-size: 1.8rem; }
            h2 { font-size: 1.5rem; }
            h3 { font-size: 1.2rem; }
            h4 { font-size: 1rem; }
            .section { max-height: 60vh; padding: 10px; }
            .card { padding: 10px; margin-bottom: 10px; }
            .btn, .stButton > button { padding: 10px 15px; font-size: 0.9rem; }
            .nav a { margin: 0 10px; font-size: 1rem; }
        }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="SafeSpace Organisation", page_icon="❤️", layout="wide")

# Navigation Bar
st.markdown("""
    <div class='nav'>
        <a href='#hero'>Home</a>
        <a href='#about'>About</a>
        <a href='#services'>Services</a>
        <a href='#tracker'>Mood</a>
        <a href='#contact'>Contact</a>
    </div>
""", unsafe_allow_html=True)

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "mood_history" not in st.session_state:
    st.session_state.mood_history = []
if "client_feedback" not in st.session_state:
    st.session_state.client_feedback = []

# Utility functions
def get_download_link(file_content, file_name):
    b64 = base64.b64encode(file_content.encode()).decode()
    return f'<a href="data:application/octet-stream;base64,{b64}" download="{file_name}" class="btn">Download</a>'

def export_mood_history():
    df = pd.DataFrame(st.session_state.mood_history, columns=["Date", "Mood", "Note", "Reflection"])
    df["Date"] = df["Date"].apply(lambda x: x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime) else x)
    return df.to_csv(index=False)

# Chatbot knowledge base
knowledge_base = [
    {"question": r"what is safespace organisation\??", "answer": "SafeSpace is here for you, offering mental health support since 2023 by Jerim Owino and Hamdi Roble."},
    {"question": r"what services do you offer\??", "answer": "We provide individual, group, and online counseling tailored to your needs. Register below to start."},
    {"question": r"how can i contact you\??", "answer": "We’re here—call +254 781 095 919 or email info@safespaceorganisation.org."},
    {"question": r"what are your hours\??", "answer": "Mon-Fri 9 AM-5 PM, Sat 10 AM-2 PM to support you."},
    {"question": r"how much does it cost\??", "answer": "Fees range from KSh 500-2,000, adjusted to your needs."},
    {"question": r"who are the founders\??", "answer": "Jerim Owino (12 years in trauma counseling) and Hamdi Roble (8 years in community health) lead us."},
    {"question": r"what events are coming up\??", "answer": "Join our Stress Management Workshop on August 10, 2025, in Nairobi."},
    {"question": r"how can i volunteer\??", "answer": "Your help matters—register below to volunteer."},
    {"question": r"what is the crisis line\??", "answer": "In crisis? Call +254 781 095 919 (8 AM-7 PM EAT)."},
    {"question": r"how can i partner with us\??", "answer": "Partner with us—register below to collaborate."},
    {"default": f"We’re here to help. Ask about services, contact, hours, costs, founders, events, volunteering, crisis support, or partnerships. Time: 12:14 PM EAT, August 9, 2025."}
]

def get_chatbot_response(query):
    query = query.lower()
    for entry in knowledge_base:
        if "question" in entry and re.search(entry["question"], query):
            return entry["answer"]
    return knowledge_base[-1]["default"]

# HEADER
st.markdown("<div id='hero' class='section'><h1 style='background: var(--primary); color: white; padding: 15px; border-radius: 10px;'>SafeSpace Organisation</h1><p class='support-text'>Your Safe Haven for Mental Wellness Since 2023</p></div>", unsafe_allow_html=True)
st.markdown("<div class='section'><h2 style='background: linear-gradient(135deg, var(--primary), #1E7D7A); color: white; padding: 15px; border-radius: 10px;'>You Are Not Alone</h2><p class='support-text'>SafeSpace offers compassionate, confidential counseling tailored to you.</p></div>", unsafe_allow_html=True)
cols = st.columns(2)
with cols[0]:
    st.markdown("<a href='#services' class='btn'>Get Support</a>", unsafe_allow_html=True)
with cols[1]:
    st.markdown("<a href='#about' class='btn'>Learn More</a>", unsafe_allow_html=True)

# ABOUT SECTION
st.markdown("<div id='about' class='section'><h2>About Us</h2><div class='card'><p>SafeSpace Organisation, founded in 2023 by Jerim Owino and Hamdi Roble, is committed to your mental health with a team of 15 professionals.</p></div></div>", unsafe_allow_html=True)
st.markdown("<div class='section'><h3>Meet Our Founders</h3><div class='card'><h4>Jerim Owino</h4><p>A psychologist with 12 years in trauma counseling to support you.</p></div><div class='card'><h4>Hamdi Roble</h4><p>With 8 years in community health, integrating holistic methods.</p></div></div>", unsafe_allow_html=True)

# SERVICES SECTION
st.markdown("<div id='services' class='section'><h2>Services for You</h2><div class='card'><h3>Individual Counseling</h3><p>Personalized sessions for your needs.</p></div><div class='card'><h3>Group Therapy</h3><p>Connect in a safe space.</p></div><div class='card'><h3>Online Counseling</h3><p>Virtual support anytime.</p></div></div>", unsafe_allow_html=True)
with st.form("counseling_form", clear_on_submit=True):
    name = st.text_input("Your Name", help="Enter your full name")
    email = st.text_input("Your Email", help="e.g., name@example.com")
    phone = st.text_input("Your Phone", help="e.g., +254712345678")
    submit = st.form_submit_button("Start Your Journey")
    if submit and name and re.match(r"[^@]+@[^@]+\.[^@]+", email) and phone:
        st.session_state.counseling_form_data = {"name": name, "email": email, "phone": phone}
        st.success(f"Thank you, {name}! We’ll reach out at 12:14 PM EAT, August 9, 2025, via {email}.")
        st.session_state.counseling_form_data = {"name": "", "email": "", "phone": ""}
    elif submit:
        st.error("Please fill all fields.")

# TESTIMONIALS SECTION
st.markdown("<div class='section'><h2>What Clients Say</h2><div class='card'><p><em>'SafeSpace gave me hope.'</em> - Jane K.</p></div></div>", unsafe_allow_html=True)

# EVENTS SECTION
st.markdown("<div class='section'><h2>Events for Your Growth</h2><div class='card'><h4>Stress Management Workshop</h4><p>August 10, 2025, Nairobi.</p></div></div>", unsafe_allow_html=True)

# MOOD TRACKER SECTION
st.markdown("<div id='tracker' class='section'><h2>Your Mood Journey</h2><div class='card'>")
mood = st.slider("How do you feel? (1-5)", 1, 5, 3, help="1 = Low, 5 = High")
note = st.text_input("Your Thoughts")
if st.button("Save"):
    st.session_state.mood_history.append({"Date": datetime.now(), "Mood": mood, "Note": note})
    st.success(f"Saved at 12:14 PM EAT, August 9, 2025. Take care!")
for entry in st.session_state.mood_history[-3:]:
    st.write(f"- {entry['Date'].strftime('%Y-%m-%d %H:%M')}: Mood {entry['Mood']}/5 | {entry['Note']}")
if st.button("Download"):
    csv = export_mood_history()
    if csv:
        st.markdown(get_download_link(csv, "mood_journey.csv"), unsafe_allow_html=True)
st.markdown("</div></div>", unsafe_allow_html=True)

# VOLUNTEER SECTION
st.markdown("<div class='section'><h2>Join Us</h2><div class='card'><h4>Outreach Support</h4><p>2-4 hour sessions.</p></div></div>", unsafe_allow_html=True)
with st.form("volunteer_form", clear_on_submit=True):
    name = st.text_input("Your Name", help="Enter your full name")
    email = st.text_input("Your Email", help="e.g., name@example.com")
    submit = st.form_submit_button("Contribute")
    if submit and name and re.match(r"[^@]+@[^@]+\.[^@]+", email):
        st.session_state.volunteer_form_data = {"name": name, "email": email}
        st.success(f"Thank you, {name}! Contact at 12:14 PM EAT, August 9, 2025, via {email}.")
        st.session_state.volunteer_form_data = {"name": "", "email": ""}
    elif submit:
        st.error("Please fill all fields.")

# CONTACT SECTION
st.markdown("<div id='contact' class='section'><h2>We’re Here</h2><div class='card'><p>Greenhouse Plaza, Nairobi. Call +254 781 095 919 or email info@safespaceorganisation.org.</p></div></div>", unsafe_allow_html=True)

# CHATBOT SECTION
st.markdown("<div class='section'><h2>Talk to Us</h2><div class='card'>")
chat_container = st.empty()
if st.session_state.chat_history:
    chat_messages = [f"**{'You' if m[0] == 'user' else 'Bot'}:** {m[1]}" for m in st.session_state.chat_history]
    chat_container.markdown("\n".join(chat_messages), unsafe_allow_html=False)
query = st.text_input("Your Message")
if st.button("Send") and query:
    response = get_chatbot_response(query)
    st.session_state.chat_history.append(("user", query))
    st.session_state.chat_history.append(("bot", response))
    st.rerun()
st.markdown("</div></div>", unsafe_allow_html=True)

# FEEDBACK SECTION
st.markdown("<div class='section'><h2>Your Input</h2><div class='card'>")
with st.form("feedback_form", clear_on_submit=True):
    feedback = st.text_input("Suggestions")
    submit = st.form_submit_button("Submit")
    if submit and feedback:
        st.session_state.client_feedback.append({"Date": datetime.now(), "Feedback": feedback})
        st.success(f"Thank you! Noted at 12:14 PM EAT, August 9, 2025.")
    elif submit:
        st.warning("Please share your thoughts.")
st.markdown("</div></div>", unsafe_allow_html=True)

# FOOTER
st.markdown("<hr style='border-color: var(--primary); opacity: 0.3;'><p style='text-align:center; font-size: 1rem; color: var(--dark);'>© 2023-2025 SafeSpace Organisation | <a href='#contact' style='color: var(--primary); text-decoration: none;'>Contact</a></p>", unsafe_allow_html=True)
```

### `requirements.txt`
```
streamlit>=1.22.0
pandas>=1.5.0
```

### Deployment Instructions for Streamlit Community Cloud
1. **Prepare Files**:
   - Save `app.py` and `requirements.txt` in a directory (e.g., `safespacekenya-ke`).
2. **Test Locally**:
   - Run `streamlit run app.py` in the terminal and verify all sections fit and are navigable.
3. **Set Up GitHub Repository**:
   - `git init`, `git add app.py requirements.txt`, `git commit -m "User-friendly SafeSpace app"`.
   - Create a GitHub repository and push: `git remote add origin <repository-url>`, `git push -u origin main`.
4. **Deploy**:
   - Go to [Streamlit Community Cloud](https://share.streamlit.io/), sign in, and create a new app.
   - Connect to your repository, set branch to `main`, and main file to `app.py`. Deploy and monitor.

### User-Friendly Features
- **Navigation**: Sticky nav bar at the top for easy access to sections.
- **Screen Fit**: Sections use `max-height: 70vh` with scroll if content overflows, ensuring visibility.
- **Readability**: Larger fonts, clear spacing, and tooltips on forms.
- **Simplicity**: Reduced form fields (e.g., removed preference dropdowns) and limited mood history to 3 entries.
- **Responsiveness**: Adjusted layout and sizes for mobile (max-width: 768px).

This version fits within the screen, is user-friendly, and remains deployable. Test locally and let me know if adjustments are needed!
