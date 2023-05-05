# 所在包    python
# 项目名称  Demo06
# 日期     2023/3/1/ 21:48
# 作者     你大锅
# 列表元素的增删改
# 向列表的末尾添加元素
lst = [10, 20, 30]
print("添加元素之前", lst, id(lst))
lst.append(100)
print("添加元素之后", lst, id(lst))
lst2 = ['x', 23]
lst.append(lst2)  # 将lst2作为 元素 (一个整体)添加到列表的末尾
print("添加元素之后", lst, id(lst))
lst.extend(lst2)
print(lst)

# 在指定的位置添加元素
lst.insert(1, 90)
print(lst)

lst3 = [True, False, "hello"]
lst[1:] = lst3  # 把后面的切片
print(lst)

# x = float(input())
# print('{:.3f}'.format(x))

string = input()
print(string[::-1])
