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
    current_x = t.xcor()
    current_y = t.ycor()
    
    t.goto(current_x + x, current_y + y)
    
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
     t.fd(size)
     t.lt(90)
     
     
def roof(t, size):
     t.fd(size)
     t.lt(135)
     t.fd(size * .707)
     t.lt(90)
     t.fd(size * .707)
     t.lt(135)


    
def olympic(t, size):
    top = (size/1.5)
    addTo(t1, size, size, 0)
    t.color('blue')
    circle(t, size)
    addTo(t1, size, size*-1.5, 0)
    t.color('yellow')
    circle(t, size)
    addTo(t1, top, size*1.5, 0)
    t.color('black')
    circle(t, size)
    addTo(t1, size, size*-1.5, 0)
    t.color('green')
    circle(t, size)
    addTo(t1, top, size*1.5, 0)
    t.color('red')
    circle(t, size)

def house(t, size):
    t.color("black")
    rectangle(t, size)
    addTo(t, 0, size/2, 0)
    roof(t, size)
    addTo(t, size/2.25, -size/2, 0)
    door(t, size/8, size/4)
    addTo(t, -size/5, size/5, 0)
    window(t, size/15)
    addTo(t, size*0.60 , 0, 0)
    window(t, size/15)
    t.lt(180)

def box(t, size):
    t.color("black")
    t.fd(size)
    t.lt(60)
    t.fd(size/3)
    t.lt(30)
    t.fd(size/2)
    t.lt(90)
    t.fd(size)
    t.lt(60)
    t.fd(size/3)
    t.lt(30)
    t.fd(size/2)
    t.lt(150)
    t.fd(size/3)
    t.lt(30)
    t.fd(size/2)
    t.backward(size/2)
    t.rt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size/2)
    t.lt(150)
    t.fd(size/3)
    t.lt(30)
    t.fd(size/2)
    t.backward(size/2)
    t.rt(90)
    t.fd(size)
    t.pu()
    t.goto(0,0)
    t.lt(180)
    t.pd()

def main():
    olympic(t1, 50)
    setTurtle(t1, 200, -100, 0)
    olympic(t1, 25)
    setTurtle(t1, -250, 100, 0)
    house(t1, 200)

    setTurtle(t1, -250, -100, 0)
    house(t1, 150)
    
    
    #Part 1
    setTurtle(t1, 250, 200, 0)
    addTo(t1, 100, 100, 0)
    for i in range(3, 9): 
        polygon(t1, i, 50)
    setTurtle(t1, 100, 200, 0)
    addTo(t1, 100, 100, 0)
    for i in range(3, 9): 
        polygon(t1, i, 25)
    
    setTurtle(t1, -300, -300, 0)
    box(t1, 200)
    setTurtle(t1, 100, -300, 00)
    box(t1, 100)
    
        
    


if __name__ == "__main__":
    main()
