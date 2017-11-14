class User:
    
    count = 0

    def __init__(self, name, USBalance, EURBalance, GBPBalance):
        self.name = name
        self.USBalance = float(USBalance)
        self.EURBalance = float(EURBalance)
        self.GBPBalance = float(GBPBalance)

    def whoami(self):
        return self.name

#Function Name: deposit
#
#Purpose: Add an amount of a type of currency to the users account
#
#Parameters:
#amount: The amount to be added
#origin: The type of currency to be added
#
#return values:
#This function returns the new account balance

   
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

#Function Name: withdraw
#
#Purpose: This function subtracts a value from the users account
#         If there are insufficient funds the program will notify the user
#
#Parameters:
#amount: The amount to be withdrawn
#origin: The type of currency to be withdrawn
#
#Return Values: 
#The new account balance after withdrawl

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

#Function Name: convert
#
#Purpose: The convert function takes in user specified inputs, it takes away from the users
#         balance of a particular currency then adds the converted currency to their account.
#         No money is lost in this process
#
#Parameters: 
#originFrom: The type of currency to be converted
#originTo: The type of currency that will be added after conversion
#amount: The amount of currency that will be converted
#
#Return Values:
#Dont really even know where to start with this
#comments and suggestions on how to return this spaghetti method would be 
#appreciated!
#Disclaimer: This function works, its just spaghetti

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

#Function Name: dump
#
#Purpose: The dump function displays instance variables in a user friendly way
#
#Parameters:
#None
#
#Return Values:
#None


    def dump(self):
        print(self.name + " has the follwing balances: ")
        print("USD Balance = " + str(self.USBalance))
        print("EUR Balance = " + str(self.EURBalance))
        print("GBP Balance = " + str(self.GBPBalance))


#Method Name: detail
#
#Purpose: The method name uses pythons syntatic sugar to return a tuple of all instance variables
#
#Parameters:
#None
#
#Return Values:
#The return values of this function are all the instance variables of the object this method is
#called upon


    def detail(self):
        return self.name, self.USBalance, self.EURBalance, self.GBPBalance


