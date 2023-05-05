# 所在包    python
# 项目名称  Demo02
# 日期     2023/2/26/ 22:33
# 作者     你大锅0

# 单分支结构
money = 1000  # 余额
s = int(input("请输入取款金额："))

# 判断余额是否充足
if money >= s:
    money -= s
    print("取款成功！")
