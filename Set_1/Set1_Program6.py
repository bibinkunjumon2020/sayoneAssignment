"""


Define a class named Circle which can be constructed by a radius.
The Circle class has a method which can compute the area.
"""
class Circle:
    def area(self):
        radius = float(input("Input Radius :  "))
        print("Areas = ",3.14*(radius**2))

circle = Circle()
circle.area()
