#!/bin/python3

import bcrypt
import csv
from functions import *
from classes import *

'''
def get_hashed_password(userPass):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(userPass, salt)

def check_password(userPass, hashPass):
    return bcrypt.checkpw(userPass, hashPass)

def new_user(username, userList):
    
    chances = 3
    newUser = True
    valid = False 

    while newUser == False:
        for i in range(len(userList)):
            if(username == userList[i].whoami()):
                newUser = False
                username = input('Warning: Username already exists, please select a different username')
            

    while valid == False:
        plainText = input("Please enter the new password: ")
        if(len(plainText) < 8 or len(plainText) > 32):
                print('Password must be between 8 and 32 characters')
            #TODO: check for at least one special character and uppercase character
            #elif(len(plaintext) > 8 and len(plaintext) < 32):
            #    while(
        else:
            valid = True
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
    newUser = User(username, 0, 0, 0, hashedPW, salt, fullHash)
    userList.append(newUser)
    myData = userList[-1].detail()

    myFile = open('newDB.csv', 'a')

    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(myData)
    
    return userList
'''
