import datetime
from tkinter import *
def nothing():
    time = datetime.date.today()
    print(time)
    time  = datetime.datetime.now().time()
    print(time)
win = Tk()
def display_entry():
    display.config(text=float(input_data.get()) / 2.54, fg="black")
button1 = Button(win, text="???", command= nothing)
button1.pack()
display = Label(win, text="red", fg="#FFFFFF", bg="#FFFFFF")
display.pack()
button2 = Button(win, text="!!!", command= nothing)
button2.pack()
input_data = Entry(win)
input_data.pack()
button3 = Button(win,text="$$$", command=display_entry)
button3.pack()
win.mainloop()