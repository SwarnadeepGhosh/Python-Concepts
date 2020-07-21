import turtle
turtle.bgcolor("#000000")
fred = turtle.Turtle()
fred.color("red")
fred.forward(100)
fred.right(135)
fred.forward(140)
fred.right(135)
fred.forward(100)

fred.penup()
fred.forward(150)
fred.pendown()
for i in range(4):
    fred.forward(100)
    fred.right(90)