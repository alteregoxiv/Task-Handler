"""
Works on user related data
"""

from taskHandler.app.utils.passwd import genCode
from taskHandler.app.utils.hash import hashed, verify
from taskHandler.app.models.user_model import create_user


def adduser(user , email , hash_pwd):
    cookie_pass = genCode(password = False)
    cookie_pass_hash = hashed(cookie_pass)
    _id = create_user(user, email, hash_pwd, cookie_pass_hash)
    return '%s%s%s' %(cookie_pass_hash, _id, len(str(_id)))
