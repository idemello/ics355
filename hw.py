#!/usr/bin/env python3


class User:
    
    count = 0

    def __init__(self, name, USBalance, JPBalance, GBRBalance):
        self.name = name
        self.USBalance = USBalance
        self.JPBalance = JPBalance
        self.GBRBalance = GBRBalance
        User.count += 1

    def whoami(self):
        print(self.name)

    def deposit(self, amount, origin):
        if origin == 'USD':
            self.USBalance += amount
            return self.USBalance
        elif origin == 'JP':
            self.JPBalance += amount
            return self.JPBalance
        else:
            self.GBRBalance += amount
            return self.GBRBalance

    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError('Insufficient Funds')
        self.balance -= amount
        return self.balance
    
    def dump(self):
        print(self.name + "has the follwing balances: ")
        print("USD Balance = " + self.USBalance)
        print("JPY Balance = " + self.JPBalance)
        print("GBR Balance = " + self.GBRBalance)

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

def Interface():

    print('What would you like to do?')
    print('1. Maint')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Convert')
    print('5. Exit')

    choice = int(input())

def main():

    print('Welcome to the Financial Database')
    userChoice = str(input('Enter your user name\n'))
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

    
    print(classList)
    for k in range(len(classList)):
        print(classList[k].dump())
        print(classList[k].whoami())

    Interface()

if __name__ == "__main__":
    main()
