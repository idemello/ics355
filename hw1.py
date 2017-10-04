#!/usr/bin/env python3

from forex_python.converter import CurrencyRates, CurrencyCodes
from forex_python.bitcoin import BtcConverter

c = CurrencyRates()
sym = CurrencyCodes()

print('Welcome to currency')
print('Choose a command:\n')
print('1. MAINT\n2. EXIT')
choice = int(input())

if choice == 1:
    print('Enter the amount of currency X you would like to convert to currency Y\n');
    print('Example: 1000 USD JPY\n')
    currs = input().split(' ')

    symbol1 = sym.get_symbol(currs[1])
    symbol2 = sym.get_symbol(currs[2])
    total = c.convert(currs[1], currs[2], int(currs[0]))
    
    print(symbol1  + currs[0] + ' '  + ' is equal to ', end = '')
    print(symbol2 + str(total) + ' ' + currs[2])

else:
    print('2')




