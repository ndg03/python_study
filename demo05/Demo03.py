# 所在包    python
# 项目名称  Demo03
# 日期     2023/3/1/ 19:18
# 作者     你大锅
# else  和  for 搭配使用
for item in range(3):
    pwd = input("请输入密码：")
    if (pwd == '123'):
        print("密码正确")
        break
    else:
        print("密码错误")
else:
    print("三次密码均错误")

# else  和while 搭配使用
a = 0
while a < 3:
    pwd = input("请输入密码：")
    if pwd == '123':
        print("密码正确")
        break
    else:
        print("密码错误")
        # 改变变量
        a += 1
else:
    print("三次密码均错误")
