# Author: Cesar Vicente
# Date  : March 15, 2019
# This program counts all the printable characters in a string.
# If there is a gap in the sequence, then a single blank line is printed.

myString = input("Enter a string: ")

for i in range(32, 127):
    i = chr(i)
    charNum = myString.count(i)
    if charNum > 0:
        print(i + " " + str(charNum))
