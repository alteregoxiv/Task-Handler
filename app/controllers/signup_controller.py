"""
Password generation, hashing and verification
"""

from taskHandler.app.utils.hash import hashed, verify
from taskHandler.app.utils.passwd import genCode
from taskHandler.app.utils.mail import mailSend
from taskHandler.app.models.user_model import get_user_data_by

def email_pwd(email):
    pwd = genCode()
    mailSend(email, pwd)
    hash_pwd = hashed(pwd)
    return hash_pwd


def verify_pwd(hash_pwd, pwd):
    return verify(pwd , hash_pwd)


def username_avl(username):
    return len(get_user_data_by(username = username)) == 0


def email_avl(email):
    return len(get_user_data_by(email = email)) == 0
