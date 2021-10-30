import json,requests
import matplotlib.pyplot as plt



from tkinter import *

base_url = "https://data.epa.gov.tw/api/v1/"
api_num = "aqx_p_432?"
offset = "0"
limit = "10"
api_key = "05bfc982-f3d3-4b6d-922c-0baee6d1b2db"
send_url = base_url
send_url += api_num
send_url += "offset=" + offset
send_url += "&limit=" + limit
send_url += "&api_key=" + api_key
city = "新店"
    
response = requests.get(send_url)
info = response.json()

if "fields" in info.keys():
    for i in range(int(limit)):
        data = info["records"][i]["SiteName"]
        if data == city:
            print("City = " + info["records"][i]["County"])
            print("SiteName = " + info["records"][i]["SiteName"])
            print("AQI = " + info["records"][i]["AQI"])
            print("PM2.5 = " + info["records"][i]["PM2.5"])
            print("Status = " + info["records"][i]["Status"] + "\n")
else:
    print("Found Error")









