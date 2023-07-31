import random as r
import turtle as t

r.seed(1)
t.pensize(2)
t.pencolor('red')
angles = 6
points = [[0, 0], [50, 40], [70, 80], [-40, 30]]

for i in range(4):
    x0, y0 = points[i]
    t.penup()
    t.goto(x0, y0)
    t.pendown()

    length = r.randint(6, 16)
    for j in range(angles):
        t.fd(length)
        t.bk(length)
        t.right(360 / angles)
t.done()
