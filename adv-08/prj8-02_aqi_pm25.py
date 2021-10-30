import numpy as np
import json,requests
import matplotlib.pyplot as plt



from tkinter import *

base_url = "https://data.epa.gov.tw/api/v1/"
api_num = "aqx_p_432?"
offset = "0"
limit = "50"
api_key = "05bfc982-f3d3-4b6d-922c-0baee6d1b2db"
send_url = base_url
send_url += api_num
send_url += "offset=" + offset
send_url += "&limit=" + limit
send_url += "&api_key=" + api_key
city = ""
    
response = requests.get(send_url)
info = response.json()

def get_weather():
    city = pos_info.get()
    if "fields" in info.keys():
        aqi_value = []
        aqi_posit = []
        aqi_pm2_5 = []
        for i in range(int(limit)):
            data = info["records"][i]["County"]
            if data == city:
                aqi_posit.append(info["records"][i]["SiteName"])
                aqi_value.append(int(info["records"][i]["AQI"]))
                aqi_pm2_5.append(int(info["records"][i]["PM2.5"]))
        show_info = ""
        for i in range(len(aqi_value)):
            show_info += ("%s AQI=%d PM2.5=%d\n" % (aqi_posit[i], aqi_value[i], aqi_pm2_5[i]))

        status.config(text=show_info)
        plt.plot(aqi_posit, aqi_value, "c--.", label="AQI")
        plt.plot(aqi_posit, aqi_pm2_5, "g--", label="PM2.5")
        plt.legend(loc="best")
        plt.show()


windows = Tk()
windows.title("My Weather")

pos = Label(windows, text = "請輸入", font=("Arial", 12))
pos.pack()

pos_info = Entry(windows)
pos_info.pack()

status = Label(windows, text=" ")
status.pack()

btn = Button(windows, text='get aqi& pm2.5', command=get_weather,color=#ffff00)
btn.pack()

windows.mainloop()






