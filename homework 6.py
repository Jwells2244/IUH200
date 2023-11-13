import math

#f

def total_freq(histogram):
    """This function takes a histogram and returns the sum of the frequencies of all characters in the histogram"""
    #Histogram -> Int
    total = 0
    for val in histogram:
        total += histogram[val]
    return total

#g

def hist_to_dist(histogram):
    """This function takes a histogram, and returns a histogram of probabilities, based on the likelihood each character
    a different letter"""
    #Histogram -> Histogram
    total = total_freq(histogram)
    probDistribution = {}
    for val in histogram:
        probDistribution[val] = histogram[val]/total
    return probDistribution
        
#h

def dist_to_entropy(probDistr):
    """This function takes a probability distribution and returns the corresponding entropy"""
    #Probability Distribution -> Num
    total = 0
    for val in probDistr:
        total += probDistr[val]*math.log(probDistr[val],2)
    total = total*-1
    return total
        
