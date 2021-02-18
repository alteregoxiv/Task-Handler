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
