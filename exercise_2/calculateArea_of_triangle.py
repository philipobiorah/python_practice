

"""
This program computes the area of a triangle given the lengths of its three sides.
The formula used to calculate the area is:

s = (a + b + c) / 2
area = (s(s - a)(s - b)(s - c)) ** 0.5

The program prompts the user to enter the coordinates of three points on a plane.
It then calculates the distances between these points using the distance formula.
Finally, it uses the calculated distances to compute the area of the triangle.

"""

def computedistance(x1, y1, x2, y2):
    """
    Compute the distance between two points on a plane using the distance formula.

    Parameters:
    x1 (float): x-coordinate of the first point
    y1 (float): y-coordinate of the first point
    x2 (float): x-coordinate of the second point
    y2 (float): y-coordinate of the second point

    Returns:
    distance (float): the distance between the two points
    """
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    print("The distance between the two points is", distance)
    return distance


# Prompt the user to enter the coordinates of three points
x1 = float(input("Enter x-coordinate for Point 1: "))
y1 = float(input("Enter y-coordinate for Point 1: "))
x2 = float(input("Enter x-coordinate for Point 2: "))
y2 = float(input("Enter y-coordinate for Point 2: "))
x3 = float(input("Enter x-coordinate for Point 3: "))
y3 = float(input("Enter y-coordinate for Point 3: "))

# Calculate the distances between the points
a = computedistance(x1, y1, x2, y2)
b = computedistance(x2, y2, x3, y3)
c = computedistance(x3, y3, x1, y1)

# Calculate the semi-perimeter
s = (a + b + c) / 2

# Calculate the area of the triangle
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Print the result
print("The area of the triangle is", area)

