import turtle
import sys

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):
        t.left(90)
        t.forward(sz)
        
def blueSquareSpiral():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()
    alex.color("blue")
    size = 100
    for i in range(40):
       drawSquare(alex,size)
       alex.right(15)
          

blueSquareSpiral()