# Author: Cesar Vicente
# Date  : April 18, 2019
# Will prevent the program from crashing when it can't find the txt file

print("Reading data file line by line...")

try:
    Efile = open("elements.txt", "r")
    
    for line in range(1, 11):
        print(line, Efile.readline().rstrip('\n'))
        
    Efile.close()

except FileNotFoundError as ex:
    print("ERROR: File elements.txt not found.")

print("End of program.")
