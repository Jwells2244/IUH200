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
