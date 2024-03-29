"""
A program that breaks a large amount of money into smaller units
 Cents come in coins. 
   these coins are called 
   a quarter (25 cents), 
   a dime (10 cents), 
   a nickel (5 cents) 
   and a penny (1 cent).

"""
#prompt the user to enter amount as a decimal number such as 11.56
user_input = float(input("Enter money in cents: "))
#convert the amount into cents
input_cents = user_input * 100
print(f"{input_cents} cents")

dollars = int(input_cents//100)
print(f"{dollars}  : dollars")

change = input_cents % 100
print(f"{change} : cents remaining")
    


