File Name: FinCalc

Depencies/How to run: This file only uses pythons built-in functions. As a result there are no downloads or installs necessary to run this program. Please note that this program was written in python3 and is not backwards compatible with python 2.x versions. The program can be run from the command line using: python3 finCalc.py. Please make sure that the records.txt file is in the same folder as the finCalc file.

Purpose: The purpose of this assignment was to create a financial calulator that would save a users financial information across various runs of the program. The program was to be made to add values to the users account, subtract, as well as convert values. The program must also be able to read and write the database information so that it can be used in between runs.

Documentation: All functions are better documented within the finCalc.py file itself

Sample run:

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
2
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
