# #定义一个函数“cheese_and_crackers", 这个函数有两个参数。
def cheese_and_crackers(cheese_count, boxes_of_crackers):
     print(f'You have {cheese_count} cheese!')
     print(f'You have {boxes_of_crackers} boxes of crackers!')
     print('Man that\'s enough for a party!')
     print('Get a blanket. \n')

# #使用整数传值到这个函数
# print('We can just give the function numbers directly:')
# cheese_and_crackers(20, 30)

# #使用变量传值给这个函数
# print('Or, we can use variable from our script:')
# amount_of_cheese = 10
# amount_of_crackers = 50

# cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# #函数的参数可以是表达式
# print('We can even do math inside too:')
# cheese_and_crackers(10 + 20, 5 + 6)

# #函数的参数可以是变量加上表达式
# print('And we can combine the two, variables and math:')
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#用户输入变量值
amount_of_cheese = input('请输入cheese的数量：')
amount_of_crackers = input('请输入饼干的数量：')

cheese_and_crackers(int(amount_of_cheese), int(amount_of_crackers))