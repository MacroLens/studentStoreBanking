#!/usr/bin/python3
from tkinter import *

root = Tk()
frame = Frame(root)
frame.grid(row=0, column=0)
textBox = Text(frame)
textBox.grid(row=0,column=4,rowspan=4)
textBox.insert(INSERT, "Welcome to the store!")
def clear():
    textBox.delete(1.0,END)
clearText = Button(frame, text="Clear", command=clear).grid(row=4,column=4)

def printMessage(text):
    textBox.insert(END, "\n"+str(text))

#button1 = Button(frame, text="Print Message", command=printMessage)
#button1.grid(column=1)

keypad = [7,8,9,4,5,6,1,2,3,0]


r = 1
c = 0
for i in keypad:
    if r==4:
        c = 1
    valuePress = lambda button=i: printMessage(button)
    Button(frame, text=i, command=valuePress, height=10, width=15).grid(row=r,column=c)
    c+=1
    if c >= 3:
        c = 0
        r+=1
    


root.mainloop()
