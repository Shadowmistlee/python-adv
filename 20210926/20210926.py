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

import requests
api_key = "2f7671995fd280c1b8c10843d66b3f93"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ")
units = "metric"
lang = "zh_tw"
send_url=base_url
send_url+="appid=" + api_key
send_url += "&q=" + city_name
send_url += "&units=" + units
send_url += "&lang=" + lang
response = requests.get(send_url)
info = response.json()
print("%s\n" % send_url)
response = requests.get(send_url)
info = response.json()
print(type(info))
print("天氣:" + str(info["weather"][0]["description"]))
print("溫度:" + str(info["main"]["temp"]))

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

