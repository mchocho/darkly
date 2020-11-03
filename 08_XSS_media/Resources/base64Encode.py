#!/usr/bin/python

import sys
import base64

if (len(sys.argv) == 1):
    print("Please enter a string to encode.")
    sys.exit()

value = str(sys.argv[1])


string_bytes = value.encode("ascii")

b64_bytes = base64.b64encode(string_bytes)
b64_string = b64_bytes.decode("ascii")

print("Encoded value of str " + value + " -> " + b64_string)
