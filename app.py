# app.py
import streamlit as st
from datetime import datetime
import re
import base64
import pandas as pd
import random
import textwrap
import urllib.parse
import io

# Page config
st.set_page_config(page_title="SafeSpace Organization", page_icon="🧠", layout="wide")

# ---------- Styles ----------
st.markdown(
    """
    <style>
    :root { --primary: #4a9b8e; --accent: #ff9a8b; --light: #f0f7f5; --dark: #2c3e50; --deep-blue: #1E3A8A; }
    .stApp { background-color: var(--light); font-family: 'Inter', sans-serif; color: var(--dark); min-height: 100vh;
            background-image: url('https://www.transparenttextures.com/patterns/soft-wallpaper.png'); background-attachment: fixed; }
    h1,h2,h3,h4 { font-family: 'Merriweather', serif; color: var(--deep-blue); font-weight: 400; }
    .safe-container { background: rgba(255,255,255,0.95); border-radius: 12px; padding: 1.6rem; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 1.6rem; border-left: 4px solid var(--primary); }
    .calming-card { background: white; border-radius: 10px; padding: 1.2rem; margin: 1rem 0; box-shadow: 0 2px 8px rgba(0,0,0,0.03); border: 1px solid #e6f2f0; transition: all 0.18s ease; }
    .primary-btn { background: linear-gradient(135deg, var(--primary), #5ab4a7); color: white; padding: 0.6rem 1.1rem; border-radius: 8px; text-decoration: none; display: inline-block; font-weight: 600; }
    .testimonial { padding: 1.2rem; background: linear-gradient(to right, #f8fbfa, #e6f2f0); border-radius: 8px; margin: 1rem 0; border-left: 3px solid var(--accent); font-style: italic; position: relative; }
    .testimonial::before { content: "“"; font-size: 2.2rem; position: absolute; top: -12px; left: 8px; color: var(--primary); opacity:0.25; }
    .therapist-card { padding: 1rem; background: white; border-radius: 8px; box-shadow: 0 3px 8px rgba(0,0,0,0.06); text-align: center; margin: 0.6rem; }
    .confidential { font-size: 0.95rem; color:#5a6c75; margin-top: 1rem; padding: 0.9rem; background:#f8f9fa; border-radius:6px; border-left:3px solid var(--primary); }
    .small-muted { font-size:0.9rem; color:#6c757d; }
    @media (max-width: 768px) { .calming-card { padding: 0.9rem; } h1 { font-size: 1.9rem; } }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Configuration (user details) ----------
SAFESPACE_WHATSAPP_NUMBER = "254758943430"  # user's number (no plus)
SAFESPACE_EMAIL = "owinojerim269@gmail.com"

# ---------- Session State ----------
if "mood_history" not in st.session_state:
    st.session_state.mood_history = []
if "intake_submissions" not in st.session_state:
    st.session_state.intake_submissions = []
if "contact_messages" not in st.session_state:
    st.session_state.contact_messages = []
if "quiz_results" not in st.session_state:
    st.session_state.quiz_results = None

# ---------- Helpers ----------
def get_download_link_bytes(bytes_content: bytes, file_name: str, mime="application/octet-stream"):
    b64 = base64.b64encode(bytes_content).decode()
    href = f'<a href="data:{mime};base64,{b64}" download="{file_name}" class="primary-btn">Download {file_name}</a>'
    return href

def get_download_link_text(text_content: str, file_name: str):
    return get_download_link_bytes(text_content.encode(), file_name, mime="text/plain")

def validate_email(email: str):
    return bool(re.match(r"^[a-zA-Z0-9_.+\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-.]+$", email))

def validate_phone_kenya(phone: str):
    s = re.sub(r"[^\d+]", "", phone)
    return bool(re.match(r"^\+?254\d{9}$|^0\d{9}$|^254\d{9}$", s))

def whatsapp_link_for_message(phone_digits: str, message: str):
    encoded = urllib.parse.quote(message)
    return f"https://wa.me/{phone_digits}?text={encoded}"

def generate_safety_plan_pdf_bytes(plan: dict):
    """
    Try to generate a simple PDF using reportlab if available.
    If reportlab not available, raise ImportError to let caller fallback.
    """
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen import canvas
    except Exception as e:
        raise ImportError("reportlab required for PDF generation") from e

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    margin = 40
    y = height - margin
    c.setFont("Helvetica-Bold", 16)
    c.drawString(margin, y, "Personal Safety Plan")
    y -= 30
    c.setFont("Helvetica", 11)
    for k, v in plan.items():
        # write key as bold
        c.setFont("Helvetica-Bold", 11)
        c.drawString(margin, y, f"{k}:")
        y -= 16
        c.setFont("Helvetica", 10)
        # wrap long text
        text = c.beginText(margin + 10, y)
        for line in wrap_text(v, 85):
            text.textLine(line)
            y -= 12
        c.drawText(text)
        y -= 10
        if y < 80:
            c.showPage()
            y = height - margin
            c.setFont("Helvetica", 11)
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer.read()

def wrap_text(text, width):
    import textwrap as _tw
    return _tw.wrap(text, width)

# ---------- Static Data ----------
therapists = [
    {"name": "Dr. Amina Hassan", "specialty": "Trauma & PTSD Specialist", "approach": "EMDR, Somatic Therapy, CBT", "experience": "12 years", "credentials": "PhD Clinical Psychology"},
    {"name": "Ben Ochieng", "specialty": "Relationships & Family Therapy", "approach": "Emotion-Focused Therapy, Gottman Method", "experience": "8 years", "credentials": "MA Marriage & Family Therapy"},
    {"name": "Grace Mwangi", "specialty": "Depression & Mood Disorders", "approach": "CBT, Positive Psychology", "experience": "10 years", "credentials": "MA Clinical Psychology"},
]

therapy_services = [
    {"title":"Individual Therapy", "desc":"One-on-one confidential sessions tailored to your needs using evidence-based techniques.", "audience":"Adults & adolescents", "delivery":"Online / In-person", "benefits":"Better emotional regulation and symptom reduction"},
    {"title":"Couples & Family Therapy", "desc":"Support for relationships, parenting, and family transitions using established models (EFT, Gottman).", "audience":"Couples & families", "delivery":"Online / In-person", "benefits":"Improved communication and repaired trust"},
    {"title":"Trauma-Informed Care & EMDR", "desc":"Targeted trauma treatment including safety planning and EMDR when clinically indicated.", "audience":"Survivors of trauma", "delivery":"Assessment then online/in-person", "benefits":"Reduced PTSD symptoms"},
    {"title":"Youth & Adolescent Support", "desc":"Developmentally-appropriate therapy with family involvement.", "audience":"Children & teens", "delivery":"In-person / Online", "benefits":"Better school & social functioning"},
    {"title":"Group Programs", "desc":"DBT skills groups, mindfulness, caregiver support and workplace wellbeing workshops.", "audience":"Community & workplaces", "delivery":"Scheduled groups", "benefits":"Peer support and skills-building"}
]

symptom_guide = {
    "Anxiety": {"physical":"Racing heart, sweating, trembling", "emotional":"Worry, irritability", "coping":"Breathing, grounding, structured activity"},
    "Depression": {"physical":"Fatigue, sleep change", "emotional":"Low mood, loss of interest", "coping":"Behavioural activation, structure, social support"},
    "PTSD": {"physical":"Startle, insomnia", "emotional":"Flashbacks, avoidance", "coping":"Grounding, trauma-focused therapy"}
}

# ---------- App structure ----------
tabs = st.tabs(["Home","Services","Therapy & Intake","Tools & Journal","Founders","Team","Contact & Support","Assessments & Resources"])

# ----- HOME -----
with tabs[0]:
    st.markdown("<div class='safe-container' style='text-align:center; background: linear-gradient(rgba(74,155,142,0.95), rgba(90,180,167,0.95)); color:white;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='margin-bottom:0.1rem;'>SafeSpace Organization</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='margin-top:0.2rem; font-size:1.05rem; color:rgba(255,255,255,0.95)'>Accessible, culturally-sensitive mental health & counselling services. Contact: {SAFESPACE_EMAIL} • WhatsApp: +{SAFESPACE_WHATSAPP_NUMBER}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### Quick actions")
    c1,c2,c3 = st.columns(3)
    with c1:
        st.markdown("**Mood Journal**")
        if st.button("Open Journal"):
            st.experimental_set_query_params(tab="Tools & Journal")
            st.experimental_rerun()
    with c2:
        st.markdown("**Request Intake**")
        if st.button("Request Intake"):
            st.experimental_set_query_params(tab="Therapy & Intake")
            st.experimental_rerun()
    with c3:
        st.markdown("**Safety Check**")
        if st.button("Open Safety Checker"):
            st.experimental_set_query_params(tab="Tools & Journal")
            st.experimental_rerun()

# ----- SERVICES -----
with tabs[1]:
    st.markdown("<div class='safe-container'>", unsafe_allow_html=True)
    st.markdown("## Services Offered")
    st.markdown("We provide a range of clinical and community services. Below are details to help you choose what's right.")
    for s in therapy_services:
        st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
        st.markdown(f"### {s['title']}")
        st.markdown(f"{s['desc']}")
        st.markdown(f"**Who it's for:** {s['audience']}  •  **Delivery:** {s['delivery']}")
        st.markdown(f"**Benefits:** {s['benefits']}")
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div class='confidential'>If you have a medical or safety concern, please seek immediate medical attention. We provide referrals when specialist care is needed.</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ----- THERAPY & INTAKE -----
with tabs[2]:
    st.markdown("<div class='safe-container'>", unsafe_allow_html=True)
    st.markdown("## Therapy Pathway & Intake")
    st.markdown("Complete intake below to request a therapist match. You can also contact us via WhatsApp for quicker coordination.")
    st.markdown("---")
    with st.form("intake_form"):
        col1, col2 = st.columns(2)
        with col1:
            full_name = st.text_input("Full name")
            email = st.text_input("Email", value=SAFESPACE_EMAIL)
            phone = st.text_input("Phone (Kenya preferred)", placeholder="+2547XXXXXXXX")
        with col2:
            concern = st.selectbox("Primary concern", ["Anxiety","Depression","Trauma/PTSD","Relationships","Adolescent concerns","Workplace stress","Other"])
            mode = st.radio("Preferred mode", ["Online","In-person"])
            availability = st.text_area("Availability (e.g., weekdays after 5pm)", height=80)
        consent = st.checkbox("I consent to be contacted", value=True)
        submit = st.form_submit_button("Submit intake request")
        if submit:
            errs=[]
            if not full_name or not email or not phone:
                errs.append("Complete name, email and phone.")
            if email and not validate_email(email):
                errs.append("Enter a valid email.")
            if phone and not validate_phone_kenya(phone):
                errs.append("Enter a valid Kenyan phone (e.g. +2547XXXXXXXX or 07XXXXXXXX).")
            if not consent:
                errs.append("Consent required.")
            if errs:
                for e in errs:
                    st.error(e)
            else:
                rec = {"name":full_name,"email":email,"phone":phone,"concern":concern,"mode":mode,"availability":availability,"time":datetime.now()}
                st.session_state.intake_submissions.append(rec)
                st.success("Intake recorded. We'll match and contact within 24 hours.")
                # WhatsApp quick contact
                msg = f"Hello SafeSpace, my name is {full_name}. I requested intake for {concern}. Phone: {phone}. Prefer: {mode}. Please contact me."
                digits = re.sub(r"[^\d]", "", phone)
                if digits.startswith("0"):
                    digits = "254" + digits[1:]
                if digits.startswith("254") and len(digits) >= 12:
                    wa = whatsapp_link_for_message(digits, msg)
                    st.markdown(f"[Confirm via WhatsApp]({wa})", unsafe_allow_html=True)
                else:
                    wa_main = whatsapp_link_for_message(SAFESPACE_WHATSAPP_NUMBER, msg)
                    st.markdown("Unable to create personal WhatsApp link — use SafeSpace main WhatsApp:")
                    st.markdown(f"[WhatsApp SafeSpace]({wa_main})", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ----- TOOLS & JOURNAL -----
with tabs[3]:
    st.markdown("<div class='safe-container'>", unsafe_allow_html=True)
    st.markdown("## Tools: Mood Journal, Safety Plan & Quick Checks")

    # --- Mood Journal ---
    st.markdown("### Mood Journal")
    st.markdown("Log moods quickly — export to bring to sessions.")
    moods = {"Radiant":"😊","Calm":"😌","Neutral":"😐","Anxious":"😟","Sad":"😔"}
    col1, col2 = st.columns([2,3])
    with col1:
        mood = st.selectbox("Current mood", ["Choose a mood"] + list(moods.keys()))
        intensity = st.slider("Intensity (1 low - 5 high)", 1, 5, 3)
        note = st.text_area("Short note (optional)", height=100)
        if st.button("Save mood"):
            if mood == "Choose a mood":
                st.warning("Select a mood first.")
            else:
                st.session_state.mood_history.append({"Date":datetime.now(),"Mood":mood,"Intensity":intensity,"Note":note})
                st.success("Saved.")
    with col2:
        st.markdown("**Journal tips**")
        st.markdown("- Note triggers, body sensations, helpful actions, and next steps.")
        st.markdown("- Short daily notes are more effective than long irregular ones.")

    if st.session_state.mood_history:
        df = pd.DataFrame(st.session_state.mood_history)
        df_display = df.copy()
        df_display["Date"] = df_display["Date"].dt.strftime("%b %d, %Y %I:%M %p")
        st.dataframe(df_display[["Date","Mood","Intensity","Note"]], hide_index=True)
        csv_bytes = export_mood_history_csv().encode()
        st.markdown(get_download_link_bytes(csv_bytes, "mood_journal.csv", mime="text/csv"), unsafe_allow_html=True)
        if st.button("Clear local journal"):
            st.session_state.mood_history = []
            st.success("Local journal cleared.")

    st.markdown("---")
    # --- Safety Plan PDF generator ---
    st.markdown("### Create a Personal Safety Plan (downloadable PDF)")
    st.markdown("Fill this short plan and download it. Keep it somewhere safe and share with your support person if needed.")
    sp_name = st.text_input("Your name (for plan)", "")
    sp_triggers = st.text_area("My triggers (what tends to make things worse)", "", height=80)
    sp_warning_signs = st.text_area("Warning signs I notice", "", height=80)
    sp_coping = st.text_area("Things I can do to feel safer / cope", "", height=80)
    sp_contacts = st.text_area("People I can contact (name + phone/WhatsApp)", f"Jerim Owino: +{SAFESPACE_WHATSAPP_NUMBER}\n", height=80)
    sp_professionals = st.text_area("Professional resources I can contact", f"SafeSpace WhatsApp: +{SAFESPACE_WHATSAPP_NUMBER}\nEmail: {SAFESPACE_EMAIL}", height=80)

    if st.button("Generate Safety Plan (PDF)"):
        plan = {
            "Name": sp_name or "Not provided",
            "Triggers": sp_triggers or "Not provided",
            "Warning signs": sp_warning_signs or "Not provided",
            "Coping strategies": sp_coping or "Not provided",
            "Support contacts": sp_contacts or "Not provided",
            "Professional contacts": sp_professionals or "Not provided",
            "Generated": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        # Try PDF generation
        try:
            pdf_bytes = generate_safety_plan_pdf_bytes(plan)
            st.success("Safety Plan PDF generated. Download below.")
            st.markdown(get_download_link_bytes(pdf_bytes, "safety_plan.pdf", mime="application/pdf"), unsafe_allow_html=True)
        except Exception:
            # fallback to text file
            txt = "\n\n".join([f"{k}:\n{v}" for k,v in plan.items()])
            st.warning("PDF generation not available on this environment — downloading plain text file instead.")
            st.markdown(get_download_link_text(txt, "safety_plan.txt"), unsafe_allow_html=True)

    st.markdown("---")
    # --- Safety Checker ---
    st.markdown("### Quick Safety Checker (not diagnostic)")
    st.markdown("If in immediate danger call local emergency number (999 Kenya).")
    s1 = st.radio("Are you safe right now?", ["Yes","Not sure","No"])
    s2 = st.radio("Have you had thoughts of harming yourself in past week?", ["No","Sometimes","Frequently"])
    s3 = st.radio("Do you have a plan or means now?", ["No","Not sure","Yes"])
    if st.button("Run safety check"):
        if s1 == "No" or s2 == "Frequently" or s3 == "Yes":
            st.error("You may be at risk. Please seek immediate help.")
            st.markdown(f"- Emergency (Kenya): **999**")
            st.markdown(f"- SafeSpace Crisis (WhatsApp): +{SAFESPACE_WHATSAPP_NUMBER}")
            wa_link = whatsapp_link_for_message(SAFESPACE_WHATSAPP_NUMBER, "I need urgent help. I'm not safe right now.")
            st.markdown(f"[Send urgent WhatsApp]({wa_link})", unsafe_allow_html=True)
        else:
            st.success("Low immediate risk indicated. Use coping skills and check-in with supports. Contact SafeSpace if concerned.")

    st.markdown("</div>", unsafe_allow_html=True)

# ----- FOUNDERS -----
with tabs[4]:
    st.markdown("<div class='safe-container'>", unsafe_allow_html=True)
    st.markdown("## Founders & Vision")
    st.markdown("### Jerim Owino — Founder & Program Lead")
    st.markdown(textwrap.dedent("""
        Jerim Owino founded SafeSpace to increase access to culturally-informed mental health care in Kenya. Jerim focuses on training, community outreach and trauma-informed practice.
    """))
    st.markdown("</div>", unsafe_allow_html=True)

# ----- TEAM -----
with tabs[5]:
    st.markdown("<div class='safe-container'>", unsafe_allow_html=True)
    st.markdown("## Our Team")
    cols = st.columns(2)
    idx = 0
    for t in therapists:
        with cols[idx % 2]:
            st.markdown("<div class='therapist-card'>", unsafe_allow_html=True)
            st.markdown(f"### {t['name']}")
            st.markdown(f"**{t['specialty']}**")
            st.markdown(f"{t['approach']}")
            st.markdown(f"<div class='small-muted'>{t['credentials']} • {t['experience']}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        idx += 1
    st.markdown("</div>", unsafe_allow_html=True)

# ----- CONTACT & SUPPORT -----
with tabs[6]:
    st.markdown("<div class='safe-container'>", unsafe_allow_html=True)
    st.markdown("## Contact & Support")
    st.markdown(f"Email: {SAFESPACE_EMAIL}  •  WhatsApp: +{SAFESPACE_WHATSAPP_NUMBER}")
    st.markdown("<div class='calming-card'>", unsafe_allo_
