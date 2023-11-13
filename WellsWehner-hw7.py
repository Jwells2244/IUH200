

def file_to_grid(filename):
    """This function takes a filename, and uses the data in the file to create a soduku grid"""
    #filename -> List
    returnList = []
    
    with open(filename, "r") as file:
        for line in file:
            appendList = []
            for character in line:
                if character != "\n":
                    appendList.append(character)
            returnList.append(appendList)
    return returnList
            
