import streamlit as st
from datetime import datetime
import re
import base64
import pandas as pd
import random
import textwrap
import matplotlib.pyplot as plt

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
if "counseling_form_data" not in st.session_state:
    st.session_state.counseling_form_data = {}
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
    {"name": "Acceptance and Commitment Therapy (ACT)", "desc": "Focuses on accepting thoughts and committing to values-based actions.", "uses": "Anxiety, depression, chronic pain"},
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
    },
    "OCD": {
        "physical": "Compulsions like repeated checking or cleaning",
        "emotional": "Intrusive thoughts, anxiety from not performing rituals",
        "coping": "Exposure and response prevention, mindfulness"
    },
    "Bipolar Disorder": {
        "physical": "Sleep disturbances, energy fluctuations",
        "emotional": "Mood swings from mania to depression",
        "coping": "Mood tracking, medication adherence, routine"
    }
}

testimonials = [
    "SafeSpace gave me tools to manage my anxiety that I'll use for life.",
    "After 6 sessions I feel like a different person — hope is back.",
    "Culturally-sensitive therapists made all the difference for me.",
    "The mood journal helped me see patterns I never noticed."
]

# ---------- Navigation ----------
query_params = st.experimental_get_query_params()
selected_section = query_params.get("section", [None])[0]

pages = ["Home", "Services", "Education", "Tools & Activities", "Founders", "Therapists", "Contact & Support", "FAQ & Resources"]

default_index = 0
if selected_section == "tools":
    default_index = pages.index("Tools & Activities")
elif selected_section == "therapy":
    default_index = pages.index("Services")
elif selected_section == "contact":
    default_index = pages.index("Contact & Support")

st.sidebar.title("Navigation")
selected_page = st.sidebar.selectbox("Select Page", pages, index=default_index)

# -------- HOME --------
if selected_page == "Home":
    st.markdown("<div class='safe-container' style='text-align: center; background: linear-gradient(rgba(74,155,142,0.95), rgba(90,180,167,0.95)); color: white; padding: 2rem; border-radius: 12px;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: white; font-size: 2.4rem; margin-bottom: 0.3rem;'>SafeSpace Organization</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: rgba(255,255,255,0.95); font-size: 1.1rem; max-width: 900px; margin: 0 auto;'>A compassionate, evidence-based mental health organization supporting individuals, couples and families. Confidential care, culturally-informed, and accessible resources for emotional wellbeing. We offer more than just counselling – comprehensive support including education, self-help tools, community programs, and preventive care.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("## Quick Actions")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("### Mood Journal")
        st.markdown("Quickly log how you feel and track patterns.")
        if st.button("Open Mood Tools"):
            st.experimental_set_query_params(section="tools")
            st.experimental_rerun()
    with c2:
        st.markdown("### Get Matched")
        st.markdown("Complete our intake form to get matched to a therapist within 24 hours.")
        if st.button("Start Intake Form"):
            st.experimental_set_query_params(section="therapy")
            st.experimental_rerun()
    with c3:
        st.markdown("### Self-Check")
        st.markdown("A short self-assessment to help you reflect on your current wellbeing.")
        if st.button("Take Quiz"):
            st.experimental_set_query_params(section="tools")
            st.experimental_rerun()

    st.markdown("---")
    st.markdown("### Our Mission")
    st.markdown(textwrap.dedent("""
        We provide confidential, culturally-sensitive, evidence-based mental health care and resources to strengthen individuals and communities.
        Our approach centers dignity, access, and long-term wellbeing through individual therapy, group programs, and community outreach.
    """))

# -------- SERVICES --------
elif selected_page == "Services":
    st.markdown("<div class='safe-container'>", unsafe_allow_html=True)
    st.markdown("## Services Offered")
    st.markdown("Our organization offers a wide range of services beyond traditional counselling. We provide individualized plans, group sessions, workshops, crisis support, community outreach, and preventive care programs. All therapists are credentialed and engage in ongoing supervision and training.")
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.markdown("### Individual Therapy")
    st.markdown("- One-on-one sessions (50 minutes). Evidence-based methods tailored to you: CBT, psychodynamic, humanistic, EMDR when appropriate.")
    st.markdown("### Couples & Family Therapy")
    st.markdown("- Focus on communication, conflict resolution, parenting, and relationship repair.")
    st.markdown("### Group Programs & Workshops")
    st.markdown("- Psychoeducation groups, coping skills, mindfulness courses, and trauma-informed groups.")
    st.markdown("### Specialized Services")
    st.markdown("- Youth & adolescent therapy, trauma-focused care, grief counselling, and employee support programs.")
    st.markdown("### Community Outreach")
    st.markdown("- Programs to raise mental health awareness and provide support in local communities, schools, and workplaces.")
    st.markdown("### Preventive Care")
    st.markdown("- Workshops and seminars on stress management, resilience building, and early intervention strategies.")
    st.markdown("### Telehealth Services")
    st.markdown("- Convenient online sessions for remote access to care.")
    st.markdown("### Corporate Wellness Programs")
    st.markdown("- Employee Assistance Programs (EAP) to support mental health in professional settings.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### Therapy Approaches (short primer)")
    for m in therapy_methods:
        st.markdown(f"**{m['name']}** — {m['desc']}  \n*Common uses:* {m['uses']}")

    st.markdown("</div>", unsafe_allow_html=True)

    # Intake form
    st.markdown("<div class='safe-container'>", unsafe_allow_html=True)
    st.markdown("### Request a Consultation (Intake Form)")
    with st.form("intake_form"):
        name = st.text_input("Full name")
        email = st.text_input("Email address")
        phone = st.text_input("Phone (Kenya preferred, e.g. +2547XXXXXXXX)")
        concern = st.selectbox("Primary concern", ["Anxiety", "Depression", "Trauma/PTSD", "Relationship Issues", "Grief/Loss", "Stress", "Other"])
        preference = st.radio("Session preference", ["Online", "In-person"])
        brief = st.text_area("Briefly describe what you're seeking support for (optional)", height=120)
        submit = st.form_submit_button("Submit Request")
        if submit:
            errors = []
            if not name or not email or not phone:
                errors.append("Please complete name, email and phone.")
            if email and not validate_email(email):
                errors.append("Please enter a valid email.")
            if phone and not validate_phone(phone):
                errors.append("Please enter a valid Kenyan phone number (e.g. +2547XXXXXXXX).")
            if errors:
                for e in errors:
                    st.error(e)
            else:
                st.session_state.counseling_form_data = {
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "concern": concern,
                    "preference": preference,
                    "brief": brief,
                    "submitted_at": datetime.now()
                }
                st.success("Thank you — your request has been received. We'll match you with a therapist within 24 hours.")
                st.balloons()
    st.markdown("</div>", unsafe_allow_html=True)

# -------- EDUCATION --------
elif selected_page == "Education":
    st.markdown("<div class='safe-container'>", unsafe_allow_html=True)
    st.markdown("## Mental Health Education")
    st.markdown("Comprehensive, evidence-based information about common mental health conditions, risk factors, and support strategies.")
    st.markdown("### Common Conditions (overview)")
    for cond, info in symptom_guide.items():
        st.markdown(f"**{cond}**")
        st.markdown(f"- *Physical:* {info['physical']}")
        st.markdown(f"- *Emotional/Cognitive:* {info['emotional']}")
        st.markdown(f"- *Coping & early interventions:* {info['coping']}")
        st.markdown("")
    st.markdown("### Understanding Therapy: What to expect")
    st.markdown(textwrap.dedent("""
        - The first session typically focuses on assessment and establishing goals.
        - Evidence-based therapies (CBT, DBT, EMDR) have structured techniques and measurable outcomes.
        - Confidentiality is maintained; limits apply if there's imminent risk to safety.
        - Therapy often requires patience: progress can take weeks to months depending on the issue.
    """))
    st.markdown("### Harm reduction and safety planning")
    st.markdown(textwrap.dedent("""
        - If you or someone else is at immediate risk, contact local emergency services.
        - Safety planning: identify triggers, coping strategies, supportive contacts, ways to make the environment safer, and professional resources.
        - Keep a list of crisis numbers and trusted contacts available.
    """))
    st.markdown("</div>", unsafe_allow_html=True)

# -------- TOOLS & ACTIVITIES --------
elif selected_page == "Tools & Activities":
    st.markdown("<div class='safe-container'>", unsafe_allow_html=True)
    st.markdown("## Tools & Activities")
    st.markdown("Use these self-help tools between sessions to strengthen coping and track mood.")

    # Mood tracker
    st.markdown("### Mood Tracker & Journal")
    mood_cols = st.columns(5)
    mood_map = {
        "Radiant": "😊",
        "Calm": "😌",
        "Neutral": "😐",
        "Anxious": "😟",
        "Sad": "😔"
    }
    selected_mood = st.selectbox("Select current mood", ["Choose a mood"] + list(mood_map.keys()))
    note = st.text_area("Journal entry (optional)", height=120, placeholder="What happened today? What thoughts or body sensations did you notice?")
    if st.button("Save Entry"):
        if selected_mood == "Choose a mood":
            st.warning("Please select a mood first.")
        else:
            entry = {"Date": datetime.now(), "Mood": selected_mood, "Note": note}
            st.session_state.mood_history.append(entry)
            st.success("Journal entry saved.")
    if st.session_state.mood_history:
        df = pd.DataFrame(st.session_state.mood_history)
        df_display = df.copy()
        df_display["Date"] = df_display["Date"].dt.strftime("%b %d, %Y %I:%M %p")
        st.dataframe(df_display[["Date", "Mood", "Note"]], hide_index=True)
        csv = export_mood_history_csv()
        st.markdown(get_download_link(csv, "mood_journal.csv"), unsafe_allow_html=True)
        
        # Add mood trend chart to make more informative and prevent empty plot errors
        if len(st.session_state.mood_history) > 1:
            mood_levels = {"Radiant": 5, "Calm": 4, "Neutral": 3, "Anxious": 2, "Sad": 1}
            moods_num = [mood_levels.get(m['Mood'], 3) for m in st.session_state.mood_history]
            dates = [m['Date'] for m in st.session_state.mood_history]
            fig, ax = plt.subplots()
            ax.plot(dates, moods_num, marker='o')
            ax.set_ylabel("Mood Level (5=Best, 1=Worst)")
            ax.set_title("Mood Trend Over Time")
            st.pyplot(fig)
        else:
            st.info("Log at least two entries to view your mood trend chart.")

    st.markdown("---")
    # Breathing exercise
    st.markdown("### Guided Breathing Exercises (instructions)")
    st.markdown("**Box Breathing:** inhale 4s — hold 4s — exhale 4s — hold 4s. Repeat 4–6 cycles.")
    st.markdown("**4-7-8 breathing:** inhale 4s — hold 7s — exhale 8s. Repeat 4 cycles for sleep aid.")
    st.markdown("Try a 3-minute breathing practice: set a timer and follow any of the above.")

    st.markdown("---")
    # Self-assessment quiz (simple screener)
    st.markdown("### Short Self-Assessment (not diagnostic)")
    st.markdown("Answer how often you've experienced the following in the past 2 weeks (0=Not at all, 1=Several days, 2=More than half the days, 3=Nearly every day).")
    q1 = st.slider("1. Little interest or pleasure in doing things", 0, 3, 0)
    q2 = st.slider("2. Feeling down, depressed, or hopeless", 0, 3, 0)
    q3 = st.slider("3. Feeling nervous, anxious, or on edge", 0, 3, 0)
    q4 = st.slider("4. Not being able to stop worrying", 0, 3, 0)
    q5 = st.slider("5. Trouble falling or staying asleep", 0, 3, 0)
    if st.button("Get self-check result"):
        # Simple heuristic: PHQ-4 style small screener
        anxiety_score = q3 + q4
        depression_score = q1 + q2
        st.session_state.quiz_results = {"anxiety": anxiety_score, "depression": depression_score}
        st.markdown("**Result (informal):**")
        st.markdown(f"- Depression-related score: {depression_score} (0-6)")
        st.markdown(f"- Anxiety-related score: {anxiety_score} (0-6)")
        if depression_score >= 3 or anxiety_score >= 3:
            st.warning("Your score suggests you may be experiencing moderate symptoms. Consider contacting a mental health professional for a full assessment.")
        else:
            st.success("Your score is in the mild/low range. Continue self-care and monitor changes. Reach out if symptoms worsen.")

    st.markdown("</div>", unsafe_allow_html=True)

# -------- FOUNDERS --------
elif selected_page == "Founders":
    st.markdown("<div class='safe-container'>", unsafe_allow_html=True)
    st.markdown("## Founders")
    st.markdown("<div style='display: grid; grid-template-columns: 1fr 2fr; gap: 1.2rem; align-items: center;'>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.markdown("<div style='background: var(--primary); width: 110px; height: 110px; border-radius: 50%; margin: 0 auto 1rem; display: flex; align-items: center; justify-content: center; font-size: 2.4rem; color: white;'>J</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div>", unsafe_allow_html=True)
    st.markdown("### Jerim Owino — Founder & Program Lead")
    st.markdown(textwrap.dedent("""
        Jerim Owino is the visionary behind SafeSpace Organization. With a background in community mental health, education, and counseling practice, Jerim established SafeSpace to improve access to culturally-informed therapy, training, and advocacy across Kenya.
        \n**Vision:** Build resilient communities with accessible mental health care and preventative education.
        \n**Work:** Program design, therapist supervision, community outreach, and partnership development.
        \nJerim is committed to training lay counselors, supporting survivors, and integrating mental health into schools and workplaces.
    """))
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# -------- THERAPISTS --------
elif selected_page == "Therapists":
    st.markdown("<div class='safe-container'>", unsafe_allow_html=True)
    st.markdown("## Our Therapeutic Team")
    st.markdown("Licensed professionals, diverse approaches, and trauma-informed care.")
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
elif selected_page == "Contact & Support":
    st.markdown("<div class='safe-container'>", unsafe_allow_html=True)
    st.markdown("## Contact & Support")
    st.markdown("If you need help, please reach out. For emergencies, use local emergency numbers.")
    # Crisis contacts
    st.markdown("<div class='calming-card'>", unsafe_allow_html=True)
    st.markdown("### Emergency & Crisis Contacts")
    st.markdown("- SafeSpace Crisis Line: +254 781 095 919 (24/7)")
    st.markdown("- Befrienders Kenya Suicide Prevention Hotline: 1199")
    st.markdown("- National Emergency (Kenya): 999")
    st.markdown("- Nairobi Women's Hospital Gender Violence Recovery Centre: +254 20 272 6300")
    st.markdown("</div>", unsafe_allow_html=True)

    # Contact form
    st.markdown("### Send us a message")
    with st.form("contact_form"):
        full = st.text_input("Your full name")
        email = st.text_input("Your email")
        phone = st.text_input("Phone (optional)")
        message = st.text_area("How can we help you?", height=150)
        send = st.form_submit_button("Send Message")
        if send:
            if not full or not email or not message:
                st.error("Please complete name, email and message.")
            elif not validate_email(email):
                st.error("Please provide a valid email.")
            else:
                # In a production app you'd send/store this securely
                st.success("Thanks — we received your message. We'll contact you shortly.")
    st.markdown("</div>", unsafe_allow_html=True)

# -------- FAQ & RESOURCES --------
elif selected_page == "FAQ & Resources":
    st.markdown("<div class='safe-container'>", unsafe_allow_html=True)
    st.markdown("## FAQ & Resources")
    st.markdown("**Q:** How do I know therapy is right for me?  \n**A:** If distress affects daily functioning, relationships, sleep, work or school — consider seeking assessment. A trained clinician can advise on appropriate steps.")
    st.markdown("**Q:** Is therapy confidential?  \n**A:** Yes. Confidentiality is standard except where safety laws require disclosure (risk of harm to self/others, child protection concerns).")
    st.markdown("**Q:** How long does therapy take?  \n**A:** Varies — some brief problems respond in 6-12 sessions; complex trauma may require longer-term work.")
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
            <strong>SafeSpace Organization</strong> — Professional, confidential mental health care for individuals, couples, and families.
            <div style='margin-top: 0.6rem; font-size: 0.9rem; color: #6c757d;'>Contact: +254 781 095 919 • info@safespace.org</div>
            <div style='margin-top: 0.6rem; font-size: 0.85rem; color: #6c757d;'>© 2025 SafeSpace Organization • Licensed & Confidential</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
