import os

def logtrack(message):
    log_file = open('log_file.txt', 'a')  
    log_file.write(message)
    log_file.close()

directory = './report_files' 


try:
    for filename in os.listdir(directory):
        report_file = os.path.join(directory, filename)
        with open(report_file, 'r') as rf:
            logtrack("File found.\n")
            rf.read()

except FileNotFoundError:
    logtrack("File not found or path is incorrect\n")

finally:
    logtrack("Exit\n")







# with open('D:\\text.txt', 'r') as report_file:
