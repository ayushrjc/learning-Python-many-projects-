import tkinter
from tkinter import *
from tkinter import messagebox

win = Tk()

# frame = Frame(win)
# frame.pack()
#
# frame2 = Frame(win)
# frame2.pack()
#
# rb = Button(frame , text='Red',fg='red')
# rb.pack(side=LEFT)
#
# gb = Button(frame , text='Green',fg='green')
# gb.pack(side=LEFT)

# lb = Listbox(win)
# lb.insert(1,'python')
# lb.insert(2,'c')
# lb.insert(3,'c++')
# lb.insert(4,'java')
# # lb.pack()
#
# win.title('first')
# top=Toplevel()
# top.title('second')
#
# def hello():
#     messagebox.showinfo('from computer','hey there')
# b = Button(win,text='popup',command=hello)
# b.pack()


# mb = Menubutton(win, text='file')
# mb.grid()
# mb.menu = Menu(mb)
# mb['menu'] = mb.menu
#
# x1 = IntVar()
# x2= IntVar()
#
# mb.menu.add_checkbutton(label='open',variable=x1)
# mb.menu.add_checkbutton(label='close',variable=x2)


# def nothing():
#     file = Toplevel(win)
#     button = Button(file,text='do nothing')
#     button.pack()
#
# menubar= Menu(win)
#
# filemenu = Menu(menubar)
# filemenu.add_command(label='New Window',command=nothing)
# filemenu.add_command(label='New File',command=nothing)
# filemenu.add_separator()
# filemenu.add_command(label='Open',command=nothing)
# filemenu.add_command(label='Save',command=nothing)
# filemenu.add_separator()
# filemenu.add_command(label='Save As',command=nothing)
# filemenu.add_command(label='Exit',command=win.quit())
#
# menubar.add_cascade(label='File',menu = filemenu)
# win.config(menu=menubar)

#
# s = Scale()
# s.pack()
#
# sb = Spinbox(win, from_ = 0, to = 10)
# sb.pack()
#
# scrollbar = Scrollbar(win)
# scrollbar.pack(side=RIGHT,fill=Y)
# list = Listbox(win , yscrollcommand=scrollbar.set)
#
# for line in range(100):
#     list.insert(END,'This is line no '+str(line))
#
# list.pack(side= LEFT,fill=BOTH)

# win.mainloop()


#### Paned Window ####
# pw = PanedWindow()
# pw.pack(fill = BOTH,expand=1)
#
# left = Entry(pw,bd=5)
# pw.add(left)
#
# pw2 = PanedWindow(pw,orient=VERTICAL)
# pw.add(pw2)
#
# top = Scale(pw,orient=HORIZONTAL)
# pw2.add(top)
#
# bottom = Button(pw2,text='ok')
# pw2.add(bottom)
#
# mainloop()


####### GEOMETRY METHOD #######
# b=0
# for i in range(6):
#     for j in range(6):
#         b= b+1
#         Button(win,text=str(b),borderwidth=1).grid(row=i, column=j)
#

# l1= Label(win,text='Maths')
# l1.place(x=10 ,y =10)
# e1=Entry(win,bd=5)
# e1.place(x=60,y=10)
#
# l1= Label(win,text='Eng')
# l1.place(x=10 ,y =60)
# e1=Entry(win,bd=5)
# e1.place(x=60,y=60)
#
# b = Button(win,text='submit')
# b.place(x=100,y=100)


win.mainloop()