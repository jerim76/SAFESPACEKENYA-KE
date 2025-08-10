import streamlit as st
from datetime import datetime
import re
import base64
import pandas as pd
import random

# ... (custom CSS remains the same) ...

# Initialize session state
if "current_view" not in st.session_state:
    st.session_state.current_view = "home"
if "mood_history" not in st.session_state:
    st.session_state.mood_history = []
if "counseling_form_data" not in st.session_state:
    st.session_state.counseling_form_data = {"name": "", "email": "", "phone": "", "concern": "Anxiety", "preference": "Online"}

# ... (other functions remain the same) ...

# HERO SECTION (remains the same)

# ... (other sections remain the same until mood tracker) ...

# MOOD TRACKER - FIXED SECTION
st.markdown("<div id='mood_tracker'></div>", unsafe_allow_html=True)
st.markdown("## Mood & Wellness Journal")
st.markdown("""
<div class='safe-container'>
    <p style='margin-bottom: 1.5rem;'>Track your emotional patterns between sessions. This private journal helps identify triggers and progress, providing valuable insights for your therapy.</p>
</div>
""", unsafe_allow_html=True)

# Mood selection with Streamlit components
mood_options = {
    "😊 Radiant": "Hopeful, joyful, energized",
    "😌 Calm": "Peaceful, centered, balanced",
    "😐 Neutral": "Steady, indifferent, stable",
    "😟 Anxious": "Worried, tense, overwhelmed",
    "😔 Sad": "Grieving, low, disconnected"
}

selected_mood = st.selectbox(
    "Select your current mood:", 
    ["Choose a mood"] + list(mood_options.keys()),
    key="mood_select"
)

if selected_mood != "Choose a mood":
    st.caption(mood_options[selected_mood])

note = st.text_area(
    "Journal your thoughts and experiences (optional)", 
    height=140, 
    placeholder="What thoughts, events, or physical sensations are you experiencing today? What coping strategies did you try? Your therapist will see this in your next session."
)

if st.button("Save Journal Entry", use_container_width=True):
    if selected_mood != "Choose a mood":
        entry = {
            "Date": datetime.now(),
            "Mood": selected_mood,
            "Note": note
        }
        st.session_state.mood_history.append(entry)
        st.success("Journal entry saved. This information can help your therapist support you better.")
    else:
        st.warning("Please select a mood before saving")

if st.session_state.mood_history:
    st.markdown("### Your Mood History")
    mood_df = pd.DataFrame(st.session_state.mood_history)
    mood_df["Date"] = mood_df["Date"].dt.strftime("%b %d, %Y %I:%M %p")
    st.dataframe(mood_df[["Date", "Mood", "Note"]], hide_index=True)
    
    csv = export_mood_history()
    st.markdown(get_download_link(csv, "mood_journal.csv"), unsafe_allow_html=True)

# ... (rest of the code remains the same) ...
