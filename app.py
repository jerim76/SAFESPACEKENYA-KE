import streamlit as st
import datetime
import pandas as pd
from io import BytesIO
import base64

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="SafeSpace Counseling", page_icon="💚", layout="wide")

# ---------- CUSTOM STYLING ----------
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #d4fc79, #96e6a1);
    font-family: 'Segoe UI', sans-serif;
}
h1, h2, h3 {
    color: #2E8B8B;
}
.calming-card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
.stButton>button {
    background-color: #2E8B8B;
    color: white;
    border-radius: 10px;
    padding: 8px 16px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# ---------- PDF DOWNLOAD ----------
def create_pdf(content):
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    text_object = c.beginText(40, 750)
    text_object.setFont("Helvetica", 12)
    for line in content.split("\n"):
        text_object.textLine(line)
    c.drawText(text_object)
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# ---------- MOOD JOURNAL STORAGE ----------
if "journal_entries" not in st.session_state:
    st.session_state.journal_entries = []

# ---------- TABS ----------
tabs = st.tabs(["🏠 Home", "💼 Services", "📘 Education", "🛠 Tools", "👤 Founders", "📞 Contact"])

# ---------- HOME TAB ----------
with tabs[0]:
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.title("Welcome to SafeSpace Counseling 💚")
    st.write("Your journey to healing, growth, and emotional wellness starts here.")
    st.write("At SafeSpace, we provide compassionate counseling services, practical tools, and mental health education to empower your well-being.")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- SERVICES TAB ----------
with tabs[1]:
    st.header("Our Services")
    services = {
        "Individual Therapy": "One-on-one sessions tailored to your needs. Helps with anxiety, depression, stress, and personal growth.",
        "Couples Counseling": "Improve communication, resolve conflicts, and strengthen your relationship.",
        "Trauma Recovery": "Evidence-based support for PTSD, abuse recovery, and life-changing events.",
        "Group Therapy": "Connect with others facing similar challenges in a safe, moderated space.",
        "Youth Support": "Guidance for teens and young adults to navigate life’s challenges.",
        "Workplace Wellness": "Mental health workshops and programs for organizations."
    }
    for name, desc in services.items():
        st.markdown(f"**{name}** — {desc}")

# ---------- EDUCATION TAB ----------
with tabs[2]:
    st.header("Mental Health Education")
    st.subheader("Common Conditions")
    st.markdown("- **Depression:** Persistent sadness, loss of interest, fatigue.")
    st.markdown("- **Anxiety Disorders:** Excessive worry, restlessness, rapid heartbeat.")
    st.markdown("- **PTSD:** Flashbacks, nightmares, severe anxiety after trauma.")
    st.markdown("- **Bipolar Disorder:** Extreme mood swings from highs to lows.")
    st.subheader("Myths vs Facts")
    st.markdown("- Myth: Mental illness is rare. **Fact:** 1 in 4 people experience it annually.")
    st.markdown("- Myth: You can ‘snap out of it’. **Fact:** Recovery needs support and treatment.")

# ---------- TOOLS TAB ----------
with tabs[3]:
    st.header("Wellness Tools")

    # Mood Tracker
    st.subheader("Mood Tracker")
    mood = st.radio("How are you feeling today?", ["😊 Happy", "😔 Sad", "😤 Stressed", "😐 Neutral"])
    note = st.text_area("Notes about your day")
    if st.button("Save Mood Entry"):
        st.session_state.journal_entries.append(f"{datetime.date.today()} - {mood} - {note}")
        st.success("Mood entry saved!")

    # Download Journal as PDF
    if st.session_state.journal_entries:
        pdf_buffer = create_pdf("\n".join(st.session_state.journal_entries))
        b64 = base64.b64encode(pdf_buffer.read()).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="mood_journal.pdf">📄 Download Mood Journal as PDF</a>'
        st.markdown(href, unsafe_allow_html=True)

    # Safety Checker
    st.subheader("Safety Checker")
    safe_now = st.radio("Do you feel safe right now?", ["Yes", "No"])
    if safe_now == "No":
        st.error("If you are in crisis, please contact a helpline immediately.")
        st.markdown("[Kenya Suicide Prevention Hotline: 1199](tel:1199)")
        st.markdown(f"[WhatsApp SafeSpace](https://wa.me/254758943430)")
    else:
        st.success("Glad you feel safe. Remember to practice self-care today!")

# ---------- FOUNDERS TAB ----------
with tabs[4]:
    st.header("Founder: Jerim Owino")
    st.write("""
    Jerim Owino founded SafeSpace with a vision of creating a supportive, stigma-free environment 
    where people can access mental health services without fear or judgment.
    """)
    st.markdown("> *'Mental wellness is a journey, and no one should walk it alone.'*")

# ---------- CONTACT TAB ----------
with tabs[5]:
    st.header("Get in Touch")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    message = st.text_area("How can we help you?")
    if st.button("Submit"):
        st.success("Thank you for reaching out! We will contact you soon.")
    st.markdown(f"📧 Email: [owinojerim269@gmail.com](mailto:owinojerim269@gmail.com)")
    st.markdown(f"💬 WhatsApp: [Message Us](https://wa.me/254758943430)")
    st.markdown("**Crisis Helplines:**")
    st.markdown("- Kenya: 1199")
    st.markdown("- Befrienders Worldwide: https://www.befrienders.org/")
