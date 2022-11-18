#!/bin/python3
import hashlib
import base64

print("Please ensure that your file is in the same directory as the script :)")

file_name = input("Please Enter Filename: ")
print("the options for encoding format are md5, base64")
encoding = input("Please Enter the Encoding format you want: ")

with open(file_name,'r') as file:
    lines = file.read().splitlines()
    
if encoding == "md5": #for md5
    md5_output = open('md5_output.txt','w')
    for line in lines:
        hashed_line = hashlib.md5(line.encode())
        hashes = hashed_line.hexdigest()
        md5_output.write(hashes)
        md5_output.write('\n')
        
if encoding == "base64":  #for base64
    base64_output = open('base64_output.txt','w')
    for line in lines:
        line_bytes = line.encode('ascii')
        base64_bytes = base64.b64encode(line_bytes)
        base64_line = base64_bytes.decode('ascii')
        base64_output.write(base64_line)
        base64_output.write('\n')
        
        
      





