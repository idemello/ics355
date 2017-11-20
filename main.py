#TODO: incorporate the two different DB's
#TODO: make it so that the users can transfer funds

from classes import *
from functions import *
from pas import *
import csv

def main():

    print('Welcome to the Financial Database')
    classList = []
    credsList = []
    recordsList = []

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
    #put all lines in the database to a list
    #includes the newline char
    for line in accountList:
        userList = accountList.readlines()
        numUser += 1

    #remove the newline char from the list so that elements
    #can be easily accessed and parsed
    for a in range (len(userList)):
        userList[a] = userList[a][:-1]

    

    passCount = 0;

    username = input('Please enter your username\n')
    ufound = 0
    #iterates through all the usernames in the database
    #To find a match
    #If a match is found then the user will be able to access
    #The database
    for c in range(len(credsList)):
        if username == 'Admin':
            for z in range(2):
                adminPass = input('Please enter your password')
                if check_password(adminPass, credsList[0][3]):
                    print('Welcome Admin')
                    AdminInterface(recordsList)
                else:
                    print('incorrect password! You have ' + str((3 - passCount)) + ' attempts remaining')
                    passCount += 1
            if passCount == 0:
                quit()
                
        for y in range(len(credsList)):
            if credsList[y][0] == username:
                userPass = input('Please enter your password')
                if check_password(userPass, credsList[y][3]):
                    print('Welcome ' + username)
                    Interface(credsList[y][0])

        if ufound == 0:
            print('User not found, please try again')
            username = input('Please enter your username\n')
        passCount += 1  

    #this creates a list of tuples so that the write()
    #function can be performed more simply
    outputList = []
    for d in range(len(classList)):
        outputList.append(classList[d].detail())

    outputList.insert(0, '\n')
    
    myFile = open('records.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(recordsList)

if __name__ == "__main__":
    main()
