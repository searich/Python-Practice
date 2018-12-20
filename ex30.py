people = 30
cars = 10
trucks = 15 


if cars > people and cars > trucks:
    print('We should take the cars.')
elif cars < people and cars < trucks:
    print('We should not take the cars.')
else:
    print('We cant\'t decide.')


if trucks > cars:
    print('That is too many trucks.')
elif trucks < cars:
    print('Maybe we could take the trucks.')
else:
    print('We stll can\'t decide.')

if people > trucks:
    print('Alright, let\'s just take the trucks.')
else:
    print('Fine, let\'s stay home then.')