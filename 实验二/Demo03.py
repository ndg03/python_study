# 所在包    python
# 项目名称  Demo03
# 日期     2023/3/9/ 14:47
# 作者     你大锅
for i in range(101):
    for j in range(101):
        for k in range(101):
            if (i + j + k == 100) & (5 * i + 3 * j + 1.0 / 3 * k == 100):
                print("公鸡{}只\t".format(i), end="")
                print("母鸡{}只\t".format(j), end="")
                print("小鸡{}只\t".format(k), end="")
                print()
