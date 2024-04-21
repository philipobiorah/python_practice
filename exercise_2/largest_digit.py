"""
A program that prompts the user to enteer a 
four digit integer ande displays the freatest digit among the four digits

"""

digit = int(input("Enter four-digit integer: "))

largest = 0
while digit > 0:
    last =  digit % 10
    digit = digit // 10
    temp = last

    if temp > largest:
        largest = last

    
  
    
    print(f"rem_digit: {digit} : last {last}")

print(f"largest: {largest}")