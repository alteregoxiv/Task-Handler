"""
Password generation, hashing and verification
"""

from taskHandler.app.utils.hash import hashed, verify
from taskHandler.app.utils.passwd import genCode
from taskHandler.app.utils.mail import mailSend

def email_pwd(email):
    pwd = genCode()
    mailSend(email, pwd)
    hash_pwd = hashed(pwd)
    return hash_pwd


def verify_pwd(hash_pwd, pwd):
    return verify(pwd , hash_pwd)

def adduser(user , email , hash_pwd):
    print(user , email , hash_pwd , sep = "\n")
