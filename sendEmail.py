#watch youtube video "how to send an email in python with attachments easy for beginners"

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
import os

#sends email and fills in inputs from a configuration file
def sendEmail():
    config = open('/home/pi/Desktop/urmum.cfg', mode = 'r')
    config = config.readlines()
    email_user = config[0][:-1]
    email_password = config[1][:-1]
    email_send = config[2][:-1]
    email_server = config[3][:-1]
    port = config[4][:-1]
    
    subject = config[5][:-1]
    body = config[6][:-1]
    
    dir_path = config[7][:-1]
    
    
    
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    
    files = os.listdir(dir_path)          #store images in the folder in a list

    
    msg.attach(MIMEText(body,'plain'))

    #add multiple images to the message
    #convert jpg files so that they can send as a string
    for f in files: 
        file_path = os.path.join(dir_path,f)
        attachment = MIMEApplication(open(file_path, "rb").read(), _subtype="txt")
        attachment.add_header('Content-Disposition','attachment', filename=f)
        msg.attach(attachment)

    server = smtplib.SMTP(email_server, port)
    server.starttls()
    server.login(email_user, email_password)


    server.sendmail(email_user,email_send,msg.as_string())

    server.quit()
    
sendEmail()