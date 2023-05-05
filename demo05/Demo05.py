# 所在包    python
# 项目名称  Democrats
# 日期     2023/3/1/ 21:32
# 作者     你大锅
# 切片操作
lst=[10,20,30,40,50,60,70,80]
print(lst[1:6:1])
print("原列表",id(lst))

lst2=lst[1:6:1]
print("切片后",id(lst2))  # id 发生了改变
print(lst[1:6])  # 默认步长为1
print(lst[1:6:])
print(lst[1:6:2])
print(lst[:6:2])

# 当step为负数时，
print("原列表",lst[::-1])
print(lst[7::-1])
print(lst[6:0:-2])