"""
A program that 
displays the sales tax with two digits after the decimal point
eg: purchaseamount : 197.55. The sales tax is 6% of the purchase, tax 
is evaluated as 11.853
"""

#Prompt the user for input
purchaseAmount = float(input("Enter purchase amount: "))


#compute sales tax
tax = purchaseAmount * 0.06
print(tax)
#Display tax amount with two digits after decimal point
print("Sales tax is", int(tax * 100) / 100.0)