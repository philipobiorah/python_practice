import turtle

#Prompt the user for inputing two points

x1 = float(input("Enter x-coordinate for  Point 1: "))
y1 = float(input("Enter y-coordinate for Point 2:  "))
x2 = float(input("enter x-coordinate for Point 2: "))
y2 = float(input("Enter y-coordinate for Point 2: "))


#Compute the distance
distance = ((x2 - x1)**2 +(y2 - y1)**2)**5

#Display two points and the connecting line
turtle.penup()
turtle.goto(x1, y1)  # Move to (x1, y1)
turtle.pendown()
turtle.write("Point 1", font=("Times", 12))