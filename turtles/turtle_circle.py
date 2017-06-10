import turtle

def drawPolygon(t, sideLength, numSides): 
    turnAngle = 360 / numSides 
    for i in range(numSides): 
        t.forward(sideLength) 
        t.right(turnAngle)

def drawCircle(anyTurtle, radius, color): 
    anyTurtle.color(color) 
    anyTurtle.penup() 
    anyTurtle.left(90) 
    anyTurtle.forward(20) 
    anyTurtle.pendown() 
    anyTurtle.begin_fill()
    circumference = 2 * 3.1415 * radius 
    sideLength = circumference / 360 
    drawPolygon(anyTurtle, sideLength, 360) 
    anyTurtle.end_fill() 
    anyTurtle.penup() 
    anyTurtle.right(90) 
    anyTurtle.forward(20)

wn = turtle.Screen() 
wheel = turtle.Turtle()

drawCircle(wheel, 20, "blue")

wn.exitonclick()