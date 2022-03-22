
def unbound_knapsack(weights, values, capacity): 

    # utilizing memoization
    # dp[i] is going to store the available maximum value 
    # with capacity i
    n = len(values)
    dp = [0 for x in range(capacity+1)]

    # Fill our dp table with a recursive formula
    for i in range(capacity+1): 
        for j in range(n): 
            if(weights[j] <= i): 
                dp[i] = max(dp[i], dp[i-weights[j]] + values[j])

    return dp[capacity]

## Test
test_capacity = 100
test_values = [10, 30, 20] 
test_weights = [5, 10, 15]

print(f"The unbounded knapsack solution for the test values is {unbound_knapsack(test_weights, test_values, test_capacity)}")

