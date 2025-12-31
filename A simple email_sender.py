## THIS IS A SIMPLE EMAIL SENDER (How to send email with python).
 # Go to email account and setup "App Password" if 2FA is enabled.
 # Here is the function to send email using SMTP.
 # This sends only one email at a time.

import smtplib
import ssl
from email.message import EmailMessage

email_sender = "YOU_EMAIL_ADDRESS"
email_password = "16-character APP_PASSWORD"
email_receiver = "RECEIVER_EMAIL_ADDRESS"
subject = "Test Email from Python"
body = "Hello!" \
"Thank you for your email." \
"I will get back to you as soon as posible." \
"Best Regards," \
"Your Name"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em.set_content(body)
em['Subject'] = subject
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    