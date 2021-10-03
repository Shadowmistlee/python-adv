import json
'''
what = {
    "meme":"popcat",
    "singer":"rick asley"
}
print(what['meme'])
what["meme"] = 'rickroll'
print(what['meme'])
keys = what.keys()
for key in keys:
    print(key)
    print(what[key])
for value in what.values():
    print(value)
'''
'''
data = {
    "Name": "Singular",
    "Score": [
	{"Math": 100, "English": 99}, 
	{"Chinese": 98, "Nature": 97}
	]
}
print(data["Score"][0]["English"])
print(data["Score"][1]["Chinese"])
json_str = json.dumps(data)
json_data = json.loads(json_str)
print(json_str)
print(json_data)
print(type(json_str))
'''

import requests
from tkinter import *
def get_weather():
    api_key = "2f7671995fd280c1b8c10843d66b3f93"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = input('enter city name')
    units = "metric"
    lang = "zh_tw"

    send_url = base_url
    send_url += "appid=" + api_key
    send_url += "&q=" + city_name
    send_url += "&units=" + units
    send_url += "&lang=" + lang

    # print("%s\n" % send_url)
    response = requests.get(send_url)
    info = response.json()

    if "main" in info.keys():
        temp_info = info["main"]["temp"]
        weather_info = info["weather"][0]["description"]
        print("City = " + city_name)
        put_city.config(text="City = " + city_name)
        print("Temperature = " + str(temp_info))
        put_temp.config(text="Temperature = " + str(temp_info))
        print("Description = " + str(weather_info))
        put_disc.config(text="Description = " + str(weather_info))
    else:
        print(" City Not Found ")

windows = Tk()
windows.title("My Weather")

put_city = Label(windows, text="city:")
put_city.pack

put_temp = Label(windows, text="temp:")
put_temp.pack()

put_disc = Label(windows, text="disc:")
put_disc.pack()

city_info = Entry(windows)
city_info.pack()

btn = Button(windows, text='get weather', command=get_weather)
btn.pack()

windows.mainloop()






'''
info = {
    "coord": {
        "lon": 121.5319,
        "lat": 25.0478
    },
    "weather": [{
        "id": 801,
        "main": "Clouds",
        "description": "晴，少雲",
        "icon": "02d"
    }],
    "base":
    "stations",
    "main": {
        "temp": 28.64,
        "feels_like": 32.64,
        "temp_min": 26.98,
        "temp_max": 30.07,
        "pressure": 1014,
        "humidity": 74
    },
    "visibility":
    10000,
    "wind": {
        "speed": 3.58,
        "deg": 90,
        "gust": 8.05
    },
    "clouds": {
        "all": 20
    },
    "dt":
    1632616331,
    "sys": {
        "type": 2,
        "id": 266033,
        "country": "TW",
        "sunrise": 1632606230,
        "sunset": 1632649603
    },
    "timezone":
    28800,
    "id":
    1668341,
    "name":
    "Taipei",
    "cod":
    200
}
'''

