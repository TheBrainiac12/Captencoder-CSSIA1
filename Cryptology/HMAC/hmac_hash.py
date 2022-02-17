import hashlib
import binascii
import os

def hash_password(password):
    salt =hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 200000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    print("Provided Password:",provided_password)
    salt = stored_password[:64]
    pwdhash = hashlib.pbkdf2_hmac('sha512',provided_password.encode('utf-8'),salt.encode('ascii'),200000)
    stored_password = stored_password[64:]
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

stored_password = hash_password('buffer') 
print("Stored Password",stored_password)
x=verify_password(stored_password, 'buffer')
print(x)
y=verify_password(stored_password, 'buffet')
print(y)