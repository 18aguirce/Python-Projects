# Author:   Cesar Vicente
# Date:     23 Jan 2019
# Prompt the user for the radius of a sphere.
# Compute the volume of the sphere.
# Compute the surface area of the sphere.
# Print the volume to 2 decimal places with a thousands separator.
# Print the surface area to 2 decimal places with a thousands separator.

radius = int (input("What's the radius of the sphere? "))

pi = 3.14159265359

volume = 4/3 * pi * radius ** 3
surfaceArea = 4 * pi * radius ** 2

print()

print ("V = " + format(volume, '0,.2f'))

print ("A = " + format(surfaceArea, '0,.2f'))   
