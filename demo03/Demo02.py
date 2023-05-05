# 所在包    python
# 项目名称  Demo02
# 日期     2023/2/26
# 作者     你大锅

#从键盘输入两个整数，计算两个整数的和
a = int(input('请输入一个加数：'))  #可以在输入的时候直接进行类型转换
a= int(a) #类型转换，str-->int
b = input('请输入另一个加数：')
b= int(b)
print(type(a),type(b))
print(a+ b)#起连接作用