{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf200
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;\red19\green19\blue19;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c9804\c9804\c9804;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww16120\viewh10880\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs32 \cf2 \expnd0\expndtw0\kerning0
import hashlib\
""""This code allows you to create a file in which to store a username and hashed password."""\
def hash_pass(input_pass):\
\'a0 \'a0 salt= user_name # the salt is the username in case two users have the same password, the hash is still different\
\'a0 \'a0 hashed= hashlib.md5(salt.encode())\
\'a0 \'a0 hashed.update(input_pass.encode())\
\'a0 \'a0 new_pass= hashed.digest()\
\'a0 \'a0 return new_pass\
\pard\pardeftab720\partightenfactor0
\cf0 \
\pard\pardeftab720\partightenfactor0
\cf2 password_file= input('Enter the filename where the credentials are stored.')\
user_name = input("Enter the user's account name.")\
credentials = \{\}\
password = input('Password: ')\
password1 = input('Please Re-Type The Password: ')\
count= 0\
\pard\pardeftab720\partightenfactor0
\cf0 \
\pard\pardeftab720\partightenfactor0
\cf2 while password!=password1 and count==0:\
\'a0 \'a0 print('Password Mismatch! Please Re-Type the password: ')\
\'a0 \'a0 password1= input()\
\'a0 \'a0 count= 1\
\'a0 \'a0 if password!= password1:\
\'a0 \'a0 \'a0 \'a0 count= 0\
\pard\pardeftab720\partightenfactor0
\cf0 \
\pard\pardeftab720\partightenfactor0
\cf2 str_pass= str(hash_pass(password)) # converting the hash to a string\
try:\
\'a0 \'a0 \'a0with open(password_file, 'a') as f:\
\'a0 \'a0 \'a0 \'a0 f.write('Username: \{\}\\n'.format(user_name))\
\'a0 \'a0 \'a0 \'a0 f.write("Password: ")\
\'a0 \'a0 \'a0 \'a0 f.write(str_pass)\
except OSError as e:\
\'a0 \'a0 pass}