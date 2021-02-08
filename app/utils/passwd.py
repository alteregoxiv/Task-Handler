from random import choice , randint

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@_-#"

def genPwd():
    n = randint(6 , 8)
    s = ""
    for i in range(n):
        s += choice(chars)
    return s
