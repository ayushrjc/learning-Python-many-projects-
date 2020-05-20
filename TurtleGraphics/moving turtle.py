import turtle as t
import random as rd
import time as ti

def inside_window():
    l_limit = (-t.window_width()/2) +100
    r_llimit = (t.window_width() / 2) -100
    t_limit = (t.window_width() / 2) -100
    b_limit = (-t.window_width() / 2) +100
    (x,y) = t.pos()
    inside = l_limit<x < r_llimit and b_limit < y < t_limit
    return inside

def mov_turtle():
    if inside_window():
        angle = rd.randint(0,100)
        t.right(angle)
        t.forward(200)
    else:
        t.backward(200)



t.shape('turtle')
t.fillcolor('green')
t.bgcolor('black')
t.speed('slow')

while True:
    mov_turtle()

