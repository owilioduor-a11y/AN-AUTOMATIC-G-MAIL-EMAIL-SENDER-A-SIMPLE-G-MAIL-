# AN-AUTOMATIC-G-MAIL-EMAIL-SENDER-A-SIMPLE-G-MAIL-
## Automated Gmail Sender 
A lightweight Python-based tool designed to automate the process of sending emails via Gmail using the smtplib library. This project simplifies bulk mailing or notification alerts with minimal configuration.

## Features
Automated Delivery: Send emails programmatically without manual intervention.
Custom Content: Supports plain text and HTML email bodies.
Attachment Support: Easily attach documents, images, or PDFs to your emails.
Secure Connection: Uses SSL/TLS to ensure your login credentials and data are encrypted.
## Prerequisites
Before running the script, ensure you have:
Python 3.x installed.
A Gmail account.
App Password: Google no longer allows "Less Secure Apps." You must generate a 16-digit App Password from your Google Account settings under Security > 2-Step Verification.

   ##  ----1. Gmail setup (one‑time)-------
  Here’s a minimal auto‑reply system that works specifically with Gmail using Python.
  ## steps to follow before automation
  1. Enable IMAP  
     In Gmail:  
            Settings → See all settings → Forwarding and POP/IMAP → IMAP access → Enable IMAP.

  2. Create an App Password (recommended and often required)  
     Turn on 2‑Step Verification for your Google account.
     Go to: https://myaccount.google.com/app passwords
     Create an app password for “Mail” → “Other” (or “Windows Computer”).  
     Copy the 16‑character password (no spaces).
  3. Set it in an environment variable (PowerShell example):
     $env:GMAIL_APP_PASSWORD = "your-16-char-app-password"

  4. How to Enable IMAP in Gmail 
     Open Gmail in a Web Browser: Go to gmail.com and sign in to your account. 
     Click the Gear icon (⚙) in the upper-right corner of the page 
     Navigate to the IMAP Settings:
     Click the Forwarding and POP/IMAP tab at the top of the Settings page.
     Enable IMAP Access: Scroll down to the IMAP access section ,Select the radio button next to Enable IMAP.
     Save Your Changes: Scroll to the very bottom of the page and click the Save Changes button
  
  5.If you have 2-Step Verification (2FA) enabled on your Google account
     (which is highly recommended for security)
     you cannot use your regular Google password to connect your email client.
    ##### Instead, you must:
        *Generate an App Password:* 
    - You will need to generate a unique, 16-character App Password from your Google Account security settings.
    - Use the App Password: Use this generated App Password(when setting up your Gmail account in your 
      third-party email client.)
      
  6. HOW TO RUN IT
     From the folder where the script is saved:
      AUTO_REPLY_GMAIL.PY               
    Leave it running; it will check Gmail every POLL_INTERVAL_SECONDS seconds 
    and auto‑reply to new unread emails.
  7.There's also a simple g-mail email sender to send one reply at a time

## best regards: 
OWILI PETER

      AUTO_REPLY_GMAIL.PY               
    Leave it running; it will check Gmail every POLL_INTERVAL_SECONDS seconds 
    and auto‑reply to new unread emails.
