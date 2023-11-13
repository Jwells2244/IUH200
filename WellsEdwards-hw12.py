from tkinter import *

from tkinter.ttk import *

import random


class Main_Window(Tk):
    """The main window of our application"""

    def __init__(self):
        """Sets up the main window and all it's widgets
        Main_window -> None"""
        super().__init__()
        self.filename = StringVar()
        self.create_widgets()


    def create_widgets(self):
        """Creates all the widgets for self
        Main_window -> None"""
        self.frame = Frame(self, padding = 10)
        self.frame.grid()
        
        self.intro_Label = Label(self.frame, text="Welcome to File-Loader, V1.0", font=("Garamond", 20, "bold"))
        self.intro_Label.grid(row=0, column=0)
        

        self.info_Label = Label(self.frame, text="This program is a file opener used to display flashcards. Simply input the \n" \
                                "file name into the text box below, click the 'Go!' button, and if you've entered an \n appropriate file name that exists," \
                                " it will open up as flashcards!. \n If you get an error, either the file name is incorrect, or it doesnt exist!", justify="center", font=("Garamond", 18))
        self.info_Label.grid(row=1, column=0)

        self.filename_Entry = Entry(self.frame, textvariable=self.filename, justify="center")
        self.filename_Entry.grid(row=2, column=0)
        print(self.filename.get())
        self.go_Button = Button(self.frame, text="Go!", command=self.open_file)
        self.go_Button.grid(row=3, column=0)

    def open_file(self):
        """Attempts to open up a file with the name of self.filename
        Main_Window -> None"""
        temp = []
        indexlist = []
        counter = 1
        try:
            with open(self.filename.get()) as file:
                print("opened")
                while True:
                    if counter %3 != 0:
                        line = file.readline()
                        if line == "":
                            break
                        else:
                            indexlist.append(line)
                            counter += 1
                    else:
                        temp.append(indexlist)
                        indexlist = []
                        counter = 1

                print(temp)
            card1 = Card_Window(temp)
            
        except FileNotFoundError:
            self.fail_Label = Label(self.frame, text="Error, Filename either doesn't exist, or is spelled incorrectly!", justify="center", font=("Garamond", 12))
            self.fail_Label.grid(row=4, column=0)
            
class Card_Window(Toplevel):
    """The window that displays the flashcards"""

    def __init__(self, cardlist):
        """Sets up the flashcard window and all of it's cards
        Card_Window -> None"""
        super().__init__()
        cardlist[-1][1] = cardlist[-1][1]+"\n"
        self.cardList = cardlist
        random.shuffle(self.cardList)
        print(self.cardList)
        self.cardIndex = 0
        self.card = StringVar()
        self.frontVal = 0
        self.create_screen()

    def create_screen(self):
        """Creates the screen of the Card Window
        Card Window -> None"""
        self.frame = Frame(self, padding = 10, )
        self.frame.grid()

        self.card.set(self.cardList[self.cardIndex][self.frontVal])
        
        self.random_card_Label = Label(self.frame, textvariable=self.card, font=("Garamond", 16))
        self.random_card_Label.grid(row=2, column=0)

        self.flip_Button = Button(self.frame, text="Flip the card", command=self.flip_card)
        self.flip_Button.grid(row=3, column=0)

        self.next_Button = Button(self.frame, text="Next card->", command=self.next_card)
        self.next_Button.grid(row=4, column=0)

        self.previous_Button = Button(self.frame, text="Previous card <-", command=self.previous_card)
        self.previous_Button.grid(row=5, column=0)

        self.quit_Button = Button(self.frame, text="Home", command=self.destroy)
        self.quit_Button.grid(row=6, column=0)


    def flip_card(self):
        """Shows the opposite side of the current flashcard
        Card_Window -> None"""
        if self.frontVal == 0:
            self.frontVal = 1
        else:
            self.frontVal = 0
        self.card.set(self.cardList[self.cardIndex][self.frontVal])

    def next_card(self):
        """Goes to the next card in the deck
        Card_Window -> None"""
        if self.cardIndex == len(self.cardList)-1:
            pass
        else:
            self.cardIndex += 1

        self.frontVal = 1
        self.flip_card()

    def previous_card(self):
        """Goes to the previous card
        Card_Window -> None"""
        
        if self.cardIndex == 0:
            pass
        else:
            self.cardIndex -= 1

        self.frontVal = 1
        self.flip_card()

    


root = Main_Window()

root.mainloop()
        
