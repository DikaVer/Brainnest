import smtplib
import email
import os
import schedule

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication



# list of recipients
receivers = ['email1@gmail.com', 'email2@gmail.com', 'email3@gmail.com'] # exemple

# email subject and body
subject = 'Daily Report'
body = 'Hello,\n Attached is the daily report for your reference.\n Thank you.'


# report files directory
report_dir = '/Users/user/Desktop/projet/email' # exemple


# iterate through recipients
for recipient in receivers:
   msg = MIMEMultipart()
   msg['From'] = username
   msg['To'] = recipient
   msg['Subject'] = subject
   msg.attach(MIMEText(body))

# add report files as attachments
for report_file in os.listdir(report_dir):
   with open(os.path.join(report_dir, report_file), 'rb') as f:
       attachment = MIMEApplication(
           f.read(),
           _subtype="pdf" #exemple
       )
   attachment.add_header(
       'content-disposition', 'attachment', filename=report_file
   )
   msg.attach(attachment)
