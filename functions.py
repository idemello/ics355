from pas import *
from classes import *
import csv


def deleteUser(username, data, userList):
    
    myFile = open('records.csv', 'w')
    print(data)
    i = 0
    while(userList[i].whoami() != data[i][0]):
        i += 1
    
    userList.pop(i+1)


    Save(userList)
    
    return userList

'''
Function Name: Converter
Purpose: The Converter function converts a certain amount of a currency into another
         the function will subtract the converted amount and add the desired type of 
         currency to the user account
Parameters:
:convertFrom: This value is the type of currency that the user would like to convert from.
             this currency type is taken away from the user's account BEFORE conversion.
convertTo:   This value is the type of currency that the user would like to convert to.
             This currency type is add to the user's account AFTER conversion.
amount:      The amount to be converted.
Return values: 
ConvertedTotal: This returns the amount that was converted
'''

def Converter(convertFrom, convertTo, amount):

    currDB = open('currencyList.txt', 'r')
    currList = list(currDB)
    newCurrList = []
    a, b, c = [], [], []

    for i in range(0, len(currList)):
        newCurrList.append(currList[i].split())

    for j in range (0, len(currList) - 1):
        a.append(newCurrList[j][0])
        b.append(newCurrList[j][-2])
        c.append(newCurrList[j][-1])

    toDict = dict(zip(a,c))
    fromDict = dict(zip(a,b))

    convertFromValue = float(toDict[convertFrom])
    convertToValue = float(fromDict[convertTo])
    convertAmount = amount * convertFromValue
    convertedTotal = convertAmount * convertToValue

    return float(convertedTotal)

'''
Function Name: Options
Purpose: This funciton only serves to condense my code
Parameters:
None
Return:
None
'''
def Options():

    print('What would you like to do?')
    print('1. Maint')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Transfer')
    print('5. Exit')

'''
Function Name:Interface
Purpose: The interface function, interacts with the user and calls the appropriate functions
Parameters:
username: The username is actually an object of the type user this
          make is easier to call the methods of the user class
Return Values:
1: The function will return 1 when the user is ready to exit
'''
    
def Interface(username):

    print("Welcome " + username.whoami())
    Options()
    try:
        choice = int(input())
        while choice != 5:
            if choice == 1:
                print("Info: Maint is used to convert one currency to another")
                currTypeFrom = str(input("What currency would you like to convert from?\n"))
                currTypeTo = str(input("What currency would you like to convert to?\n"))
                currAmount = float(input("What amount would you like to convert?\n"))
                username.convert(currTypeFrom, currTypeTo, currAmount)
            elif choice == 2:
                print("Info: Deposit will add money to the users account")
                currType = str(input("What currency type will you add(USD, EUR, GBP)?\n"))
                currAmount = int(input("How much will you add?"))
                username.deposit(currAmount, currType)
                 
            elif choice == 3:
                print("Info: Withdraw will remove money from the users account")
                currType = str(input("What currency type will you withdraw(USD, EUR, GBP)?\n"))
                currAmount = int(input("How much will you withdraw?\n"))
                username.withdraw(currAmount, currType)
            
            elif choice == 4:
                print("Info: Transfer money from one user to another")
                transferTo = input("Which user would you like to transfer money to?")
                currType = input("Which currency would you like to transfer?")
                amount = float(input("How much would you like to transfer?"))
                username.transfer(transferTo, currType, amount)

            Options()
            choice = int(input())
     
    except ValueError:
        print("Invalid Entry, please enter a number")
    quit()

def AdminInterface(data, userList):
    print("Welcome Admin")
    saveList = []
    AdminOptions()
    try:
        choice = int(input())
        while choice != 7:
            if choice == 1:
                print("Info: Maint is used to convert one currency to another")
                currTypeFrom = str(input("What currency would you like to convert from?\n"))
                currTypeTo = str(input("What currency would you like to convert to?\n"))
                currAmount = float(input("What amount would you like to convert?\n"))
                username.convert(currTypeFrom, currTypeTo, currAmount)
            
            elif choice == 2:
                print("Info: Add funds will add money to the users account")
                username = input('Which user would you like to add funds to?')
                i = isUser(username, data, userList)
                if i == 0:
                    print('Username not found')
                else:
                    currType = str(input("What currency type will you add(USD, EUR, GBP)?\n"))
                    currAmount = int(input("How much will you add?"))
                    print(userList[i].dump())
                    userList[i].deposit(currAmount, currType)
                    print(userList[i].dump())
                 
            elif choice == 3:
                print("Info: Subtract will remove money from the users account")
                username = input('Which user would you like to remove funds from?')
                i = isUser(username, data, userList)
                if i == 0:
                    print('Username not found')
                else:
                    currType = str(input("What currency type will you withdraw(USD, EUR, GBP)?\n"))
                    currAmount = int(input("How much will you withdraw?\n"))
                    userList[i].withdraw(currAmount, currType)
                
            elif choice == 4:
                print("Info: Add a new user")
                username = input("Enter the new username")
                print("Creating new user")
                userList = new_user(username, userList)
                print("New user created")

            elif choice == 5:
                print("Info: Delete a user")
                userToBeDeleted = input("Which user would you like to delete?")
                if isUser(userToBeDeleted, data, userList) == 0:
                    print('Username not found')
                else:
                    userList = deleteUser(userToBeDeleted, data, userList)
            elif choice == 6:
                print("Info: List all users and their balances")
                for x in range(len(userList)):
                    print(userList[x].detail())

            else:
                print("Please enter a valid number")
            AdminOptions()
            choice = int(input())
    
    except ValueError:
        print("Invalid Entry, please enter a number")
    
    Save(userList)

    print('Goodbye!')
    return userList

def Save(userList):
    
    saveList = []

    myFile = open('records.csv', 'w')
    for i in range(len(userList)):
        saveList.append(userList[i].detail())

    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(saveList)

def AdminOptions():
    print('What would you like to do?')
    print('1. Maint')
    print('2. Add Funds')
    print('3. Subtract Funds')
    print('4. Add User')
    print('5. Delete User')
    print('6. List Users')
    print('7. Exit')

def isUser(username, data, userList):
    
    result = 0
    for i in range(len(userList)):
        if username == userList[i].whoami():
            result = i
    
    return result

    
