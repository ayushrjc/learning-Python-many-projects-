import tkinter
from tkinter import *

#create window
win = Tk()
win.geometry("400x400") #its 400 x 400 not *

# def fn():
#     print('hi')

#add button
#b = Button(win, text = 'button' , command = fn , padx = 20, pady= 40, activeforeground='red')
# b.pack()
# pack

# b.grid(row=2, column=1)
# grid

#b.place(x=150,y=150)
# place

# creating canvas

# c = Canvas(win, height= 250, width =300, bg='blue')
# coord = 10,50,240,210
# arc = c.create_arc(coord,start = 0, extent =90,fill='red')
# line = c.create_line(10,10,200,200, fill='white')
# c.pack()


#creating checkButton

# c1 = IntVar()
# c2 = IntVar()
# cb = Checkbutton(win, text = 'Music' , offvalue = 0 , onvalue = 1, height= 2, width = 3 , variable = c1)
# cb.pack()
# cb2 = Checkbutton(win, text = 'Video' , offvalue = 0 , onvalue = 1, height= 2, width = 3 , variable = c2)
# cb2.pack()
#
# var = IntVar()
# r1 = Radiobutton(win, text='option1' ,variable = var , value = 1)
# r1.pack()
# r2 = Radiobutton(win, text='option2' ,variable = var , value = 2)
# r2.pack()
# r3 = Radiobutton(win, text='option3' ,variable = var , value = 3)
# r3.pack()



win.mainloop()