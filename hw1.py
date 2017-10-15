#!/usr/bin/env python3

#class User(curr):

#    def __init__(self, name, currencies):
#        self.name = name
#        self.currencies = currencies
#   
#    def convert(currency):
#        #converts user balance to new currency
#        #CANNOT convert if desired converstion is greater than balance
# 
#    def newCurr(currency):
#        #Adds a new currency to the user's account
#
#    def details():
#        #prints out the user name and all currencies in that users possesion

def ClearList(recList):
    for j in range(0, len(recList)):
        recList[j] = recList[j].replace("\n", "")
    return recList

def UserMenu():
    
    currDB = open('curr.txt', 'r')
    currList = list(currDB)
    newCurrList = []
    a, b, c  = [], [], []

    print(currList)
    print('**************')
    print(len(currList))
    print('\n\n\n\n\n\n\n\n')
    for i in range(0, len(currList)):
        print(currList[i])
        newCurrList.append(currList[i].split())
    print(newCurrList)
    print(newCurrList[0][3])
    print(type(newCurrList[0][3]))

    #Curr1 to Standard the from Standard
    for j in range (0, len(currList) - 1):
        print(j)
        a.append(newCurrList[j][0])
        b.append(newCurrList[j][-2])
        c.append(newCurrList[j][-1])
    
    toDict = dict(zip(a,c))
    fromDict = dict(zip(a,b))


    print(toDict)
    print(fromDict)
    print(toDict)
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
            print('What currency would you like to convert?')
            print('EX: USD, JPY, GBP')
            convertFrom = str(input())
            print (float(toDict[convertFrom]))
            convertFromValue = (float(toDict[convertFrom]))
            print('What currency would you like to convert to?')
            convertTo = str(input())
            convertToValue = float(fromDict[convertTo])
            print(convertToValue)
            print('What amount would you like to convert?')
            amount = float(input())
            convertAmount = amount * convertFromValue
            total = convertAmount * convertToValue
            print("Converting " + str(amount) + " " + convertFrom + " to " + convertTo)
            print("The final value is: " + str(total) + " " + convertTo)

        elif choice == 2:
            print('Goodbye')
        else:
            print('Invalid Entry')
    
    currDB.close()

def UserFind(recList, user):
    uFound = 0
    valid = 0

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
        while(
        newUser = str(input()).lower()
        if newUser == 'y':
            newUserName = str(input('Enter new user name\n'))
            recList.append(newUserName)
        if newUser == 'n':
            print('Goodbye')

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
