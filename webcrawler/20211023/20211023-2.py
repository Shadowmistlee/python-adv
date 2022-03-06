import json,requests
import matplotlib.pyplot as plt



from tkinter import *

base_url = "https://data.epa.gov.tw/api/v1/"
api_num = "aqx_p_432?"
offset = "0"
limit = "1000"
api_key = "05bfc982-f3d3-4b6d-922c-0baee6d1b2db"
send_url = base_url
send_url += api_num
send_url += "offset=" + offset
send_url += "&limit=" + limit
send_url += "&api_key=" + api_key
city = ""
    
response = requests.get(send_url)
info = response.json()

if "fields" in info.keys():
    for i in range(int(limit)):
        data = info["records"][i]["County"]
        if data == "新北市":
            print(info["records"][i]["SiteName"])
else:
    print("Found Error")









