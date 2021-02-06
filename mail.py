"""
Mail to send Password
"""

from os import environ 
from smtplib import SMTP
from passwd import genPwd
from random import randint
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email, pwd = environ['EMAIL'].split()

print(email, pwd)

def mailSend(rec):

    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Password for your Account'
    msg['From'] = email

    smtp = SMTP('smtp.gmail.com' , 587)
    smtp.starttls()

    #Login to email services
    smtp.login(email , pwd)

    content = "Hi " + rec + ",\nThanks for using our services and best wishes for the days ahead\nYour password is : " + genPwd(randint(6 , 8))
    msg['To'] = rec
    mail_content = MIMEText(content , 'plain')
    msg.attach(mail_content)

    #Send Mail
    smtp.sendmail(email , rec , msg.as_string())

    print(f"Mail sent to {rec}")

    smtp.quit()
