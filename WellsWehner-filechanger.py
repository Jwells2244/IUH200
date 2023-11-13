

#Question 2

#A
def modified(string):
    """This function takes a string, and returns a modified version of that string"""
    #String -> String
    string = string.replace("Hey","Samantha")
    string = string.replace("Sam","Bam")
    string = string.replace("ou","zx")
    string = string.replace("y","fake vowel here")
    string = string.replace("I","i")
    return string


while True:
    try:
        sourceFileName = input("Enter the source filename: ")
        destinationFileName = input("Enter the destination filename: ")
        with open(sourceFileName, "r") as source:
            with open(destinationFileName, "x") as dest:
                for line in source:
                    dest.write(modified(line))
        break
    except FileExistsError:
        print("The destination filename you entered already exists")
    except FileNotFoundError:
        print("The filename you entered does not exist")
    except:
        print("Encountered an error during runtime")
    

#FileExistsError
#FileNotFoundError

        
                    
    
