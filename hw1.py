#!/usr/bin/env python3


class User:

    def __init__(self, name):
        self.name = name
   
#    def convert(currency):
        #converts user balance to new currency
        #CANNOT convert if desired converstion is greater than balance
 
#    def newCurr(currency):
        #Adds a new currency to the user's account

#    def withdraw(currency):
        #subtracts currency from users account

#    def details():
        #prints out the user name and all currencies in that users possesion

def ClearList(recList):
    for j in range(0, len(recList)):
        recList[j] = recList[j].replace("\n", "")
    return recList

def UserMenu():
    
    currDB = open('curr.txt', 'r')
    currList = list(currDB)
    newCurrList = []
    a, b, c  = [], [], []

    for i in range(0, len(currList)):
        newCurrList.append(currList[i].split())

    #Curr1 to Standard the from Standard
    for j in range (0, len(currList) - 1):
        a.append(newCurrList[j][0])
        b.append(newCurrList[j][-2])
        c.append(newCurrList[j][-1])
    
    toDict = dict(zip(a,c))
    fromDict = dict(zip(a,b))

    choice = 0
    convertFrom = ''
    convertFromValue = 0
    total = 0

    print('What would you like to do?')
    while choice != 2:
        print('1. MAINT')
        print('2. EXIT')
        choice = int(input())
        if choice == 1:
            try:
                print('What currency would you like to convert?')
                print('EX: USD, JPY, GBP')
                convertFrom = str(input())
    #           print (float(toDict[convertFrom]))
                convertFromValue = (float(toDict[convertFrom]))
                print('What currency would you like to convert to?')
                convertTo = str(input())
                convertToValue = float(fromDict[convertTo])
    #           print(convertToValue)
                print('What amount would you like to convert?')
                amount = float(input())
                convertAmount = amount * convertFromValue
                total = convertAmount * convertToValue
                print("Converting " + str(amount) + " " + convertFrom + " to " + convertTo)
                print("The final value is: " + str(round(total,2)) + " " + convertTo)
            except KeyError:
                print("Currency not found, please enter a valid currency")

        elif choice == 2:
            print('Goodbye')
        else:
            print('Invalid Entry')
    
    currDB.close()

def UserFind(recList, user):
    
    uFound = 0
    valid = 0
    
    uDB = open('records.txt', 'r')
    uSave.close('records.txt', 'r')

    for i in range(0, len(recList)):

        if user == str(recList[i]):
            uFound = 1

    if uFound == 1:
        print('Welcome ' + user)
        UserMenu()
    else: 
        print('User not found')
        print('Would you like to add yourself as a user?')
        print('y/n?')
        uChoice = str(input()).lower()
        while(valid == 0):
            if uChoice == 'y':
                newUserName = str(input('Enter new user name\n'))
                newUser = User(newUserName)
                recList.append(newUser)
                valid = 1
            if uChoice == 'n':
                print('Goodbye')
                valid = 1
            else:
                print('Please enter y/n')
                print('Would you like to add yourself as a user')
                print('y/n?')
                
    uDB.close()
    uSave.close()

    return recList

def main():

    
    recDB = open('records.txt', 'r')

    print('Welcome to the Financial Calculator')
    #print('Enter your user name')

    user = str(input('Enter your user name\n'))
    recList = list(recDB)
    uFound = 0

    recList = ClearList(recList)
    UserFind(recList, user)

    recDB = open('records.txt', 'w')
    for x in range(len(recList)):
        recDB.write(str(recList[x]) + '\n')

    recDB.close()

if __name__ == "__main__":
    main()
