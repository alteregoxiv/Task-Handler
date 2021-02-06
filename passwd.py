from random import choice , randint

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@_-#"

def genPwd(n):
    s = ""
    for i in range(n):
        s += choice(chars)
    return s
