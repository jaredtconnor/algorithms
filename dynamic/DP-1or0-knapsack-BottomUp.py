

def knapsack_0_1(capacity, n, weights, values):

    dp = [[0 for x in range(n+1)] for y in range(capacity+1)]

    for i in range(1,capacity+1):
        for j in range(1,n+1):
            dp[i][j]=dp[i][j-1]
            w_j = weights[j-1]
            v_j = values[j-1]
            if i >= w_j:
                dp[i][j] = max(dp[i][j] , dp[i-w_j][j-1] + v_j)
    
    return dp[capacity][n]

## Test
test_capacity = 10
test_values = [4, 9, 3, 5, 7]
test_weights = [10, 25, 13, 20, 8]

print(f"1/0 Knapsack problem is: {knapsack_0_1(test_capacity, 5, test_weights, test_values)}")