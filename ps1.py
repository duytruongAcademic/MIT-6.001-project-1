###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cowDict = dict()

    f = open(filename, 'r')
    
    for line in f:
        lineData = line.split(',')
        cowDict[lineData[0]] = int(lineData[1])
    return cowDict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    #sort the keys of dictionary cow and put them into a list
    cow = sorted(cows,key=cows.get,reverse=True)
    #create an empty list to append a final list of appropriate keys
    result = []
    while True:
        #create an empty list containing elements of the given cow dictionary
        trip = []
        #create a counter to start counting the total weights for each trip
        totalValue = 0
        for i in cow:            
            if totalvalue + cows[i] <= limit:
                #append to the trip list if the total weights are less or equal than the limit for each trip.
                trip.append(i)
                totalValue += cows[i]
        #append appropriate trip to the final list
        result.append(trip)
        #create an empty list that tells the function to pick up elements that are not included in the first trip
        temp=[]
        for i in cow:
            if i not in trip:
               temp.append(i)
        #Initialize the second "while true" loop by replacing the original list with list that contains only elements that are not included in the first trip
        cow=temp
        #if all elements are included in the trip lists, break out the loop
        if len(cow)==0:
            break
    return result

        
            
        


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    #create a list containing the keys of dictionary cow
    cowList=list(cows.keys())
    #using get_partitions() function to generate all possible combinations and append them into a list
    cowAllList=[]
    for item in get_partitions(cowList):
        cowAllList.append(item)
    #create a copy of the combinations and sort low-high on number of element in list'
    cowAllList.sort(key=len)
    #loop through the combination trips and return the first set of trips that satisfy the condition.
    for listInList in cowAllList:
        condition= True
        for listElement in listInList:
            count=0
            for element in listElement:
                count=count + cows[E]
            if count>limit:
                condition=False
                break
        if condition:
            return listInList
    
            

                    
    



