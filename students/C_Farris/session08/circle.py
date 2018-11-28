#!/usr/bin/env Python3

##############
# Date: November 28, 2018
# Author: Carol Farris
# Goal: Gain familiarity with generating classes
##############


from math import pi, pow


class Circle():

    def __init__(self, radius=1):
        self.radius = radius
   
    @property 
    def diameter(self):
        return self.radius * 2
    
    @diameter.setter 
    def diameter(self, value):
        self.radius = value / 2

    @property 
    def area(self):
        return self.radius * self.radius * pi

    def __str__(self):
        return f'Circle with a radius {self.radius:.6f}'.format(self.radius)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.radius})'

    def __add__(self, other):
        return f'{self.__class__.__name__}({self.radius + other.radius})'

    def __mul__(self, other):
        if self.radius:
            print("here!")
            return f'{self.__class__.__name__}({(self.radius * other)})'

    def __rmul__(self, other):
        return f'{self.__class__.__name__}({(self.radius * other)})'

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius


class Sphere(Circle):
    def __init__(self, radius=1):
        Circle.__init__(self, radius)
    
    @property
    def volume(self):
        return 1.25 * pi * pow(self.radius, 3)

    def __str__(self):
        return f'Sphere with a radius {self.radius:.6f}'.format(self.radius)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.radius})'

    @property
    def area(self):
        return 4 * pi * self.radius * self.radius
        