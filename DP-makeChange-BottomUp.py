## Dynamic Programming - Algorithm for making change problem, given some amount, bottom up approach
import math

def makechange_BU(coins, amount): 

    # Define out bottom up table
    change_table = [math.inf]*(amount + 1)

    # Populate our base conditions
    change_table[0] = 0

    # Use an iterative approach starting from our base conditions
    for i in range(1, amount+1): # Iterating trhough all possible amounts _from_ base case
        for j in range(0, len(coins)): # Checking each possible coin denomination

            coin = coins[j]

            # If the current denomination value is less than the amount, then we can use the coin, add to the bottom up table
            if(coin <= amount and (i-coin)>=0): 
                change_table[i] = min(change_table[i], change_table[i-coin]+1) 

    if change_table[amount] > amount: 
        result = -1
    else: 
        result = change_table[amount]

    return result
    
print(makechange_BU([1,3,5], 8))