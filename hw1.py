#!/usr/bin/env python3

recDB = open('records.txt', 'r')
currDB = open('curr.txt', 'r')


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

def UserFind(recList, user):
    uFound = 0

    for i in range(0, len(recList)):

        if user == str(recList[i]):
            uFound = 1

    if uFound == 1:
        print('Welcome ' + user)
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
currDB.close()
