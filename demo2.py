# a = 0
# b = 10
# while a < b:
#     a += 1
#     if a % 2 != 0:
#         continue
#     print(a, end=' ')


# a = 0
# b = 10
# while a < b:
#     a += 1
#     if a == 5:
#         break
#     print(a, end=' ')


# y = 29
# x = y // 2
# while x > 1:
#     if y % x == 0:
#         print(f'{y} has a factory {x}')
# #        print('{} has a factory {}'.format(y, x))
#         break
#     x -= 1
# else:
#     print(f'{y} is prime')


# D = {'a': 1, 'b': 2, 'c': 3}
# for (key, value) in D.items():
#     print(key, '---->', value)


# for key in D:
#     print(key, '---->', D[key])


# file = open('demo3.txt', 'r')
# print(file.read())

# for line in open('demo3.txt', 'r'):
#     print(line, end=' ')


# print(list(range(-5, 5)))


# s = 'abcdefghijklmn'
# for i in range(0, len(s), 2):
#    print(s[i], end=' ')

# for k in s[::3]:
#     print(k, end=' ')

keys = ['A', 'B', 'C']
values = [1, 2, 3, 4]
D = dict(zip(keys, values))
L = list(zip(keys, values))

print(D)
print(L)


print([x[1] for x in L])
