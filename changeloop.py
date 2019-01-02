# 可变循环
# num_stars = int(input('How many stars do you want?'))
# for i in range(num_stars):
#     print('*')

import time

start = int(input('Enter start time: '))
for i in range(start, 0, -1):
    print(i)
    time.sleep(1)
print('Game over!')
