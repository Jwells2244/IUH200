#When you use open() to create a file object, the mode tells python the intended purpose of the file

#The defualt mode "r" is read mode, meaning the file is supposed to already exist, and you intend
#to access it's contents

#'w' is for "write" mode, in which case a new file is created, and you intend to put content in that file
#this enables the .write method and this allows you to write content into the file in stages if you like

#If there is already a file with the given name, the file is immediatley overwritten with a new blank text
#file with no warning, and no way to retrieve the old contents. This is a problem

#So don't use w mode. It is way too dangerous
#Instead, there's a mode called "x" (for exclusive create) which acts exactly like "w" when there isnt a file with
#the same name, but will raise a FileExistsError, if you try to create a file when there's already a file with that
#name

#there is also the mode "a" (for append) where the file must already exist, but the intention is that .write will add
#text to the end of the existing file (without overwriting the existing contents)


pd1 = {"fries":3.49,"burger":5.99,"sandwich":4.99}


def pricedict_to_tsv(pricedict, filename):
    """Writes the content of pricedict to a tab-seperated-values file. Returns true if succeeds, false if error occurs"""
    #pricedict, string -> boolean
    try:
        with open(filename,"x") as file:
            for itemName in pricedict:
                file.write(item_name)
                file.write("\t")
                file.write(str(pricedict[itemName]))
                file.write("\n")
        return True
    except OSError:
        return False

#Quiz 7a
def tsv_to_pricedict(filename):
    """Opens a given file and returns a pricedict based on the data in the file, which should be a tab seperated value
    (One line per item, item name first, then price"""
    #filename -> pricedict
    pd = {}
    try:
        with open(filename) as file:
            for line in file:
                splitList = line.split("\t")
                pd[splitList[0]] = float(splitList[1].strip())
        return pd
    except OSError:
        return {}
    return None


#Polymorphism is a function that works on multiple types
#Polymorphic signatures
#bisect:
    #Number -> number , or sequence -> Sequence
    #or number | sequence -> number | sequence
    #The first one is slightly more specific
        
        
            
    
