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
    # TODO: Your code here
    comb = []
    for i in get_partitions(cows.keys()):
        comb.append(i)
    
    z = []    
    for i in range(len(comb)):
        a = []
        for j in range(len(comb[i])):
            b = []
            for k in comb[i][j]:
                b.append(cows[k])
            if sum(b) > limit:
                break
            a.append(comb[i][j])
        if len(a) == len(comb[i]):    
            z.append(a)
            
    num = []        
    for i in range(len(z)):
        num.append(len(z[i]))
              
    for i in z:
        if len(i) == min(num):
            return i
