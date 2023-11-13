#A transition matrix is a way of keeping track of which items occur after other items
#and how frequently they do. Transition matrixes keep track of how many times a word
#comes after another word.
#Syntax for a transition matrix
# tMatrix = multiple lists of integers inside a big list of lists
# [[4,5,6,0],[2,4,1,0],[1,2,0,4]]




#Question 1
def get_reviews(count):
    """This function takes a positive integer argument 'count', and asks the user to enter
    'count' reviews about movies, in text or number rating format. Then once 'count' reviews have been
    entered, the reviews will be returned, with the average of the numberical reviews as well as the text reviews.
    # Positive integer -> None"""
    if count <= 0:
        return None
    reviewList = []
    reviewSum = 0
    numCount = 0
    for c in range(count):
        print("Please enter review #" + str(c+1) + ".")
        review = input(":   ")
        while review == "":
            print("Please enter review #" + str(c+1) + ".")
            review = input(":\t")
        try:
            reviewSum += float(review)
            numCount += 1
        except:
            reviewList.append(review)
    print("Here are your comments: ")
    for val in reviewList:
        print("\"" + val + "\"")
    print("The average numerical rating was:   " + str(reviewSum/numCount))
        
#Question 2
def filter_and_save(dic, keyList, filename):
    """This function takes a dictionary of string keys and string values, a list of keys and the name of the file that the function
    will write in. It checks to see if every key in keyList has a value in dic, and if it does, it writes the key and value into
    filename. This function will return True if it is successful, and return False if an OSError is encountered
    #dictionary with strings as keys and values, list, string -> Boolean"""
    try:
        with open(filename, "x") as file:
            for val in keyList:
                if val in dic:
                    file.write(val + ":" + dic[val] + "\n")
                else:
                    file.write(val + ":undefined" + "\n")
        return True
    except OSError:
        return False


#Question 3A
def cleaned_text(string):
    """this function takes a string and returns a copy of the string with all the commas, periods, exclamation points
    and question marks removed.
    String -> String"""
    cleanedString = ""
    for i in range(len(string)):
        if string[i] in "?,!.":
            pass
        else:
            cleanedString += string[i].lower()
    return cleanedString

#Question 3B
def str_to_words(string):
    """This function takes a string, and returns a list with every word as an element in the list, using the
    cleaned_text function
    String -> List of strings"""
    returnList = string.split()
    for i in range(len(returnList)):
        returnList[i] = cleaned_text(returnList[i])
    return returnList

#Question 3C
def str_to_unique_words(string):
    """This function works similarily to str_to_words, except for the list it returns of each word in the string does
    not contain any duplicate strings, instead of just returning every word in the string in a list
    string -> List of strings"""
    firstList = string.split()
    returnList = []
    for val in firstList:
        if cleaned_text(val) not in returnList:
            returnList.append(cleaned_text(val))
    return returnList

#Question 3D
def transitions(string, first, second):
    """This function takes 3 strings, the intial string, then the two transition values first and second. This function
    returns the count of how many times first and second are in a row in string.
    String, string, string -> Int"""
    count = 0
    stringList = str_to_words(string)
    if len(stringList) != 0:
        for i in range(len(stringList)):
            try:
                if stringList[i] == first and stringList[i+1] == second:
                    count += 1
            except IndexError:
                return count
    return count

#Question 3E
def xmatrix(string):
    """This function takes the test string and returns a transition matrix(list of lists of ints) for all transitions in the
    given string
    string -> Transition matrix(list of lists of ints)"""
    string = cleaned_text(string)
    wordList = str_to_words(string)
    uniqueList = str_to_unique_words(string)
    matrix = []
    for word in uniqueList:
        addList = []
        for val in uniqueList:
            addList.append(transitions(string, word, val))
        matrix.append(addList)
    return matrix
#Testing    
ham = "To be, or not to be?"

