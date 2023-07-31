import turtle

n = 4
for j in range(n):
    turtle.pendown()
    for i in range(4):
        turtle.fd(40)
        turtle.right(90)
    turtle.penup()
    turtle.fd(80)
turtle.done()
