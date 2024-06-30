"""
A person invest $1000 in a savings account yielding 5% interest. Assumming tht the person leaves all interst on depoist in the accont, calculate 
and display the amount of money in the account at the end of each year for 10 yars. formular ''   a = p(1 + r)**n


"""

principal = 1000
rate = 5/100

for year in range(1, 11):
    if year == 5:
        continue
    amount = principal * (1 + rate) ** year
    print(f'{year:>2} {amount:>10.2f}')
  




