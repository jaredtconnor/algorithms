
# Rod cutting problem solved via bottom up tabularization
def rodcutting_bottomup(n, prices): 

    # Define a rod dp table 
    rod_table = [0 for x in range(n + 1)]

    # Starting from rod length of 1 finding the optimum answer for each
    for length in range(1, n+1):

        max_revenue = 0

        # if we find a new maximum value, replace the current value in the rod_table with that value
        # note - we defined the rod_table as indexed by 1 so we need to index possible cuts with + 1
        for cut in range(length): 
            if((prices[cut] + rod_table[length - (cut+1)]) > max_revenue): 
                max_revenue = prices[cut] + rod_table[length - (cut+1)]

        rod_table[length] = max_revenue

    # Return the final n length of the rod 
    return rod_table[n]

prices_test = [1,5,8,9,10]
rod_length = 4 
print("The optimum rod revenue is: ", rodcutting_bottomup(rod_length, prices_test))