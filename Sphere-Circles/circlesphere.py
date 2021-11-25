# Author: Cesar Vicente
# Date  : Feb. 27, 2019
# Module that does various computations for a circle/sphere

import math

def diameter(radius):
    """Compute diameter of a circle
    given its radius."""
    diameter = 2 * radius
    return diameter

def circumference(radius):
    """Compute circumference of a circle
    given its radius."""
    circumference = 2 * math.pi * radius
    return circumference

def area(radius):
    """Compute area of a circle
    given its radius"""
    area = math.pi * radius**2
    return area

def sphere_volume(radius):
    """Compute the volume of a sphere
    given its radius."""
    volume = 4/3 * math.pi * radius**3
    return volume

def sphere_surfacearea(radius):
    """Compute the surface area of a sphere
    given its radius."""
    surface_area = 4 * math.pi * radius**2
    return surface_area

def hemisphere_volume(radius):
    """Compute the hemisphere
    given its radius."""
    #Below is an example of calling another function.
    volume = sphere_volume(radius)/2
    return volume

def hemisphere_surfacearea(radius):
    """Compute the surface area of a hemisphere
    given its radius"""
    surface_area = sphere_surfacearea(radius) / 2 + area(radius)
    return surface_area
