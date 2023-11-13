from math import log
#2a
# This script has tools for creating histograms and working with histograms 
# The histograms will be represented as a dictionary
# The key will be the character and the value is the amount of times it occurs 

#2b
def get_freq(char, histogram):
    """fThis function takes a character and a histogram and returns 
    the frequency associated with that character in the given histogram. 
    If the character doesn’t appear in the histogram, it should return 0.
    char, dict -> int"""
    if char in histogram:
        return histogram[char]
    else: 
        return 0

#2c
def add_to_hist(char, histogram):
    """This function takes a character and a histogram and adds one 
    occurrence of that character to the histogram.
    char, dict -> None"""
    if char not in histogram:
        histogram[char] = 1
    else:
        histogram[char] += 1

#2d
def file_to_hist(filename):
    """This function takes a string representing a filename and opens it and
    reads its contents, makes a histogram based on the letter frequencies in 
    the file, then closed the file.
    str -> Histogram"""
    histogram = {}
    try:
        with open(filename) as file:
            for line in file:
                #print(line)
                for char in line:
                    #print(char)
                    add_to_hist(char,histogram)
        return histogram
    except OSError:
        return {}

#2e
def histoprint(histogram,scale):
    """This function takes a histogram and a scaling factor and makes a graphical
    representation of the histogram as a bar chart.
    histogram, int -> dict"""
    scaledHisto = {}
    scaledHisto = histogram.copy()
    for occurrences in histogram:
        scaledHisto[occurrences] = int(histogram[occurrences]/10) * "#"
    #Was not sure if you wanted the graphical histogram printed or returned because 
    #if we return it does not display the way it is shown in the example but if we print
    #the way we have with the for loop it does. We have provided both ways of doing it below.
    #We have also commented out the return line so the graphical histogram is displayed
    #the way of the example.
    for key in scaledHisto:
        print(key+ ": " + scaledHisto[key])
    #return [key+ ": " + scaledHisto[key] for key in scaledHisto]

#2f
def total_freq(histogram):
    """This function takes a histogram and returns the sum of the frequencies 
    of all characters in the histogram
    Histogram -> Int"""
    total = 0
    for val in histogram:
        total += histogram[val]
    return total

#2g
def hist_to_dist(histogram):
    """This function takes a histogram, and returns a histogram of probabilities, 
    based on the likelihood each character a different letter
    Histogram -> Histogram"""
    total = total_freq(histogram)
    probDistribution = {}
    for val in histogram:
        probDistribution[val] = histogram[val]/total
    return probDistribution
        
#2h
def dist_to_entropy(probDistr):
    """This function takes a probability distribution and returns the corresponding 
    entropy
    Probability Distribution -> Num"""
    total = 0
    for val in probDistr:
        total += probDistr[val]*log(probDistr[val],2)
    total = total*-1
    return total

