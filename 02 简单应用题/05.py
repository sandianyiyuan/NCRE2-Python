# 1：
# import turtle as t
# for i in range(8):
#     t.seth(i*45)   # 设置指针相对于x轴的角度
#     t.fd(100)

# 2：
import turtle
turtle.pensize(2)   # 设置线的宽度
d = 0
for i in range(1, 9):
    turtle.fd(100)
    d += 360/8
    turtle.seth(d)
