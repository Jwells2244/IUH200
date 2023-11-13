#Quiz 6B

#Devin and Jonathan

pl = {"fries":3.99, "burger":5.49, "milkshake":3.89}


def change_name(priceList, oldName, newName):
    """This function changes the name of the thing called oldname to newname in the given pricelist"""
    #pricelist, string, string -> None
    priceList[newName] = pricedict[oldName]
    del priceList[oldName]

#Modify this script so when there's a problem with this file it asks the user to keep trying until it works

while True:
    fileName = input("Please enter a filename: ")
    try:
        file = open(fileName)
        while True:
            line = file.readline()
            if line == "":
                break
            else:
                print(line)
        file.close()
        break
    except OSError:
        print("Problem")
