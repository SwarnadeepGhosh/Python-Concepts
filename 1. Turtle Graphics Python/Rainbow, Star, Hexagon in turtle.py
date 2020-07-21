import turtle
rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle.bgcolor("#000000")
turtle.title('Rainbow Star, Hexagon')
hexa = turtle.Turtle()
hexa.speed(0)

hexa.width(5)
hexa.penup()
hexa.back(150)

# coloured hexagon
for i in rainbow:
    hexa.color(i)
    hexa.pendown()
    hexa.forward(50)
    hexa.right(60)

#moving to draw the first star
hexa.left(90)
hexa.penup()
hexa.forward(50)    
hexa.width(2)
for i in rainbow:
    hexa.pendown()
    hexa.color(i)
    #take a colour and make a 8 sided star every time
    for j in range(8):
        hexa.forward(50)
        hexa.right(135)
    #going forward to draw a new star
    hexa.penup()
    hexa.right(45)
    hexa.forward(90)
    
    

    
      
