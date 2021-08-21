from tkinter import *

windows = Tk()
windows.title("My first GUI")
canvas = Canvas(windows, width=600, height=600)
canvas.pack()
img = PhotoImage(file="adv-02/crocodile2.gif")
my_img = canvas.create_image(300, 300, image = img)

windows.mainloop