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
    root.geometry("300x500")
    textbox = tk.Entry(root,justify="right",width=10,font=(("Times New Roman",40)))
    textbox.grid(row = 0,columnspan = 5)
    r,c = 1,0

    for i,num in enumerate(["%",".","x10","R",9,8,7,"←",6,5,4,"C",3,2,1,"*","+",0,"/","="]):
        button = tk.Button(root,text=f"{num}",height=2,width=4,font=("Times New Roman",20))
        button.grid(row=r,column=c)
        c += 1
        if (i+1)%4 == 0:
            r += 1
            c = 0
        button.bind("<1>",button_click)

    root.mainloop()
    

   
    
    


    #button2 = tk.Button(root,text="8",height=2,width=4,font=("Times New Roman",30))
    #button2.grid(row=1,column=1)
    #button2.bind("<1>",button_click)

    #button3 = tk.Button(root,text="7",height=2,width=4,font=("Times New Roman",30))
    #button3.grid(row=1,column=2)
    #button3.bind("<1>",button_click)
    
    #button4 = tk.Button(root,text="6",height=2,width=4,font=("Times New Roman",30))
    #button4.grid(row=2,column=0)
    #button4.bind("<1>",button_click)

    #button5 = tk.Button(root,text="5",height=2,width=4,font=("Times New Roman",30))
    #button5.grid(row=2,column=1)
    #button5.bind("<1>",button_click)

    #button6 = tk.Button(root,text="4",height=2,width=4,font=("Times New Roman",30))
    #button6.grid(row=2,column=2)
    #button6.bind("<1>",button_click)

    #button7 = tk.Button(root,text="3",height=2,width=4,font=("Times New Roman",30))
    #button7.grid(row=3,column=0)
    #button7.bind("<1>",button_click)

    #button8 = tk.Button(root,text="2",height=2,width=4,font=("Times New Roman",30))
    #button8.grid(row=3,column=1)
    #button8.bind("<1>",button_click)

    #button9 = tk.Button(root,text="1",height=2,width=4,font=("Times New Roman",30))
    #button9.grid(row=3,column=2)
    #button9.bind("<1>",button_click)

    #button10 = tk.Button(root,text="0",height=2,width=4,font=("Times New Roman",30))
    #button10.grid(row=4,column=0)
    #button10.bind("<1>",button_click)

    #button10 = tk.Button(root,text="+",height=2,width=4,font=("Times New Roman",30))
    #button10.grid(row=4,column=1)
    #button10.bind("<1>",button_click)

    #button10 = tk.Button(root,text="=",height=2,width=4,font=("Times New Roman",30))
    #button10.grid(row=4,column=2)
    #button10.bind("<1>",equal_click)

    #def equal_click(event):
    #    text = textbox.get()
    #    textbox.delete(0,tk.END)
    #    ans = eval(text)
    #
    #   return textbox.insert(tk.END,ans)


    root.mainloop()


