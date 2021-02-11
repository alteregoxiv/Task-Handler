"""
Password generation, hashing and verfification
"""

from taskHandler.app.utils.template import template
from taskHandler.app.utils.hash import hashed, verfify
from taskhandler.app.utils.psswd import genCode
from taskhandler.app.utils.mail import mailSend

def email_pwd(user, email):
    pwd = genCode()
    mailSend(pwd)
    return hash_pwd


def verify_pwd(user, email, hash_pwd, pwd):
    pass

if 'user' not in request.POST and 'email' not in request.POST:
   hash_pwd  = email_pwd(user , email)
