import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm
<<<<<<< HEAD
=======
import random
import time
>>>>>>> add_func

def key_down(event):
    global key
    key = event.keysym
    return key

def key_up(event):
    global key
    key = ""
    return key

def main_proc():
    global cx,cy,mx,my
<<<<<<< HEAD
=======
    time_start = time.time()
>>>>>>> add_func
    if key == "Up":
        my -= 1
        if maze[my][mx] == 1:
            my += 1
    if key == "Down":
        my += 1
        if maze[my][mx] == 1:
            my -= 1
    if key == "Left":
        mx -= 1
        if maze[my][mx] == 1:
            mx += 1
    if key == "Right":
        mx += 1
        if maze[my][mx] == 1:
            mx -= 1
<<<<<<< HEAD
    cx,cy = mx * 100 + 50 , my * 100 + 50
    canvas.coords("koukaton",cx,cy)
    root.after(100,main_proc) 


if __name__ == "__main__":
    key = ""
    mx,my = 1,1
    cx,cy = mx * 100 + 50 , my * 100 + 50
=======

    cx,cy = mx * 100 + 50 , my * 100 + 50
    canvas.coords("koukaton",cx,cy)
    jid = root.after(100,main_proc)

    if mx == 13 and my == 7:
        root.after_cancel(jid)
        tkm.showinfo("クリア",f"ゲームクリアおめでとう！クリアタイムは{str(time_start-time_end)}秒")
        return root.destroy()



if __name__ == "__main__":
    time_start = time.time()
    key = ""
    mx,my = 1,1
    cx,cy = mx * 100 + 50 , my * 100 + 50
    tori_list = ["ex03/fig/0.png","ex03/fig/1.png","ex03/fig/2.png",
                 "ex03/fig/3.png","ex03/fig/4.png","ex03/fig/5.png",
                 "ex03/fig/6.png","ex03/fig/7.png","ex03/fig/8.png",
                 "ex03/fig/9.png"]
    check = 0
>>>>>>> add_func

    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root,width=1500,
                       height=900,bg="black")
<<<<<<< HEAD
    maze = mm.make_maze(15,9)
    mm.show_maze(canvas,maze)
    koukaton = tk.PhotoImage(file="ex03/fig/1.png")
=======
    
    maze = mm.make_maze(15,9)
    mm.show_maze(canvas,maze)
    tori = random.choice(tori_list)
    koukaton = tk.PhotoImage(file=tori)
>>>>>>> add_func
    canvas.create_image(cx,cy,image=koukaton,tag="koukaton")
    canvas.pack()

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
<<<<<<< HEAD
=======
    time_end = time.time()
>>>>>>> add_func

    root.mainloop()