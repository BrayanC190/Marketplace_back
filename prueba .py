import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    pas = bcrypt.hashpw(password.encode('utf-8'), salt)
    return pas.decode('utf-8')

hashed_password = hash_password("user")
print(hashed_password)


