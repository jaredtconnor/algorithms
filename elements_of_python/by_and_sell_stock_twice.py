
# Brute Force Example 

prices = [12,11,13,9,12,8,14,13,15]

def buy_and_sell_stock_twice(prices: list[float]) -> float: 
    
    # Record the best solution for A[0, j]
    max_total_profit = 0.0
    min_price_so_far = float('inf')

    first_buy_sell = [0.0] * len(prices)
    
    for i, price in enumerate(prices): 
        min_price_so_far = min(min_price_so_far, price) 
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profits[i] = max_total_profits

    # Perform a reverse iteration, computing best soliution 
    # for a single buy-and-sell for A[j, n-1]




    # Combine the result from the forward iteration for the previous
    # day



print(f"Testing the largest profit: {result}")
