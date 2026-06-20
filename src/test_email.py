import smtplib
from email.mime.text import MIMEText

EMAIL = "anjaniai2026@gmail.com"
PASSWORD = "onwt clvx erbg qtii"

msg = MIMEText("Hello Anjani! This is a test email from Python.")

msg["Subject"] = "Test Email"
msg["From"] = EMAIL
msg["To"] = EMAIL

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(EMAIL, PASSWORD)

server.send_message(msg)

print("Email Sent Successfully!")

server.quit()