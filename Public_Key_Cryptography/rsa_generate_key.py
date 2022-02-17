from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify

message = b'Hey!!, This is Krutika'

#Generating private key (RsaKey object) of key length of 1024 bits
private_key = RSA.generate(1024)

public_key = private_key.publickey()

private_pem = private_key.export_key().decode()
public_pem = public_key.export_key().decode()


with open('private_pem.pem', 'w') as pr:
    pr.write(private_pem)
with open('public_pem.pem', 'w') as pu:
    pu.write(public_pem)
   

pr_key = RSA.import_key(open('private_pem.pem', 'r').read())
pu_key = RSA.import_key(open('public_pem.pem', 'r').read())
print("\n",private_pem)
print("\n",public_key)

cipher = PKCS1_OAEP.new(key=pu_key)
cipher_text = cipher.encrypt(message)
print("\n\nCipher Key : ",cipher_text)
decrypt = PKCS1_OAEP.new(key=pr_key)
decrypted_message = decrypt.decrypt(cipher_text)
print("\n\nDecrypted message",decrypted_message)
