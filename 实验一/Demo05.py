# 所在包    python
# 项目名称  Demo05
# 日期     2023/2/28/ 11:00
# 作者     你大锅
import time
import turtle
t = turtle.Turtle()
t.pensize(1)
t.pencolor("red")
t.fillcolor("red")

t.begin_fill()

for i in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()
time.sleep(5)
t.penup()
