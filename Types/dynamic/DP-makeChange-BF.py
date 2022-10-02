## Dynamic Programming - Make change problem but from a top down approach
## i.e., utilizing memoization.

def makechangeBF(coins, amount):

    countmemo = {0:0}

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