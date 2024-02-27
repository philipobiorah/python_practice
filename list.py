bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[0].title())


message = f"My first bicyle  was a {bicycles[-1].title()}."

# print(message)


#added elements to the list
bicycles.append("awesome")


#inserting items into the list

for i in range(len(bicycles)-1):
    print(bicycles[i].title())