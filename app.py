import streamlit as st
from datetime import datetime
from PIL import Image
import os

# Set page configuration
st.set_page_config(
    page_title="Safe Space Kenya",
    layout="wide"
)

# App title and intro
st.title("Safe Space Kenya")
st.markdown("### Healing Minds, Restoring Lives")

# Hero Banner
st.markdown("""
<div style='background-color:#2a7a7c;padding:2rem;border-radius:10px;text-align:center;color:white;'>
    <h1>Welcome to Safe Space Kenya</h1>
    <p>Your trusted mental health partner.</p>
</div>
""", unsafe_allow_html=True)

# --------------------- Services --------------------- #
st.header("🛠️ Our Services")

with st.expander("📱 Online Counseling"):
    st.write("""
**What We Offer:**  
Secure, confidential video or phone therapy sessions.

**Who It’s For:**  
Busy individuals, clients in remote areas, or those preferring privacy.

**Why Choose Us:**  
Flexible scheduling, culturally respectful care, and licensed therapists.
    """)

with st.expander("👤 Individual Counseling"):
    st.write("""
**What We Offer:**  
One-on-one therapy addressing anxiety, depression, trauma, and personal development.

**Who It’s For:**  
Anyone seeking emotional support or struggling with mental health.

**Why Choose Us:**  
Evidence-based approaches tailored to your needs.
    """)

with st.expander("👥 Group Therapy"):
    st.write("""
**What We Offer:**  
Facilitated support groups tackling grief, addiction, stress, and identity.

**Who It’s For:**  
Teens, young adults, and community members seeking peer healing.

**Why Choose Us:**  
Safe, inclusive spaces with shared experiences.
    """)

with st.expander("🏠 Family Counseling"):
    st.write("""
**What We Offer:**  
Sessions that bring families together to improve communication and resolve conflicts.

**Who It’s For:**  
Parents, guardians, and children needing emotional connection.

**Why Choose Us:**  
Therapists trained in family systems and adolescent care.
    """)

with st.expander("🎓 Workshops & Training"):
    st.write("""
**What We Offer:**  
On-demand mental health workshops and trauma-informed training for schools, NGOs, and corporates.

**Who It’s For:**  
Teachers, youth leaders, HR departments, caregivers.

**Why Choose Us:**  
Custom-tailored, engaging sessions rooted in Kenyan contexts.
    """)

with st.expander("❤️ Trauma Support"):
    st.write("""
**What We Offer:**  
Counseling for survivors of abuse, accidents, loss, and PTSD.

**Who It’s For:**  
Anyone healing from trauma and needing professional guidance.

**Why Choose Us:**  
Culturally-sensitive, multilingual care with evidence-based therapy.
    """)

# --------------------- Team Section --------------------- #
st.header("👩🏾‍🤝‍👨🏾 Meet Our Professional Team")

team_profiles = [
    {
        "name": "Jerim Owino",
        "title": "Founder & CEO",
        "bio": "Mental Health Advocate and Youth Empowerment Trainer, age 23. Jerim focuses on accessible mental health support for young adults and communities across Kenya.",
        "image": "da8eb2f3-7a6c-4aee-ba84-93421ef313f4.jpg"
    },
    {
        "name": "Hamdi Roble",
        "title": "Co-Founder & Senior Therapist",
        "bio": "Trauma-informed counselor passionate about inclusive healing and youth-focused therapy. Age 22. She brings culturally respectful care to every session.",
        "image": "A_digital_photograph_features_a_portrait_of_a_youn.png"
    }
]

cols = st.columns(len(team_profiles))

for col, member in zip(cols, team_profiles):
    with col:
        try:
            image = Image.open(member["image"])
            st.image(image, use_column_width=True, caption=member["name"])
        except Exception as e:
            st.error(f"Could not load image for {member['name']}. Ensure the image file is in the same folder.")
        st.markdown(f"**{member['title']}**")
        st.write(member["bio"])

# --------------------- Contact --------------------- #
st.header("📞 Contact Us")

st.markdown("""
- **Email:** [owinojerim269@gmail.com](mailto:owinojerim269@gmail.com)  
- **Phone:** +254 781 095 919 / +254 720 987 654  
- **Location:** Greenhouse Plaza, Ngong Road, Nairobi  
- **Hours:** Monday – Friday: 8:00 AM – 7:00 PM | Saturday: 9:00 AM – 4:00 PM
""")

# --------------------- Footer --------------------- #
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>© 2025 Safe Space Kenya | All rights reserved | Designed with ❤️ for Mental Wellness</div>",
    unsafe_allow_html=True
)
