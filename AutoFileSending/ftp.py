import ftplib
import os
import shutil
import schedule
import time
import json
from datetime import datetime


def transfer_files():
    # Local directory where files will be stored
    local_dir = str(os.getcwd()) + "\\Local"

    # Internal network directory where files will be moved
    internal_dir = str(os.getcwd()) + "\\Internal_network"

    # Connect to FTP server
    # Create a FTP server "python3 -m pyftpdlib -w --user=username --password=password"

    # FTP server details
    ftp_host = '127.0.0.1'
    ftp_user = 'username'
    ftp_password = 'password'

    ftp = ftplib.FTP()
    ftp.connect(ftp_host, 2121)
    ftp.login(ftp_user, ftp_password)

    # Check if local directory exists, create if not
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)


    # List files
    files = ftp.nlst()


    # open log file
    with open(str(os.getcwd()) + "\\log.json", 'r') as log:
        data = json.load(log)

    for file in files:
        with open(local_dir + '/' + file, 'wb') as f:
            ftp.retrbinary("RETR " + file, f.write)
        data['Fails'].append(str(file))
    json_object = json.dumps(data)

    # Write sent files to log file
    with open(str(os.getcwd()) + "\\log.json", 'w') as log:
        log.write(json_object)

    # Move files from local directory to internal network
    for file in os.listdir(local_dir):
        shutil.move(local_dir + '\\' + file, internal_dir)

    print("File transferring was successful!")
    # Close FTP connection
    ftp.quit()


if __name__ == "__main__":
    try:
        # Set up schedule
        schedule.every().day.at("10:00").do(transfer_files)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e:  # Catch errors in the code

        # Get current time
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        # Write an error with the time and description
        with open('error.txt', 'w') as f:
            f.write(f'''The error is occurred at {dt_string}.
               The reason is {e}''')
