import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm

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
    cx,cy = mx * 100 + 50 , my * 100 + 50
    canvas.coords("koukaton",cx,cy)
    root.after(100,main_proc) 


if __name__ == "__main__":
    key = ""
    mx,my = 1,1
    cx,cy = mx * 100 + 50 , my * 100 + 50

    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root,width=1500,
                       height=900,bg="black")
    maze = mm.make_maze(15,9)
    mm.show_maze(canvas,maze)
    koukaton = tk.PhotoImage(file="ex03/fig/1.png")
    canvas.create_image(cx,cy,image=koukaton,tag="koukaton")
    canvas.pack()

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()

    root.mainloop()