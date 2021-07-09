import math
## Dynamic brute force algorithm for making change problem, given some amount

def makechangeBF(coins, amount):

    # Base case or stopping condition
    if(amount == 0): 
        return 0

    # Specify starting result amount
    result = amount + 1

    for i in range(len(coins)): 
        if(coins[i] <= amount): 
            result = min(result, makechangeBF(coins, amount-coins[i])+1)

    return result

print(makechangeBF([1,3,5] , 9 ))