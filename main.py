#TODO: USERTo in classes.py needs to be an object not string
#TODO: Check save method
#TODO: users not being added properly check list initialization

from classes import *
from functions import *
from pas import *
import csv

def main():

    print('Welcome to the Financial Database')
    userList = []
    userInfoList = []

    accountList = open("records.csv", "r")
    numUser = 0
    numCreds = 0

    #username[0], Amount(USD)[1], currType(USD)[2], Amount(EUR)[3], currType(EUR)[4], Amount[GBR][5]
    #currTYpe(GBR)[6], hashedPW[7], salt[8], fullHash[9]
    
    with open('newDB.csv') as userInfoFile:
        csvReader = csv.reader(userInfoFile)
        for row in csvReader:
            userInfoList.append(row)

    print(userInfoList)

    for q in range (len(userInfoList)-1):
        print(q)
        userList.append(User(userInfoList[q][0], userInfoList[q][1], userInfoList[q][3], userInfoList[q][5], userInfoList[q][7], userInfoList[q][8], userInfoList[q][9]))


    print(userList)
    print(userList[0].detail())
    print(userList[0].fullHash)
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
                #adminPass = input('Please enter your password\n')
                #if check_password(adminPass, userList[0].fullHash):
                    #print('Welcome Admin')
                    AdminInterface(userList)
                    break
               # else:
                    print('incorrect password! You have ' + str((3 - passCount)) + ' attempts remaining')
                    passCount += 1
            if passCount == 0:
                quit()
                
        else:
            for y in range(len(userList)):
                if userList[y].name == username:
                    userPass = input('Please enter your password')
                    if check_password(userPass, userList[y].fullHash):
                        Interface(userList[y])
                        break
        if ufound == 0:
            print('User not found, please try again')
            username = input('Please enter your username\n')
        passCount += 1  

if __name__ == "__main__":
    main()
