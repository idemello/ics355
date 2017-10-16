#!/usr/bin/env python3
'''
Program Name: FinCalc.py

Author: Isaac DeMello

Class: ICS 355 - Security and Trust

Instructors: Dan Clark, Mark Nelson

Date: October 15, 2017
'''

class User:
    
    count = 0

    def __init__(self, name, USBalance, EURBalance, GBPBalance):
        self.name = name
        self.USBalance = float(USBalance)
        self.EURBalance = float(EURBalance)
        self.GBPBalance = float(GBPBalance)
        User.count += 1
'''
Function Name: whoami

Purpose: To check the name of the object quickly

Parameters:
None

Return Values:
Returns the name of the object
'''

    def whoami(self):
        print(self.name)
        return self.name
'''
Function Name: deposit

Purpose: Add an amount of a type of currency to the users account

Parameters:
amount: The amount to be added
origin: The type of currency to be added

return values:
This function returns the new account balance

'''
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
'''
Function Name: withdraw

Purpose: This function subtracts a value from the users account
         If there are insufficient funds the program will notify the user

Parameters:
amount: The amount to be withdrawn
origin: The type of currency to be withdrawn

Return Values: 
The new account balance after withdrawl

'''

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
'''
Function Name: convert

Purpose: The convert function takes in user specified inputs, it takes away from the users
         balance of a particular currency then adds the converted currency to their account.
         No money is lost in this process

Parameters: 
originFrom: The type of currency to be converted
originTo: The type of currency that will be added after conversion
amount: The amount of currency that will be converted

Return Values:
Dont really even know where to start with this
comments and suggestions on how to return this spaghetti method would be 
appreciated!
Disclaimer: This function works, its just spaghetti
'''
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
'''
Function Name: dump

Purpose: The dump function displays instance variables in a user friendly way

Parameters:
None

Return Values:
None

'''

    def dump(self):
        print(self.name + " has the follwing balances: ")
        print("USD Balance = " + str(self.USBalance))
        print("EUR Balance = " + str(self.EURBalance))
        print("GBP Balance = " + str(self.GBPBalance))

'''
Method Name: detail

Purpose: The method name uses pythons syntatic sugar to return a tuple of all instance variables

Parameters:
None

Return Values:
The return values of this function are all the instance variables of the object this method is
called upon
'''

    def detail(self):
        return self.name, self.USBalance, self.EURBalance, self.GBPBalance

'''
Function Name: Converter

Purpose: The Converter function converts a certain amount of a currency into another
         the function will subtract the converted amount and add the desired type of 
         currency to the user account

Parameters:
convertFrom: This value is the type of currency that the user would like to convert from.
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
    print('4. Exit')

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
    print(username.whoami())
    Options()
    try:
        choice = int(input())
        while choice != 4:
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
                
            Options()
            choice = int(input())
    
    except ValueError:
        print("Invalid Entry, please enter a number")

    return 1;

def main():

    print('Welcome to the Financial Database')
    classList = []
    userDB = open("records.txt", "r")
    
    #put all lines in the database to a list
    #includes the newline char
    for line in userDB:
        userList = userDB.readlines()

    #remove the newline char from the list so that elements
    #can be easily accessed and parsed
    for i in range (len(userList)):
        userList[i] = userList[i][:-1]

    print(userList)
    
    #Make all the users saved in the database objects so they 
    #Can be easily accessed through the objects methods
    for j in range(0,3):
        name, name2 = userList[8*j], userList[8*j]
        name = User(name2, userList[(8*j)+1], userList[(8*j)+3], userList[(8*j)+5])
        classList.append(name)
 
   
    username = input('Please enter your username\n')
    ufound = 0
    
    #iterates through all the usernames in the database
    #To find a match
    #If a match is found then the user will be able to access
    #The database
    for x in range(len(classList)): 
        if username == classList[x].whoami():
           Interface(classList[x])
           ufound = 1

    if ufound == 0:
        print('User not found, please try again')
    
    #this creates a list of tuples so that the write()
    #function can be performed more simply
    outputList = []
    for z in range(len(classList)):
        outputList.append(classList[z].detail())

    
    output = open("records.txt", "w")
    
    #A very ugly write method
    #would love suggestions on how to clean this up or make it more "pythonic"
    outputList.insert(0, '\n')
    print(outputList)
    for n in range( 1 , len(outputList)):
        output.write(outputList[0])
        output.write(outputList[n][0] + '\n')
        output.write(str(outputList[n][1]) + '\n')
        output.write('USD\n')
        output.write(str(outputList[n][2]) + '\n')
        output.write('EUR\n')
        output.write(str(outputList[n][3])+ '\n')
        output.write('GBR\n')

if __name__ == "__main__":
    main()
