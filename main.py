import hashlib
""""This code allows you to create a file in which to store a username and hashed password."""
def hash_pass(input_pass):
    salt= user_name # the salt is the username in case two users have the same password, the hash is still different
    hashed= hashlib.md5(salt.encode())
    hashed.update(input_pass.encode())
    new_pass= hashed.digest()
    return new_pass

password_file= input('Enter the filename where the credentials are stored.')
user_name = input("Enter the user's account name.")
credentials = {}
password = input('Password: ')
password1 = input('Please Re-Type The Password: ')
count= 0

while password!=password1 and count==0:
    print('Password Mismatch! Please Re-Type the password: ')
    password1= input()
    count= 1
    if password!= password1:
        count= 0

str_pass= str(hash_pass(password)) # converting the hash to a string
try:
     with open(password_file, 'a') as f:
        f.write('Username: {}\n'.format(user_name))
        f.write("Password: ")
        f.write(str_pass)
except OSError as e:
    pass