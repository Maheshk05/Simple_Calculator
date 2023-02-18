from tkinter import *

root = Tk()
root.geometry("644x900")
root.title("CALCULATOR")
root.wm_iconbitmap("") #iconlink
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar = scvalue, font = "lucida 40 bold", justify = "right")
screen.pack(fill = X, ipadx = 8, pady = 10, padx = 10)

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
             
    elif text == "C":
        scvalue.set("")
        screen.update()
        
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
    

f = Frame(root, bg = "grey")
b = Button(f, text = "9",padx = 8, pady = 8, font = "lucida 40 bold")
b.pack(side = LEFT, padx = 8, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, text = "8",padx = 8, pady = 8, font = "lucida 40 bold")
b.pack(side = LEFT, padx = 8, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, text = "7",padx = 8, pady = 8, font = "lucida 40 bold")
b.pack(side = LEFT, padx = 8, pady = 5)
b.bind("<Button-1>",click)
f.pack()


f = Frame(root, bg = "grey")
b = Button(f, text = "6",padx = 8, pady = 8, font = "lucida 40 bold")
b.pack(side = LEFT, padx = 8, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, text = "5",padx = 8, pady = 8, font = "lucida 40 bold")
b.pack(side = LEFT, padx = 8, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, text = "4",padx = 8, pady = 8, font = "lucida 40 bold")
b.pack(side = LEFT, padx = 8, pady = 5)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg = "grey")
b = Button(f, text = "3",padx = 8, pady = 8, font = "lucida 40 bold")
b.pack(side = LEFT, padx = 8, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, text = "2",padx = 8, pady = 8, font = "lucida 40 bold")
b.pack(side = LEFT, padx = 8, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, text = "1",padx = 8, pady = 8, font = "lucida 40 bold")
b.pack(side = LEFT, padx = 8, pady = 5)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg = "grey")
b = Button(f, text = "0",padx = 16, pady = 8, font = "lucida 40 bold")
b.pack(side = LEFT, padx = 8, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, text = "-",padx = 8, pady = 8, font = "lucida 40 bold")
b.pack(side = LEFT, padx = 8, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, text = "*",padx = 8, pady = 8, font = "lucida 40 bold")
b.pack(side = LEFT, padx = 8, pady = 5)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg = "grey")
b = Button(f, text = "/",padx = 8, pady = 8, font = "lucida 40 bold")
b.pack(side = LEFT, padx = 8, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, text = "%",padx = 8, pady = 8, font = "lucida 40 bold")
b.pack(side = LEFT, padx = 8, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, text = "=",padx = 8, pady = 8, font = "lucida 40 bold")
b.pack(side = LEFT, padx = 8, pady = 5)
b.bind("<Button-1>",click)
f.pack()




root.mainloop()

