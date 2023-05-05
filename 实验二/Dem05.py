# 所在包    python
# 项目名称  Dem05
# 日期     2023/3/9/ 15:31
# 作者     你大锅
def isSu(i):
    for j in range(2, i):
        if i % j == 0:
            return False
        else:
            continue
    return True


def isBack(i):
    j = str(i)
    j = j[::-1]
    k = int(j)
    if i == k:
        return True
    else:
        return False


for i in range(2, 1001):
    if isSu(i) & isBack(i):
        print(i)
