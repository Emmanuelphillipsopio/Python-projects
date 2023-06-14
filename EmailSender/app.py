#go over to our gmail account and setup 2 factor authentication
#generate app password
#create a function to send an email
from email.message import EmailMessage
import ssl
import smtplib

app_password = "app.py"

email_sender = "pencoug@gmail.com"
email_password = app_password
email_receiver = "emmauelphillpsopio@gmail.com"
subject = "Project Progress Report"
body ="""
    Greetings Doctor,
    I hope this email finds you well. Below we have attached a progress report documenting our progress with the final year project.
    We hope to hear from you.
    Thanks
"""

em = EmailMessage() #instance of the Emailmessage library
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())