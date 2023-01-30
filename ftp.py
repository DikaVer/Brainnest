import ftplib
import os
import shutil
import schedule
import time

# FTP server details
ftp_host = 'ftp.example.com'
ftp_user = 'username'
ftp_password = 'password'

# Local directory where files will be stored
local_dir = '/path/to/local/directory'

# Internal network directory where files will be moved
internal_dir = '/path/to/internal/network'

# Connect to FTP server
ftp = ftplib.FTP(ftp_host)
ftp.login(ftp_user, ftp_password)

# Check if local directory exists, create if not
if not os.path.exists(local_dir):
    os.makedirs(local_dir)

# Download files from FTP server to local directory
ftp.cwd('/path/to/ftp/directory')
files = ftp.nlst()
for file in files:
    with open(local_dir + '/' + file, 'wb') as f:
        ftp.retrbinary('RETR ' + file, f.write)

# Move files from local directory to internal network
for file in os.listdir(local_dir):
    shutil.move(local_dir + '/' + file, internal_dir)

# Close FTP connection
ftp.quit()

# Schedule script to run daily at specific time
schedule.every().day.at("10:00").do(transfer_files)

while True:
    schedule.run_pending()
    time.sleep(1)