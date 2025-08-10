import streamlit as st
import datetime
import pandas as pd
from fpdf import FPDF
import urllib.parse

# --- PAGE CONFIG ---
st.set_page_config(page_title="SafeSpace Kenya", layout="wide")

# --- CUSTOM STYLES + ANIMATED BACKGROUND ---
st.markdown("""
<style>
body {
    font-family: 'Arial', sans-serif;
    animation: gradient 15s ease infinite;
    background: linear-gradient(-45deg, #e0f7fa, #fce4ec, #f3e5f5, #fff3e0);
    background-size: 400% 400%;
}
@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
.calming-card {
    background-color: rgba(255, 255, 255, 0.9);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
h1, h2, h3 {
    color: #2E8B8B;
}
</style>
""", unsafe_allow_html=True)

# --- STORAGE ---
if "mood_entries" not in st.session_state:
    st.session_state["mood_entries"] = []
if "appointments" not in st.session_state:
    st.session_state["appointments"] = []

# --- HELPER FUNCTIONS ---
def save_mood_entry(date, mood, notes):
    st.session_state["mood_entries"].append({
        "date": date,
        "mood": mood,
        "notes": notes
    })

def save_appointment(name, date, time, notes):
    st.session_state["appointments"].append({
        "name": name,
        "date": date,
        "time": time,
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
tabs = st.tabs(["Home", "Services", "Education", "Tools", "Founder", "Contact"])

# --- HOME TAB ---
with tabs[0]:
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.title("Welcome to SafeSpace Kenya")
    st.write("Providing accessible, compassionate, and professional mental health support for all. We believe mental health care should be stigma-free, affordable, and human-centered.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- SERVICES TAB ---
with tabs[1]:
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.header("Our Services")
    st.write("""
    **1. Individual Therapy**  
    Private one-on-one sessions with qualified therapists. Helps with anxiety, depression, trauma, relationship issues, and self-esteem.

    **2. Group Counselling**  
    Guided discussions where participants share experiences, gain peer support, and learn coping skills.

    **3. Crisis Intervention**  
    Immediate assistance for people in acute emotional distress or at risk of harm.

    **4. Workshops & Training**  
    We run mental health awareness sessions, workplace wellness programs, and resilience-building workshops.

    **5. Couples & Family Therapy**  
    Helping partners and families improve communication, resolve conflicts, and strengthen bonds.

    **6. Addiction Support**  
    Confidential programs for individuals struggling with substance use or harmful habits.

    **7. Youth & Student Support**  
    Tailored counselling for young people facing academic stress, peer pressure, and identity challenges.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.subheader("Book an Appointment")
    name = st.text_input("Full Name")
    appt_date = st.date_input("Preferred Date", datetime.date.today())
    appt_time = st.time_input("Preferred Time", datetime.time(10, 0))
    appt_notes = st.text_area("Additional Notes")

    if st.button("Book Appointment"):
        save_appointment(name, appt_date, appt_time, appt_notes)
        st.success("Your appointment has been booked. We'll contact you soon.")

    if st.session_state["appointments"]:
        st.write("### Upcoming Appointments")
        df_appt = pd.DataFrame(st.session_state["appointments"])
        st.table(df_appt)
    st.markdown("</div>", unsafe_allow_html=True)

# --- EDUCATION TAB ---
with tabs[2]:
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.header("Mental Health Education")
    st.write("""
    We create accessible resources to help individuals and communities understand mental well-being, self-care strategies, and ways to support loved ones.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# --- TOOLS TAB ---
with tabs[3]:
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

    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.header("Safety Checker")
    feeling_safe = st.radio("Do you feel safe right now?", ["Yes", "No"])
    if feeling_safe == "No":
        st.error("Please reach out to a crisis helpline immediately.")
        st.write("Kenya Mental Health Helpline: 1199")
    else:
        st.success("Glad to hear you're feeling safe.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- FOUNDER TAB ---
with tabs[4]:
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.header("Founder")
    st.subheader("Jerim Owino")
    st.write("""
    Jerim Owino founded SafeSpace Kenya to create a safe, supportive, and stigma-free environment for mental health care.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# --- CONTACT TAB ---
with tabs[5]:
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.header("Contact Us")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    message = st.text_area("Message")

    last_mood = ""
    if st.session_state["mood_entries"]:
        last_entry = st.session_state["mood_entries"][-1]
        last_mood = f"\nLast Mood Entry:\nDate: {last_entry['date']} | Mood: {last_entry['mood']}\nNotes: {last_entry['notes']}"

    if st.button("Send via WhatsApp"):
        whatsapp_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}{last_mood}"
        encoded_message = urllib.parse.quote(whatsapp_message)
        whatsapp_url = f"https://wa.me/254758943430?text={encoded_message}"
        st.markdown(f"[Click here to send on WhatsApp]({whatsapp_url})", unsafe_allow_html=True)

    st.write("📧 Email: owinojerim269@gmail.com")
    st.write("📞 WhatsApp: +254 758 943 430")
    st.write("Kenya Mental Health Helpline: 1199")
    st.markdown("</div>", unsafe_allow_html=True)
