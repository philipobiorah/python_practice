

"""
Write a Python program to compute the area of a triangle given the lengths of its three sides.
s = (a + b + c) / 2

area = (s(s - a)(s - b)(s - c)) ** 0.5

"""

def computedistance(x1,y1, x2, y2):
    # Compute the distance
    distance = ((x2 - x1)**2 + (y2 - y1) **2)** 0.5
    print("The distance between the two point is ", distance)


# Enter the first point with two double values
x1 = input("Enter x-coordinate for Point 1: ")
y1 = input("Enter y-coordinate for Point 1: ")
x2 = input("Enter x-coordinate for Point 2: ")
y2 = input("Enter y-coordinate for Point 2: ")
x3 = input("Enter x-coordinate for Point 3: ")
y3 = input("Enter y-coordinate for Point 3: ")

computedistance(x1,y1, x2, y2)
