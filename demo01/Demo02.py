# 转义字符
print('Hello\nWorld')  # \ + 转义功能的首字母   n--> newline 表示换行
print('hello\tworld')
print('helloooo\tworld')
print('hello\rworld')  # \r是回车，world将hello 进行了覆盖
print('hello\bworld')  # \b是退格，将o退没了

print('http:\\\\www.baidu.com')
print('老师说：\'大家好\'')

# 原字符，不希望字符串中的转义符起作用，就使用原字符，就是在字符串之气加上r，或者R
print(r'hello\nworld')  # 有了r  ，\n  不起作用了
# 注意事项，最后一个字符不能是反斜杠
# print(r'hello\nworld\')
print(r'hello\nworld\\')
