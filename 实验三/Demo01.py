# 所在包    python
# 项目名称  Demo01
# 日期     2023/3/21/ 10:43
# 作者     你大锅
import random

# 生成包含大写字符、小写字母或数字的所有可选字符列表
chars = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
# 定义一个空列表用于存储每次生成的随机字符
code = []
# 循环生成6个随机字符并添加到code列表中
for i in range(6):
    code.append(random.choice(chars))
# 将code列表转换为字符串形式输出验证码结果
result = ''.join(code)  # 使用字符串方法`.join()`将整个验证码序列拼接成字符串
print("Your verification code is: ", result)
