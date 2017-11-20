#!/bin/python3

import random
import bcrypt
import csv

def Salt():

    salt = []
    saltChar = random.randrange(33,126)
    saltChar = chr(saltChar)

    for i in range(10):
        saltChar = random.randrange(33,126)
        saltChar = chr(saltChar)
        salt.append(saltChar)

    salt = "".join(salt)
    return salt

def get_hashed_password(userPass):
    salt = bcrypt.gensalt()
    print("the salt is " + salt)
    return bcrypt.hashpw(userPass, salt)

def check_password(userPass, hashPass):
    return bcrypt.checkpw(userPass, hashPass)

username = input("Enter your username")
userInput = input("Enter a password:")
print("The password is: ")
hashed = get_hashed_password(userInput)

print("the hash is : " + hashed)
salt = hashed[7:29]
hashedPW = hashed[29:]


myData = [[username, hashedPW, salt]]
myFile = open('userDB.csv', 'a')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)

