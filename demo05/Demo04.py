# 所在包    python
# 项目名称  Demo04
# 日期     2023/3/1/ 19:31
# 作者     你大锅
# 列表
a = 10  # 变量
lst = ["hello", "world", 123]
print(id(lst))
print(type(lst))
print(lst)

# 列表的创建
"""使用[]"""
lst1 = ["hello", "world", 123, 'hello']
"""使用 内置函数list（）"""
lst2 = list(["hello", "world", 123])
print(lst2)
"""1.有序排列
2.索引从0  开始  /   右到左   -1开始
3.可以存储重复数据
4.任意数据类型混存
5.动态分配回收内存"""

# index() 方法获取索引
print(lst.index("hello"))  # 如果列表当中含有相同元素，只访问列表中第一个元素
print(lst[-1])

# 可以在指定的范围内进行查找
# print(lst.index("hello",1,3))  # 在1-3之间查找 hello   报错：ValueError: 'hello' is not in list，不存在
print(lst.index("hello", 1, 4))

