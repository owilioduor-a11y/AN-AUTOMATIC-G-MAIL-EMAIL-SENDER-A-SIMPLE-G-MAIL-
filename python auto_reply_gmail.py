## import the required requirement(liraries)

import imaplib
import smtplib
import email
from email.message import EmailMessage
import time
import os


# ==== CONFIGURE THESE ====

GMAIL_ADDRESS = "yourname@gmail.com"              # your Gmail address
APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")
IMAP_HOST = "imap.gmail.com"
IMAP_PORT = 993
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
POLL_INTERVAL_SECONDS = 60                         # how often to check for new emails /time interval between each reaply
# ==========================


def create_auto_reply(original_msg: email.message.Message, to_addr: str) -> EmailMessage:
    """Create an automatic reply email."""
    original_subject = original_msg.get("Subject", "")
    subject = original_subject or "(no subject)"

    if not subject.lower().startswith("re:"):
        reply_subject = "Re: " + subject
    else:
        reply_subject = subject

    body = (
        "Hello,\n\n"
        "I have received your message and will "
        "get back to you as soon as possible.\n\n"
        "Best regards,\n"
    )

    reply = EmailMessage()
    reply["From"] = GMAIL_ADDRESS
    reply["To"] = to_addr
    reply["Subject"] = reply_subject

    # Threading headers (optional but useful part)

    msg_id = original_msg.get("Message-ID")
    if msg_id:
        reply["In-Reply-To"] = msg_id
        reply["References"] = msg_id

    reply.set_content(body)
    return reply


def check_and_reply():
    if not APP_PASSWORD:
        print("ERROR: Environment variable GMAIL_APP_PASSWORD is not set.")
        return

    # --- Connect to IMAP (read emails) ---

    imap = imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT)
    imap.login(GMAIL_ADDRESS, APP_PASSWORD)
    imap.select("INBOX")

    # Search for unread messages

    status, data = imap.search(None, "UNSEEN")
    if status != "OK":
        print("IMAP search failed:", status)
        imap.logout()
        return

    msg_nums = data[0].split()
    if not msg_nums:
        print("No new unread messages.")
        imap.logout()
        return

    # --- Connect to SMTP (send replies) ---

    smtp = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
    smtp.starttls()
    smtp.login(GMAIL_ADDRESS, APP_PASSWORD)

    for num in msg_nums:
        status, msg_data = imap.fetch(num, "(RFC822)")
        if status != "OK":
            print(f"Failed to fetch message {num}")
            continue

        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        from_addr = email.utils.parseaddr(msg.get("From"))[1]
        if not from_addr:
            print(f"Message {num} has no valid From, skipping.")
            continue

        # Avoid replying to yourself

        if from_addr.lower() == GMAIL_ADDRESS.lower():
            print(f"Message {num} is from ourselves, skipping.")
            imap.store(num, "+FLAGS", "\\Seen")
            continue

        # Create and send reply

        reply_msg = create_auto_reply(msg, from_addr)
        try:
            smtp.send_message(reply_msg)
            print(f"Replied to {from_addr}")
            # Mark original as seen so we don't reply again
            imap.store(num, "+FLAGS", "\\Seen")
        except Exception as e:
            print(f"Error sending reply to {from_addr}: {e}")

    smtp.quit()
    imap.logout()


def main():
    print("Starting Gmail auto-reply service...")
    while True:
        try:
            check_and_reply()
        except Exception as e:
            print("Error in check_and_reply:", e)
        print(f"Sleeping for {POLL_INTERVAL_SECONDS} seconds...\n")
        time.sleep(POLL_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()