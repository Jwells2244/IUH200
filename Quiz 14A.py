class Main_Window(Tk):
    """The main window for our application"""

    def __init__(self):
        """Sets up the main window and all its widgets.
        Main_Window -> None"""
        super().__init__()
        self.create_widgets()
        self.counter = 0

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

    def increase_count(self):
        """Increases counter by 1
        Main_window -> None"""
        self.counter += 1
        print(self.counter)


root = Main_Window()
root.mainloop()
