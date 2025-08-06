import streamlit as st
import pandas as pd

# CONTACT SECTION
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align: center; padding-bottom: 15px; margin-bottom: 30px;'>"
    "<h2 style='color: #1E3A5F; font-size: 2.2rem; font-weight: 600;'>We're Here for You</h2>"
    "<div style='width: 100px; height: 4px; background: #26A69A; margin: 0 auto; border-radius: 2px;'></div>"
    "</div>", 
    unsafe_allow_html=True
)

contact_content = """
<div style='background: #E8F4F8; padding: 20px; border-radius: 12px; border: 1px solid #26A69A; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);'>
    <div style='display: flex; flex-wrap: wrap; gap: 15px; margin-bottom: 25px;'>
        <div style='flex: 1; min-width: 200px; padding: 15px; background: rgba(255, 255, 255, 0.9); border-radius: 8px;'>
            <h4 style='color: #1E3A5F; font-size: 1.3rem; margin-bottom: 10px;'>Contact Information</h4>
            <p style='font-size: 1rem; color: #333; line-height: 1.5;'>
                📍 Greenhouse Plaza, 3rd Floor, Ngong Road, Nairobi, Kenya<br>
                📞 <a href='tel:+254781095919' style='color: #26A69A; text-decoration: none;'>+254 781 095 919</a><br>
                ✉️ <a href='mailto:info@safespaceorganisation.org' style='color: #26A69A; text-decoration: none;'>info@safespaceorganisation.org</a><br>
                🌐 <a href='https://www.safespaceorganisation.org' style='color: #26A69A; text-decoration: none;'>www.safespaceorganisation.org</a>
            </p>
            <div style='margin-top: 15px; display: flex; gap: 10px; flex-wrap: wrap;'>
                <a href='tel:+254781095919' style='background: #26A69A; color: white; padding: 8px 15px; border-radius: 20px; text-decoration: none; font-size: 0.9rem; font-weight: 600;'>Call Now</a>
                <a href='mailto:info@safespaceorganisation.org' style='background: #26A69A; color: white; padding: 8px 15px; border-radius: 20px; text-decoration: none; font-size: 0.9rem; font-weight: 600;'>Email Us</a>
            </div>
        </div>
        
        <div style='flex: 1; min-width: 200px; padding: 15px; background: rgba(255, 255, 255, 0.9); border-radius: 8px;'>
            <h4 style='color: #1E3A5F; font-size: 1.3rem; margin-bottom: 10px;'>Operating Hours</h4>
            <p style='font-size: 1rem; color: #333; line-height: 1.5;'>
                Monday-Friday: 9:00 AM - 6:00 PM<br>
                Saturday: 10:00 AM - 2:00 PM<br>
                Sunday: Closed<br>
                <em style='color: #666;'>Crisis support available 24/7</em>
            </p>
            <div style='margin-top: 15px;'>
                <h4 style='color: #1E3A5F; font-size: 1.3rem; margin-bottom: 10px;'>Emergency Contact</h4>
                <p style='font-size: 1rem; color: #333;'>📞 <a href='tel:+254781095919' style='color: #26A69A; text-decoration: none;'>+254 781 095 919</a> (24/7)</p>
                <a href='tel:+254781095919' style='background: #FF6F61; color: white; padding: 8px 15px; border-radius: 20px; text-decoration: none; font-size: 0.9rem; font-weight: 600;'>Emergency Call</a>
            </div>
        </div>
    </div>
    
    <div>
        <h4 style='color: #1E3A5F; font-size: 1.3rem; margin-bottom: 10px;'>Visit Our Center</h4>
        <p style='font-size: 1rem; color: #333; margin-bottom: 15px;'>Find us at Greenhouse Plaza, Ngong Road, Nairobi</p>
"""

st.markdown(contact_content, unsafe_allow_html=True)

# Map with precise coordinates for Greenhouse Plaza
try:
    map_data = pd.DataFrame({'lat': [-1.2985], 'lon': [36.7848]})
    st.map(map_data, zoom=14, use_container_width=True)
except Exception as e:
    st.error("Unable to display map. Please check your internet connection or visit our center at Greenhouse Plaza, Ngong Road, Nairobi.")

st.markdown("</div>", unsafe_allow_html=True)  # Closing the main container
