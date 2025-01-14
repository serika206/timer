### インポート
import datetime
import time
import tkinter
import threading
from playsound import playsound

import os

# print('getcwd:      ', os.getcwd())

sound_list = []
with open(f"{os.getcwd()}/time.txt","r") as fp:
    for val in fp:
        sound_list.append(val.strip())

print(sound_list)

def sound_on():
    canvas.delete("all")
    canvas.create_text(10,10, text="時間です", font=(None,14),anchor=tkinter.NW)
    playsound(f"{os.getcwd()}/sound.mp3")
    
### 時刻取得関数
def get_time():
 
    ### 無限ループ
    while True:
 
        ### 現在時刻取得
        now = datetime.datetime.now()
 
        ### 時刻設定
        tm = "{:02}:{:02}:{:02}".format(now.hour, now.minute, now.second)
        if(tm in sound_list):
            sound_on()
 
        ### キャンバス初期化
        canvas.delete("all")
 
        ### キャンバスに時刻表示
        canvas.create_text(10, 10, text=tm, font=(None,12),anchor=tkinter.NW)
 
        #### 待ち時間
        time.sleep(1)
 
### キャンバス作成
canvas = tkinter.Canvas(None, width=200, height=25)
 
### キャンバス表示
canvas.pack()
 
### スレッド作成
thread = threading.Thread(target=get_time, daemon=True)
 
### スレッド開始
thread.start()
 
### イベントループ
canvas.mainloop()