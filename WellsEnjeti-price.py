
class Price:
    """Stores information for representing a cost, measured in dollars
    and cents

    Attributes:

    price_in_cents
        an int
    """
    def __init__(self, dollars=00, cents=00):
        """Initializes self using the given dollars and cents amount
        Price, Int, int -> None"""
        if isinstance(dollars, str):
            unformatted = str(dollars)[1:]
            self.price_in_cents = ""
            for letter in unformatted:
                if letter != ".":
                    self.price_in_cents += letter
            self.price_in_cents = int(self.price_in_cents)
        elif "." in str(dollars):
            self.price_in_cents = round(dollars, 2)
        elif dollars == 00 and cents == 00:
            self.price_in_cents = 0
        else:
            self.price_in_cents = int(str(dollars)+str(cents))

    def get_dollars_part(self):
        """This method returns the amount of dollars in the int price_in_cents
        Price -> int"""
        return int(str(self.price_in_cents)[0: len(str(self.price_in_cents))-2])

    def get_cents_part(self):
        """This method returns the amount of cents in the int price_in_cents
        Price -> int"""
        return int(str(self.price_in_cents)[len(str(self.price_in_cents))-2:])

    def __repr__(self):
        """Returns a string of the form Price(dollars, cents)
        Price -> String"""
        if self.price_in_cents == "0"0:
            return "Price(0)"
        return "Price("+str(Price.get_dollars_part(self))+", " + str(Price.get_cents_part(self))+")"

    def __str__(self):
        """This method produces a string that represents the price to the user
        Price -> String"""
        returnString = "$"
        if len(str(self.price_in_cents)) == 1:
            returnString += str(self.price_in_cents)
        else:
            returnString += str(Price.get_dollars_part(self)) + "." + str(Price.get_cents_part(self))
        return returnString
        



