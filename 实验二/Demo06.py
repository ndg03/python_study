# 所在包    python
# 项目名称  Demo06
# 日期     2023/3/9/ 15:57
# 作者     你大锅
import math
def isWoter(i):
    a = i // 100
    b = (i // 10) % 10
    c = i % 10
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)
    else:
        return False


for i in range(100, 1000):
    isWoter(i)
