#!/usr/bin/python

import sys
import hashlib

if (len(sys.argv) == 1):
    print("Please enter a string to encrypt.")
    sys.exit()

string = str(sys.argv[1])

value = hashlib.sha256(string.encode()).hexdigest()

print("Encrypted value of " + string + " -> " + value)
