# 所在包    python
# 项目名称  Demo06
# 日期     2023/2/26
# 作者     你大锅

#比较运算符
a,b = 10,20
print('a>b吗？',a>b)#False
print('a<b吗？',a<b)#True
print('a>=b吗？',a>=b) #False
print('a<=b吗？',a<=b) #True
print('a==b吗？',a==b) #False
print('a!=b吗？',a!=b) #True

''' 一个  =  称为赋值运算符 ， == 称为比较运算符
    一个变量有三部分组成，标识，类型，值
    == 比较的是值还是标识呢？  比较的是值
    比较对象的标识使用   is 
'''

a=10
b=10
print(a == b) #True
print(a is b) #True  说明标识相同，都指向10的标识

#以下代码没学过  后面讲解
list1=[11,22,33,44]
list2=[11,22,33,44]
print(list1 == list2) #True
print(list1 is list2) #False
print(id(list1))
print(id(list2)) #标识不同

print(a is not b) #False   a的id与b的id的是不相同的？
print(list1 is not list2)  #True
