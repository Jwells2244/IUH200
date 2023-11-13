#Importing modules

##from math import pi
##from math import (sin,cos,tan)

#A command like this ^^ takes all of the definitions from the module named math (which is either one of
#the modules packaged with your python distribution or the one you have installed using pip or is just the name
# of a python file in the same directory as the script and makes them accessible to you as part of the math namespace

#If you want to import speciifc definitions directly into the main namespace (no math.), you can use the from-import
#notation
#Or to get everything, you can write from math import *


#################
from tkinter import *
#tkinter has all the tools for creating TCL code from Python code, and for executing that TCL code to create windows
#and similar things on your machine

from tkinter.ttk import *
#ttk has modern versions of definitions for various widgets: Labels, Buttons, Scrollbars, etc.

##root = Tk()
###a Tk object representing the main window of our application
##
##frm = Frame(root, padding=10)
###This creates a Frame object which has all the tools for positioning the widgets inside of it
##
##frm.grid()
###this sets up the frms geometry manager as a grid, meaning each widget inside of it will be positioned using a row and
###a column number (starting with row 0 and column 0 in the upper left corner of the window
##
##greeting_Label = Label(frm, text="Hello World")
##greeting_Label.grid(row=0, column=0)
##
##quit_Button = Button(frm, text="Quit", command=root.destroy)
##quit_Button.grid(row=0, column=1)
##
##root.mainloop()
#This command continues to run and wait for user input in the window such as button presses or text entry and updates
#the widgets inside it accordingly

#A slightly more realistic way to implement this is to create a subclass of the Tk object that contains all of it's widgets as
#attributes

class Main_Window(Tk):
    """The main window for our application"""

    def __init__(self):
        """Sets up the main window and all its widgets.
        Main_Window -> None"""
        super().__init__()
        self.counter = IntVar()
        self.counter.set(0)
        self.add_amt = StringVar()

        self.create_widgets()

    def create_widgets(self):
        """Creates all the widgets for self
        Main_window -> None"""
        self.frame = Frame(self, padding = 10)
        self.frame.grid()

        self.greeting_Label = Label(self.frame, text="Hello World")
        self.greeting_Label.grid(row=0, column=0)

        self.quit_Button = Button(self.frame, text="Quit", command=self.destroy)
        self.quit_Button.grid(row=0, column=1)
    
        self.count_Button = Button(self.frame, text="Count", command=self.increase_count)
        self.count_Button.grid(row=0, column=2)

        self.counter_Label = Label(self.frame, textvariable=self.counter)
        self.counter_Label.grid(row=1, column=2)

        self.add_amt_Entry = Entry(self.frame, textvariable=self.add_amt)
        self.add_amt_Entry.grid(row=2, column=3)

        self.add_Button = Button(self.frame, text="Add the amount", command=self.add)
        self.add_Button.grid(row=0, column=3)

        #Tkinter provides classes called string var, int var, etc. Which are mutable versions of the class str, int, etc. types,
        #that when updated, informs any widget connected to them that they've been updated

    def increase_count(self):
        """Increases counter by 1
        Main_window -> None"""
        self.counter.set(self.counter.get()+1)

    def add(self):
        """increases the counter by whatever is in the text entry box.
        Main_Window -> None"""
        try:
            int(self.add_amt.get())
            self.counter.set(self.counter.get()+int(self.add_amt.get()))
        except:
            print("Enter a number next time: ")
#If you wanted to make a new window pop up with an error message, you could create a new class for an error window
#with it;s own frame and widgets for the error message, and an accept button or something




root = Main_Window()
root.mainloop()

#Quiz 14A Add a .count attribute to the Main_Window class and create a second button that increases count when it is
#Quiz 14B make it so if the user types in a non numeric value, no error is raised
