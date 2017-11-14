#!/bin/python3

import random

salt = []
saltChar = random.randrange(33,126)
saltChar = chr(saltChar)

for i in range(10):
    saltChar = random.randrange(33,126)
    saltChar = chr(saltChar)
    salt.append(saltChar)

salt = "".join(salt)
print(salt)

