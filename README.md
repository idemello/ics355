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

Welcome to the Financial Database
Please enter your username
Isaac
Welcome Isaac
What would you like to do?
1. Maint
2. Deposit
3. Withdraw
4. Exit
1
Info: Maint is used to convert one currency to another
What currency would you like to convert from?
USD
What currency would you like to convert to?
EUR
What amount would you like to convert?
1000
What would you like to do?
1. Maint
2. Deposit
3. Withdraw
4. Exit
2:
Info: Deposit will add money to the users account
What currency type will you add(USD, EUR, GBP)?
USD
How much will you add?99
What would you like to do?
1. Maint
2. Deposit
3. Withdraw
4. Exit
3
Info: Withdraw will remove money from the users account
What currency type will you withdraw(USD, EUR, GBP)?
GBP
How much will you withdraw?
3000
What would you like to do?
1. Maint
2. Deposit
3. Withdraw
4. Exit
4

This is after a run of the program:

Isaac
99.0
USD
2843.0954306
EUR
0.0
GBR

Trump
100000000.0
USD
0.0
EUR
0.0
GBR

Satan
666.0
USD
666.0
EUR
666.0
GBR
