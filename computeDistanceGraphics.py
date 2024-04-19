import turtle
import math

# Prompt the user for inputing two points
x1 = float(input("Enter x-coordinate for Point 1: "))
y1 = float(input("Enter y-coordinate for Point 1: "))
x2 = float(input("Enter x-coordinate for Point 2: "))
y2 = float(input("Enter y-coordinate for Point 2: "))

# Compute the distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Set up the Turtle graphics window
turtle.setup(width=600, height=400)  # Adjust width and height as needed

# Display two points and the connecting line
turtle.speed(1)  # Slow down the drawing speed
turtle.penup()
turtle.goto(x1, y1)  # Move to (x1, y1)
turtle.pendown()
turtle.write("Point 1", font=("Times", 12))
turtle.goto(x2, y2)  # Draw a line to (x2, y2)
turtle.write("Point 2", font=("Times", 12))
turtle.penup()
turtle.goto((x2 + x1) / 2, (y2 + y1) / 2)
turtle.write(distance, font=("Times", 12))
turtle.done()
