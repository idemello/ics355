#TODO: USERTo in classes.py needs to be an object not string
#TODO: Check save method
#TODO: users not being added properly check list initialization

from classes import *
from functions import *
from pas import *
import csv

def main():

    print('Welcome to the Financial Database')
    credsList = []
    recordsList = []
    saveList = []
    userList = []
    

    accountList = open("records.csv", "r")
    numUser = 0
    numCreds = 0

    with open('userDB.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            credsList.append(row)
   
    with open('records.csv') as recordsCSV:
       csvReader = csv.reader(recordsCSV)
       for row in csvReader:
           recordsList.append(row)

    print(recordsList)
    print(credsList)

    for q in range (len(recordsList)):
        userList.append(User(recordsList[q][0], recordsList[q][1], recordsList[q][3], recordsList[q][5]))

    passCount = 0;

    username = input('Please enter your username\n')
    ufound = 0
    #iterates through all the usernames in the database
    #To find a match
    #If a match is found then the user will be able to access
    #The database
    while True:
        if username == 'Admin':
            for z in range(2):
                adminPass = input('Please enter your password')
                if check_password(adminPass, credsList[0][3]):
                    print('Welcome Admin')
                    AdminInterface(recordsList, userList)
                    break
                else:
                    print('incorrect password! You have ' + str((3 - passCount)) + ' attempts remaining')
                    passCount += 1
            if passCount == 0:
                quit()
                
        for y in range(len(credsList)):
            if credsList[y][0] == username:
                userPass = input('Please enter your password')
                if check_password(userPass, credsList[y][3]):
                    Interface(userList[y])
                    break
        if ufound == 0:
            print('User not found, please try again')
            username = input('Please enter your username\n')
        passCount += 1  

if __name__ == "__main__":
    main()
