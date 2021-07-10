## Dynamic brute force algorithm for making change problem, given some amount
import math

def makechangeBF(coins, amount): 

    if(amount == 0): 
        return 0

    countmemo = [0] * (amount + 1) 

    return makechangeBF_helper(coins, amount, countmemo)

def makechangeBF_helper(coins, amount, countmemo):

    if (amount < 0): 
        return -1

    if(amount == 0): 
        return 0

    if(countmemo[amount] != 0): 
        return countmemo[amount]

    # Specify starting result amount
    min_coins = math.inf

    # Search for the new min coin count
    for coin in coins:
        temp_coincount = makechangeBF_helper(coins, amount - coin, countmemo) 

        if(temp_coincount >= 0 and temp_coincount < min_coins): 
            min_coins = 1 + temp_coincount

    # If a new min is found use it in memoization of coins
    countmemo[amount] = -1 if (min_coins == math.inf) else min_coins  # if we found a new minimum use it

    return countmemo[amount]

print(makechangeBF([5,3,1] , 9 ))