"""
Password generation, hashing and verification
"""

from taskHandler.app.utils.hash import hashed, verify
from taskHandler.app.utils.passwd import genCode
from taskHandler.app.utils.mail import mailSend

def email_pwd(user, email):
    pwd = genCode()
    mailSend(email, pwd)
    hash_pwd = hashed(pwd)
    return hash_pwd


def verify_pwd(user, email, hash_pwd, pwd):
    pass
