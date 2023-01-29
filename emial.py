""" This code assumes that you have an SMTP server set up and that you know the server's address, port, and login credentials. 
You'll also need to replace path/to/attachment.pdf with the actual path to the attachment file on your computer.

This code will send an email to each recipient in the list, with the specified subject, body, and attachment.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Email server details
server = smtplib.SMTP('smtp.example.com', 587)
server.starttls()
server.login("sender@example.com", "password")

# Email details
recipients = ["recipient1@example.com", "recipient2@example.com", "recipient3@example.com"]
sender = "sender@example.com"
subject = "Email with Attachment"
body = "Hello,\nPlease find the attachment.\n\nBest regards,"
attachment = "path/to/attachment.pdf"

# Iterate through the list of recipients
for recipient in recipients:
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(body,'plain'))

    # open the file in bynary
    binary = open(attachment,'rb')
    payload = MIMEBase('application','octate-stream', Name = attachment.split('/')[-1])
    payload.set_payload((binary).read())

    # enconding the binary into base64
    encoders.encode_base64(payload)

    # add header with pdf name
    payload.add_header('Content-Decomposition', 'attachment', filename=attachment.split('/')[-1])
    msg.attach(payload)
    server.sendmail(sender, recipient, msg.as_string())

server.quit()

