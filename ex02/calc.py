import tkinter as tk
from random import randint

if __name__ == "__main__":
    def button_click(event):
        check = event.widget["text"]
        if check == "=":
            text = textbox.get()
            textbox.delete(0,tk.END)
            ans = eval(text)
            
            return textbox.insert(tk.END,ans)
        
        if check == "C":
            return textbox.delete(0,tk.END)

        if check == "R":
                random = randint(0,10)
                return textbox.insert(tk.END,random)

        if check == "←":
            sub = textbox.get()
            return textbox.delete(len(sub)-1,tk.END)

        if check == "x10":
            sub = textbox.get()
            textbox.delete(0,tk.END)
            ans = float(sub)*10
            return textbox.insert(tk.END,ans)
        
        if check == ".":
            sub = textbox.get()
            textbox.delete(0,tk.END)
            ans = float(sub)/10
            return textbox.insert(tk.END,ans)

        else:
            return textbox.insert(tk.END,check)


    root = tk.Tk()
    root.geometry("300x600")
    textbox = tk.Entry(root,justify="right",width=10,font=(("Times New Roman",40)))
    textbox.grid(row = 0,columnspan = 5)
    r,c = 1,0

    for i,num in enumerate(["%",".","x10","R",9,8,7,"←",6,5,4,"C",3,2,1,"*","+",0,"/","=","","-","",""]):
        button = tk.Button(root,text=f"{num}",height=2,width=4,font=("Times New Roman",20))
        button.grid(row=r,column=c)
        c += 1
        if (i+1)%4 == 0:
            r += 1
            c = 0
        button.bind("<1>",button_click)

    root.mainloop()


