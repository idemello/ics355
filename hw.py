#!/usr/bin/env python3

import pickle

class User:
    
    count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        User.count += 1

    def whoami(self):
        print(self.name)

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError('Insufficient Funds')
        self.balance -= amount
        return self.balance
    
    def dump(self):
        print(self.name + "has the follwing balances: ")
        print(self.balance)
        
def UserMenu():

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

def main():


    with open("recordList.txt", "rb") as fp
        uList = pickle.load(fp)

    print(uList)
    
    
    print('Welcome to the Financial Database')
    userChoice = str(input('Enter your user name\n'))
    recList = list(recDB)
    
    userChoice = User(userChoice, 1000)
    userChoice.whoami()
    userChoice.dump()
    
    recDB.close()

if __name__ == "__main__":
    main()
