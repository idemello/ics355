#!/bin/python3

import csv
import bcrypt
import getpass 

class User:
    

    def __init__(self, name, USBalance, EURBalance,  GBPBalance, hashedPW, salt, fullHash):
        print('creating new user')
        self.name = name
        self.USBalance = float(USBalance)
        self.EURBalance = float(EURBalance)
        self.GBPBalance = float(GBPBalance)
        self.hashedPW = hashedPW
        self.salt = salt
        self.fullHash = fullHash
    
    def whoami(self):
        return self.name

    def pwCheck(self, pwUserEntered, hashPass):
        print(hashass)
        return bcrypt.checkpw(pwUserEntered, hashPass)

    def newPW(self, userPass):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(userPass, salt)


#Function Name: deposit
#
#Purpose: Add an amount of a type of currency to the users account
#
#Parameters:
#amount: The amount to be added
#origin: The type of currency to be added
#
#return values:
#This function returns the new account balance
    
    def transfer(self, userTo, currType, amount):

        try:
            if currType == 'USD':
                if amount > self.USBalance:
                    raise RuntimeError('Insufficient Funds')
                self.USBalance -= amount
                userTo.USBalance += amount
                return self.USBalance

            elif currType == 'EUR':
                if amount > self.EURBalance:
                    raise RuntimeError('Insufficient Funds')
                self.EURBalance -= amount
                userTo.EURBalance += amount
                return self.EURBalance
            else:
                if amount > self.GBPBalance:
                    raise RuntimeError('Insufficient Funds')
                self.GBPBalance -= amount
                userTo.EURBalance += amount
                return self.GBPBalance

        except RuntimeError:
            print("Insufficient Funds, please enter a valid number")
   
    def deposit(self, amount, origin):
        if origin == 'USD':
            self.USBalance += amount
            return self.USBalance
        elif origin == 'EUR':
            self.EURBalance += amount
            return self.EURBalance
        else:
            self.GBPBalance += amount
            return self.GBPBalance

#Function Name: withdraw
#
#Purpose: This function subtracts a value from the users account
#         If there are insufficient funds the program will notify the user
#
#Parameters:
#amount: The amount to be withdrawn
#origin: The type of currency to be withdrawn
#
#Return Values: 
#The new account balance after withdrawl

    def withdraw(self, amount, origin):
        
        try:
            if origin == 'USD':
                if amount > self.USBalance:
                    raise RuntimeError('Insufficient Funds')
                self.USBalance -= amount
                return self.USBalance
            
            elif origin == 'EUR':
                if amount > self.EURBalance:
                    raise RuntimeError('Insufficient Funds')
                self.EURBalance -= amount
                return self.EURBalance
                
            else:
                if amount > self.GBPBalance:
                    raise RuntimeError('Insufficient Funds')
                self.GBPBalance -= amount
                return self.GBPBalance
        except RuntimeError:
            print("Insufficient Funds, please enter a valid number")

#Function Name: convert
#
#Purpose: The convert function takes in user specified inputs, it takes away fr$
#         balance of a particular currency then adds the converted currency to $
#         No money is lost in this process
#
#Parameters: 
#originFrom: The type of currency to be converted
#originTo: The type of currency that will be added after conversion
#amount: The amount of currency that will be converted
#
#Return Values:
#Dont really even know where to start with this
#comments and suggestions on how to return this spaghetti method would be 
#appreciated!
#Disclaimer: This function works, its just spaghetti

    def convert(self, originFrom, originTo, amount):
        if originFrom == 'USD':
            self.USBalance -= amount
            if originTo == 'USD':
                self.USBalance += amount
                return self.USBalance
            elif originTo == 'EUR':
                self.EURBalance += Converter('USD', 'EUR', amount)
                return self.EURBalance
            elif originTo == 'GBP':
                self.GBPBalance += Converter('USD', 'GBP', amount)
                return self.GBPBalance
        elif originFrom == 'EUR':
            self.EURBalance -= amount
            if originTo == 'USD':
                self.USBalance += Converter('EUR', 'USD', amount)
                return self.USBalance
            elif originTo == 'EUR':
                self.EURBalance += amount
                return self.EURBalance
            elif originTo == 'GBP':
                self.GBPBalance += Converter('EUR', 'GBP', amount)
                return self.GBPBalance
        elif originFrom == 'GBP':
            self.GBPBalance -= amount
            if originTo == 'USD':
                self.USBalance += Converter('GBP', 'USD', amount)
                return self.USBalance
            elif originTo == 'EUR':
                self.EURBalance += Converter('GBP', 'EUR', amount)
                return self.EURBalance
            elif originTo == 'GBP':
                self.GBPBalance += amount
                return self.GBPBalance

#Function Name: dump
#
#Purpose: The dump function displays instance variables in a user friendly way
#
#Parameters:
#None
#
#Return Values:
#None


    def dump(self):
        print(self.name + " has the follwing balances: ")
        print("USD Balance = " + str(self.USBalance))
        print("EUR Balance = " + str(self.EURBalance))
        print("GBP Balance = " + str(self.GBPBalance))



#Method Name: detail

#Purpose: The method name uses pythons syntatic sugar to return a tuple of all $
#
#Parameters:
#None
#
#Return Values:
#The return values of this function are all the instance variables of the objec$
#called upon


    def detail(self):
        data =[self.name, self.USBalance, 'USD',  self.EURBalance, 'EUR', self.GBPBalance, 'GBP', self.hashedPW, self.salt, self.fullHash]
        return data

def save(userList):
    
    saveList = []
    
    for i in range(len(userList)):
        saveList.append(userList[i].detail())

    myFile = open('newDB.csv', 'w')
    
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(saveList)
    
    print('Database updated')


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
                username = input('Warning: Username already exists, please select another username\n')

    while valid == False:
        plainText = getpass.getpass('Please enter your new password')
        if(len(plainText) < 8 or len(plainText) > 32):
                print('Password must be between 8 and 32 characters')
        else:
            valid = True
        matchPass = getpass.getpass("Please re-enter the password: ")
    
    while plainText != matchPass:
        print("Warning: passwords do not match! Re-enter password")
        matchPass = getpass.getpass("Please re-enter the password: ")
        chances -= 1
        if chances == 0:
            print('Too many invalid entries, program will shut down')
            quit()
    fullHash = get_hashed_password(plainText)
    salt = fullHash[7:29]
    hashedPW = fullHash[29:]
    newUser = User(str(username), 0, 0, 0, str(hashedPW), str(salt), str(fullHash))
    userList.append(newUser)
    save(userList)
    
    return userList

def deleteUser(username, userList):
    
    i = 0
    while(userList[i].whoami() != username):
        i += 1
    
    userList.pop(i)


    save(userList)
    
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
    print('5. Info')
    print('6. Exit')

'''
Function Name:Interface
Purpose: The interface function, interacts with the user and calls the appropriate functions
Parameters:
username: The username is actually an object of the type user this
          make is easier to call the methods of the user class
Return Values:
1: The function will return 1 when the user is ready to exit
'''
    
def Interface(username, userList):

    
    print("Welcome " + username.whoami())
    print(username)
    print(type(username))
    
    Options()
    try:
        choice = int(input())
        while choice != 6:
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
                i = isUser(transferTo, userList)
                if i == -1:
                    print('Username not found')
                else:
                    transferTo = userList[i]
                    currType = input("Which currency would you like to transfer?")
                    amount = float(input("How much would you like to transfer?"))
                    username.transfer(transferTo, currType, amount) 
            elif choice == 5:
                print("Info: View account details")
                username.dump()
            else:
                print("Invalid input!")

            Options()
            choice = int(input())
     
    except ValueError:
        print("Invalid Entry, please enter a number")
    save(userList)
    quit()

def AdminInterface(userList):
    AdminOptions()
    try:
        choice = int(input())
        while choice != 8:
            if choice == 1:
                print("Info: Maint is used to convert one currency to another")
                currTypeFrom = str(input("What currency would you like to convert from?\n"))
                currTypeTo = str(input("What currency would you like to convert to?\n"))
                currAmount = float(input("What amount would you like to convert?\n"))
                username.convert(currTypeFrom, currTypeTo, currAmount)
            
            elif choice == 2:
                print("Info: Add funds will add money to the users account")
                username = input('Which user would you like to add funds to?')
                i = isUser(username,  userList)
                if i == -1:
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
                i = isUser(username,  userList)
                print(i)
                if i == -1:
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
                if isUser(userToBeDeleted, userList) == -1:
                    print('Username not found')
                else:
                    deleteUser(userToBeDeleted, userList)
            elif choice == 6:
                print("Info: List all users and their balances")
                for x in range(len(userList)):
                    print(userList[x].dump())
            elif choice == 7:
                print("Info: Transfer money from one user to another")
                transferTo = input("Which user would you like to transfer money to?")
                i = isUser(transferTo)
                if i == -1:
                    print('Username not found')
                else:
                    transferTo = userList[i]
                    currType = input("Which currency would you like to transfer?")
                    amount = float(input("How much would you like to transfer?"))
                    userList[0].transfer(transferTo, currType, amount) 
            else:
                print("Please enter a valid number")
            AdminOptions()
            choice = int(input())
    
    except ValueError:
        print("Invalid Entry, please enter a number")
    
    save(userList)
    
    print('Goodbye!')
    quit()

def AdminOptions():
    print('What would you like to do?')
    print('1. Maint')
    print('2. Add Funds')
    print('3. Subtract Funds')
    print('4. Add User')
    print('5. Delete User')
    print('6. List Users')
    print('7. Transfer')
    print('8. Exit')

def isUser(username,  userList):
    
    result = -1
    for i in range(len(userList)):
        print(username)
        print(userList[i].whoami())
        if username == userList[i].whoami():
            result = i
    
    return result

