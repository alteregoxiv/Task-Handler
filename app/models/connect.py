"""
Connect to database
"""

from pydal import DAL

db = DAL("sqlite://app/models/test.db")

db.commit()
