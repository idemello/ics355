#!/usr/bin/env python3

recDB = open('records.txt', 'r')
currDB = open('curr.txt', 'r')

'''
class User(curr):

    def __init__(self, name, currencies):
        self.name = name
        self.currencies = currencies
   
    def convert(currency):
        #converts user balance to new currency
        #CANNOT convert if desired converstion is greater than balance
 
    def newCurr(currency):
        #Adds a new currency to the user's account

    def details:
        #prints out the user name and all currencies in that users possesion
'''
print('Welcome to the Financial Calculator')
print('Enter your user name')

user = str(input())
recList = list(recDB)
uFound = 0

for j in range(0, len(recList)):
    recList[j] = recList[j].replace("\n", "")

#[x for x in recList if x != ""]


for i in range(0, len(recList)):

    if user == str(recList[i]):
        uFound = 1

if uFound == 1:
    print('Welcome ' + user)
else: 
    print('User not found')

recDB.close()
currDB.close()
