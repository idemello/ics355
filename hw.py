#!/usr/bin/env python3


class User:
    
    count = 0

    def __init__(self, name, USBalance, EURBalance, GBPBalance):
        self.name = name
        self.USBalance = float(USBalance)
        self.EURBalance = float(EURBalance)
        self.GBPBalance = float(GBPBalance)
        User.count += 1

    def whoami(self):
        print(self.name)
        return self.name

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

    def dump(self):
        print(self.name + " has the follwing balances: ")
        print("USD Balance = " + str(self.USBalance))
        print("EUR Balance = " + str(self.EURBalance))
        print("GBP Balance = " + str(self.GBPBalance))

    def detail(self):
        return self.name, self.USBalance, self.EURBalance, self.GBPBalance

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

def Options():

    print('What would you like to do?')
    print('1. Maint')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Exit')


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
 
    print(classList)
    for k in range(len(classList)):
        print(classList[k].dump())
        print(classList[k].whoami())
        print(type(classList[k].whoami()))

    username = input('Please enter your username\n')
    ufound = 0

    for x in range(len(classList)): 
        if username == classList[x].whoami():
           Interface(classList[x])
           ufound = 1

    if ufound == 0:
        print('User not found, please try again')

    for y in range(len(classList)):
        print(classList[y].dump())

    outputList = []
    for z in range(len(classList)):
        outputList.append(classList[z].detail())

    print(outputList[0][0])
    print(outputList)
    output = open("records.txt", "w")
    
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
