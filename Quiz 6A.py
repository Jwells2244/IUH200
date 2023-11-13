#Jonathan Wells and Devin Thakker

pricelist1 = [["fries",3.99],["burger",5.99],["milkshake",3.49]]

#Quiz 6A

def get_price(itemName, pricelist):
    """Returns the price of itemName from the pricelist"""
    #String, Pricelist -> Float
    counter = 0
    while counter < len(pricelist):
        if pricelist[counter][0] == itemName:
            return pricelist[counter][1]
        counter += 1
    #If we don't find the item with the given name
    raise ValueError("No item with the name "+ itemName)
