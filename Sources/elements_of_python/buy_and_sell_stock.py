
# Brute Force Example
# Two pointer approach:

prices = [301, 315, 275, 295, 260, 270, 290, 230, 255, 250]


def buy_and_sell_stock_once_brute(prices: list[float]) -> float:

    current_profit = 0

    for i in range(0, len(prices)):
        for j in range(i, len(prices)):

            if (j > i) and (prices[j] - prices[i]) > current_profit:
                current_profit = prices[j] - prices[i]

    return current_profit


def buy_and_sell_stock_once(prices: list[float]) -> float:

    min_price = float('inf')
    max_profit = 0.0

    for price in prices:

        max_profit_sell_today = price - min_price
        max_profit = max(max_profit, max_profit_sell_today)
        min_price = min(min_price, price)

    return max_profit


result_1 = buy_and_sell_stock_once_brute(prices)
result = buy_and_sell_stock_once(prices)
print(f"Testing the largest profit: {result}")
