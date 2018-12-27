cats = []
while True:
    name = input("enter cat's name: ")
    if name == '':
        break
    # cat = cat.extend([name])
    # cat = cat.append(name)
    # cats.extend([name])
    cats.append(name)
    # cats = cats + [name]

for name in cats:
    print(name)
print(cats)
