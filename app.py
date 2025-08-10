import streamlit as st
from datetime import datetime
import re
import base64
import pandas as pd
import random
import textwrap

st.set_page_config(page_title="SafeSpace Organization", page_icon="🧠", layout="wide")

# ---------- CSS ----------
st.markdown(
    """
    <style>
    :root {
        --primary: #4a9b8e;
        --accent: #ff9a8b;
        --light: #f0f7f5;
        --dark: #2c3e50;
        --deep-blue: #1E3A8A;
    }
    .stApp {
        background-color: var(--light);
        font-family: 'Inter', sans-serif;
        color: var(--dark);
        min-height: 100vh;
        background-image: url('https://www.transparenttextures.com/patterns/soft-wallpaper.png');
        background-attachment: fixed;
    }
    h1, h2, h3, h4 {
        font-family: 'Merriweather', serif;
        color: var(--deep-blue);
        font-weight: 400;
    }
    .safe-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 12px;
        padding: 1.8rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 1.8rem;
        border-left: 4px solid var(--primary);
    }
    .calming-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1.2rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
        border: 1px solid #e6f2f0;
        transition: all 0.3s ease;
    }
    .calming-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 12px rgba(74, 155, 142, 0.15);
    }
    .primary-btn {
        background: linear-gradient(135deg, var(--primary), #5ab4a7);
        color: white;
        padding: 0.7rem 1.5rem;
        border-radius: 8px;
        border: none;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
        font-size: 1rem;
        margin: 0.5rem 0;
    }
    .mood-option {
        padding: 1rem;
        margin: 0.5rem;
        border-radius: 8px;
        cursor: pointer;
        text-align: center;
        background: #f8fbfa;
        transition: all 0.2s;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 110px;
    }
    .mood-emoji { font-size: 2.2rem; margin-bottom: 0.5rem; }
    .testimonial { padding: 1.5rem; background: linear-gradient(to right, #f8fbfa, #e6f2f0); border-radius: 8px; margin: 1.2rem 0; border-left: 3px solid var(--accent); font-style: italic; position: relative; }
    .testimonial::before { content: "“"; font-size: 3rem; position: absolute; top: -15px; left: 10px; color: var(--primary); opacity: 0.3; }
    .therapist-card { padding: 1.2rem; background: white; border-radius: 8px; box-shadow: 0 3px 8px rgba(0,0,0,0.06); text-align: center; margin: 0.7rem; height: 100%; }
    .confidential { font-size: 0.95rem; color: #5a6c75; margin-top: 1.2rem; padding: 1rem; background: #f8f9fa; border-radius: 6px; border-left: 3px solid var(--primary); line-height: 1.6; }
    @media (max-width: 768px) {
        .calming-card { padding: 1rem; margin: 1rem 0; }
        h1 { font-size: 2rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Session State ----------
if "mood_history" not in st.session_state:
    st.session_state.mood_history = []
if "support_form_data" not in st.session_state:
    st.session_state.support_form_data = {}
if "quiz_results" not in st.session_state:
    st.session_state.quiz_results = None

# ---------- Helper functions ----------
def get_download_link(text_content: str, file_name: str):
    b64 = base64.b64encode(text_content.encode()).decode()
    href = f'<a href="data:file/text;base64,{b64}" download="{file_name}" class="primary-btn">Download</a>'
    return href

def export_mood_history_csv():
    df = pd.DataFrame(st.session_state.mood_history)
    if not df.empty:
        df["Date"] = df["Date"].apply(lambda d: d.strftime("%Y-%m-%d %H:%M"))
    return df.to_csv(index=False)

def validate_email(email: str):
    return re.match(r"^[a-zA-Z0-9_.+\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-.]+$", email)

def validate_phone(phone: str):
    s = phone.replace(" ", "").replace("-", "")
    return re.match(r"^\+?254\d{9}$|^0\d{9}$", s)

# ---------- Static data ----------
therapists = [
    {
        "name": "Dr. Amina Hassan",
        "specialty": "Trauma & PTSD Specialist",
        "approach": "EMDR, Somatic Therapy, CBT",
        "experience": "12 years",
        "bio": "Specializes in trauma recovery with expertise across East Africa.",
        "credentials": "PhD Clinical Psychology, Certified EMDR Therapist"
    },
    {
        "name": "Ben Ochieng",
        "specialty": "Relationships & Family Therapy",
        "approach": "Emotion-Focused Therapy, Gottman Method",
        "experience": "8 years",
        "bio": "Works with couples and families to rebuild trust and communication.",
        "credentials": "MA Marriage & Family Therapy"
    },
    {
        "name": "Grace Mwangi",
        "specialty": "Depression & Mood Disorders",
        "approach": "CBT, Positive Psychology",
        "experience": "10 years",
        "bio": "Strength-based approach for depression recovery.",
        "credentials": "MA Clinical Psychology, CBT Practitioner"
    },
    {
        "name": "David Kimani",
        "specialty": "Youth & Adolescent Mental Health",
        "approach": "Play Therapy, Art Therapy",
        "experience": "7 years",
        "bio": "Creates safe spaces for children and teens using creative modalities.",
        "credentials": "MS Child Psychology"
    }
]

therapy_methods = [
    {"name": "Cognitive Behavioral Therapy (CBT)", "desc": "Identifies and changes negative thought patterns and behaviors.", "uses": "Depression, anxiety, phobias"},
    {"name": "EMDR", "desc": "Processes traumatic memories with bilateral stimulation.", "uses": "PTSD, trauma"},
    {"name": "DBT", "desc": "Builds skills in emotional regulation and distress tolerance.", "uses": "Emotion dysregulation, self-harm"},
    {"name": "MBSR", "desc": "Mindfulness program for stress reduction.", "uses": "Stress, chronic pain, anxiety"},
]

symptom_guide = {
    "Anxiety": {
        "physical": "Racing heart, sweating, trembling, dizziness, stomach issues",
        "emotional": "Excessive worry, fear of losing control, irritability",
        "coping": "Deep breathing, grounding, scheduled worry time"
    },
    "Depression": {
        "physical": "Fatigue, sleep changes, appetite changes",
        "emotional": "Persistent sadness, loss of interest, hopelessness",
        "coping": "Behavioral activation, structured routines, social re-engagement"
    },
    "PTSD": {
        "physical": "Insomnia, hypervigilance, exaggerated startle response",
        "emotional": "Flashbacks, avoidance, numbness",
        "coping": "Grounding, safety plan, trauma-focused therapy"
    }
}

testimonials = [
    "SafeSpace gave me tools to manage my anxiety that I'll use for life.",
    "The community workshops helped me connect with others and feel less alone.",
    "The mood journal helped me see patterns I never noticed.",
    "SafeSpace's resources empowered me to take charge of my mental health."
]

# ---------- Layout: Multi-tabs ----------
tabs = st.tabs(["Home", "Support Services", "Education", "Tools & Activities", "Founders", "Therapists", "Contact & Support", "FAQ & Resources"])

# -------- HOME --------
with tabs[0]:
    st.markdown("<div class='safe-container' style='text-align: center; background: linear-gradient(rgba(74,155,142,0.95), rgba(90,180,167,0.95)); color: white; padding: 2rem; border-radius: 12px;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: white; font-size: 2.4rem; margin-bottom: 0.3rem;'>SafeSpace Organization</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: rgba(255,255,255,0.95); font-size: 1.1rem; max-width: 900px; margin: 0 auto;'>A holistic mental health platform offering therapy, community support, self-help tools, and preventative education. Our culturally-informed services empower individuals, families, and communities across Kenya and beyond.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("## Quick Actions")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='calming-card'>", unsafe_mood = True)
        st.markdown("### Mood Journal")
        st.markdown("Log your emotions, identify patterns, and gain insights with our guided journal. Downloadable entries for sharing with your support network.")
        if st.button("Open Mood Journal"):
            st.experimental_set_query_params(section="tools")
            st.experimental_rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
        st.markdown("### Get Matched")
        st.markdown("Complete a brief form to connect with a therapist or peer support group tailored to your needs within 24 hours.")
        if st.button("Start Matching Process"):
            st.experimental_set_query_params(section="contact")
            st.experimental_rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
        st.markdown("### Self-Check")
        st.markdown("Take a quick, confidential self-assessment to reflect on your mental wellbeing and receive personalized recommendations.")
        if st.button("Take Self-Check"):
            st.experimental_set_query_params(section="tools")
            st.experimental_rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Our Mission")
    st.markdown(textwrap.dedent("""
        SafeSpace Organization is dedicated to fostering mental wellness through accessible, evidence-based support, education, and community engagement.
        We provide therapy, peer support groups, crisis intervention, and preventative workshops to empower individuals and strengthen communities.
    """))

# -------- SUPPORT SERVICES --------
with tabs[1]:
    st.markdown("<div class='safe-container'>", unsafe_allow_html=True)
    st.markdown("## Support Services")
    st.markdown("SafeSpace offers a range of services beyond traditional counseling, including therapy, peer support, community programs, and crisis intervention.")
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.markdown("### Individual Therapy")
    st.markdown("- Personalized 50-minute sessions using evidence-based methods (CBT, EMDR, psychodynamic) tailored to your unique needs.")
    st.markdown("### Peer Support Groups")
    st.markdown("- Facilitated groups for shared experiences, including anxiety, grief, parenting, and youth mental health. Build connection and resilience.")
    st.markdown("### Community Workshops & Outreach")
    st.markdown("- Free or low-cost workshops on stress management, mindfulness, and mental health literacy for schools, workplaces, and communities.")
    st.markdown("### Crisis Intervention")
    st.markdown("- Immediate support through our 24/7 crisis line and safety planning for individuals in distress.")
    st.markdown("### Specialized Services")
    st.markdown("- Youth programs, trauma-informed care, workplace wellness, and culturally-sensitive support for diverse communities.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### Therapy Approaches (Short Primer)")
    for m in therapy_methods:
        st.markdown(f"**{m['name']}** — {m['desc']}  \n*Common uses:* {m['uses']}")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='safe-container'>", unsafe_allow_html=True)
    st.markdown("### Request Support (Intake Form)")
    st.markdown("Complete this form to get matched with a therapist, peer group, or community program.")
    with st.form("support_form"):
        name = st.text_input("Full name")
        email = st.text_input("Email address")
        phone = st.text_input("Phone (Kenya preferred, e.g. +2547XXXXXXXX)")
        concern = st.selectbox("Primary concern", ["Anxiety", "Depression", "Trauma/PTSD", "Relationship Issues", "Grief/Loss", "Stress", "Community Support", "Other"])
        preference = st.radio("Support preference", ["Therapy", "Peer Support Group", "Community Workshop", "Crisis Support"])
        brief = st.text_area("Briefly describe what you're seeking support for (optional)", height=120)
        submit = st.form_submit_button("Submit Request")
        if submit:
            errors = []
            if not name or not email or not phone:
                errors.append("Please complete name, email, and phone.")
            if email and not validate_email(email):
                errors.append("Please enter a valid email.")
            if phone and not validate_phone(phone):
                errors.append("Please enter a valid Kenyan phone number (e.g. +2547XXXXXXXX).")
            if errors:
                for e in errors:
                    st.error(e)
            else:
                st.session_state.support_form_data = {
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "concern": concern,
                    "preference": preference,
                    "brief": brief,
                    "submitted_at": datetime.now()
                }
                st.success("Thank you — your request has been received. We'll connect you with the right support within 24 hours.")
                st.balloons()
    st.markdown("</div>", unsafe_allow_html=True)

# -------- EDUCATION --------
with tabs[2]:
    st.markdown("<div class='safe-container'>", unsafe_allow_html=True)
    st.markdown("## Mental Health Education")
    st.markdown("Explore evidence-based resources to understand mental health, recognize symptoms, and learn proactive coping strategies.")
    st.markdown("### Common Conditions (Overview)")
    for cond, info in symptom_guide.items():
        st.markdown(f"**{cond}**")
        st.markdown(f"- *Physical:* {info['physical']}")
        st.markdown(f"- *Emotional/Cognitive:* {info['emotional']}")
        st.markdown(f"- *Coping & Early Interventions:* {info['coping']}")
        st.markdown("")
    st.markdown("### Understanding Support Options")
    st.markdown(textwrap.dedent("""
        - **Therapy:** One-on-one sessions with licensed professionals using evidence-based methods.
        - **Peer Groups:** Safe, facilitated spaces to share experiences and build community.
        - **Workshops:** Interactive sessions on stress management, resilience, and mental health literacy.
        - **Confidentiality:** All services prioritize privacy, with legal limits for safety concerns (e.g., risk of harm).
    """))
    st.markdown("### Harm Reduction and Safety Planning")
    st.markdown(textwrap.dedent("""
        - In crisis? Contact our 24/7 crisis line or local emergency services.
        - Create a safety plan: identify triggers, coping strategies, trusted contacts, and professional resources.
        - Keep crisis numbers and support contacts easily accessible.
    """))
    st.markdown("</div>", unsafe_allow_html=True)

# -------- TOOLS & ACTIVITIES --------
with tabs[3]:
    st.markdown("<div class='safe-container'>", unsafe_allow_html=True)
    st.markdown("## Tools & Activities")
    st.markdown("Access self-help tools to support your mental wellness, track progress, and build resilience.")

    # Mood tracker
    st.markdown("### Mood Tracker & Journal")
    st.markdown("Track your emotions daily to identify patterns and triggers. Add notes to reflect on your experiences and download your journal to share with your therapist or support group.")
    mood_cols = st.columns(5)
    mood_map = {
        "Radiant": "😊",
        "Calm": "😌",
        "Neutral": "😐",
        "Anxious": "😟",
        "Sad": "😔"
    }
    selected_mood = st.selectbox("Select current mood", ["Choose a mood"] + list(mood_map.keys()))
    note = st.text_area("Journal entry (optional)", height=120, placeholder="What happened today? What thoughts, feelings, or body sensations did you notice? How did you cope?")
    if st.button("Save Entry"):
        if selected_mood == "Choose a mood":
            st.error("Please select a mood first to ensure accurate tracking.")
        else:
            entry = {"Date": datetime.now(), "Mood": selected_mood, "Note": note}
            st.session_state.mood_history.append(entry)
            st.success("Journal entry saved successfully.")
    if st.session_state.mood_history:
        df = pd.DataFrame(st.session_state.mood_history)
        df_display = df.copy()
        df_display["Date"] = df_display["Date"].dt.strftime("%b %d, %Y %I:%M %p")
        st.dataframe(df_display[["Date", "Mood", "Note"]], hide_index=True)
        csv = export_mood_history_csv()
        st.markdown(get_download_link(csv, "mood_journal.csv"), unsafe_allow_html=True)

    st.markdown("---")
    # Breathing exercise
    st.markdown("### Guided Breathing Exercises")
    st.markdown("Practice these evidence-based techniques to reduce stress and promote calm. Use them anytime, anywhere.")
    st.markdown("**Box Breathing:** Inhale for 4 seconds, hold for 4 seconds, exhale for 4 seconds, hold for 4 seconds. Repeat 4–6 cycles.")
    st.markdown("**4-7-8 Breathing:** Inhale for 4 seconds, hold for 7 seconds, exhale for 8 seconds. Ideal for relaxation or sleep. Repeat 4 cycles.")
    st.markdown("Set a timer for a 3-minute practice and follow either technique for immediate relief.")

    st.markdown("---")
    # Self-assessment quiz
    st.markdown("### Self-Assessment Tool")
    st.markdown("This confidential, non-diagnostic tool helps you reflect on your mental wellbeing over the past 2 weeks. Results include personalized recommendations.")
    with st.form("self_assessment_form"):
        st.markdown("Rate how often you've experienced the following (0=Not at all, 1=Several days, 2=More than half the days, 3=Nearly every day).")
        q1 = st.slider("1. Little interest or pleasure in doing things", 0, 3, 0)
        q2 = st.slider("2. Feeling down, depressed, or hopeless", 0, 3, 0)
        q3 = st.slider("3. Feeling nervous, anxious, or on edge", 0, 3, 0)
        q4 = st.slider("4. Not being able to stop worrying", 0, 3, 0)
        q5 = st.slider("5. Trouble falling or staying asleep", 0, 3, 0)
        submit_quiz = st.form_submit_button("Submit Self-Check")
        if submit_quiz:
            if q1 + q2 + q3 + q4 + q5 == 0:
                st.error("Please answer at least one question to receive results.")
            else:
                anxiety_score = q3 + q4
                depression_score = q1 + q2
                st.session_state.quiz_results = {"anxiety": anxiety_score, "depression": depression_score}
                st.markdown("**Your Results (Informal):**")
                st.markdown(f"- Depression-related score: {depression_score}/6")
                st.markdown(f"- Anxiety-related score: {anxiety_score}/6")
                if depression_score >= 3 or anxiety_score >= 3:
                    st.warning("Your scores suggest moderate symptoms. We recommend connecting with a therapist or joining a peer support group for further assessment.")
                    st.markdown("Try our **Get Matched** tool to find the right support.")
                else:
                    st.success("Your scores are in the mild/low range. Continue using our tools and reach out if symptoms change.")
                    st.markdown("Explore our **Mood Journal** or **Community Workshops** for ongoing support.")

    st.markdown("</div>", unsafe_allow_html=True)

# -------- FOUNDERS --------
with tabs[4]:
    st.markdown("<div class='safe-container'>", unsafe_allow_html=True)
    st.markdown("## Founders")
    st.markdown("<div style='display: grid; grid-template-columns: 1fr 2fr; gap: 1.2rem; align-items: center;'>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.markdown("<div style='background: var(--primary); width: 110px; height: 110px; border-radius: 50%; margin: 0 auto 1rem; display: flex; align-items: center; justify-content: center; font-size: 2.4rem; color: white;'>J</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div>", unsafe_allow_html=True)
    st.markdown("### Jerim Owino — Founder & Program Lead")
    st.markdown(textwrap.dedent("""
        Jerim Owino founded SafeSpace Organization to make mental health support accessible and culturally relevant across Kenya. With expertise in community mental health and education, Jerim leads innovative programs and advocacy.
        \n**Vision:** Empower resilient communities through holistic mental health care and education.
        \n**Work:** Oversees therapy services, peer groups, community outreach, and partnerships.
        \nJerim is passionate about training lay counselors and integrating mental health into schools and workplaces.
    """))
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# -------- THERAPISTS --------
with tabs[5]:
    st.markdown("<div class='safe-container'>", unsafe_allow_html=True)
    st.markdown("## Our Therapeutic Team")
    st.markdown("Our licensed professionals provide trauma-informed, culturally-sensitive care across diverse specialties.")
    cols = st.columns(2)
    idx = 0
    for t in therapists:
        with cols[idx % 2]:
            st.markdown("<div class='therapist-card'>", unsafe_allow_html=True)
            st.markdown(f"<h4>{t['name']}</h4>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: var(--primary); font-weight: 600;'>{t['specialty']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 0.95rem;'>{t['bio']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 0.85rem; background: #f0f7f5; padding: 0.6rem; border-radius:6px;'>{t['credentials']} • {t['experience']}</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        idx += 1
    st.markdown("</div>", unsafe_allow_html=True)

# -------- CONTACT & SUPPORT --------
with tabs[6]:
    st.markdown("<div class='safe-container'>", unsafe_allow_html=True)
    st.markdown("## Contact & Support")
    st.markdown("Reach out for support or inquiries. For immediate crises, use our 24/7 crisis line or local emergency services.")
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.markdown("### Emergency & Crisis Contacts")
    st.markdown("- SafeSpace Crisis Line: +254 781 095 919 (24/7)")
    st.markdown("- Befrienders Kenya Suicide Prevention Hotline: 1199")
    st.markdown("- National Emergency (Kenya): 999")
    st.markdown("- Nairobi Women's Hospital Gender Violence Recovery Centre: +254 20 272 6300")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### Send Us a Message")
    with st.form("contact_form"):
        full = st.text_input("Your full name")
        email = st.text_input("Your email")
        phone = st.text_input("Phone (optional)")
        message = st.text_area("How can we help you?", height=150)
        send = st.form_submit_button("Send Message")
        if send:
            if not full or not email or not message:
                st.error("Please complete name, email, and message.")
            elif not validate_email(email):
                st.error("Please provide a valid email.")
            else:
                st.success("Thanks — we received your message. We'll contact you shortly.")
    st.markdown("</div>", unsafe_allow_html=True)

# -------- FAQ & RESOURCES --------
with tabs[7]:
    st.markdown("<div class='safe-container'>", unsafe_allow_html=True)
    st.markdown("## FAQ & Resources")
    st.markdown("**Q:** How do I know if I need support?  \n**A:** If you're experiencing distress affecting daily life, relationships, or wellbeing, our services—therapy, peer groups, or workshops—can help.")
    st.markdown("**Q:** Are services confidential?  \n**A:** Yes, all services are confidential, except in cases of imminent risk or legal requirements (e.g., harm to self/others).")
    st.markdown("**Q:** What’s the difference between therapy and peer support?  \n**A:** Therapy involves professional, one-on-one care; peer support offers group-based connection with shared experiences.")
    st.markdown("---")
    st.markdown("### Recommended Reading")
    st.markdown("- _The Body Keeps the Score_ — Bessel van der Kolk")
    st.markdown("- _Feeling Good_ — David D. Burns")
    st.markdown("- _Self-Compassion_ — Kristin Neff")
    st.markdown("---")
    st.markdown("### Online Resources")
    st.markdown("- Kenya Psychological Association (KPA)")
    st.markdown("- Befrienders Worldwide")
    st.markdown("- National Alliance on Mental Illness (NAMI)")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown(
    """
    <div style='margin-top: 2rem; padding: 1.6rem; text-align: center; background: #e8f4f8; border-top: 1px solid #d1e7e3;'>
        <div style='max-width:900px; margin: 0 auto;'>
            <strong>SafeSpace Organization</strong> — Holistic mental health support through therapy, peer groups, and community programs.
            <div style='margin-top: 0.6rem; font-size: 0.9rem; color: #6c757d;'>Contact: +254 781 095 919 • info@safespace.org</div>
            <div style='margin-top: 0.6rem; font-size: 0.85rem; color: #6c757d;'>© 2025 SafeSpace Organization • Licensed & Confidential</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
