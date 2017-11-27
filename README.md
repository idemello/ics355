# File Name: FinCalc

## Depencies/How to run: 
The only module not included with python 3.X.X is the cyrptography module bcrypt. This is done by using the pip installation package. simply run the command:

```
$ pip install bcrypt
```

Once bycrypt is installed in your console clone the repository.
Once the repo is cloned onto your computer enter:

```
$ python3 main.py
```

This will prompt you to enter your username and password. If you are just cloning the repo for the first time, there will be one user, Admin. The Admin password is the very secure password of 'password'. Once this is entered the admin menu will pop up, from there the Admin can convert the currency in his/her account, add/subtract currency, add/delete suers, or find out the current balance of all users.

## Purpose: 
The purpose of this assignment was to create a financial calulator that would save a users financial information across various runs of the program. The program was to be made to add values to the users account, subtract, as well as convert values. The program must also be able to read and write the database information so that it can be used in between runs.
The assigment was then evolved to ensure that an Administrator could be added. This admin would be able to manipulate data for all users at their will. 

## Features

Passwords: The passwords in the program use the python built-in getpass module. This module allows users to input their password 'Unix style' meaning that their passwords are not displayed on screen while typing this prevents the ubiquitous shoulder surfing.

bcrypt: This program uses the bcyrpt password hashing function. The function is based off the blowfish cipher and contains several other security features to prevent attacks from rainbow tables and brute force attacks. In order to protect from rainbow tables the bcrypt function automatically incorporates a salt. To prevent against brute force attacks bcrypt implements variable round sizes controlled by the cost parameter which can be changed by the programmer. The default value of 12 specifies a cost parameter of 2^12 ey expansion rounds. The users password is never stored using bcrypt.
## Documentation: 
All functions are better documented within the functions.py file itself

## Sample run:

Here is the record.txt file before a run is performed

Isaac
1000
USD
2000
EUR
3000
GBR

Trump
100000000
USD
0
EUR
0
GBR

Satan
666
USD
666
EUR
666
GBR

This is what a run of the program will consist of:

idemello@mango:~/Desktop/ics/ics355$ python3 main.py 
Welcome to the Financial Database
Please enter your username
Admin
Password for Admin: 
Welcome Admin
What would you like to do?
1. Maint
2. Add Funds
3. Subtract Funds
4. Add User
5. Delete User
6. List Users
7. Transfer
8. Exit
6
Info: List all users and their balances
Admin has the follwing balances: 
USD Balance = 1500.0
EUR Balance = 0.0
GBP Balance = 0.0
None
What would you like to do?
1. Maint
2. Add Funds
3. Subtract Funds
4. Add User
5. Delete User
6. List Users
7. Transfer
8. Exit
4
Info: Add a new user
Enter the new usernameIsaac^CTraceback (most recent call last):
  File "main.py", line 64, in <module>
    main()
  File "main.py", line 50, in main
    AdminInterface(userList)
  File "/home/idemello/Desktop/ics/ics355/functions.py", line 456, in AdminInterface
    username = input("Enter the new username")
KeyboardInterrupt
idemello@mango:~/Desktop/ics/ics355$ vim functions.py 
idemello@mango:~/Desktop/ics/ics355$ man nmap
No manual entry for nmap
idemello@mango:~/Desktop/ics/ics355$ python3 main.py 
Welcome to the Financial Database
Please enter your username
Admin
Password for Admin: 
Welcome Admin
What would you like to do?
1. Maint
2. Add Funds
3. Subtract Funds
4. Add User
5. Delete User
6. List Users
7. Transfer
8. Exit
6
Info: List all users and their balances
Admin has the follwing balances: 
USD Balance = 1500.0
EUR Balance = 0.0
GBP Balance = 0.0
None
What would you like to do?
1. Maint
2. Add Funds
3. Subtract Funds
4. Add User
5. Delete User
6. List Users
7. Transfer
8. Exit
4
Info: Add a new user
Enter the new username
Isaac
Creating new user
Please enter your new password
Please re-enter the password: 
Database updated
New user created
What would you like to do?
1. Maint
2. Add Funds
3. Subtract Funds
4. Add User
5. Delete User
6. List Users
7. Transfer
8. Exit
6
Info: List all users and their balances
Admin has the follwing balances: 
USD Balance = 1500.0
EUR Balance = 0.0
GBP Balance = 0.0
None
Isaac has the follwing balances: 
USD Balance = 0.0
EUR Balance = 0.0
GBP Balance = 0.0
None
What would you like to do?
1. Maint
2. Add Funds
3. Subtract Funds
4. Add User
5. Delete User
6. List Users
7. Transfer
8. Exit
4
Info: Add a new user
Enter the new username
Donald Trump
Creating new user
Please enter your new password
Please re-enter the password: 
Warning: passwords do not match! Re-enter password
Please re-enter the password: 
Warning: passwords do not match! Re-enter password
Please re-enter the password: 
Warning: passwords do not match! Re-enter password
Please re-enter the password: 
Too many invalid entries, program will shut down
idemello@mango:~/Desktop/ics/ics355$ python3 main.py 
Welcome to the Financial Database
Please enter your username
Isaac
Password: 
Welcome Isaac
What would you like to do?
1. Maint
2. Deposit
3. Withdraw
4. Transfer
5. Info
6. Exit
6
Database updated
Goodbye!
idemello@mango:~/Desktop/ics/ics355$ vim main.py 
idemello@mango:~/Desktop/ics/ics355$ vim functions.py 
idemello@mango:~/Desktop/ics/ics355$ python3 main.py 
Welcome to the Financial Database
Please enter your username
Isaac
Password: 
Welcome Isaac
What would you like to do?
1. Maint
2. Deposit
3. Withdraw
4. Transfer
5. Info
6. Exit
5
Info: View account details
Isaac has the follwing balances: 
USD Balance = 0.0
EUR Balance = 0.0
GBP Balance = 0.0
What would you like to do?
1. Maint
2. Deposit
3. Withdraw
4. Transfer
5. Info
6. Exit
2
Info: Deposit will add money to the users account
What currency type will you add(USD, EUR, GBP)?
USD
How much will you add?1000
What would you like to do?
1. Maint
2. Deposit
3. Withdraw
4. Transfer
5. Info
6. Exit
5
Info: View account details
Isaac has the follwing balances: 
USD Balance = 1000.0
EUR Balance = 0.0
GBP Balance = 0.0
What would you like to do?
1. Maint
2. Deposit
3. Withdraw
4. Transfer
5. Info
6. Exit
4
Info: Transfer money from one user to another
Which user would you like to transfer money to?Admin
Which currency would you like to transfer?USD
How much would you like to transfer?500
What would you like to do?
1. Maint
2. Deposit
3. Withdraw
4. Transfer
5. Info
6. Exit
6
Database updated
Goodbye!
idemello@mango:~/Desktop/ics/ics355$ vim functions.py 
idemello@mango:~/Desktop/ics/ics355$ python3 main.py 
Welcome to the Financial Database
Please enter your username
Admin
Password for Admin: 
Password for Admin: 
Welcome Admin
What would you like to do?
1. Maint
2. Add Funds
3. Subtract Funds
4. Add User
5. Delete User
6. List Users
7. Transfer
8. Exit
6
Info: List all users and their balances
Admin has the follwing balances: 
USD Balance = 2000.0
EUR Balance = 0.0
GBP Balance = 0.0
None
Isaac has the follwing balances: 
USD Balance = 500.0
EUR Balance = 0.0
GBP Balance = 0.0
None
What would you like to do?
1. Maint
2. Add Funds
3. Subtract Funds
4. Add User
5. Delete User
6. List Users
7. Transfer
8. Exit
5
Info: Delete a user
Which user would you like to delete?Isaac
Database updated
What would you like to do?
1. Maint
2. Add Funds
3. Subtract Funds
4. Add User
5. Delete User
6. List Users
7. Transfer
8. Exit
6
Info: List all users and their balances
Admin has the follwing balances: 
USD Balance = 2000.0
EUR Balance = 0.0
GBP Balance = 0.0
None
What would you like to do?
1. Maint
2. Add Funds
3. Subtract Funds
4. Add User
5. Delete User
6. List Users
7. Transfer
8. Exit
8
Database updated
Goodbye!

