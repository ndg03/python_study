# 所在包    python
# 项目名称  Demo01
# 日期     2023/3/1/ 13:00
# 作者     你大锅
# range()  函数三种使用方式

"""第一种方式，只有一个参数，"""
r = range(10)  # 默认步长为1
print(r)
print(list(r))  # list用于查看整数序列，list是列表的意思

"""第二种创建方式，有两个参数"""
r = range(1,10)  # 指定了起始值，从1开始，到9结束，默认步长为1
print(list(r))

"""第三种创建方式，给三个参数，"""
r = range(1,10,2)  # 步长为2
print(list(r))  # [1,3,5,7,9]

print(10 in list(r))
print(9 not in list(r))