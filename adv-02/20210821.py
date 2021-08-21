from tkinter import *
def move(event):
    key=event.keysym
    print(key)
    if key == "d":
        canvas.move(circle, 10, 0)
    elif key == "a":
        canvas.move(rect, -10, 0)
    elif key =="w":
        canvas.move(rect, 0, -10)
    elif key == "s":
        canvas.move

windows = Tk()
windows.title("My first GUI")
move()

canvas = Canvas(windows, width=600, height=600)
canvas.pack()
'''
img = PhotoImage(file="adv-02/crocodile2.gif")
my_img = canvas.create_image(300, 300, image = img)

circle = canvas.create_oval(100, 100, 300, 300, fill="red")
rect = canvas.create_rectangle(220, 400, 340, 430, fill="blue")
msg = canvas.create_text(300, 100, text="Corcodile", fill="black,font = ( "Arial", 30))
'''
windows.mainloop