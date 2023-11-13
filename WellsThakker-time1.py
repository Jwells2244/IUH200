
#Question 1

class Time:
    """Stores information for representing a time, measured with hours, minutes, and whether it's AM or PM

    Attributes:

    _hours
        an int

    _minutes
        an int

    _ampm
        a string
    """
    #D
    def __init__(self, hours, minutes=00, ampm="AM"):
        """Initializes self using the give hours, minutes, and ampm arguments
        Time, int, int, string -> None
        OR
        Time, String -> None"""
        if isinstance(hours, str):
            hoursList = hours.split(":")
            hours2 = hoursList[1]
            self.set_hour(int(hoursList[0]))
            self.set_minute(int(hours2[0:2]))
            if hours2[2:].upper() == "AM":
                self.set_AM()
            elif hours2[2:].upper() == "PM":
                self.set_PM()
            else:
                raise ValueError("Error: AM/am or PM/pm is not on the end of the passed string")
        else:
            self.set_hour(hours)
            self.set_minute(minutes)
            if ampm.upper() == "AM":
                self.set_AM()
            elif ampm.upper() == "PM":
                self.set_PM()
            else:
                raise ValueError("Error: ampm string needs to equal AM/am or PM/pm")

    #B
    def set_hour(self, integer):
        """Sets the hours of the Time object to the given integer, if its between 1-12
        Time, int -> None"""
        if integer in range(1, 13):
            self._hours = integer
        else:
            raise ValueError("Error: Hour given not between 1-12")

    def set_minute(self, integer):
        """Sets the minute of the Time object to the given integer, if its between 0-59
        Time, int -> None"""
        if integer in range(0,60):
            self._minutes = integer
        else:
            raise ValueError("Error: Minutes given not between 0-59")

    #C
    def set_AM(self):
        """Sets the ampm property of the time object to "AM"
        Time -> None"""
        self._ampm = "AM"

    def set_PM(self):
        """Sets the ampm property of the time object to "PM"
        Time -> None"""
        self._ampm = "PM"

    def get_hour(self):
        """Returns the hour
        Time -> int"""
        return self._hours
    
    def get_minute(self):
        """Returns the minute
        Time -> int"""
        return self._minutes
    
    def get_AMPM(self):
        """Returns AM or PM depending on whether the time is AM or PM
        Time -> str"""
        return self._ampm
    
    def __repr__(self):
        """Returns a string in the form of Time(hour,minute,AM/PM)
        Time -> str"""
        return "Time(" + str(self.get_hour()) + ", " + str(self.get_minute()) + ", " + self.get_AMPM() + ")"
    
    def __str__(self):
        """Returns a string in the form of hour:minute am/pm
        Time -> str"""
        return str(self.get_hour()) + ":" + str(self.get_minute()).zfill(2) + self.get_AMPM()
    
    def __eq__(self, other):
        """This function takes a Time, and then a second Time, and checks to whether they are equivalent,
        returning a boolean
        Time, time -> Boolean"""
        if self.get_hour() == other.get_hour():
            if self.get_minute() == other.get_minute():
                if self.get_AMPM() == other.get_AMPM():
                    return True 
        else: 
            return False
    
    def __gt__(self, other):
        """This function takes a Time, and then a second Time, and checks to whether the first is greater then the second,
        returning a boolean
        Time, time -> Boolean"""
        if self.get_AMPM() == "PM" and other.get_AMPM() != " PM":
            return True
        else:
            if other.get_AMPM() == "PM" and self.get_AMPM() != " PM":
                return False
            else:
                if self.get_hour() == 12 and other.get_hour == 12:
                    if self.get_minute() > other.get_minute():
                        return True
                    elif self.get_minute() < other.get_minute():
                        return False
                elif self.get_hour() == 12 and other.get_hour() != 12:
                    return False
                elif self.get_hour() != 12 and other.get_hour() == 12:
                    return True
                else:
                    if self.get_hour() > other.get_hour():
                        return True
                    elif self.get_hour() < other.get_hour():
                        return False
                    else:
                        if self.get_minute() > other.get_minute():
                            return True
                        elif self.get_minute() < other.get_minute():
                            return False
                
            
            

    
    
