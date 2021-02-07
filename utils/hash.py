from passlib.hash import pbkdf2_sha256

def hashed(pwd):
    return pbkdf2_sha256.hash(pwd)

def verify(pwd , hasche):
    return pbkdf2_sha256.verify(pwd , hasche)

p = hashed("Ahobaka1234")
print(p)
print(verify("Ahobaka1234" , p))
