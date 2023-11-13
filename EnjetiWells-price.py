#1
class Price:
    """Represents cost measured in dollars and cents.

    Attributes:

    Price
        an integer
    """

    def __init__(self, dollars=0, cents=0):
        """Intializes self using the given dollars and cents.
        Price, int, int -> None"""
        self.dollars = dollars
        self.cents = cents
        self.price_in_cents = int(round((self.clean_dollars()*100), 0) + cents)

    def clean_dollars(self):
        """Removes "$" from self.price.
        Price -> float/int"""
        if isinstance(self.dollars, str):
            clean = self.dollars
            clean = float(clean[1:])
            clean = round(clean, 2)
            return clean
        else:
            return self.dollars

    def get_cents_part(self):
        """Returns the amount of cents in the given price.
        Price -> int"""
        if self.cents == 0:
            deci = str(self.clean_dollars()).find(".")
            if deci != -1:
                return self.price_in_cents - (self.get_dollars_part() * 100)
            else:
                return self.cents
        else:
            return self.cents

    def get_dollars_part(self):
        """Returns an integer representing the given dollars in price.
        Price -> int"""
        if self.cents == 0:
            deci = str(self.clean_dollars()).find(".")
            if deci != -1:
                return int((self.price_in_cents - int(str(self.clean_dollars())[deci+1:]))/100)
            else:
                return int((self.price_in_cents/100))
        else:
            return self.clean_dollars()

    def __repr__(self):
        """Returns a string of the form Book(dollars, cents).
        Price -> str"""
        return "Price(" + repr(self.get_dollars_part()) + ", " + repr(self.get_cents_part()) + ")"

    def __str__(self):
        """Returns a string of the form $dollars.cents.
        Price -> str"""
        return "$" + repr(self.get_dollars_part()) + "." + repr(self.get_cents_part())








