#从系统调用argv模块
from sys import argv

script, input_file = argv

#创建一个打印文件对象的函数
def print_all(f):
    print(f.read())

# 光标移到第0字节（文件开头）
def rewind(f):
    f.seek(0)

#创建一个打印一行对象的函数
def print_a_line(line_count, f):
    print(line_count, f.readline(), end='')

#打开文件，赋值给变量“current_file"
current_file = open(input_file)

# 调用打印文件对象函数
print('First let\'s print the whole file:\n')
print_all(current_file)

# 把光标移到文件开头
print('Now, let\'s rewind, kind of like a tape')
rewind(current_file)

# # 调用打印当前行函数打印当前行
# current_line = 1
# print_a_line(current_line, current_file)

# # 打印下一行
# current_line += 1
# print_a_line(current_line, current_file)

# # 打印下一行 
# current_line += 1
# print_a_line(current_line, current_file)

# 用while循环打印前三行
i = 0
while i < 3:
    print_a_line(i,current_file)
    i += 1