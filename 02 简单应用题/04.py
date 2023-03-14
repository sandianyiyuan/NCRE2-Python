import turtle as t

for i in range(4):
    t.seth(i*90)   # 设置指针相对于x轴的角度
    t.fd(100)
    t.fd(-100)
