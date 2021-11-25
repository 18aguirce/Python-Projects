# Author: Cesar Vicente
# Date  : Feb. 27, 2019
# This is program does fun things with circles.

# This is the start of the program

import circlesphere

r = float(input("Input the radius of a circle or a sphere: "))

print("You entered: " + str(r))

myDiameter = circlesphere.diameter(r)
print("The diameter = " + str(myDiameter) + " units.")

print("The circumference = " + str(circlesphere.circumference(r)) + " units.")

print("The area = " + str(circlesphere.area(r)) + " unit.")

myBeachBallVolume = circlesphere.sphere_volume(r)
print("The volume of my beach ball is " + str(myBeachBallVolume)
      + " cubic units.")

print("I'll need " + str(circlesphere.sphere_surfacearea(r))
     + " square units of material to cover the beachball.")

print("The volume of a hemisphere is: " + str(circlesphere.hemisphere_volume(r))
      + " cubic units.")

print("The surface area of the hemisphere is: "
      + str(circlesphere.sphere_surfacearea(r)) + " square units.")
