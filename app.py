import streamlit as st
from datetime import datetime

# ==================== PDF SAFETY CHECK ====================
try:
    from fpdf import FPDF
    pdf_enabled = True
except ImportError:
    pdf_enabled = False

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="SafeSpace Kenya",
    page_icon="🕊",
    layout="wide"
)

# ==================== CUSTOM CSS ====================
page_bg = """
<style>
body {
    background: linear-gradient(120deg, #c2e9fb, #a1c4fd);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.calming-card {
    background-color: rgba(255, 255, 255, 0.88);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    animation: fadeIn 1s ease-in-out;
}
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ==================== NAVIGATION TABS ====================
tabs = st.tabs(["🏠 Home", "💙 Services", "📓 Tools", "📅 Book Appointment", "📞 Contact", "👤 Founder"])

# ==================== HOME TAB ====================
with tabs[0]:
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.title("🕊 Welcome to SafeSpace Kenya")
    st.write("""
        SafeSpace Kenya is your confidential and compassionate partner in mental wellness. 
        We provide counseling, tools, and resources to support emotional and psychological health.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ==================== SERVICES TAB ====================
with tabs[1]:
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.header("💙 Our Services")

    services = {
        "Individual Counseling": "One-on-one confidential sessions with a trained therapist to address personal challenges, anxiety, depression, trauma, and self-esteem issues.",
        "Group Therapy": "Therapeutic group sessions where participants share experiences, foster mutual support, and learn coping strategies in a safe space.",
        "Family & Couples Counseling": "Professional guidance to improve communication, resolve conflicts, and strengthen relationships within families and couples.",
        "Crisis Intervention": "Immediate support for individuals experiencing severe emotional distress, suicidal thoughts, or traumatic events.",
        "Workplace Wellness Programs": "Custom mental health programs, workshops, and seminars to promote emotional well-being in organizations.",
        "Psychoeducation": "Educational sessions on mental health topics to empower communities with knowledge and reduce stigma.",
        "Youth Mentorship & Guidance": "Mentoring services for young people to help navigate life challenges, career choices, and academic stress."
    }

    for service, description in services.items():
        st.subheader(f"🔹 {service}")
        st.write(description)

    st.markdown("</div>", unsafe_allow_html=True)

# ==================== TOOLS TAB ====================
with tabs[2]:
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.header("📓 Tools for Your Mental Health")

    mood_entries = []

    # Mood Journal
    st.subheader("📝 Mood Journal")
    mood = st.selectbox("How are you feeling today?", ["😊 Happy", "😔 Sad", "😟 Anxious", "😠 Angry", "😌 Relaxed"])
    notes = st.text_area("Add some notes about your day...")
    if st.button("Save Entry"):
        mood_entries.append({"date": datetime.now().strftime("%Y-%m-%d %H:%M"), "mood": mood, "notes": notes})
        st.success("Mood entry saved!")

    # PDF Export with Safety Check
    if pdf_enabled:
        if st.button("Download Mood Journal PDF"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Mood Journal Entries", ln=True, align='C')
            for entry in mood_entries:
                pdf.multi_cell(0, 10, f"{entry['date']} - {entry['mood']}\n{entry['notes']}")
            pdf_output = "mood_journal.pdf"
            pdf.output(pdf_output)
            with open(pdf_output, "rb") as f:
                st.download_button("📄 Download Your Mood Journal PDF", f, file_name="mood_journal.pdf")
    else:
        st.warning("📄 PDF export unavailable. Please install `fpdf` to enable this feature.")

    # Safety Checker
    st.subheader("🛡 Safety Checker")
    feeling_safe = st.radio("Do you feel safe right now?", ["Yes", "No"])
    if feeling_safe == "No":
        st.error("If you feel unsafe, please call 1195 (GBV helpline Kenya) or reach out to someone you trust immediately.")

    st.markdown("</div>", unsafe_allow_html=True)

# ==================== APPOINTMENT BOOKING TAB ====================
with tabs[3]:
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.header("📅 Book an Appointment")
    name = st.text_input("Your Full Name")
    email = st.text_input("Your Email Address")
    phone = st.text_input("Your Phone Number")
    date = st.date_input("Select Date")
    time = st.time_input("Select Time")
    if st.button("Confirm Booking"):
        st.success(f"Appointment booked for {name} on {date} at {time}. We will contact you soon!")

    st.markdown("</div>", unsafe_allow_html=True)

# ==================== CONTACT TAB ====================
with tabs[4]:
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.header("📞 Contact Us")
    contact_name = st.text_input("Your Name")
    contact_email = st.text_input("Your Email")
    contact_phone = st.text_input("Your Phone Number")
    contact_message = st.text_area("Your Message")

    last_mood = mood_entries[-1]['mood'] + " - " + mood_entries[-1]['notes'] if mood_entries else "No mood entry recorded."
    whatsapp_message = f"Hello SafeSpace, my name is {contact_name}. My email is {contact_email}, phone: {contact_phone}. Message: {contact_message}. Last Mood Entry: {last_mood}"
    whatsapp_url = f"https://wa.me/254758943430?text={whatsapp_message.replace(' ', '%20')}"

    if st.button("Send via WhatsApp"):
        st.markdown(f"[Click here to send WhatsApp message]({whatsapp_url})")

    st.info("📧 Email: owinojerim269@gmail.com")
    st.info("📱 WhatsApp: +254 758 943 430")
    st.info("☎ Helpline Kenya: 1195")

    st.markdown("</div>", unsafe_allow_html=True)

# ==================== FOUNDER TAB ====================
with tabs[5]:
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.header("👤 Founder: Jerim Owino")
    st.write("""
        Jerim Owino is a passionate mental health advocate and counselor with a vision to create safe and accessible spaces for emotional well-being in Kenya. 
        Through SafeSpace, Jerim aims to break the stigma surrounding mental health and provide tools, education, and professional support for individuals and communities.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
