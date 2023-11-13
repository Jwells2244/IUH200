#__repr__ and __str__
# "time(4, 15, 0) " is the kind of string repr produces, whereares str produces 4:15am

#encapsulation: a layer of seperation between the programmer who is defining the class and the programmer
# who is using the class as part of their program

# The programmer who is defining the class absolutely needs to know exactly what attributes the class has,
# what format the data is being stored in, and other implementation details.

#The progammer who is using the class doesn't neccesarily need to know all that info. They need to have some way
#to retrieve the data being stored, and maybe need some way to change the data

#If we just leave the attributes as public, then there's no seperation here. The user programmers can just directly access
#and alter the attributes directly

#But if the data needs to be in a particular format for everything to work, we don't want other programmers to directly
#modify the attributes or they could mess up that format

#So instead of allowing direct access to the attributes, we will make methods that can retrieve the data *accessors* in the 
#attributes and methods that can alter the data in the attributes *settors or mutators*

#Another reason to practice encapsulation like this is when the way you are storing the data isn't really in the format people
#want when they use that data

#In python, when we declare that an attribute is private, we are saying that programmers using our class shouldn't directly
#access the attributes, and should only use the getters and/or setters

#To indicate an attribute is private, we give it a name that starts with an underscore

#####
from math import gcd

class Fraction:
    """Represents a rational number - (a ratio of integers)"""

    #Private attributes
    # _numerator (an int)
    # _denominator (a nonzero int)

    def __init__(self, numerator, denominator=1):
        """Initializes the given fraction with the given numerator and denominator.
        Fraction, int, int -> None"""

        if denominator == 0:
            raise ZeroDivisionError("denominator must not be zero")

        self._numerator = numerator
        self._denominator = denominator
        self.simplify()

    def simplify(self):
        """Raises an error if the denominator is zero and converts to the lowest terms.
        Fraction -> None"""
        if self._denominator == 0:
            raise ZeroDivisionError("Denominator must not be zero")

        GCD = gcd(self._numerator, self._denominator)
        self._numerator = self.get_numerator()//GCD
        self._denominator = self.get_denominator()//GCD

    def get_numerator(self):
        """Returns the numerator
        Fraction -> Int"""
        return self._numerator

    def get_denominator(self):
        """Returns the denominator
        Fraction -> Int"""
        return self._denominator

    #Quiz 11A
    def __repr__(self):
        """This repr method enables the numerator and denominator to be viewed by a human
        Fraction -> String"""
        return "Fraction("+repr(self.get_numerator()) +", "+ repr(get_denominator()) +")"

    #So far we have getters, but no setters. This means you can create a fraction and access it's data,
    #but you can't change a fraction once it's created. This allows you to create a class that mimics an inmutable
    #data type. If you want programmers using your class to be able to modify a fraction after it's created, then you
    #should provide setters.

    def set_value(self, numerator, denominator):
        """Changes the value of self to have the given numerator and denominator
        Fraction, int, int -> None """
        self.__init__(numerator, denominator)

    def set_numerator(self, numerator):
        """Changes the numerator of self
        Fraction, int -> None"""
        self._numerator = numerator
        self.simplify()
    
    #Set denominator would be very similar
    #The magic method eq get called every time you try to compare one Fraction to something else using ==

    def __eq__(self, other):
        """Since fractions are already simplified, compares numerators and denominators
        Fraction, Fraction -> Boolean"""
        try:
            return (self.get_numerator() == other.get_numerator()) and \
                   (self.get_denominator() == other.get_denominator())
        except AttributeError:
            return False
        #We could add clauses here so that if other is a number of some type, we could do a more sophisticated comparison

    def to_float(self):
        """Returns the value of self as a floating point number
        Fraction -> Float"""
        return self.get_numerator() / self.get_denominator()

    def __str__(self):
        """Returns a string of the form numerator/denominator
        Fraction -> String"""
        return str(self.get_numerator()) + " / " + str(self.get_denominator())
        
    def __mul__(self, other):
        """Returns the product of self and other
        Fraction, Fraction-> Fraction"""
        return Fraction(self.get_numerator() * other.get_numerator(), self.get_denominator() * other.get_denominator())

    #If you create an attribute with a name that starts with two underscores, Python makes it so that you can only use
    # the name inside of the class definition, and outside of the class definition, the name of the attribute is *munged*, which
    # means that it has some extra characters added to the beginning, making it very unlikely that someone would accidentally
    #override that attribute.
    
        
        
