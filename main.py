from classes import *
from functions import *

def main():

    print('Welcome to the Financial Database')
    classList = []
    userDB = open("records.txt", "r")
    numUser = 0

    #put all lines in the database to a list
    #includes the newline char
    for line in userDB:
        userList = userDB.readlines()
        numUser += 1

    #remove the newline char from the list so that elements
    #can be easily accessed and parsed
    for i in range (len(userList)):
        userList[i] = userList[i][:-1]

    
    #Make all the users saved in the database objects so they 
    #Can be easily accessed through the objects methods
    for j in range(0,3):
        name, name2 = userList[8*j], userList[8*j]
        name = User(name2, userList[(8*j)+1], userList[(8*j)+3], userList[(8*j)+5])
        classList.append(name)
 
   
    username = input('Please enter your username\n')
    ufound = 0
    
    #iterates through all the usernames in the database
    #To find a match
    #If a match is found then the user will be able to access
    #The database

    for x in range(len(classList)): 
        if username == classList[x].whoami():
           Interface(classList[x])

        elif ufound == 0:
            print('User not found, please try again')
            username = input('Please enter your username\n')
        

    #this creates a list of tuples so that the write()
    #function can be performed more simply
    outputList = []
    for z in range(len(classList)):
        outputList.append(classList[z].detail())

    
    output = open("records.txt", "w")
    
    #A very ugly write method
    #would love suggestions on how to clean this up or make it more "pythonic"
    outputList.insert(0, '\n')
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
