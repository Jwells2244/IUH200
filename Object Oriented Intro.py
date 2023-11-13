#Object Oriented Programming (OOP)

#an object has a type, and each type comes with data it needs to store as well as tools
#for working with that data.

#Data is stored in *member variables/attributes
#Tools for working with that data are created by defining member functions, also known as methods

#Just about everything we do using operators and many keywords is handled by hidden methods called magic
#methods or __methods__
#When you add 5 and 7, the int method .__add__ is called for 5, with the extra argument 7

#Today we are going to create our own datatypes called classes

#To make our own class, we need to decide: what data needs to be stored for each object, and how should it be stored?
#and what do we want to do with that data

#Let's create a class for storing information about books

class Book:
    """Stores information about a book

    Attributes:

    title
        a string

    author
        a string

    price
        a float
    """
#We want to be able to create a Book object using commands like
#Book("1984", "George Orwell", 8.99)
    def __init__(self, title, author, price):
        """Initializes self using the given title, author, and price
        Book, str, str, float -> None"""
        self.title = str(title)
        self.author = str(author)
        try:
            self.price = float(price)
        except:
            self.price = 0.0
    #Quiz 10B
    #Fix this init method so that .title and .author are always strings, and .price is always a price

    def discount(self, discount):
        """Reduces the price by the percentage given
        Book, number -> None"""
        self.price = self.price * (1-(discount/100))
    #To tell python how to create a string that represents a Book object as a line of code, such as when the interactive
    #shell displays a Book object or when an error message displays a book object, we define the .__repr__ method

    def __repr__(self):
        """Return a string of the form Book(title, author, price)
        Book -> String"""
        return "Book(" + repr(self.title) + ", " + repr(self.author) + ", " + repr(self.price) + ")"
