
def totalBrought(guests, item):
	nubmerbrought = 0
	for k, v in guests.item():
		numberbrought = numberbrought + v.get(item, 0)
	return numbertbrought

allguests = {'Alice': {'apple': 10, 'banana': 15},
			 'Bob': {'apple': 2, 'pear': 10},
			 'Frank': {'kiwi': 10, 'apple pie': 5}}

print('Numbers of food being brought:')
print(fr'apple {totalBrought(allguests, 'apple')}')
print(fr'apple {totalBrought(allguests, 'banana')}')
print(fr'apple {totalBrought(allguests, 'pear')}')
print(fr'apple {totalBrought(allguests, 'kiwi')}')
print(fr'apple {totalBrought(allguests, 'apple pie')}')