#Final Practical Questions
from math import factorial, sqrt
from random import *

#a
def shorten(list1):
    """This function takes a list of numbers, and removes the largest number from the list, does not modify if the
    list is empty
    list -> list"""
    if list1 == []:
        return list1
    else:
        largest = list1[0]
        for ind in range(len(list1)):
            if largest < list1[ind]:
                largest = list1[ind]
        list1.remove(largest)
        return list1


#b
def no_zeros(dic):
    """Takes a dictionary and returns True if none of the values equal 0
    dictionary -> Boolean"""
    for key in dic:
        if dic[key] == 0:
            return False
    return True



#c
def iterations(start, func, num):
    """This function takes a start value, a function, and a number of times to apply that function in a list
    num, Function, num -> List"""
    returnList = [start]
    for i in range(num):
        returnList.append(func(returnList[i]))
    return returnList

#d
def square_sum(n):
    """This function takes a non negative integer n, and returns the sum of all perfect squares up to and including n
    Integer >= 0 -> Integer"""
    if n == 0:
        return n
    else:
        return n**2 + square_sum(n-1)


#2
class Circle:
    """This is a class used to represent a circle, using a radius, and a tuple of the vertex (h, k)
    attributes:

    Im assuming these can be public
    .radius
        an int

    .vertex:
        a 2 element tuple
    """

    def __init__(self, radius, vertex=(0,0)):
        """Initializes self with the given radius and vertex
        Circle, integer, two-element-tuple -> None"""
        self.radius = radius
        self.vertex = vertex

    def __repr__(self):
        """Returns a string in the form Circle(radius, vertex)
        Circle -> String"""
        return "Circle("+repr(self.radius)+", "+repr(self.vertex)+")"

    def __str__(self):
        """Returns a string in the form of a circle with a radius of # and the center at (#,#)
        Circle -> String"""
        return "A circle with a radius of " + str(self.radius) + ", and a center at " + str(self.vertex) + "."

    def move(self, x, y):
        """Adds x and y to the first and second element of self.vertex respectively
        Circle, int, int -> None"""
        newTuple = (self.vertex[0]+x, self.vertex[1]+y)
        self.vertex = newTuple

    def __eq__(self, other):
        """Returns true if self is equal to other, false if not
        Circle, Circle -> Boolean"""
        if self.radius == other.radius:
            if self.vertex == other.vertex:
                return True
            else:
                return False
        else:
            return False


#3

#a
class Oracle:
    """This class represents a mystic seer who can answer any question

        attributes
        .choices:
            a list of strings
    """
    def __init__(self, choices):
        """Intializes self to the given choices if it is a list, if it is a text file, sets self.choices to a list of words from that file
        Oracle, list of strings or string -> None"""
        if isinstance(choices, str):
            with open(choices, "r")  as file:
                choiceList = []
                while True:
                    line = file.readline()
                    choiceList.append(line)
                    if line == "":
                        break
            self.choiceList = choiceList
        else:
            self.choiceList = list(choices)

    def __repr__(self):
        """Returns a string in the form of Oracle([list of strings])
        Oracle -> String"""
        return "Oracle("+repr(self.choiceList)+")"

    def get_choices(self):
        """Returns the list of choices
        Self -> None"""
        return self.choiceList
    
    def consult(self):
        """This function randomly returns one of the strings in self.choices
        Oracle -> String"""
        element = choice(self.choiceList)
        return element


#3b             
class Mega_Oracle(Oracle):
    """Subclass of Oracle that counts the amount of times that Oracle has been consulted

    """
    #Private Attributes:
    #_count
        #an int

    def __init__(self, choices):
        """Initializes self with the given choices, with choices either being a text file or a list of string
        Mega_Oracle, str/list of strings -> None"""
        super().__init__(choices)
        self._count = 0

    def consult(self):
        """This function randomly returns one of the strings in the given list
        Mega_Oracle -> String"""
        self._count += 1
        return super().consult()
        

    def get_count(self):
        """Returns the amount of times the oracle has been consulted
        Mega_Oracle -> int"""
        return self._count

    def __repr__(self):
        """Returns a string in the form Mega_Oracle(choices)
        Mega_Oracle -> None"""
        return "Mega_Oracle("+repr(self.choiceList)+")"

#PTree
#A PTree is a tree where every node except the root and the leaves, is labeled as a single character string


#4

def match(pt, string):
    """Takes a PTree and a string and returns true if the PTree matches the string, and false otherwise
    PTree, String -> Boolean"""
    for val in pt:
        if val == string[0]:
            if len(string) == 1:
                return True
            else:
                return match(pt[val], rest(string))
    return False



def rest(string):
    """Takes a string and returns the string without the first character
    String -> String"""
    return string[1:]



#Testing
pt1 = {"a":{"":{}, "b" : {"":{}}, "c" : {"":{}}}, "d" : {"e" : {"" :{}}}}
pt2 = {"a" : {"" : {}, "b" : {"" : {}}, "c" : {"" : {}}}, "d" : {"e" : {"": {}}}}




        
        
