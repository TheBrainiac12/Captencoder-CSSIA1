from bcrypt import hashpw, gensalt
from time import sleep


name = input('Please enter your Name:')
user_name = input('Please enter your Username:')
password = input('Please enter your Password:')

sleep(2)

print(f'''\nHello {name}, your original username and password are as follows:
{user_name}
{password}''')

user_name = str.encode(user_name)
password = str.encode(password)

salt = gensalt()
hash_user_name = hashpw(user_name,salt)
hash_user_password = hashpw(password,salt)

sleep(2)

print(f'''\nYour hashed username and password are as:
Username:{hash_user_name}
Password: {hash_user_password}''')