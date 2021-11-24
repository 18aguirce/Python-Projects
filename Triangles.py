# Author: Cesar Vicente
# Date  : Feb 18, 2019
# Prompt the user for the largest side of the triangle
# Print te results based on the calculation a^2 + b^2 = c^2


Max = int(input("What is the largest side of the triangle? "))

for a in range(1, Max+1):
   for b in range(1, Max+1):
      for c in range(1, Max+1):
         if c*c == a*a + b*b:
            print("a = " + str(a) + " " + "b = " + str(b)+ " " + "c = " + str(c))
