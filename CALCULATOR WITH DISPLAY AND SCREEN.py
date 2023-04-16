from tkinter import *
def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(scvalue.get())
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")  
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
root = Tk()
root.title("Simple Calculator by Siddhartha")
root.geometry("640x900")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar=scvalue, font = "lucida 40 bold")
screen.pack(fill=X,ipadx=9,pady= 11,padx=11)
# Frame 1
f = Frame(root, bg= "green")
b = Button(f,text="9",padx= 11, pady= 11,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=3)
b.bind("<Button-1>",click)
b = Button(f,text="8",padx= 11, pady= 11,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=3)
b.bind("<Button-1>",click)
b = Button(f,text="7",padx= 11, pady= 11,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=3)
b.bind("<Button-1>",click)
f.pack()
# Frame 2 
f = Frame(root, bg= "green")
b = Button(f,text="6",padx= 11, pady= 11,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=3)
b.bind("<Button-1>",click)
b = Button(f,text="5",padx= 11, pady= 11,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=3)
b.bind("<Button-1>",click)
b = Button(f,text="4",padx= 11, pady= 11,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=3)
b.bind("<Button-1>",click)
f.pack()
# Frame 3
f = Frame(root, bg= "green")
b = Button(f,text="3",padx= 11, pady= 11,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=3)
b.bind("<Button-1>",click)
b = Button(f,text="2",padx= 11, pady= 11,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=3)
b.bind("<Button-1>",click)
b = Button(f,text="1",padx= 11, pady= 11,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=3)
b.bind("<Button-1>",click)
f.pack()
# Frame 4 
f = Frame(root, bg= "green")
b = Button(f,text="0",padx= 11, pady= 11,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=3)
b.bind("<Button-1>",click)
b = Button(f,text="-",padx= 11, pady= 11,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=3)
b.bind("<Button-1>",click)
b = Button(f,text="*",padx= 11, pady= 11,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=3)
b.bind("<Button-1>",click)
f.pack()
# Frame 5
f = Frame(root, bg= "green")
b = Button(f,text="/",padx= 11, pady= 11,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=3)
b.bind("Button-1>",click)
b = Button(f,text="+",padx= 11, pady= 11,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=3)
b.bind("<Button-1>",click)
b = Button(f,text="=",padx= 11, pady= 11,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=3)
b.bind("<Button-1>",click)
f.pack()
# Frame 6
f = Frame(root, bg= "green")
b = Button(f,text="C",padx= 11, pady= 11,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=3)
b.bind("<Button-1>",click)
b = Button(f,text="%",padx= 11, pady= 11,font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=3)
b.bind("<Button-1>",click)
f.pack()

root.mainloop()











