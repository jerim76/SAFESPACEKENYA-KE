import streamlit as st
import datetime
import pandas as pd
from fpdf import FPDF
import urllib.parse

# --- PAGE CONFIG ---
st.set_page_config(page_title="SafeSpace Kenya", layout="wide")

# --- CUSTOM STYLES WITH ANIMATED BACKGROUND + FADE-IN ---
st.markdown("""
<style>
@keyframes gradientMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(15px);}
    to {opacity: 1; transform: translateY(0);}
}
body {
    background: linear-gradient(-45deg, #e0f7fa, #fce4ec, #e1bee7, #fff9c4);
    background-size: 400% 400%;
    animation: gradientMove 15s ease infinite;
    font-family: 'Arial', sans-serif;
}
.calming-card {
    background-color: rgba(255, 255, 255, 0.88);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    margin-bottom: 20px;
    animation: fadeIn 1s ease forwards;
}
.tab-content {
    animation: fadeIn 1s ease forwards;
}
h1, h2, h3 {
    color: #2E8B8B;
}
</style>
""", unsafe_allow_html=True)

# --- STORAGE FOR MOOD JOURNAL ---
if "mood_entries" not in st.session_state:
    st.session_state["mood_entries"] = []

# --- HELPER FUNCTIONS ---
def save_mood_entry(date, mood, notes):
    st.session_state["mood_entries"].append({
        "date": date,
        "mood": mood,
        "notes": notes
    })

def download_mood_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, "Mood Journal - SafeSpace", ln=True, align="C")
    pdf.ln(10)
    for entry in st.session_state["mood_entries"]:
        pdf.multi_cell(0, 10, f"Date: {entry['date']} | Mood: {entry['mood']}\nNotes: {entry['notes']}\n")
        pdf.ln(2)
    return pdf

# --- TABS ---
tabs = st.tabs(["Home", "Services", "Education", "Tools", "Appointments", "Founder", "Contact"])

# --- HOME TAB ---
with tabs[0]:
    st.markdown("<div class='tab-content'>", unsafe_allow_html=True)
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.title("Welcome to SafeSpace Kenya")
    st.write("Providing accessible, compassionate, and professional mental health support for all. We believe that everyone deserves a safe space to heal, grow, and thrive.")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- SERVICES TAB ---
with tabs[1]:
    st.markdown("<div class='tab-content'>", unsafe_allow_html=True)
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.header("Our Services")
    st.write("""
    - **Individual Therapy** – Confidential one-on-one sessions with licensed therapists to help you navigate life challenges, trauma, and emotional distress.
    - **Group Counselling** – Support groups for shared healing, where individuals facing similar challenges connect, share, and grow together.
    - **Couples & Family Therapy** – Sessions aimed at improving communication, resolving conflicts, and building stronger relationships.
    - **Crisis Intervention** – Immediate, compassionate help during moments of crisis.
    - **Workshops & Training** – Mental health awareness programs for schools, workplaces, and communities.
    - **Online Counselling** – Secure sessions from the comfort of your space.
    - **Psychoeducation** – Learn about mental health conditions, coping strategies, and self-care.
    - **Referral Services** – Linking clients to specialized medical or psychiatric care when needed.
    - **Wellness Programs** – Mindfulness, yoga, and guided relaxation sessions.
    - **Addiction Recovery Support** – Helping individuals overcome substance abuse and compulsive behaviors.
    - **Child & Adolescent Therapy** – Age-appropriate therapy for young people facing emotional or behavioral challenges.
    - **Corporate Wellness Packages** – Workplace mental health solutions to improve employee well-being.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- EDUCATION TAB ---
with tabs[2]:
    st.markdown("<div class='tab-content'>", unsafe_allow_html=True)
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.header("Mental Health Education")
    st.write("""
    We provide educational resources, videos, and guides to empower individuals and communities. 
    Topics include stress management, emotional regulation, trauma recovery, mindfulness practices, and supporting loved ones.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- TOOLS TAB ---
with tabs[3]:
    st.markdown("<div class='tab-content'>", unsafe_allow_html=True)
    # Mood Journal
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.header("Mood Tracker & Journal")
    date = st.date_input("Date", datetime.date.today())
    mood = st.selectbox("Mood", ["😊 Happy", "😐 Neutral", "😢 Sad", "😡 Angry", "😰 Anxious"])
    notes = st.text_area("Notes")
    if st.button("Save Entry"):
        save_mood_entry(date, mood, notes)
        st.success("Mood entry saved!")

    if st.session_state["mood_entries"]:
        st.subheader("Your Mood Journal")
        df = pd.DataFrame(st.session_state["mood_entries"])
        st.table(df)
        pdf = download_mood_pdf()
        pdf_output = "/mnt/data/mood_journal.pdf"
        pdf.output(pdf_output)
        with open(pdf_output, "rb") as f:
            st.download_button("Download PDF", f, file_name="mood_journal.pdf")
    st.markdown("</div>", unsafe_allow_html=True)

    # Safety Checker
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.header("Safety Checker")
    feeling_safe = st.radio("Do you feel safe right now?", ["Yes", "No"])
    if feeling_safe == "No":
        st.error("Please reach out to a crisis helpline immediately. You matter and your safety is important.")
        st.write("Kenya Mental Health Helpline: 1199")
    else:
        st.success("Glad to hear you're feeling safe.")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- APPOINTMENTS TAB ---
with tabs[4]:
    st.markdown("<div class='tab-content'>", unsafe_allow_html=True)
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.header("Book an Appointment")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    service = st.selectbox("Service Type", [
        "Individual Therapy", "Group Counselling", "Couples Therapy", 
        "Child & Adolescent Therapy", "Addiction Recovery Support", "Corporate Wellness"
    ])
    date = st.date_input("Preferred Date", datetime.date.today())
    time = st.time_input("Preferred Time", datetime.time(10, 0))
    if st.button("Confirm Appointment"):
        appointment_details = f"Appointment Request:\nName: {name}\nEmail: {email}\nService: {service}\nDate: {date}\nTime: {time}"
        encoded_message = urllib.parse.quote(appointment_details)
        whatsapp_url = f"https://wa.me/254758943430?text={encoded_message}"
        st.markdown(f"[Click here to confirm via WhatsApp]({whatsapp_url})", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- FOUNDER TAB ---
with tabs[5]:
    st.markdown("<div class='tab-content'>", unsafe_allow_html=True)
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.header("Founder")
    st.subheader("Jerim Owino")
    st.write("""
    Jerim Owino founded SafeSpace Kenya with a deep passion for mental wellness, inclusivity, and creating a stigma-free society. 
    He envisions a Kenya where mental health care is accessible to all, regardless of location or background.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- CONTACT TAB ---
with tabs[6]:
    st.markdown("<div class='tab-content'>", unsafe_allow_html=True)
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.header("Contact Us")
    cname = st.text_input("Name")
    cemail = st.text_input("Email")
    cphone = st.text_input("Phone")
    cmessage = st.text_area("Message")

    last_mood = ""
    if st.session_state["mood_entries"]:
        last_entry = st.session_state["mood_entries"][-1]
        last_mood = f"\nLast Mood Entry:\nDate: {last_entry['date']} | Mood: {last_entry['mood']}\nNotes: {last_entry['notes']}"

    if st.button("Send via WhatsApp"):
        whatsapp_message = f"Name: {cname}\nEmail: {cemail}\nPhone: {cphone}\nMessage: {cmessage}{last_mood}"
        encoded_message = urllib.parse.quote(whatsapp_message)
        whatsapp_url = f"https://wa.me/254758943430?text={encoded_message}"
        st.markdown(f"[Click here to send on WhatsApp]({whatsapp_url})", unsafe_allow_html=True)

    st.write("📧 Email: owinojerim269@gmail.com")
    st.write("📞 WhatsApp: +254 758 943 430")
    st.write("Kenya Mental Health Helpline: 1199")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
