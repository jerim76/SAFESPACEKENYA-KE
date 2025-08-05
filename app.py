import streamlit as st
from datetime import datetime

# Set page config
st.set_page_config(page_title="Safe Space Kenya", layout="wide")

# Header
st.title("Safe Space Kenya")
st.subheader("Empowering minds, nurturing hope.")

# Navigation-like layout
st.markdown("""
### Our Services
Explore our wide range of support services designed for your mental and emotional wellbeing.
""")

# Services Section
services = [
    {
        "icon": "🧠",
        "title": "Individual Counseling",
        "description": "Confidential one-on-one sessions with licensed counselors.",
        "image": "https://images.unsplash.com/photo-1588776814546-ec7e4b2dfb70",
        "details": "We provide a safe environment for you to express yourself and work through personal challenges."
    },
    {
        "icon": "👨‍👩‍👧‍👦",
        "title": "Group Therapy",
        "description": "Peer support through shared experiences and moderated group sessions.",
        "image": "https://images.unsplash.com/photo-1610484827409-866c7a58b983",
        "details": "Group sessions are facilitated by professionals and designed to foster empathy and support among peers."
    },
    {
        "icon": "🎓",
        "title": "Youth Mentorship",
        "description": "Guidance for adolescents in school and life decisions.",
        "image": "https://images.unsplash.com/photo-1594643799515-65bcd1fb982b",
        "details": "Our youth mentorship initiative pairs teens with mentors to build confidence and life skills."
    }
]

for service in services:
    st.image(service["image"], use_container_width=True)
    st.markdown(f"#### {service['icon']} {service['title']}")
    st.write(service["description"])
    with st.expander("Learn more"):
        st.write(service["details"])
    st.markdown("---")

# Videos Section
st.markdown("### 🎥 Videos & Community Voices")
st.write("Watch these powerful videos on mental health awareness and the work Safe Space Kenya supports:")

videos = [
    "https://www.youtube.com/watch?v=xDj6xgZh3e4",
    "https://www.youtube.com/watch?v=TozWl2FovkY",
    "https://www.youtube.com/watch?v=OjIVqGxK3jY",
    "https://www.youtube.com/watch?v=B2zXz2WcQZg"
]
for video in videos:
    st.video(video)

st.markdown("[📺 Watch More on Mental Health in Kenya](https://www.youtube.com/results?search_query=mental+health+in+kenya)")

# Testimonials
st.markdown("### 💬 Real Stories")
testimonials = [
    """_"I never thought healing was possible until I found Safe Space Kenya. The counselors were kind and professional."_
    – Achieng, Kisumu""",
    """_"As a teacher, I’ve seen major improvements in my students since the awareness sessions. Thank you Safe Space!"_
    – Mr. Wekesa, Bungoma""",
    """_"Their group therapy gave me courage and a new support system. Highly recommend!"_
    – Njeri, Nairobi"""
]
for quote in testimonials:
    st.info(quote)

# FAQ Section
st.markdown("### ❓ Maswali ya Mara kwa Mara (FAQs)")
with st.expander("Je, huduma zenu ni za siri?"):
    st.write("Ndiyo. Tunahakikisha kuwa mazungumzo yako na mshauri yanabaki kati yenu wawili.")

with st.expander("Ni lazima nikuwe na appointment?"):
    st.write("Hapana. Unaweza tembelea ofisi zetu au tutumie ujumbe kupitia fomu ya mawasiliano.")

with st.expander("Huduma hizi ni za bure?"):
    st.write("Baadhi ni za bure, lakini huduma maalum hutozwa kiasi kidogo cha gharama ili kudumisha ubora.")

# Contact Form
st.markdown("### 📬 Wasiliana Nasi")
with st.form(key='contact_form'):
    name = st.text_input("Jina lako")
    email = st.text_input("Barua pepe yako")
    message = st.text_area("Ujumbe wako")
    appointment_type = st.selectbox("Aina ya Huduma", ["Ushauri Binafsi", "Tiba ya Kikundi", "Ushauri kwa Vijana"])
    submit = st.form_submit_button("Tuma Ujumbe")
    if submit:
        st.success(f"Asante {name}, ujumbe wako umetumwa kwa owinojerim269@gmail.com. Tutakujibu hivi karibuni.")

# Footer
st.markdown("""
---
**📍 Location:** Nairobi, Kenya  
**📧 Email:** [owinojerim269@gmail.com](mailto:owinojerim269@gmail.com)  
**📱 Simu:** +254 758 943 430  
**🔗 Social Media:** [Facebook](https://facebook.com) | [Twitter](https://twitter.com) | [Instagram](https://instagram.com)

© 2025 Safe Space Kenya. All rights reserved.
""")
