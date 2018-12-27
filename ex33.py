# i = 0
# numbers = []

# while i < 6:
#     print(f'At the top i is {i}')
#     numbers.append(i)

#     i += 1
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")


# print("The numbers: ")

# for num in numbers:
#     print(num)


def numberlist(x, y, z):
    list = []

    for i in range(x, y, z):
        list.append(i)
    return list


i = 0

while i < 6:
    b = i + 1
    print(f"At the top y is {i}")
    print(f"Numbers now:", numberlist(0, i+1, 1))
    print(f"At the bottom i is {b}")
    i += 1
