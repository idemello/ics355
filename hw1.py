#!/usr/bin/env python3

from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter

print('Welcome to currency')
print('Choose a command:\n')
print('1. MAINT\n2. EXIT')
choice = int(input())

if choice == 1:
    print('Enter the amount of currency X you would like to convert to currency Y\n');
    print('Example: 1000 USD JPY\n')
    currs = input().split(' ')
    print(currs)
    amt = int(currs[0])
else:
    print('2')

