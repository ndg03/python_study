# 所在包    python
# 项目名称  Dem02
# 日期     2023/2/28/ 10:14
# 作者     你大锅
def age(n):  #n代表是第几个人，从5开始
    if n==1:
        return 10
    else :
        return age(n-1)+2
print(age(5))