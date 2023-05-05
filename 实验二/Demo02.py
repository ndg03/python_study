# 所在包    python
# 项目名称  Demo02
# 日期     2023/3/9/ 14:36
# 作者     你大锅
for i in range(1, 10):
    for j in range(1, i + 1):
        print("{} * {} = {}\t".format(j, i, i * j), end="")
    print()
