import turtle

#set up the screen
wn = turtle.Screen()
wn.title("snake game")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"


# Main game loop
while True:
    wn.update()

turtle.mainloop()