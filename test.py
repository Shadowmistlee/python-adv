"""
from tkinter import *
windows = Tk()
windows.title("My first GUI")
canvas = Canvas(windows, width=600, height=600)
canvas.pack()
img = PhotoImage(file="adv-02/crocodile2.gif")
my_img = canvas.create_image(300, 300, image = img)

circle = canvas.create_oval(100, 100, 300, 300, fill="red")
rect = canvas.create_rectangle(220, 400, 340, 430, fill="blue")
msg = canvas.create_text(300, 100, text="Corcodile", fill="black)
windows.mainloop()
"""
license()
