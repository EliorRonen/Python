import turtle
turtle.Screen().bgcolor("cyan")
turtle.Screen().setup(300,400)
polygan = turtle.Turtle()
l = 70
ns = 6
angle = 60
for i in range(ns):
    polygan.forward(l)
    polygan.right(angle)

turtle.done()