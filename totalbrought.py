allGuests = {'Alice': {'apple': 3, 'pear': 10},
             'Bob': {'banana': 10, 'cracker': 20, 'apple': 30},
             'Carol': {'cup': 30, 'apple pies': 15}}


def totalBrought(guests, item):
    numbrought = 0
    for k, v in guests.items():
        numbrought = numbrought + v.get(item, 0)
    return numbrought


print('Number of things being brought:')
print(f"apples {totalBrought(allGuests, 'apple')}")
print(f"banana {totalBrought(allGuests, 'banana')}")
print(f"apple pies {totalBrought(allGuests, 'apple pies')}")
print(f"cup {totalBrought(allGuests, 'cup')}")
