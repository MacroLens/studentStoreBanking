#!/usr/bin/python3
from tkinter import *
from nfcScript import *
root = Tk()
frame = Frame(root)
frame.grid(row=0, column=0)
textBox = Text(frame)
textBox.grid(row=0,column=4,rowspan=4,columnspan=2)
textBox.insert(INSERT, "Welcome to the store!")
clearText = Button(frame, text="Clear", command=lambda: textBox.delete(1.0,END)).grid(row=4,column=5)

def scanCard():
    x = decode()
    printMessage(x)
scan = Button(frame, text="Scan Card", command=scanCard).grid(row=4,column=4)

def printMessage(text):
    if text != "Enter\nReturn":
        textBox.insert(END, str(text))
    else:
        textBox.insert(END, "\n")

#button1 = Button(frame, text="Print Message", command=printMessage)
#button1.grid(column=1)

keypad = [7,8,9,4,5,6,1,2,3,0,".","Enter\nReturn"]

class keyPad:
    def __init__(self,myFrame):
        r = 1
        c = 0
        for i in keypad:
            valuePress = lambda button=i: printMessage(button)
            Button(myFrame, text=i, command=valuePress, height=5, width=3).grid(row=r,column=c)
            c+=1
            if c >= 3:
                c = 0
                r+=1
    
keypad = keyPad(frame)


root.mainloop()
