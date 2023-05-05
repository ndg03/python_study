# 所在包    python
# 项目名称  Demo04
# 日期     2023/3/9/ 15:03
# 作者     你大锅
import random


def game():
    suma = 0
    sumb = 0
    for i in range(5):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        suma += a
        sumb += b
        print("第{}局[{},{}]\t".format(i + 1, a, b), end="")
    print()
    if suma > sumb:
        return 1
    else:
        return 2


suma = 0
sumb = 0
for i in range(50):
    print("第{}盘\t".format(i + 1), end="")
    if game() == 1:
        suma += 1
    else:
        sumb += 1
print("a赢了{}盘".format(suma))
print("b赢了{}盘".format(sumb))
if suma > sumb:
    print("所以a获胜")
else:
    print("所以b获胜")
