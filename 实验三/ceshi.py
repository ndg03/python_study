# # 所在包    python
# # 项目名称  ceshi
# # 日期     2023/3/21/ 11:21
# # 作者     你大锅
# print("三国演义人物出场次数：")
# import jieba
#
# txt = open("三国演义.txt", "r", encoding="ANSI").read()
# excludes = {"将军", "却说", "二人", "后主", "上马", "不知", "天子", "大叫", "众将", "不可",
#             "主公", "只见", "如何", "商议", "都督", "一人", "汉中", "不敢", "人马",
#             "陛下", "天下", "今日", "左右", "东吴", "于是", "荆州", "不能", "如此",
#             "大喜", "引兵", "次日", "军士", "军马"}
# words = jieba.lcut(txt)
# counts = {}
# for word in words:
#     if len(word) == 1:
#         continue
#     elif word == "诸葛亮" or word == "孔明曰":
#         rword = "孔明"
#     elif word == "关公" or word == "云长":
#         rword = "关羽"
#     elif word == "玄德" or word == "玄德曰":
#         rword = "刘备"
#     elif word == "孟德" or word == "丞相":
#         rword = "曹操"
#     else:
#         rword = word
#     counts[rword] = counts.get(rword, 0) + 1
# for word in excludes:
#     del counts[word]
# items = list(counts.items())
# items.sort(key=lambda x: x[1], reverse=True)
# for i in range(10):
#     word, count = items[i]
#     print("{0:<10}{1:>5}次".format(word, count))

# import numpy as np
# print(np.empty((2, 3)))

import math

n = float(input("请输入"))
print(math.modf(n))
print(round(n,2))