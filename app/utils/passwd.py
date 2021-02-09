from random import choice , randint

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@_-#"

def genCode(password = True):
    n = randint(6, 8) if password else randint(10, 70)
    s = ""
    for i in range(n):
        s += choice(chars)
    return s
