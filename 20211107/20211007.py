import json,requests
from tkinter import *
import matplotlib.pyplot as plt



def get_youbike():
    base_url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"

    response = requests.get(base_url)
    info = response.json()
    status_info = ""
    position = []
    total_bike = []
    remain_bike = []
    for num in info["retVal"]:
        if info["retVal"][num]["sarea"] == pos_info.get():
            print("place:%s" % info["retVal"][num]["sna"].split("(")[0])
            print("place:%s" % info["retVal"][num]["sarea"])
            print('all:%s' % int(info["retVal"][num]["tot"]))
            print("left:%s\n" % int(info["retVal"][num]["sbi"]))

            status_info += "place:{} all:{} left:{}\n".format(
                info["retVal"][num]["sna"].split("(")[0],
                int(info["retVal"][num]["tot"]),
                int(info["retVal"][num]["sbi"]))

            position.append(info["retval"][num]["sna"].split("(")[0])
            total_bike.append(int(info["retVal"][num]["tot"]))
            remain_bike.append(int(info["retVal"][num]["sbi"]))
    status.config(text=status_info)


    plt.plot(position, total_bike, "r-o", label="total")
            

def clr_youbike():
    status.config(text="")


windows = Tk()
windows.title("???")

pos = Label(windows, text="enter")
pos.pack()

pos_info = Entry(windows)
pos_info.pack()

status = Label(windows, text="")
status.pack()

btn = Button(windows, text="get info", command=get_youbike)
btn.pack()

btn = Button(windows, text="clear info", command=clr_youbike)
btn.pack()
windows.mainloop()