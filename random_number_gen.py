import random 


#random.seed(32)
for roll in range(10):
    print(random.randrange(1,7), end= ' ')

print()


for i in range(20):
    print('H' if random.randrange(2) == 0 else 'T', end= ' ')