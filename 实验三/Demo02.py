# 所在包    python
# 项目名称  Demo02
# 日期     2023/3/21/ 10:46
# 作者     你大锅
import jieba

# 读取文件内容并转换为字符串形式
with open('西游记.txt', 'r', encoding='ANSI') as f:
    content = f.read()
# 使用jieba分词对文本进行处理，并返回一个生成器对象
words = jieba.lcut(content)
# 定义角色字典，用于存储每个角色的出场次数
roles = {'唐僧': 0, '悟空': 0, '猪八戒': 0, '沙僧': 0}
# 遍历分词结果并统计各个角色的出场次数
for word in words:
    if word == '唐僧' or word == "师父" or word == "三藏" or word == "圣僧" or word == "御弟":
        roles['唐僧'] += 1
    elif word == "大圣" or word == "老孙" or word == "行者" or word == "孙大圣" or word == "孙行者" or word == "猴王" or word == "悟空" or word == "齐天大圣" or word == "猴子":
        roles['悟空'] += 1
    elif word == '猪八戒' or word == "呆子" or word == "八戒" or word == "老猪":
        roles['猪八戒'] += 1
    elif word == '沙僧' or word == "沙和尚":
        roles['沙僧'] += 1
# 对角色字典按值（即出场次数）排序，并返回一个元组列表
sorted_roles = sorted(roles.items(), key=lambda x: x[1], reverse=True)
print("《西游记》人物出场统计：")
for role in sorted_roles:
    print(role[0], ":", role[1])
