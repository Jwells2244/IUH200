
#Question 1

class Time:
    """Stores information for representing a time, measured with hours, minutes, and whether it's AM or PM

    Attributes:

    _minutes_after_midnight
        an int
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
        """Adds 60*integer to minutes after midnight, if its between 1-12
        Time, int -> None"""
        if integer in range(1, 13):
            self._minutes_after_midnight = 0 + (integer*60)
        else:
            raise ValueError("Error: Hour given not between 1-12")

    def set_minute(self, integer):
        """Adds the integer to minutes after midnight, if its between 0-59
        Time, int -> None"""
        if integer in range(0,60):
            self._minutes_after_midnight += integer
        else:
            raise ValueError("Error: Minutes given not between 0-59")

    #C
    def set_AM(self):
        """Minuses 720 to the minutes after midnight, to signify the loss of 12 hours
        Time -> None"""
        self._minutes_after_midnight = self._minutes_after_midnight - 720

    def set_PM(self):
        """Adds 720 to the minutes after midnight, to signify the addition of 12 hours"
        Time -> None"""
        self._minutes_after_midnight = self._minutes_after_midnight + 720

    def get_hour(self):
        """Returns the hour
        Time -> int"""
        if self._minutes_after_midnight > 720:
            remainder = (self._minutes_after_midnight-720) % 60
            hours = int(((self._minutes_after_midnight-720) - remainder) / 60)
        else:
            remainder = self. _minutes_after_midnight % 60
            hours =  int((self. _minutes_after_midnight - remainder) / 60)
        if hours == 0:
            return 12
        else:
            return hours
    
    def get_minute(self):
        """Returns the minutes
        Time -> int"""
        return self._minutes_after_midnight % 60
    
    def get_AMPM(self):
        """Returns AM or PM depending on whether the time is AM or PM
        Time -> str"""
        if self._minutes_after_midnight > 720:
            return "PM"
        else:
            return "AM"
    
    def __repr__(self):
        """Returns a string in the form of Time(hour,minute,AM/PM)
        Time -> str"""
        return "Time(" + repr(self.get_hour()) + ", " + repr(self.get_minute()).zfill(2) + ", " + repr(self.get_AMPM()) + ")"
    
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
                
            
            

    
    
