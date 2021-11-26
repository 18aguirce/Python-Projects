# Author: Cesar Vicente
# Date  : Feb. 26, 2018
# This program counts the vowels in a string.
# Assume upper and lowercase characters are in the string.

def countVowels(inString):
    """Return the number of vowels in the string.
    Ignores case. Vowels are aeiou"""
    
    testString = inString.lower()

    count = 0
    
    for vowels in inString:
        if vowels in 'aeiou':
            count += 1
    return count

myString = input("Insert text here: ")
numVowelsFound = countVowels(myString)
print("Number of vowels found = " + str(numVowelsFound))
