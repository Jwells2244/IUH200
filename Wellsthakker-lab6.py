#Lab 6, Jonathan Wells, Devin Thakker


#Question 1 A
def half_of(arg):
    """this function takes an argument and returns half of the number if the arg is a float or int,
    and half of the string, tuple, or list if it's not a number. If it is nothing it will return an error string"""
    #One of Str-Float-Int-Tuple-List -> The same type that came in
    if isinstance(arg, int) or isinstance(arg, float):
        return(arg/2)
    elif isinstance(arg, str) or isinstance(arg, list) or isinstance(arg, tuple):
        return arg[0:int((len(arg))/2)]
    else:
        raise TypeError("is not an int, float, str, tuple, or list.")
        
#Question 1 B

def bisect(arg):
    """This function does a similar thing to half off, except for it doesn't need to use the is instance, and instead
    uses a try and except"""
    #One of Str-Float-Int-Tuple-List -> The same type that came in
    try:
        return(arg/2)
    except:
        try:
            return(arg[slice(0,int(len(arg)/2))])
        except:
            raise TypeError("is not an int, float, str, tuple, or list.")
       # raise TypeError("is not an int, float, str, tuple, or list.")
    
    
