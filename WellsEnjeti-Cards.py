

class Card:
    """Stores information for representing a playing card, measured with suit, caste, and rank

    Attributes:

    suit
        a string

    caste
        a string

    rank
        an int
    """
    def __init__(self, rank, caste, suit):
        """Initializes self using the given suit, caste, and rank arguments
        Card, String, String, Int -> None"""
        self.rank = int(rank)
        self.caste = caste
        lowerSuit = suit.lower()
        if lowerSuit == "triangles" or lowerSuit == "triangle":
            self.suit = "triangles"
        elif lowerSuit == "pentagons" or lowerSuit == "pentagon":
            self.suit = "pentagons"
        elif lowerSuit == "squares" or lowerSuit == "squares":
            self.suit = "squares"
        lowerCaste = caste.lower()
        if lowerCaste == "common":
            self.caste = "common"
        elif lowerCaste == "royal":
            self.caste = "royal"

    def get_rank(self):
        """Returns the rank of the card as an int
        Card -> Int"""
        return self.rank

    def get_suit(self):
        """Returns the suit of the card as a string
        Card -> Plural string"""
        return self.suit

    def get_caste(self):
        """Returns the string of the cast of the card
        Card -> String"""
        return self.caste

    def __repr__(self):
        """Returns a string in the form Card(rank, caste, suit)
        Card -> String"""
        return "Card("+str(Card.get_rank(self))+", " + Card.get_caste(self) +", " + Card.get_suit(self) + ")"

    def __str__(self):
        """Returns a string in the form: rank of caste suit
        Card -> String"""
        return str(Card.get_rank(self)) + " of " + Card.get_caste(self) + " " + Card.get_suit(self)

    def __gt__(self, other):
        """This function takes a Card, and then a second card object, card1, and returns a True or False depending
        on whether Card is bigger than card1
        Card, card -> Boolean"""
        if self.caste == other.caste:
            if self.suit == other.suit:
                if self.rank < other.rank:
                    return False
                else:
                    return True
            elif self.suit == "pentagons" and other.suit != "pentagons":
                return True
            elif self.suit == "squares" and other.suit != "squares":
                return True
            elif other.suit == "pentagons" and self.suit != "pentagons":
                return False
            elif other.suit == "squares" and self.suit != "squares":
                return False
        elif self.caste == "royal" and other.caste == "common":
            return True
        else:
            return False
        
