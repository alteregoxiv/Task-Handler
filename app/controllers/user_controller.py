"""
Works on user related data
"""

import taskHandler.app.models.user_model

def adduser(user , email , hash_pwd):
    print(user , email , hash_pwd , sep = "\n")
