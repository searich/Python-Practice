the_count = [1, 2, 3, 4, 5]
fruits = ['Apple', 'Oranges', 'Pears', 'Apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for i in change:
    if type(i) != int:
        print(f"I got {i}")

elements = [[],[]]
elements.append(10)

for i in range(0, 6):
    #print(f"Adding {i} to the list.")
    elements.append(i)
print(elements)

#for i in elements:
#    print(f"Element was: {i}")