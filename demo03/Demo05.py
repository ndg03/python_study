# 所在包    python
# 项目名称  Demo05
# 日期     2023/2/26
# 作者     你大锅

#赋值运算符，运算顺序从右到左
i= 3+4
print(i)

a=b=c = 20 # 支持链式赋值
print(a,id(a))
print(b,id(b)) # 三个的标识相同
print(c,id(c))

#支持参数赋值
# +=   -=   *=   /=   //=   %=
a=20
a//=2
print(a ,type(a))


#支持系列解包赋值
a,b,c=20,30,40
print(a,b,c)
#a,b = 10,20,30  报错，因为左右变量的个数和值的个数不对应

a,b = 10,20
print('交换之前：',a,b)
a,b = b,a
print('交换之后：',a,b)
