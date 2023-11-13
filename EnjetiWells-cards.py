#2
class Card:
    """Store information about playing cards' rank, suit, and caste. The rank can be represented with the intgers
    0-9; the suits are represented as "t" -> triangle, "s" -> square, and "p" -> pentagon;
    the caste is represented as "r" -> royal and "c" -> common.

    Attributes:

    rank
        an integer
    suit
        a string
    caste
        a string
    """

    def __init__(self, rank, suit, caste):
        """Initializes self using the given rank, suit, and caste.
        Card, int, str, str -> None"""
        self.rank = rank
        self.suit = suit
        self.caste = caste

        self.get_rank()
        self.get_suit()
        self.get_caste()

    def get_rank(self):
        """Rank of the Card.
        Card -> None"""
        self.get_rank = int(self.rank)

    def get_suit(self):
        """Suit of the card.
        Card -> None"""
        if self.suit.casefold() == "t":
            self.get_suit = "triangles"
        if self.suit.casefold() == "s":
            self.get_suit = "squares"
        if self.suit.casefold() == "p":
            self.get_suit = "pentagons"

    def get_caste(self):
        """Caste of the card.
        Card -> None"""
        if self.caste.casefold() == "r":
            self.get_caste = "royal"
        if self.caste.casefold() == "c":
            self.get_caste = "common"

    def __repr__(self):
        """Returns a string of the form Card(rank, suit, caste).
        Card -> str"""
        return "Card(" + repr(self.rank) + ", " + repr(self.suit.casefold()) + ", " + repr(self.caste.casefold()) + ")"

    def __str__(self):
        """Returns a string of the form "rank of caste suit".
        Card -> str"""
        return str(self.get_rank) + " of " + self.get_caste + " " + self.get_suit


    def __gt__(self, Card):
        """Returns True if self is greater than Card and returns False otherwise.
        Card, Card -> bool"""

        suit_rank = {"triangles": 1, "squares": 2, "pentagons": 3}
        
        if self.get_caste != Card.get_caste:
            if self.get_caste > Card.get_caste:
                return True
            else:
                return False
        elif self.get_suit != Card.get_suit:
            if suit_rank[self.get_suit] > suit_rank[Card.get_suit]:
                return True
            else:
                return False
        else:
            if self.get_rank > Card.get_rank:
                return True
            else:
                return False
            
            
            





    
