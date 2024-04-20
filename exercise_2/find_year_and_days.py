"""
A program that prompts the user to enter the minutes(eg. 1 billon) and displays
the number of years and days for the ninutes. For simplicity , assume a year has 365
"""

min = int(input("Enter the number of minutes: "))


years = min//(60*24*365)


rem_mins = min % (60*24*365)

days = rem_mins // (60*24)

print(f"{min } minutes is approximately {years} years and {days} days" )