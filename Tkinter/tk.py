import tkinter
from tkinter import *

win = Tk()
win.geometry("400x400")
l1 = Label(win,text = '1st Number')
l1.grid(row=1 , column = 0)
l2 = Label(win,text = '3nd Number')
l2.grid(row=2, column=0)
l = Label(win,text = '1st Number')
l2.grid(row=3 , column = 2)
t = Text()
e = Entry(win, textvariable=t)
# e.pack(side=LEFT)


win.mainloop()