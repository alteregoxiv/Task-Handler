"""
Model for database user table
"""

from pydal import Field
from .connect import db


db.define_table('users',
               Field('username', length=60, required=True, unique=True, notnull=True),
               Field('email', required=True, unique=True, notnull=True),
               Field('password', required=True, notnull=True),
               Field('cookie_pass', required=True, notnull=True),
              )

db.commit()


def create_user(username, email, passwd, cookie_pass):
    _id = db.users.insert(
            username = username,
            email = email,
            password = passwd,
            cookie_pass = cookie_pass
          )
    db.commit()
    return _id


def get_user_by(username = '', email = '', _id = ''):
    if username:
        return db(db.users.username == username).select().as_list()
    if email:
        return db(db.users.email == email).select().as_list()
    if _id:
        return db(db.users.id == _id).select().as_list()
