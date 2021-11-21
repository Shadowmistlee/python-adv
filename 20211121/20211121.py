import requests
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def createLabels(data, title):
    for item in data:
        height = item.get_height()
        plt.text(
            item.get_x() + item.get_width() / 2,
            height,
            title + str(height),
            ha="center",
        )


df = pd.DataFrame(None, columns=["date", "host", "guest"])
base_url = "https://tw.global.nba.com/stats2/scores/daily.json"
contry = "TW"
date = "2021-11-1"
locale = "zh_TW"
tz = "%2B8"
send_url = base_url
send_url += "?contry=" + contry
send_url += "&date=" + date
send_url += "&locale=" + locale
send_url += "&tz=" + tz
response = requests.get(send_url)
info = response.json()

data = info["payload"]["date"]["games"]

host_win = 0
guest_win = 0

print(",date,host,guest")
for num in data:
    print("guest:{}".format(num["boxscore"]["awayScore"]))
    print("host:{}".format(num["boxscore"]["homeScore"]))
    if num["boxscore"]["awayScore"] > num["boxscore"]["homeScore"]:
        guest_win += 1
    else:
        host_win += 1
df = df.append({
    'date': date,
    'host': host_win,
    'guest': guest_win
},
               ignore_index=True)

df.to_csv("20211121/temp.csv")
# /////////////////////////////////////////////////////////////////////////////////////////////////////
df = pd.read_csv("20211121/temp.csv")
game_date = df.loc[:, "date"]
guest_win_list = df.loc[:, "guest"]
host_win_list = df.loc[:, "host"]
index = np.arange(len(game_date))
fig, ax = plt.subplots()

A = ax.bar(index, host_win_list, label='host win', width=0.25)
B = ax.bar(index + 0.25, guest_win_list, label="guest win", width=0.25)

ax.set_xticks(index)
ax.set_xticklabels(game_date)

createLabels(A, "host win")
createLabels(B, "guest")

plt.legend("left upper")
plt.show()