from pytube import YouTube
import ssl
from tkinter import *

ssl._create_default_https_context = ssl._create_unverified_context


def get_video():

    yt = YouTube("" + pos_info.get())
    video = yt.streams
    length = len(video)
    result = video.filter(progressive=True, subtype="mp4", res="720p")
    print(result[0])
    load_name = "C:/Users/Xavier/Desktop/youtube download/" + status_info.get(
    ) + ".mp4"
    result[0].download(filename=load_name)
    print("download finished")


windows = Tk()
windows.title("???")

pos = Label(windows, text="enter link")
pos.grid(row=0, column=0)

pos_info = Entry(windows)
pos_info.grid(row=1, column=0)

status = Label(windows, text="enter name")
status.grid(row=2, column=0)

status_info = Entry(windows)
status_info.grid(row=3, column=0)

btn = Button(windows, text="get video", command=get_video)
btn.grid(row=5, column=0)

name = Label(windows, text="name")
name.grid(row=6, column=0)

v_length = Label(windows, text="length")
v_length.grid(row=7, column=0)

windows.geometry("300x150")
windows.mainloop()

# print("video name", yt.title)
# print("video author", yt.author)
# print("video length", yt.length)
# print("縮圖網址", yt.thumbnail_url)