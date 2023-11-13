def zero_out_first_3(L):
    """Replaces the first three items in L with 0's
    list -> None"""
    L[0:3] = [0,0,0]

fib = [1, 1, 2, 3, 5, 8, 13, 21]
print("fib = " + str(fib))
print("Running zero_out_first_3(fib)...")
zero_out_first_3(fib)
print("fib shound now be [0, 0, 0, 3, 5, 8, 13, 21]")
print("fib = " + str(fib))

print("")
print("")

def gir(str_list):
    """Replaces the last two items in str_list with the single string "gir".
    list-of-strings -> None"""
    str_list[-2:] = ["gir"]

names = ["zim", "gaz", "dib", "tak"]
print("names = " + str(names))
print("Running gir(names)...")
gir(names)
print("names shound now be ['zim', 'gaz', 'gir']")
print("names = " + str(names))

print("")
print("")

def zim(str_list):
    """Replaces the middle of str_list (everything except the first and last
    items) with four copies of the string "ZIM!".
    list-of-strings -> None"""
    str_list[1:-1] = ["ZIM!","ZIM!","ZIM!","ZIM!"]
    

names2 = ["gir", "gaz", "dib", "tak"]
print("names2 = " + str(names2))
print("Running zim(names2)...")
zim(names2)
print("names2 shound now be ['gir', 'ZIM!', 'ZIM!', 'ZIM!', 'ZIM!', 'tak']")
print("names2 = " + str(names2))
print("")
print("")

def insert_5678(wordlist):
    """Inserts the strings "five", "six", seven", and "eight" at the beginning
    of wordlist.
    list-of-strings -> None"""
    wordlist[0:0] = ["five","six","seven","eight"]
    #Hint: you can use slice replacement to insert by replacing an empty slice.

moves = ['turn', 'turn', 'touch', 'down', 'back', 'step']
print("moves = " + str(moves))
print("Running insert_5678(moves)...")
insert_5678(moves)
print("moves shound now be ['five', 'six', 'seven', 'eight', 'turn', 'turn', 'touch', 'down', 'back', 'step']")
print("moves = " + str(moves))
    

