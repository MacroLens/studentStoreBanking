from tkinter import *

# Simple making of a window in tkinter
root = Tk() # creates a window

#label = Label(root, text="This is a test") # creates a label
#label.pack() # packs all the stuff in a window together, as tight as possible


# Frames, a rectangle to put things in.

# A frame and sides
#topFrame = Frame(root); # a container that goes in our main window root
#topFrame.pack() # to have anything display in our window it has to be packed, this can also be explicit, but it would
                # redundant

#bottomFrame = Frame(root)
#bottomFrame.pack(side=BOTTOM) # You can pass parameters, to decide location on window



# Creating Buttons, a type of widget
#button1 = Button(topFrame, text="Button 1", fg="red") #create a button, can be given two parameters one optional, where to put it, and a value, and a foreground(text) color.
#button2 = Button(topFrame, text="Button 2", fg="blue")
#button3 = Button(topFrame, text="Button 3", fg="green")
#button4 = Button(bottomFrame, text="Button 4", fg="purple")

#button1.pack(side=LEFT)
#button2.pack(side=LEFT)
#button3.pack(side=LEFT)
#button4.pack(side=BOTTOM) # this is the only one in bottom frame so this is redundant



# Widgets and layout
#one = Label(root, text="one", bg="salmon", fg="white")
#two = Label(root, text="two", bg="salmon", fg="white")
#three = Label(root, text="three", bg="blue", fg="white")

#one.pack()
#two.pack(fill=X) # Will fill in the X Direction, stetch and shrink depending on size of window
#three.pack(side=LEFT, fill=Y) # Fills in the Y direction



# A grid Layout, making a grid a layout
#label_name = Label(root, text="Name:");
#label_password = Label(root, text="Password:");
#entry_name = Entry(root)
#entry_password = Entry(root)

#label_name.grid(row=0, sticky=E) # column is defaulted to zero, everything is also center aligned in their columns be default.
# Sticky is a parameter to change alignment North East South West
#entry_name.grid(row=0, column=1, sticky=E)
#label_password.grid(row=1)
#entry_password.grid(row=1, column=1)
# Column spanning
#c = Checkbutton(root, text="Keep me logged in.")
#c.grid(row=3, columnspan=2)


# Calling Functions with buttons
#def printName():
#    print("You pressed my button!")
#def printEvent(event):
#    print("You did something that caused an event")

#button = Button(root, text="My Button", command=printName) # calls printName()
#button = Button(root, text="My Button")
#button.bind("<Button-1>", printEvent)
#button.pack();



# Mouse click events
#def leftClick(event):
#    print("left")
#def middleClick(event):
#    print("middle")
#def rightClick(event):
#    print("right")
#frame = Frame(root, width=300, height=250) # can set the pixel size. of the invisible frame
#frame.bind("<Button-1>", leftClick)
#frame.bind("<Button-2>", middleClick)
#frame.bind("<Button-3>", rightClick)
#frame.pack()


# Using Classes
class buttons:

    def __init__(self, master): #initialize an object, master means root or main window. Same thing as root window.
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT);

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT);

    def printMessage(self):
        print("I pressed Print Message");


#



b = buttons(root)
root.mainloop() # runs the window in a loop, keeps the window up without closing it
