
# Rod cutting problem solved via naive recursion
def rodcutting_BF(n, prices): 
    if n<0: 
        return 0 

    max_revenue = 0  

    for i in range(1, n+1):
        max_revenue = max(max_revenue, prices[i-1] + rodcutting_BF(n-i, prices))

    return max_revenue

prices_test = [1,5,8,9,10]
rod_length = 4 
print("The optimum rod revenue is: ", rodcutting_BF(rod_length, prices_test))