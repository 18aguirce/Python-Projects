# Author: Cesar Vicente
# Date  : May 8, 2019
# this program experiments with turtle graphics
# haha turtle goes weee

import turtle
import random

t = turtle.Pen()
t.shape("turtle")

##t.speed(7) # speed range is 0-10
##
######t.forward(100)
######t.left(90)
######t.forward(100)
######t.left(90)
######t.forward(100)
######t.left(90)
######t.forward(100)
####
####for x in range(3):
####    t.forward(100)
####    t.left(90)
####t.forward(100)
####
####t.up() #Picks the pen up
####t.forward(50)
####t.down() #puts the pen down
####
####for x in range(3):
####    t.forward(100)
####    t.left(90)
####t.forward(100)
##
##t.reset()
##t.speed(0)
##
##t.color("red", "green")
##t.begin_fill()
##for x in range(1, 9):
##    t.forward(100)
##    t.right(135)
##
##t.end_fill()
##
####t.color(0.5, 0, 0.5)
####for x in range(1, 9):
####    t.forward(100)
####    t.right(135)
##
##t.up()
##t.backward(250)
##t.left(90)
##t.forward(250)
##
##t.speed(0)
### Navy Blue
##t.color("#000080")

### Begin Jeep Logo
### Passenger side handlight
##t.down()
##t.begin_fill()
##t.circle(20) #20 is the radius
##t.end_fill()
##
##t.up()
##t.forward(20)
##
### grill slots
##for x in range(1,5):
##    t.right(90)
##    t.forward(20)
##    t.right(90)
##    t.down()
##    t.forward(100)
##    t.up()
##    t.left(90)
##    t.forward(20)
##    t.left(90)
##    if x == 4: break
##    t.down()
##    t.forward(100)
##    t.up()
##
### Driver side headlight
##t.forward(80)
##t.down()
##t.begin_fill()
##t.circle(-20)
##t.end_fill()
##t.up()
### End Jeep Logo
##
##t.speed(0)
##t.hideturtle()
##t.color("blue", "yellow")
##random.seed() #leave () empty to make it random
##
##i = 0
##while i < 30:
##    x = random.randint(-250, 250)
##    y = random.randint(-250, 250)
##    if not (x < 0 and y > 0): #Upper left corner is off limits
##        t.goto(x, y)
##        t.color(random.random(), random.random(), random.random())
##        t.begin_fill()
##        t.circle(random.randint(10, 30))
##        t.end_fill()
##        i += 1

t.speed(0)

def jump(x, y):
    t.up()
    t.goto(x, y)
    t.down()

# spiral
for size in range(15, 150, 2):
    t.forward(size)
    t.right(72)

# triangle inside triangles
t.down()
for size in range(20, 201, 20):
    for x in range(1, 4):
        t.forward(size)
        t.left(120)

jump(100,150)
# Star
for x in range(1, 9):
    t.forward(25)
    t.backward(25)
    t.right(45)
t.left(36)

# triangles
jump(-100,140)
def triangle():
    for x in range(1, 4):
        t.forward(50)
        t.right(120)
def line():
    for x in range(1, 5):
        triangle()
        t.forward(50)
for x in range(1, 3):
    line()
    t.right(60)
    line()
    t.right(120)

t.reset()
t.speed(0)
# worm
t.pensize(50)
for x in range(1, 3):
    t.color("#48ff31")
    t.forward(100)
    t.color("#A0FB94")
    t.forward(100)
t.circle(30)

t.reset()
t.speed(0)
# rotate
for x in range(15, 700, 2):
    t.forward(x)
    t.right(89)
