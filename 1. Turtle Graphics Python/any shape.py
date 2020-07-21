import turtle
turtle.bgcolor('black')
shape=turtle.Turtle()

def anyshape(side_no, shape_color, shape_length):
    shape.color(shape_color)
    for i in range(side_no):
        shape.forward(shape_length)
        shape.right(360/side_no)

anyshape(6,'blue',100)