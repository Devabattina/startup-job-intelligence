import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("anjaniai2026@gmail.com")
PASSWORD = os.getenv("onwt clvx erbg qtii")
TO = os.getenv("RECIPIENT_EMAIL")

def send_email(html):
    msg = MIMEText(html, "html")

    msg["Subject"] = "Daily Startup Funding & Hiring Report"
    msg["From"] = EMAIL
    msg["To"] = TO

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
