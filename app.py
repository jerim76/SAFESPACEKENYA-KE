import streamlit as st
from datetime import datetime
import pandas as pd
from io import BytesIO

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="SafeSpace Counseling", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
    <style>
    body {
        background-color: #f5f8fa;
        font-family: 'Arial', sans-serif;
    }
    .title {
        text-align: center;
        color: #2b6777;
    }
    .calming-card {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    .section-header {
        color: #2b6777;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)


# ---------- HOME ----------
def home():
    st.markdown("<h1 class='title'>SafeSpace Counseling & Mental Health Support</h1>", unsafe_allow_html=True)
    st.markdown("""
    Welcome to **SafeSpace**, a place where you are heard, valued, and supported.  
    Our mission is to break mental health stigma and provide accessible, empathetic counseling for all.
    """)

    st.markdown("<div class='section-header'>Quick Navigation</div>", unsafe_allow_html=True)
    cols = st.columns(3)
    with cols[0]:
        if st.button("🧠 Therapy & Counseling"):
            st.session_state.page = "Therapy & Counseling"
    with cols[1]:
        if st.button("📚 Mental Health Education"):
            st.session_state.page = "Mental Health Education"
    with cols[2]:
        if st.button("💡 Tools & Activities"):
            st.session_state.page = "Tools & Activities"


# ---------- SERVICES ----------
def therapy_counseling():
    st.markdown("<div class='section-header'>Our Counseling Services</div>", unsafe_allow_html=True)
    services = {
        "Individual Therapy": "One-on-one confidential sessions tailored to your unique needs.",
        "Couples Counseling": "Helping partners improve communication, resolve conflict, and strengthen bonds.",
        "Group Therapy": "Peer-supported healing in a guided, safe environment.",
        "Trauma Recovery": "Specialized support for those recovering from traumatic experiences.",
        "Youth & Adolescent Support": "Guidance for teens facing emotional, academic, and social challenges.",
        "Workplace Wellness": "Counseling and mental health training for corporate teams."
    }
    for service, desc in services.items():
        st.markdown(f"<div class='calming-card'><b>{service}</b><br>{desc}</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-header'>Book an Intake Session</div>", unsafe_allow_html=True)
    with st.form("intake_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email", value="owinojerim269@gmail.com")
        phone = st.text_input("Phone Number")
        reason = st.text_area("Reason for Contact")
        session_type = st.selectbox("Preferred Session Type", ["In-person", "Online"])
        submitted = st.form_submit_button("Submit & Contact via WhatsApp")
        if submitted:
            whatsapp_link = f"https://wa.me/254758943430?text=Hello%20SafeSpace%2C%20my%20name%20is%20{name}%20and%20I%20would%20like%20to%20book%20a%20{session_type}%20session.%20Reason%3A%20{reason}"
            st.success("Your request has been recorded. Click below to continue on WhatsApp:")
            st.markdown(f"[📱 Contact via WhatsApp]({whatsapp_link})")


# ---------- EDUCATION ----------
def mental_health_education():
    st.markdown("<div class='section-header'>Mental Health Education</div>", unsafe_allow_html=True)
    st.write("""
    Mental health is just as important as physical health. Understanding common conditions can help reduce stigma.
    
    **Common Conditions:**
    - Depression
    - Anxiety Disorders
    - PTSD
    - Bipolar Disorder
    - Eating Disorders
    - Substance Use Disorders
    """)
    st.markdown("<div class='calming-card'>💡 Myth: People with mental health issues are weak.<br>✅ Fact: Mental illness is not a character flaw. Seeking help is a sign of strength.</div>", unsafe_allow_html=True)


# ---------- TOOLS ----------
def tools_activities():
    st.markdown("<div class='section-header'>Self-Care Tools & Activities</div>", unsafe_allow_html=True)

    # Mood Tracker + Journal
    st.subheader("📔 Mood Journal")
    mood = st.selectbox("Select your mood:", ["😊 Happy", "😔 Sad", "😡 Angry", "😌 Calm", "😰 Anxious"])
    notes = st.text_area("Write about your day:")
    if "journal_entries" not in st.session_state:
        st.session_state.journal_entries = []

    if st.button("Save Entry"):
        st.session_state.journal_entries.append({"date": datetime.now().strftime("%Y-%m-%d %H:%M"), "mood": mood, "notes": notes})
        st.success("Entry saved!")

    if st.session_state.journal_entries:
        df = pd.DataFrame(st.session_state.journal_entries)
        st.write("Your Journal Entries")
        st.table(df)

        # Download as PDF
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
        from reportlab.lib.styles import getSampleStyleSheet
        pdf_buffer = BytesIO()
        doc = SimpleDocTemplate(pdf_buffer)
        styles = getSampleStyleSheet()
        story = [Paragraph("SafeSpace Mood Journal", styles["Title"]), Spacer(1, 12)]
        for entry in st.session_state.journal_entries:
            story.append(Paragraph(f"{entry['date']} - {entry['mood']}", styles["Heading3"]))
            story.append(Paragraph(entry['notes'], styles["BodyText"]))
            story.append(Spacer(1, 12))
        doc.build(story)
        st.download_button("📄 Download Journal as PDF", pdf_buffer.getvalue(), file_name="mood_journal.pdf")


    # Safety Checker
    st.subheader("🛡 Safety Checker")
    q1 = st.radio("Are you feeling safe right now?", ["Yes", "No"])
    if q1 == "No":
        st.error("It sounds like you might be in crisis. Please reach out immediately:")
        st.markdown("[📞 Kenya Helpline: 1199](tel:1199)")
        st.markdown(f"[📱 WhatsApp SafeSpace](https://wa.me/254758943430)")
    else:
        st.success("Glad you’re feeling safe! Check out our self-care activities above.")


# ---------- FOUNDERS ----------
def founders():
    st.markdown("<div class='section-header'>Founder</div>", unsafe_allow_html=True)
    st.markdown("""
    **Jerim Owino** — Founder of SafeSpace Counseling.  
    Jerim started SafeSpace with the vision of making mental health care more compassionate, accessible, and stigma-free.
    """)


# ---------- CONTACT ----------
def contact_support():
    st.markdown("<div class='section-header'>Contact & Support</div>", unsafe_allow_html=True)
    st.markdown("📧 Email: [owinojerim269@gmail.com](mailto:owinojerim269@gmail.com)")
    st.markdown("📱 WhatsApp: [+254758943430](https://wa.me/254758943430)")
    st.markdown("🌐 Website: Coming Soon")
    st.markdown("📞 Kenya Mental Health Helpline: 1199")


# ---------- NAVIGATION ----------
PAGES = {
    "Home": home,
    "Therapy & Counseling": therapy_counseling,
    "Mental Health Education": mental_health_education,
    "Tools & Activities": tools_activities,
    "Founders": founders,
    "Contact & Support": contact_support
}

if "page" not in st.session_state:
    st.session_state.page = "Home"

selected_page = st.sidebar.radio("Navigate", list(PAGES.keys()))
PAGES[selected_page]()
