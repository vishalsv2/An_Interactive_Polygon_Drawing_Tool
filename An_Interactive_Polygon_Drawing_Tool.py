from turtle import Turtle,Screen
tim=Turtle()
tim.pensize(2.5)
def line():
    tim.forward(100)

def tri():
    for _ in range(3):
        tim.right(120)
        line()
        tim.color("green")

def square():
    for _ in range(4):
        line()
        tim.color("black")
        tim.right(90)

def pentagon():
    for _ in range(5):
        line()
        tim.color("red")
        tim.right(72)

def hexagon():
        for _ in range(6):
            line()
            tim.color("blue")
            tim.right(60)
    
def heptagon():
        for _ in range(7):
            line()
            tim.color("peru")
            tim.right(51.42)

def octagon():
        for _ in range(8):
            line()
            tim.color("orange red")
            tim.right(45)

def nanogon():
        for _ in range(9):
            line()
            tim.color("magenta")
            tim.right(40)

def decagon():
        for _ in range(10):
            line()
            tim.color("indigo")
            tim.right(36)
    
square()
line()
tri()
tim.backward(100)
pentagon()
hexagon()
heptagon()
octagon()
nanogon()
decagon()

screen=Screen()
screen.exitonclick()

