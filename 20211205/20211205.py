import os
from moviepy.editor import *
from pytube import YouTube
from tkinter import *


def cut():
    if os.path.isfile(
            "C:/Users/Xavier/Desktop/youtube download/nevergonnaclip.mp4"):
        clip = VideoFileClip(
            "C:/Users/Xavier/Desktop/youtube download/nevergonna.mp4")
        start = pos_info.get()
        end = status_info.get()

        clip.subclip(start, end)

        i = 0
        base_path = "C:/Users/Xavier/Desktop/youtube download/"
        new_file = ent_info.get()
        new_path = base_path + new_file + str(i) + ".mp4"

        while os.path.isfile(new_path):
            i += 1
            new_path = base_path + new_file + str(i) + ".mp4"
        clip.write_videofile(new_path)
    else:
        exit()


windows = Tk()
windows.title("video")

ent = Label(windows, text="enter name")
ent.grid(row=0, column=0)

ent_info = Entry(windows)
ent.grid(row=0, column=1)

pos = Label(windows, text="enter start")
pos.grid(row=1, column=0)

pos_info = Entry(windows)
pos_info.grid(row=1, column=1)

status = Label(windows, text="enter end")
status.grid(row=2, column=0)

status_info = Entry(windows)
status_info.grid(row=2, column=1)

state = BooleanVar()
state.set(True)
chk = Checkbutton(windows, text="gif", var=state)
chk.grid(row=3, column=0)

btn = Button(windows, text="cut", command=cut)
btn.grid(row=3, columnspan=2)

windows.geometry("300x150")
windows.mainloop()
