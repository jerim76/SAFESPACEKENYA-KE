import streamlit as st

# Set page config
st.set_page_config(page_title="Safe Space Kenya", layout="wide")

# Header
st.title("Safe Space Kenya")
st.subheader("Empowering minds, nurturing hope.")

st.markdown("---")

# Define services
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

# Display Services in Tabs
st.header("🧰 Our Therapeutic Services")
tab_titles = [f"{s['icon']} {s['title']}" for s in services]
tabs = st.tabs(tab_titles)

for tab, service in zip(tabs, services):
    with tab:
        st.subheader(service['title'])
        st.markdown(f"**Overview:** {service['summary']}")
        with st.expander("📘 Learn More"):
            st.markdown(service["details"])
