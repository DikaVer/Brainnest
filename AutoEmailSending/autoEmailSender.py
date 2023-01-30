import json
import smtplib, ssl
import time
import os
import schedule
from datetime import datetime
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders

def get_message(sender, recipient):
    body = f'''\
    Hello,
    
    Please find a report in the attachment.
    
    Best regards,
    {sender}
    '''

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient #Or if we do not want for loops, we can use ", ".join(recipiets)
    msg['Subject'] = "Daily Report"

    msg.attach(MIMEText(body, 'plain'))

    filename = str(os.getcwd()) + "\\daily_report.pdf"
    with open(filename, "rb") as attachment:
        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload(attachment.read())

    # enconding the binary into base64
    encoders.encode_base64(payload)

    # add header with pdf name
    payload.add_header(
    "Content-Disposition",
    f"attachment; filename= daily_report.pdf",
)

    msg.attach(payload)

    return msg, body, filename

def send_daily_report():
    sender_email = "tbrainnest@gmail.com"
    password = "iufsuofxakrcgzci"
    receiver_email_list = ["recipient1@example.com", "recipient2@example.com", "recipient3@example.com"]
    # Create secure connection with server and send email
    context = ssl.create_default_context()

    # Connection to the server with secure protocol
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)

    # open log file
    with open(str(os.getcwd()) + "\\log.json", 'r') as log:
        data = json.load(log)

    for receiver in receiver_email_list:
        # Get a message context
        message, body_msg, dir_file = get_message(sender_email, receiver)
        # Send a message via email
        server.sendmail(sender_email, receiver, message.as_string())
        # Add a message to log data
        data['Mails'].append({"From": message['From'], "To": message['To'], "Subject": message['Subject'], "Message": body_msg, "File directory": dir_file})
    json_object = json.dumps(data)

    # Write sended messages to log file
    with open(str(os.getcwd()) + "\\log.json", 'w') as log:
        log.write(json_object)

    # Exist from the server
    server.quit()


if __name__ == "__main__":
    try:
        # Set up schedule
        schedule.every().day.at("19:39").do(send_daily_report)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e: # Catch errors in the code

        # Get current time
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        # Write an error with the time and description
        with open('error.txt', 'w') as f:
            f.write(f'''The error is occurred at {dt_string}.
            The reason is {e}''')



