from tkinter import *
import pyautogui as pyauto
import tkinter.messagebox as tsmg

file_name='Todo.txt'

with open (file_name,"r") as f:
    display=f.read()

with open (file_name,"r") as f:
    index=f.readlines()
    index=float(len(index))

def add():
    global index
    with open (file_name,"r") as f:
        compare=f.read().lower()

    toadd=task.get()
    if toadd == "":
        tsmg.showerror("Error","Can't Add Empty Task")
    elif toadd in compare:
        tsmg.showerror("Error","Task Already Exist")
    else:
        with open (file_name,"a") as f:
            f.write(f"{toadd}\n")
        TextArea.insert(index,toadd+"\n")
        index=index+1
    task.set("")

def delete():
    pyauto.press(["delete","delete"])
    TextArea.update()
    newData=TextArea.get("1.0",END)
    with open (file_name,"w") as f:
        f.write(newData)

root=Tk()
root.geometry("700x600")
root.title("ToDo")

task=StringVar()

f1=Frame(root)
Label(f1,text="Your Personalized Todo",fg="Teal",font="SegoeUI 25 bold",justify="center").pack()
f1.pack(fill="x")

f2=Frame(root)
TextArea=Text(f2,height=15,width=40,font="SegoeUI")
TextArea.pack(expand=False)
TextArea.insert("1.0",display)
f2.pack()

f3=Frame(root)
Label(f3,text="Enter New Task Here:- ",fg="black",font="SegoeUI 15 bold",justify="left").pack(side=LEFT,pady=10)
Entry(f3,textvariable=task,font="SegoeUI 14 bold",fg="black",bg="white").pack(pady=10)
f3.pack()

f4=Frame(root)
Button(f4,text="Add Task",font="SegoeUI 12 bold",fg="White",bg="Green",command=add).pack(padx=80,pady=10,side=LEFT)
Button(f4,text="Delete Task",font="SegoeUI 12 bold",fg="White",bg="Red",command=delete).pack(padx=80,pady=10,side=LEFT)
f4.pack()

root.mainloop()