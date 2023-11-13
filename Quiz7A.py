#Jonathan Wells and Noah

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
