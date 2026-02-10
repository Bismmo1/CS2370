import turtle
import time
import math

screen = turtle.Screen() #provides a canvas to draw on

screen.title("ocg1020_Lab3: CS2370") # changes window name

screen.bgcolor("gray") #changes background color

t1 = turtle.Turtle() #create a turtle "object"


##Part 1
## Create shape functions
def rectangle(t, length):
    height = length / 2
    for i in range(2):
        t.fd(length)
        t.lt(90)
        t.fd(height)
        t.lt(90)
    
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        
def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, n, length)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
        
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        
##Part 2
def setTurtle(t, x, y, angle):
    t.pu()
    t.goto(x, y)
    t.lt(angle)
    t.pd()

def addTo(t, x, y, angle):
    t.pu()
    t.pos(a, b)
    t.goto(x+a, y+b)
    t.lt(angle)
    t.pd()

def door(t, width, height):
    for i in range(2):
        t.fd(width)
        t.lt(90)
        t.fd(height)
        t.lt(90)
def window(t, size):
    circle(t, size)
    t.lt(90)
    t.fd(size*2)
    t.backward(size)
    t.lt(90)
    t.backward(size)
    t.fd(size*2)
    t.lt(180)
    
def olympic(t, size):
    setTurtle(t, size-20, size-20, 0)
    t.color('blue')
    circle(t, size)
    setTurtle(t, 150, 20, 0)
    t.color('brown')
    circle(t, size)
    setTurtle(t, 200, 100, 0)
    t.color('black')
    circle(t, size)
    setTurtle(t, 250, 20, 0)
    t.color('green')
    circle(t, size)
    setTurtle(t, 300, 100, 0)
    t.color('red')
    circle(t, size)

def main():
    #Part 3
    setTurtle(t1, -200, 100, 0)
    rectangle(t1, 200)
    #Part 4
    setTurtle(t1, -200, 200, 0)
    polygon(t1, 3, 200)
    #Part 5
    #Door
    setTurtle(t1, -110, 100, 0)
    door(t1, 25, 50)
    #window 1
    setTurtle(t1, -170, 150, 0)
    window(t1, 20)
    #window 2
    setTurtle(t1, -30, 150, 0)
    window(t1, 20)

    #Part 6
    olympic(t1, 60)
    """
    #Part 1
    for i in range(3, 9): 
        polygon(t1, i, 50)
    circle(t1, 50)
    arc(t1, 100, 180)
    polyline(t1, 50, 50, 50)"""


if __name__ == "__main__":
    main()
