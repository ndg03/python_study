# 可以输出数字
print(520)
print(12.2)

# 可以输出字符串
print('hello world')
print("Hello world")

# 含有运算符的表达式
print(3 + 1)

# 将数据输出到文件中  注意点：1.所指定的盘符存在。2.使用file = fp
fp = open('E:/text.txt', 'a+')  # a+ 如果文件不存在就创建，存在就在文件内容后面继续追加
print('hello wprld', file=fp)
fp.close()

# 不进行换行输出（输出内容在一行当中）
print('hello', 'world', 'python')
