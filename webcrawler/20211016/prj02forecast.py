import requests, json

api_key = "2f7671995fd280c1b8c10843d66b3f93"
base_url = "https://api.openweathermap.org/data/2.5/onecall?"
lat = "25"
lon = "125"
exclude = "minutely, hourly"
units = "metric"
lang = "zh_tw"
send_url = base_url
send_url += "lat=" + lat
send_url += "&lon=" + lon
send_url += "&exclude=" + exclude
send_url += "&appid=" + api_key
send_url += "&lang" + lang
print("%s\n" % send_url)
response = requests.get(send_url)
info = json.loads(response.text)

if "lat" in info.keys():
        for i in range(7):
            temps = info["daily"][i]["temp"]["day"]
            print("Day%d Temp=%s c" % (i, temps))
else:
    print(" Request Fail ")