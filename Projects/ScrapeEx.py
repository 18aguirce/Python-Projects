# Author: Cesar Vicente
# Date  : April 10, 2019
# Example program demostrating files

import os
import urllib.request

# working website: cst.ridgewater.edu
# Not all websites work.

website_name = input("Enter a website name: ")

response = urllib.request.urlopen('http://' + website_name + '/')
linecount = 0
computerwordcount = 0
for line in response:
    line = line.decode('utf-8')#Decoding the binary data as text.
    linecount += 1
    computerwordfind = line.find("Computer")

    if computerwordfind >= 0:
        computerwordcount += 1
        print("Found on line: " + str(linecount))

print(" Total lines of code" + str(linecount))
print("Number of times 'Computer' found = " + str(computerwordcount))
