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

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


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
    cow = sorted(cows,key=cows.get,reverse=True)

    result = []
    while True:        
        trip = []
        totalvalue = 0
        for i in cow:            
            if totalvalue + cows[i] <= limit:
                trip.append(i)
                totalvalue += cows[i]
        result.append(trip)
        temp=[]
        for i in cow:
            if i not in trip:
               temp.append(i) 
        cow=temp
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
    cowList=list(cows.keys())
    #using get_partitions() function to generate all possible combinations
    cowAllList=[]
    for item in get_partitions(cowList):
        cowAllList.append(item)
    #create a copy of the combinations and sort low-High on number of element in list'
    cowAllList.sort(key=len)
    for listList in cowAllList:
        total=[]
        condition= True
        for listE in listList:
            count=0
            for E in listE:
                count=count + cows[E]
            if count>limit:
                condition=False
                break
            else:
                total.append(count)
        if condition:
            return listList
    
            

                    
    



