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

def AdminInterFace():
    print("Welcome Admin")
    AdminOptions()
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
            elif choice == 4:
                print("Info: Add a new user")
            elif choice == 5:
                print("Info: Delete a user")
            Options()
            choice = int(input())
    
    except ValueError:
        print("Invalid Entry, please enter a number")

   

def AdminOptions():
    print('What would you like to do?')
    print('1. Maint')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Add User')
    print('5. Delete User')
    print('6. Exit')

