bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[0].title())


message = f"My first bicyle  was a {bicycles[-1].title()}."

# print(message)


#added elements to the list
bicycles.append("awesome")


#inserting items into the list
bicycles.insert(0, "brilliant")
bicycles.insert(3, "splendid")


#removing element form list using del
del bicycles[3]

#pop allows you to remove and use the item
#pop removes items for the end of the list

poped_item = bicycles.pop()

for i in range(len(bicycles)-1):
    print(bicycles[i].title())



print("Popped:", poped_item)

for i in range(len(bicycles)-1):
    print(bicycles[i].title())

#popping items from any position in a list
first_owned = bicycles.pop(0)
print(f"The first bicycle was {first_owned.title()}")

#removing item by value
bicycles.remove('redline')
print(".......removing item by value........")
for i in range(len(bicycles)-1):
    print(bicycles[i].title())



cars = ['bmw', 'audi', 'toyota', 'subaru']
# sort method chages the order of the list permanently. 
cars.sort()
print(cars)


cars = ['bmw', 'audi', 'toyota', 'subaru']
#sort the list in reverse order
cars.sort(reverse=True)
print(cars)

#To sort temporily use sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(sorted(cars))
print("Here is the original list again:")
print(cars)


#using range to  make a listeven numbers 
even_numbers = list(range(2, 11, 2))
print("list of even numbers")
print(even_numbers)


#list of squares
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)


#simple stats with digits 
digits = [1,2,3,4,5,6,7,8,9,0]
print("min:", min(digits))

print("max:", max(digits))

print("sum:", sum(digits))


#list comprehension
squares2 = [x ** 2 for x in range(1, 11)]
print(squares2)


#for loop to print the number  1 to 20
for x in range(1, 21):
    print(x)


#one million
one_million = [x for x in range(1, 1000000 + 1)]
for y in one_million:
    print(y)