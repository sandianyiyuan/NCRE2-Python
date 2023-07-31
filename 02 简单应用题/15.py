import random as r
import turtle as t

color = ['red', 'orange', 'blue', 'green', 'purple']
r.seed(1)
for i in range(5):
    rad = r.randint(20, 50)
    x0 = r.randint(-100, 100)
    y0 = r.randint(-100, 100)
    t.color(r.choice(color))
    t.penup()
    t.goto(x0, y0)
    t.pendown()
    t.circle(rad)
t.done()
