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

for i in range(len(bicycles)-1):
    print(bicycles[i].title())