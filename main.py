#TODO: USERTo in classes.py needs to be an object not string
#TODO: Check save method
#TODO: users not being added properly check list initialization

from functions import *
import csv
import getpass

def main():

    print('Welcome to the Financial Database')
    userList = []
    userInfoList = []

    #username[0], Amount(USD)[1], currType(USD)[2], Amount(EUR)[3], currType(EUR)[4], Amount[GBR][5]
    #currTYpe(GBR)[6], hashedPW[7], salt[8], fullHash[9]
    
    with open('newDB.csv') as userInfoFile:
        csvReader = csv.reader(userInfoFile)
        for row in csvReader:
            userInfoList.append(row)

    
    for q in range(len(userInfoList)):
        username = str(userInfoList[q][0])
        usdAmount = float(userInfoList[q][1])
        eurAmount = float(userInfoList[q][3])
        gbpAmount = float(userInfoList[q][5])
        hashed = str(userInfoList[q][7])
        salt = str(userInfoList[q][8])
        fullHash = str(userInfoList[q][9])
        newUser = User(username, usdAmount, eurAmount, gbpAmount, hashed, salt, fullHash)
        userList.append(newUser)

    username = input('Please enter your username\n')
    ufound = 0
    #iterates through all the usernames in the database
    #To find a match
    #If a match is found then the user will be able to access
    #The database
    while True:
        if username == 'Admin':
            for z in range(2):
                adminPass = getpass.getpass('Password for Admin: ')
                if check_password(adminPass, userList[0].fullHash):
                    print('Welcome Admin')
                    AdminInterface(userList)
        else:
            for y in range(len(userList)):
                if userList[y].name == username:
                    userPass = getpass.getpass('Password: ')
                    if check_password(userPass, userList[y].fullHash):
                        Interface(userList[y], userList)
                        break
        if ufound == 0:
            print('User not found, please try again')
            username = input('Please enter your username\n')
    save(userList)

if __name__ == "__main__":
    main()
    
