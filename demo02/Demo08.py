# python
# Demo08
# 2023/2/26
# @author:你大锅
name = '张三'
age = 20
print(type(name),type(age)) # 说明name与age的数据类型不同

#print('我叫'+name + '今年，' + age + '岁' )# 当将str类型进行连接时，报错解决方案，类型转换
print('我叫'+name + '今年，' + str(age) + '岁' )
# str() 将其他类型，转化成str类型
a= 10
b = 23.4
c = False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

# int() 将其他类型，转化成int类型
s1 = '123'
s2 = 34.3
ff = True
s4 = '23.2'
s3 = 'hello'
print(type(s1),type(s2),type(s3),type(ff),type(s4))
print(int(s1),type(int(s1))) #将str转成int类型，字符串为数字
print(int(s2),type(int(s2))) #将float转成int类型，截取整数部分，舍去小数部分
#print(int(s4),type(int(s4)))# 将str转换为int类型，报错，因为字符串为小数串

print(int(ff) ,type(int(ff)))
#print(int(s3) ,type(int(s3)))#将str转换为int类型时，字符串必须为整数串，非数字串不允许转换


# float()函数，将其他类型转成float类型

s1 = '128.9'
s2 = '76'
ff = True
s3 = 'hello'
i = 98
print(type(s1),type(s2),type(ff),type(s3),type(i))
print(float(s1),type(float(s1)))
print(float(s2),type(float(s2)))
#print(float(s3),type(float(s3)))#字符串中的数据如果是非数字串，则不允许转换
print(float(ff),type(float(ff)))
print(float(i),type(float(i)))

