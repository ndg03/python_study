# 所在包    python
# 项目名称  Demo02
# 日期     2023/3/1/ 19:07
# 作者     你大锅
# for in   循环
for item in "ndg": # 自定义变量 item  将取出来的赋值给item
    print(item)

# range() 产生一个整数序列，也是一个可迭代对象
for i in range(10):
    print(i)

# 如果在循环体中不需要用到自定义变量，可以用 “_” 代替
for _ in range(5):
    print("人生苦短，我学python")  # 会打印5次


