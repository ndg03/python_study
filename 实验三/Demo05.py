# 三国演义 人物出场统计升级版
import jieba

excludes = {"将军", "却说", "不可", "二人", "军士", "天下", "主公", "商议", "徐州", "不能", "如何", "左右", "先生",
            "次日", "如此", "江东", "百姓", "军马", "今日", "不知", "一人", "荆州", "大叫", "不敢", "上马", "大喜"}
txt = open("三国演义.txt", "r", encoding='ANSI').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:  # 排除单个字符的分词结果
        continue
    elif word == "诸葛亮" or word == "孔明曰" or word == "卧龙先生":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "翼德":
        rword = "张飞"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
for word in excludes:
    del (counts[word])
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(13):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
