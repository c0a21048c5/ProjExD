import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm
import random
import time

def key_down(event):
    #キーが押されたときのイベントを取得
    global key
    key = event.keysym
    return key

def key_up(event):
    #キーを放したときの返り値を空白に設定
    global key
    key = ""
    return key

def main_proc():
    global cx,cy,mx,my
    #各キーで行う動作を定義
    if key == "Up":
        my -= 1
        if maze[my][mx] == 1: #床のみを移動するように設定
            my += 1
    if key == "Down":
        my += 1
        if maze[my][mx] == 1: #上と同じ
            my -= 1
    if key == "Left":
        mx -= 1
        if maze[my][mx] == 1: #上と同じ
            mx += 1
    if key == "Right":
        mx += 1
        if maze[my][mx] == 1: #上と同じ
            mx -= 1

    canvas.coords("koukaton",mx*100+50,my*100+50)
    jid = root.after(100,main_proc)
    
    #ゴール地点で行う処理を定義
    if mx == 13 and my == 7:
        time_end = time.time() #終了時間を取得
        root.after_cancel(jid) #リアルタイム処理を中断
        tkm.showinfo("クリア",f"ゲームクリアおめでとう！クリアタイムは{int(abs(time_start-time_end))}秒")
        return root.destroy()



if __name__ == "__main__":
    time_start = time.time()
    key = ""
    mx,my = 1,1
    cx,cy = mx * 100 + 50 , my * 100 + 50

    #画像ファイル名のリストを定義
    tori_list = ["ex03/fig/0.png","ex03/fig/1.png","ex03/fig/2.png",
                 "ex03/fig/3.png","ex03/fig/4.png","ex03/fig/5.png",
                 "ex03/fig/6.png","ex03/fig/7.png","ex03/fig/8.png",
                 "ex03/fig/9.png"]

    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root,width=1500,
                       height=900,bg="black")

    maze = mm.make_maze(15,9)
    mm.show_maze(canvas,maze)
    tori = random.choice(tori_list) #リスト内からランダムでファイル名を取得
    koukaton = tk.PhotoImage(file=tori)
    canvas.create_image(cx,cy,image=koukaton,tag="koukaton")
    canvas.pack()

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    
    root.mainloop()