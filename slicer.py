def trim(s):
    # 初始化切片索引
    start = 0
    end = len(s)
    # 得到左边第一个非空格字符的索引
    for i in s:
        if i == " ":
            start += 1
        else:
            break
    # 得到右边第一个非空格字符的索引
    for j in s[::-1]:
        if j == " ":
            end -= 1
        else:
            break
    # 处理s
    s = s[start:end]
    # 返回
    return s
print(trim('  hello    '))