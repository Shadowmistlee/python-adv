from tkinter import *
import os
from moviepy.editor import *
from pytube import YouTube


def cut():
    if os.path.isfile(ent_info.get()):
        clip = VideoFileClip(ent_info.get())
        start = pos_info.get()
        end = status_info.get()

        clip.subclip(start, end)

        i = 0
        base_path = ent_info.get()
        new_file = ent_file_info.get()
        #new_path = base_path + new_file + str(i) + ".mp4"
        while os.path.isfile(new_path):
            i += 1
            new_path = base_path + new_file + str(i) + ".mp4"

        if sel.get() == 0:
            clip.write_videofile(new_path)
        elif sel.get() == 1:
            clip.write_gif(base_path + new_file + str(i) + ".gif")
        else:
            clip.audio.write_audiofile(base_path + new_file + str(i) + ".mp3")
    else:
        exit()


windows = Tk()
windows.title("my video")

ent = Label(windows, text="enter path")
ent.grid(row=0, column=0)

ent_info = Entry(windows)
ent_info.grid(row=0, column=1)

ent_file = Label(windows, text="video name")
ent_file.grid(row=0, column=5)

ent_file_info = Entry(windows)
ent_file_info.grid(row=0, column=6)

pos = Label(windows, text="enter start")
pos.grid(row=0, column=2)

pos_info = Entry(windows)
pos_info.grid(row=0, column=3)

status = Label(windows, text="enter end")
status.grid(row=2, column=0)

status_info = Entry(windows)
status_info.grid(row=2, column=1)

state = BooleanVar()
state.set(True)

sel = IntVar()
sel.set(1)
rad1 = Radiobutton(windows, text="mp4", value=0, variable=sel)
rad1.grid(row=4, column=0)
rad2 = Radiobutton(windows, text="gif", value=1, variable=sel)
rad2.grid(row=5, column=1)
rad3 = Radiobutton(windows, text="mp3", value=2, variable=sel)
rad3.grid(row=6, column=2)

btn = Button(windows, text="cut", command=cut)
btn.grid(row=7, columnspan=2)

status = Label(windows, font=('Arial', 12))
status.grid(row=8, columnspan=3, sticky="we")

windows.geometry("600x600")

windows.mainloop()