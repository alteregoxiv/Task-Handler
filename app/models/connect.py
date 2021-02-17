"""
Connect to database
"""

from pydal import DAL

db = DAL("sqlite://app/models/test.db")

# DB_URI = "mysql://{}:{}@{}:{}/{}?set_encoding=utf8mb4".format()
# db = DAL(DB_URI, pool_size=10)
