prices = [5,3,6,4]

def maxProfit(prices):
    profit = 0
    min_price = float('inf')
    for i in prices:
        min_price = min(i,min_price)
        profit = max(profit, i - min_price)
    return profit

print(maxProfit(prices))