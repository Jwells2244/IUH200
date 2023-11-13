#HW 11

#1
ROOMS = {}

#2A
class Room:
    """Represents locations within a game

    Attributes:

    name (a string)

    number (an int)
    """
    #Private Attributes:
    #exits (Stores a list of room numbers)

    
    #2B
    def __init__(self, number, name):
        """Initializes self with the given number and name, and add a value to the global ROOMS
        Room, number, name -> None"""
        if not isinstance(number, int):
            raise TypeError("Error, number should be an integer")
        if not isinstance(name, str):
            raise TypeError("Error, name should be a string")
        self.number = number
        self.name = name
        ROOMS[self.number] = self
        self._exits = []

    #2C
    def __repr__(self):
        """Returns a string in the form Room(number, name)
        Room -> String"""
        return "Room("+repr(self.number)+", " + repr(self.name) + ")"

    #2D
    def get_exits(self):
        """Returns a list of the rooms that you can access from the current room
        Room -> List"""
        return self._exits

    #2E
    def connect_to(self, other):
        """Adds the room numbers of self and other to each of their exits attribute
        Room, Room -> None"""
        self._exits.append(other.number)
        other._exits.append(self.number)



#3
class Thing:
    """Represents physical objects within a game

    Attributes:

    name (a string)

    location (an int)"""
    #3B
    def __init__(self, name, location):
        """Initializes self with the given name and location
        Thing, string, int -> None"""
        self.name = name
        self.location = location

    #3C
    def __repr__(self):
        """Returns a string in the form Thing(name, location)
        Thing -> String"""
        return "Thing("+repr(self.name)+", "+repr(self.location)+")"

    #3D
    def __str__(self):
        """Returns a string in the form 'The Thing is in room-name(using location)
        Thing -> String"""
        return "The " + repr(self.name) + " is in " + str(ROOMS[self.location].name)


#4
class Openable(Thing):
    """Subclass of Thing that represents which Things can be opened

    Attributes:
    #4A
    is_open ( a boolean )
    """
    
    #4B
    def __init__(self, name, location, ope=False):
        """Initializes self using the given attributes, with a call to its super() init
        Openable, string, int, Bool -> None"""
        super().__init__(name, location)
        self.is_open = ope

    #4C
    def __repr__(self):
        """Returns a string in the form Openable(name, number, is_open)
        Openable -> String"""
        return "Openable("+repr(self.name) + ", " + repr(self.location) +  ", " + repr(self.is_open) +")"

    #4D
    def __str__(self):
        """Returns a string in the form The Name in location is open/closed
        Openable -> String"""
        if self.is_open:
            return "The " + str(self.name) + " in the " + ROOMS[self.location].name + " is open"
        else:
            return "The " + str(self.name) + " in the " + ROOMS[self.location].name + " is closed"

    #4E
    def try_open(self):
        """Attempts to open the Openable Self object. If successful, returns True. If not, returns False
        Openable -> Boolean"""
        if self.is_open:
            return False
        else:
            self.is_open = True
            return True

#5
class Lockable(Openable):
    """Subclass of Openable that represents whether the Thing that can be opened is locked or not
    Attributes:

    is_locked (a boolean)

    key (a Thing)
    """
#5B
    def __init__(self, name, location, key, is_open=False, is_locked=False):
        """Initializes self with the given name, location, key, open status, and locked status
        Lockable, string, int, Boolean, Boolean -> None"""
        super().__init__(name, location, is_open)
        self.key = key
        self.is_locked = is_locked

#5C
    def __repr__(self):
        """Returns a string in the form Lockable(name, location, Thing(name, location), is_open, is_locked)
        Lockable -> String"""
        return "Lockable("+repr(self.name) + ", " + repr(self.location) + ", " + repr(self.key) + ", " + repr(self.is_open) \
               + ", " + repr(self.is_locked) + ")"

#5D
    def __str__(self):
        """Returns a string in the form The name in the room-name (is open)/(closed, but unlocked)/(is locked)
        Lockable -> String"""
        if self.is_open:
            return "The " + str(self.name) + " in the " + str(ROOMS[self.location].name) + " is open"
        elif self.is_locked:
            return "The " + str(self.name) + " in the " + str(ROOMS[self.location].name) + " is locked"
        else:
            return "The " + str(self.name) + " in the " + str(ROOMS[self.location].name) + " is closed, but unlocked"

    
#5E
    def try_open(self):
        """This trys to open the Thing, if it is already open, or is locked, will return false. If it is closed and unlocked, returns True
        Lockable -> Boolean"""
        if self.is_locked:
            return False
        elif super().try_open():
            self.is_open = True
            return True
        else:
            return False

#5F
    def try_unlock_with(self, other):
        """Tries to unlock the lockable object if it's locked, with the key other, returns True if successful, False if not
        Lockable, Thing -> Boolean"""
        if self.is_locked:
            if self.key == other:
                self.is_locked = False
                return True
        else:
            return False
    
    
        
