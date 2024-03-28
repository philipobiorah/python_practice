# A program that obtains minutes and remaining seconds from an amount of time in seconds. 
## eg. 500 seconds contian 8 mins and 20 second.

MIN = 60
sec_val = int(input("Enter value of seconds:"))
print(f"{sec_val} seconds")
print(f"{int(sec_val/MIN)} minutes : {int(sec_val%MIN)} seconds")

