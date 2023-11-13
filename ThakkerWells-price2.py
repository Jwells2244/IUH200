#1
class Price:
    """Represents cost measured in dollars and cents.

    Attributes:

    Price_in_cents
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
#1A
    def __add__(self, other):
        """Takes two price objects, and adds them together
        Price, Price -> Price"""
        self.price_in_cents = (self.get_dollars_part() + other.get_dollars_part()) * 100
        if self.get_cents_part() + other.get_cents_part() > 99:
            tempCents = self.get_cents_part() + other.get_cents_part()
            self.price_in_cents += 100
            tempCents = tempCents - 100
            self.price_in_cents = self.price_in_cents + tempCents
            return Price(self.price_in_cents // 100, tempCents)
        else:
            self.price_in_cents = self.price_in_cents + (self.get_cents_part() + other.get_cents_part())
            tempCents = self.get_cents_part() + other.get_cents_part()
            return Price(self.price_in_cents//100, tempCents)

#1B
    def __mul__(self, other):
        """This takes a Price object, and an integer, and returns a price object multiplied by the num
        Price, num -> Price"""
        if isinstance(other, Price):
            raise TypeError("Should be an int, not a price")
        else:
            self.price_in_cents = self.price_in_cents * other
            return Price(int(self.price_in_cents // 100), int(self.price_in_cents % 100))
#Bonus
    def __rmul__(self, other):
        """This function works the same as the __mul__ method, and returns a price object multiplied by the num
        Price, num -> Price"""
        if isinstance(other, Price):
            raise TypeError("Should be an int, not a price")
        else:
            self.price_in_cents = self.price_in_cents * other
            return Price(int(self.price_in_cents // 100), int(self.price_in_cents % 100))






