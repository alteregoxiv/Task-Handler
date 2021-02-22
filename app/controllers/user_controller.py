"""
Works on user related data
"""

from taskHandler.app.utils.passwd import genCode
from taskHandler.app.utils.hash import hashed, verify
from taskHandler.app.models.user_model import(
    create_user,
    get_a_user_data_by,
    update_cookie_pass,
)


def adduser(user , email , hash_pwd):
    cookie_pass = genCode(password = False)
    cookie_pass_hash = hashed(cookie_pass)
    _id = create_user(user, email, hash_pwd, cookie_pass_hash)
    return '%s%s%s' %(cookie_pass, _id, len(str(_id)))


def verify_user(username, password):
    data = get_a_user_data_by(username = username, which = 'password')
    if data and verify(password, data['password']):
        cookie_pass = genCode(password = False)
        cookie_pass_hash = hashed(cookie_pass)
        update_cookie_pass(cookie_pass_hash, data['id'])
        return '%s%s%s' %(cookie_pass, data['id'], len(str(data['id'])))
    return False
