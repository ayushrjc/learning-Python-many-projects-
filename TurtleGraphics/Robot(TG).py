import turtle as t
import time
def rect(hor,ver,c):
    t.pendown()
    t.pensize(1)
    t.color(c)
    t.begin_fill()
    for i in range(1,3):
        t.forward(hor)
        t.right(90)
        t.forward(ver)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed('slow')
t.bgcolor('Dodger blue')
t.goto(-100,-150)
rect(50,20,'blue')
t.goto(-30,-150)
rect(50,20,'blue')
t.goto(-25,-50)
rect(15,100,'grey')
t.goto(-70,-50)
rect(15,100,'grey')
t.goto(-90,100)
rect(100,150,'red')
t.goto(-150,70)
rect(60,15,'grey')
t.goto(-150,110)
rect(15,40,'grey')
t.goto(10,70)
rect(69,15,'grey')
t.goto(65,110)
rect(15,40,'grey')

t.goto(-50,120)
rect(15,20,'grey')

t.goto(-85,170)
rect(80,50,'red')

t.goto(-60,160)
rect(30,10,'white')

t.goto(-55,155)
rect(5,5,'black')

t.goto(-40,155)
rect(5,5,'black')
t.goto(-65,138)
rect(40,5,'black')
t.hideturtle()

time.sleep(10)





