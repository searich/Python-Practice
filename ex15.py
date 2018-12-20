#调用系统argv模块
from sys import argv

#设定两个变量给系统argv模块
script, filename = argv

#创建一个txt文件对象
txt = open(filename)
print(type(txt))

print(f'Here is your file {filename}:')
#读取该文件的文本内容
print(txt.read())
txt.close()

print('Type the filename again:')
file_again = input('>')

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()

# filename = input('>')
# txt = open(filename)
# print(txt.readlines())
# txt.close()
