
# Rod cutting problem solved via top down memoization recursion
def rodcutting_topdown(n, prices): 

    # define our memoization table for top down dynamic programming approach
    rod_memo = {}

    return rodcutting_topdown_helper(n, prices, rod_memo)

def rodcutting_topdown_helper(n, prices, rod_memo):

    # base case/stopping condition
    if n<0: 
        return 0 

    # check first if the result is in our memo table
    if n in rod_memo: 
        return rod_memo[n] 

    max_revenue = 0  

    # traverse the tree of available prices and rod lengths
    for i in range(1, n+1):
        max_revenue = max(max_revenue, prices[i-1] + rodcutting_topdown_helper(n-i, prices, rod_memo))

    rod_memo[n] = max_revenue
    return rod_memo[n]


prices_test = [1,5,8,9,10]
rod_length = 4 
print("The optimum rod revenue is: ", rodcutting_topdown(rod_length, prices_test))