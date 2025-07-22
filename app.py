import streamlit as st
from PIL import Image

# Page setup
st.set_page_config(page_title="Safe Space Kenya", layout="wide")

# Custom color scheme
st.markdown("""
<style>
body {
    background-color: #f8f9fa;
    color: #2c3e50;
}
h1, h2, h3 {
    color: #2a7a7c;
}
.stTabs [data-baseweb="tab"] {
    font-size: 16px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("Safe Space Kenya")
st.subheader("Empowering minds, nurturing hope.")
st.markdown("---")

# SERVICES
services = [
    {
        "icon": "🧠",
        "title": "Individual Counseling",
        "summary": "One-on-one therapy for personal mental wellness.",
        "details": """
**What you’ll receive:**
- Private, confidential sessions
- Help with depression, anxiety, trauma, stress
- Cognitive Behavioral Therapy (CBT), talk therapy, or person-centered support

**Best for:** Adults and youth seeking a safe, personalized space to process life.
"""
    },
    {
        "icon": "👨‍👩‍👧",
        "title": "Family Therapy",
        "summary": "Rebuilding relationships within the family system.",
        "details": """
**What you’ll receive:**
- Family group sessions (face-to-face or virtual)
- Support for conflict resolution and communication
- Tools to heal family trauma and reconnect

**Best for:** Families navigating separation, parenting conflict, or intergenerational trauma.
"""
    },
    {
        "icon": "🧒",
        "title": "Adolescent Counseling",
        "summary": "Guidance for teens on emotional, academic & identity issues.",
        "details": """
**What you’ll receive:**
- Specialized sessions for teenagers (12–19)
- Help with peer pressure, bullying, career doubts, or trauma
- Approaches like art therapy, journaling, or solution-focused therapy

**Best for:** Teens and pre-teens needing confidential, age-appropriate support.
"""
    },
    {
        "icon": "💬",
        "title": "Group Counseling",
        "summary": "Support groups with guided topics and peer sharing.",
        "details": """
**What you’ll receive:**
- Weekly themed group therapy sessions
- Peer encouragement + guided therapeutic exercises
- Topics include grief, addiction recovery, parenting, self-esteem

**Best for:** Anyone who finds healing in shared experiences.
"""
    },
    {
        "icon": "🎨",
        "title": "Art Therapy",
        "summary": "Healing through creative expression.",
        "details": """
**What you’ll receive:**
- Drawing, painting, storytelling, poetry as tools for healing
- Focus on emotions that are hard to verbalize
- Trauma-informed approach for all ages

**Best for:** Clients who struggle to speak about their pain directly.
"""
    },
    {
        "icon": "🧕",
        "title": "Faith-Sensitive Counseling",
        "summary": "Therapy that respects your cultural and religious background.",
        "details": """
**What you’ll receive:**
- Therapy that aligns with your faith, values, and beliefs
- Sessions led by therapists familiar with Christian, Muslim & traditional African practices
- Spiritually nurturing techniques (guided reflection, prayer-informed mindfulness)

**Best for:** Clients looking for culturally relevant and faith-based healing.
"""
    },
    {
        "icon": "🌐",
        "title": "Online Counseling",
        "summary": "Virtual mental health support wherever you are.",
        "details": """
**What you’ll receive:**
- Zoom or WhatsApp sessions with licensed therapists
- Flexible scheduling: day or evening sessions
- Includes individual, family, and adolescent therapy formats

**Best for:** Busy clients, remote areas, or those who prefer privacy at home.
"""
    }
]

st.header("🧰 Our Therapeutic Services")
tab_titles = [f"{s['icon']} {s['title']}" for s in services]
tabs = st.tabs(tab_titles)

for tab, service in zip(tabs, services):
    with tab:
        st.subheader(service['title'])
        st.markdown(f"**Overview:** {service['summary']}")
        with st.expander("📘 Learn More"):
            st.markdown(service["details"])

# TEAM SECTION
st.header("👥 Meet Our Team")

team_members = [
    {
        "name": "Jerim Owino",
        "role": "Founder & CEO",
        "image": "jerim.jpg",  # must be in the same folder
        "bio": "Jerim is a trained mental health advocate and youth empowerment trainer. He offers CBT-based therapy and trauma-informed counseling.",
        "contact": "owinojerim269@gmail.com",
        "phone": "+254 781 095 919",
        "availability": "Mon–Fri: 9am–6pm",
        "location": "Ngong Road, Nairobi"
    },
    {
        "name": "Hamdi Roble",
        "role": "Co-Founder & Senior Therapist",
        "image": "hamdi.jpg",  # must be in the same folder
        "bio": "Hamdi is a culturally-aware therapist with deep experience in trauma support, youth counseling, and faith-sensitive therapy.",
        "contact": "hamdi@safespacekenya.org",
        "phone": "+254 720 987 654",
        "availability": "Tue–Sat: 10am–5pm",
        "location": "Virtual & On-site"
    }
]

cols = st.columns(len(team_members))

for col, member in zip(cols, team_members):
    with col:
        try:
            img = Image.open(member["image"])
            st.image(img, use_column_width=True, caption=member["name"])
        except:
            st.warning(f"Missing image for {member['name']}")
        st.markdown(f"**{member['role']}**")
        st.write(member["bio"])
        st.markdown(f"- 📧 **Email:** {member['contact']}")
        st.markdown(f"- 📞 **Phone:** {member['phone']}")
        st.markdown(f"- 📍 **Location:** {member['location']}")
        st.markdown(f"- ⏰ **Availability:** {member['availability']}")

# CONTACT
st.header("📞 Contact Us")
st.markdown("""
We welcome you to book a session, ask questions, or walk in for support.

- 🏢 **Address:** Greenhouse Plaza, Ngong Road, Nairobi  
- 📧 **General Email:** [info@safespacekenya.org](mailto:info@safespacekenya.org)  
- 📞 **Phone:** +254 781 095 919 | +254 720 987 654  
- ⏰ **Working Hours:**  
  - Monday – Friday: 8:00 AM – 7:00 PM  
  - Saturday: 9:00 AM – 4:00 PM
""")

# FOOTER
st.markdown("---")
st.markdown(
    "<center style='color: #777;'>© 2025 Safe Space Kenya | Designed with ❤️ for Mental Wellness in Africa</center>",
    unsafe_allow_html=True
)
