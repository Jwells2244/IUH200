#Graphical User Interface (GUI): The usual visual interface for a computer with windows, text boxes, buttons, scroll bars,
# etc., as opposed to the Command Line Interface (CLI)

# If you actually want to make GUIs with Python, you'll porbably use a module like Tkinter

#Today we are going to pretend that we are programming a GUI module like Tkinter, and we'll lay out some of the
#basic features that classes in such a module might need

#########################
#Things you might see inside of a GUI window

#Buttons
#Text box
#Scroll bars
#text labels,
#images
#video players
#sliders
#radio buttons
#toggle buttons, .....

#Each of these GUI items would need their own class definition, but there are a lot of features in common
#between all of these (location, size). To avoid duplicating code, it makes sense for each of these classes to be a subclass
#of a large superclas that carries the attributes and methods that all of these classes have in common. And all of the classes
#that have certain features in common (like all the button classes) probably should be subclasses of the same core
# Button class

#Inheritance is what allows us to make subclasses like this.

#We'll start with a big abstract class that all of these GUI items will be subclasses

class GUI_Item:
    """An item in a GUI window.

    attributes:

    .x_coord (an int, the upper-left corner of the item)

    .y_coord (an int, the upper-left corner of the item)

    width (an int)

    height (an int)"""

    def __init__(self, x, y, width, height):
        """Initializes the GUI_Item with the given location and size.
        GUI_ITem, int, int, int, int -> None"""
        self.x_coord = x
        self.y_coord = y
        self.width = width
        self.height = height

    def __repr__(self):
        """Returns a string of the form GUI_Item(x_coord, y_coord, width, height)
        GUI_Item -> String"""
        return "GUI_Item(" + repr(self.x_coord) + ", " + repr(self.y_coord) + ", " + repr(self.height) + ", " + repr(self.width) + ")"


#Lets make a subclass of GUI_Item for a button

class Button(GUI_Item):
    """A GUI_Item that can be clicked on.
    Attributes:

    .label (a str that is displayed on the button)

    .action (a function (Button -> None) to be executed when the button is clicked)
    """

    def __init__(self, x, y, width, height, action, label="Button"):
        """Initializes the button with the given location, size, action, and lab
        Button, int, int, int, int, (Button -> None), [str] -> None"""
        super().self.__init__(x, y, width, height)
        #Super() with no arguments returns an object that acts like self, but is treated as a member of the superclass
        #of the current class

        self.action = action
        self.label = label

    def __repr__(self):
        """Returns a string of the form Button(x_coord, y_coord, width, height, action, label)
        Button -> String"""
        return "Button("+ repr(self.x_coord) + ", " + repr(self.y_coord) + ", " + repr(self.height) + ", " + repr(self.width) +\
               ", " + repr(self.action) + ", " + repr(self.label) + ")"
    def click(self):
        """Method that is called when the user clicks on a button
        Button -> None"""
        self.actioon(self)


def do_nothing(obj):
    """Does nothing"""
    pass

def display_click(obj):
    """Testing"""
    print("Click!")
        
#Let's make a subclass of our button class called toggle button that acts just like a button, but has an on/off state

class Toggle_Button(Button):
    """Special kind of button that has an on/off state that toggles when you call it
    Attributes:

    .is_on (a boolean)
    """

    def __init__(self, x, y, width, height, action, label="Button", starting_state = False):
        """Initializes self with the given location, size, action, and lab
        Button, int, int, int, int, (Toggle_Button -> None), [str], [Boolean] -> None"""
        super().__init__(x, y, width, height, action, label)

        self.is_on = starting_state

    def __repr__(self):
    """Returns a string of the form Toggle Button(x_coord, y_coord, width, height, action, label, is_on)
    Toggle Button -> String"""
    return "Toggle_Button("+ repr(self.x_coord) + ", " + repr(self.y_coord) + ", " + repr(self.height) + ", " + repr(self.width) +\
           ", " + repr(self.action) + ", " + repr(self.label) + ", " + repr(self.is_on) + ")"

    #Quiz 12A
    def click(self):
        """Calls the action of clicking and changes the .is_on to True
        Toggle_Button -> None"""
        super().click()
        self.is_on = not self.is_on


        
