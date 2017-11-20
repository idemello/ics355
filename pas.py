#!/bin/python3

import random
import bcrypt
import csv


def get_hashed_password(userPass):
    salt = bcrypt.gensalt()
    print("the salt is " + salt)
    return bcrypt.hashpw(userPass, salt)

def check_password(userPass, hashPass):
    return bcrypt.checkpw(userPass, hashPass)

def new_pw():
    chances = 3
    newUser = True

    username = input("Please enter the new username: ")
    while newUser == False:
        newUser = True
        with open('userDB.csv', 'r') as f:
            reader = csv.reader(f)
            for line in reader:
                if(row[line] == username):
                    print("username already in database, please select a different username")
                    newUser = False
        username = input("please enter the new username: ")

    plainText = input("Please enter the new password: ")
    matchPass = input("Please re-enter the password: ")
    while plainText != matchPass:
        print("Warning: passwords do not match! Re-enter password")
        matchPass = input("Please re-enter the password: ")
        chances -= 1
        if chances == 0:
            print('Too many invalid entries, program will shut down')
            quit()

    fullHash = get_hashed_password(plainText)
    salt = fullHash[7:29]
    hashedPW = fullHash[29:]
    myData = [[username, hashedPW, salt, fullHash]]
    myFile = open('userDB.csv', 'a')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(myData)

