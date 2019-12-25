#!/usr/bin/python3
from tkinter import *
from nfcScript import *

class store:

    def __init__(self, master):
        self.root = master
        self.frame = Frame(self.root)
        self.textBox = Text(self.frame)
        self.textBox.insert(INSERT, "Welcome to the store!")
        self.clearText = Button(self.frame, text="Clear", command=lambda: self.textBox.delete(1.0, END))
        self.scan = Button(self.frame, text="Scan Card", command=self.scanCard)
        self.retrieve = Button(self.frame, text="Retrieve", command=self.retrieve_input)
        self.defaultLayout()

    def defaultLayout(self):
        self.createKeyPad()  # decided it's easier logically to just call createKeyPad and delete it when not needed.
        self.frame.grid(row=0, column=0)
        self.textBox.grid(row=0, column=4, rowspan=4, columnspan=3)
        self.scan.grid(row=4, column=4)
        self.clearText.grid(row=4, column=5)
        self.retrieve.grid(row=4, column=6)

    def createKeyPad(self):
        keypad = [7,8,9,4,5,6,1,2,3,0,".","Enter\nReturn"]
        r = 1
        c = 0
        for i in keypad:
            valuePress = lambda button=i: store.printMessage(self, button)
            Button(self.frame, text=i, command=valuePress, height=5, width=3).grid(row=r,column=c)
            c+=1
            if c >= 3:
                c = 0
                r+=1

    def retrieve_input(self):
        # Returns all text in the textbox excluding the last new line character.
        print(self.textBox.get("1.0", 'end-1c').encode('unicode_escape'))

    def scanCard(self):
        self.printMessage("\nPlace card on reader.")
        x = decode()
        if not x:  # if the reader throws an error.
            self.printMessage("\nMake sure the reader is plugged in and turned on.")
        else:
            self.printMessage(x)



    def printMessage(self, text):
        if text != "Enter\nReturn":
            self.textBox.insert(END, str(text))
        else:
            self.textBox.insert(END, "\n")
        self.textBox.update()


storeWindow = Tk()
store(storeWindow)
storeWindow.mainloop()
