''' You work at a company that receives daily data files from external partners. These files need to be processed and analyzed, but first, they need to be transferred to the company's internal network.

The goal of this project is to automate the process of transferring the files from an external FTP server to the company's internal network.

Here are the steps you can take to automate this process:

    Use the ftplib library to connect to the external FTP server and list the files in the directory.

    Use the os library to check for the existence of a local directory where the files will be stored.

    Use a for loop to iterate through the files on the FTP server and download them to the local directory using the ftplib.retrbinary() method.

    Use the shutil library to move the files from the local directory to the internal network.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the files that have been transferred and any errors that may have occurred during the transfer process. '''


import schedule
import time
import ftplib

def transfer_files():
    ftp = ftplib.FTP('ftp.server.com')
    ftp.login(user='username', passwd='password')

    filename = 'example.txt'
    ftp.retrbinary('RETR ' + filename, open(filename, 'wb').write)

    ftp.quit()

schedule.every().day.at("10:00").do(transfer_files)

while True:
    schedule.run_pending()
    time.sleep(1)

