from moviepy.editor import *

video_path = "D:/youtube download/poor-guy.mp4"

clip = VideoFileClip(video_path)

Font_Url = "C:/Users/Xavier/Desktop/python-adv/TaipeiSansTCBeta-Bold.ttf"

txt_clip = TextClip("你怎麼那麼可憐", font=Font_Url, fontsize=36, color="white")
txt_clip = txt_clip.set_start(0).set_end(2).set_pos("bottom")

video = CompositeVideoClip([clip, txt_clip])
video.write_gif("D:/youtube download/poor-guy.gif")
