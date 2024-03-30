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
print(f"{user_input} consists of : ")
print(f"{dollars}  - dollars")

change = input_cents % 100
while change > 4:
        print(f"{int(change)} - cents")

        quarter = int(change / 25)
        print(f"{quarter} - quarters")

        change = change % 25

        dime = int(change / 10)
        print(f"{dime} - dime")

        change = change % 10

        nickels = int(change / 5)
        print(f"{int(nickels)} - nickels")

        change = change % 5
pennies = change
print(f"{int(change)} - pennies")
    


