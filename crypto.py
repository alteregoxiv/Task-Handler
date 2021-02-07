from simplecrypt import encrypt, decrypt


secret = 'ax'

def encrypted(passwd):
    encrypted = encrypt(secret, passwd.encode('utf8'))
    return encrypted

def decrypted(encrypted):
    passwd = decrypt(secret, encrypted)
    return passwd
