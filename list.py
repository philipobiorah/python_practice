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