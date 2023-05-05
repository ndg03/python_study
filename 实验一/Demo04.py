# 所在包    python
# 项目名称  Demo04
# 日期     2023/2/28/ 10:46
# 作者     你大锅
def change():

    print("欢迎进入汇率计算器：")
    # print("请选择服务项目：")
    print("1.美元 -->  人民币")
    print("2.人名币 -->  美元")
    n = int(input("请选择服务项目："))
    # m = float(input("请输入金额"))
    a1 = 6.8833
    a2 = 0.1452
    money = float(input("请输入金额："))
    if n == 1:
        print(money * a1)
    else:
        print(money * a2)


while True:
    change()
