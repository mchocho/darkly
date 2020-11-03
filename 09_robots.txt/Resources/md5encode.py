#!/usr/bin/python

import sys
import hashlib

if (len(sys.argv) == 1):
    print("Please enter a string to encode.")
    sys.exit()

value = str(sys.argv[1])
result = hashlib.md5(value.encode())

print("md5 encoded value of str: " + value + " -> " + result.hexdigest())
