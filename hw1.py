#!/usr/bin/env python3

recDB = open('records.txt', 'r')


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
    print(currList)
    print('\n\n\n\n\n\n\n\n')
    for i in range(0, len(currList)):
        print(currList[i])
        newCurrList.append(currList[i].split())
    print(newCurrList)
    print(newCurrList[0][0])
    choice = 0;
    convertFrom = ''
    convertFromValue = 0

    print('What would you like to do?')
    while choice != 2:
        print('1. MAINT')
        print('2. EXIT')
        choice = int(input())
        if choice == 1:
            print('What currency would you like to convert?')
            print('EX: USD, JPY, GBP')
            convertFrom = str(input())
            print('What currency would you like to convert to?');
            convertFromValue = int(input())
    

        elif choice == 2:
            print('Goodbye')
        else:
            print('Invalid Entry')
    
    currDB.close()

def UserFind(recList, user):
    uFound = 0

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
        newUser = str(input()).lower()
        if newUser == 'y':
            print('Enter new User Name')
            newUserName = str(input())
            recList.append(newUserName)
        if newUser == 'n':
            print('Goodbye')

    return recList



print('Welcome to the Financial Calculator')
print('Enter your user name')

user = str(input())
recList = list(recDB)
uFound = 0

recList = ClearList(recList)
UserFind(recList, user)

recDB = open('records.txt', 'w')
for x in range(len(recList)):
    recDB.write(str(recList[x]) + '\n')

recDB.close()
