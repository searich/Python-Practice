birthday = {'Alice': 'Apri 1', 'Ben': 'Nov 27', 'Frank': 'Juen 8'}

while True:
    print('Enter the name: (blank to quit)')
    name = input()
    if name == '':
        break

    elif name in birthday.keys():
        print(f"{name}'s birthday is on {birthday[name]}.")
    else:
        print('Failed. We have no such name.')
        print('What is their birthday?')

        add_birthday = input()
        birthday[name] = add_birthday
        print('Birthday data was updated!')
