"""
Mail to send Password
"""

from os import environ 
from smtplib import SMTP
from passwd import genPwd
from random import randint

email, pwd = environ['EMAIL'].split()

print(email, pwd)

def mailSend(rec):

    smtp = SMTP('smtp.gmail.com' , 587)
    smtp.starttls()

    #Login to email services
    smtp.login(email , pwd)

    msg = "Hi " + rec + ",\nThanks for using our services and best wishes for the days ahead\nYour password is : " + genPwd(randint(6 , 8))
    #Send Mail
    smtp.sendmail(email , rec , msg)

    print(f"Mail sent to {rec}")

    smtp.quit()
