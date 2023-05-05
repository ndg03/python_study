# 所在包    python
# 项目名称  Demo07
# 日期     2023/3/9/ 15:49
# 作者     你大锅
sales = int(input("请输入员工的销售额"))
salary = 2000
if sales <= 3000:
    salary += 0
elif sales <= 7000:
    salary += sales * 0.1
elif sales <= 10000:
    salary += sales * 0.15
else:
    salary += sales * 0.2
print("薪水为{}".format(salary))
