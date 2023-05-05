# 所在包    python
# 项目名称  Demo04
# 日期     2023/3/21/ 11:10
# 作者     你大锅
import random
# 使用集合存储已经生成过的数字
used_nums = set()
# 循环随机生成数字并加入集合中，直到集合大小为5时停止循环
while len(used_nums) < 5:
    num = random.randint(0, 10)
    if num not in used_nums:
        used_nums.add(num)
# 将集合转换成列表形式输出结果
result = list(used_nums)
print(result)