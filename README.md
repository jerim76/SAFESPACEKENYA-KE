SafeSpace Organisation Website
Welcome to the SafeSpace Organisation website project! This application, built with Streamlit, provides a platform for mental health support, including counseling services, volunteer opportunities, events, and partnerships. It aims to empower minds and nurture hope since its founding in 2023.
Overview

Purpose: A non-profit mental health care platform offering accessible, culturally-appropriate counseling and outreach.
Features:
Individual, Group, Family, Trauma Recovery, and Online Counseling.
Volunteer and partnership registration forms.
Mood tracking tool with export functionality.
Interactive chatbot for support.
Blog and crisis resources.


Technology: Python, Streamlit, HTML/CSS for styling.
Last Updated: 01:14 AM EAT, July 25, 2025.

Prerequisites

Python 3.8 or higher.
Required packages: streamlit, pandas.
A hosted domain (safespaceorganisation.org) with an email account (info@safespaceorganisation.org) configured for form submissions.

Installation

Clone the Repository:
git clone https://github.com/yourusername/safespace-organisation.git
cd safespace-organisation


Install Dependencies:
pip install -r requirements.txt

(Create requirements.txt with streamlit and pandas if not present.)

Set Up Environment:

Install a virtual environment (optional but recommended):python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate




Configure Email:

Host the domain and create the info@safespaceorganisation.org email account via your hosting provider or a service like Google Workspace.
Update DNS MX records as per your email host’s instructions.
Set up an email client (e.g., Outlook, Thunderbird) with IMAP/POP3 settings provided by the host.



Running the Application

Start the Streamlit App:
streamlit run app.py


Open your browser and go to http://localhost:8501 to view the site.


Deploy (Optional):

Deploy to a platform like Heroku, AWS, or your web host.
Update the app.py file with deployment-specific configurations if needed.



Usage

Navigation: Use the header links (About, Services, Events, etc.) to explore sections.
Forms: Fill out counseling, volunteer, or partnership forms to register. Emails are sent to info@safespaceorganisation.org.
Mood Tracker: Log your mood (1-5) and export as a CSV file.
Chatbot: Click the chat icon (💬) to ask questions about services or contact.

Configuration

Email Sending: Modify app.py to include smtplib for sending form emails. Example:import smtplib
from email.mime.text import MIMEText

def send_email(to_email, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'info@safespaceorganisation.org'
    msg['To'] = to_email
    with smtplib.SMTP('smtp.yourdomain.com', 587) as server:
        server.starttls()
        server.login('info@safespaceorganisation.org', 'your_password')
        server.send_message(msg)


Replace smtp.yourdomain.com and credentials with your host’s SMTP details.


Styling: Edit the CSS in st.markdown() calls in app.py for custom designs.

Contributing

Fork the repository.
Create a feature branch (git checkout -b feature-name).
Commit changes (git commit -m "Add feature").
Push to the branch (git push origin feature-name).
Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact

Email: info@safespaceorganisation.org
Phone: +254 781 095 919 (8 AM-7 PM EAT)
Location: Greenhouse Plaza, Ngong Road, Nairobi
