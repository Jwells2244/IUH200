#Topics for the midterm

#Loops, conditionals, functions, data types, user input and output,

#String, Int, Float, Boolean, tuples, Lists, Dictionaries, None, set, File/TextIOWrapper, Exception(OSError,)
#function, range
#Sets are dictionaries without a key/value relationship, cannot do indexes, can use .add(), and .remove()

#Lists (.append, del(index or slice), .remove, item/slice assignment)

#Type categories
#Number, Iterable(For loops), Sequence(Indexes, slices, concatenation, len), container (len, in)

#Tuples are inmutable
#Lists are Mutable

#Informal data definitions

#try/except/raise
#with-as with files to make sure they close

#Function terminology
#Signature, purpose statement, docstring
    #Signature = int -> List
    #Purpose statement - Description of what the function does
    #Docstring = The area on the first line of the function that contains the purpose statement and signature
#Argument, return, break
#Scope
#Local and global variables - Global variables can be used in a function, but not changed

#Working with files
#File modes: "r", "w", "x", "a"
#with open("FileName", "x") as file:

#"r" = read
#"w" = getting rid of the current file data and replacing it with a new file (dangerous, not used)
#"x" = checks to see if the file exists, then tries to write in it
#"a" = pen, adding stuff to the end of the file

#.read()-returns the remaining contents of the file based on where the pointer is, .read(3), .readline(), using a for loop
#.write
#.seek and .tell
#.seek(20) will jump to the 20th character
#.tell(will tell where you are)

#######

#.upper returns an upercased version of the original string
#sorted() returns a sorted copy of the list
#sort returns the original list sorted

#String methods
    #.casefold/.upper/.lower
    #isupper()/.islower/.isdigit
    #.replace()
    #.find()/.index() same thing. Finds the first index of the argument, and -1 if nothing
    #.count()
