
#     Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_profit = 0
    if len(prices) < 2:
        return 0
    low_price = prices[0]
    for i in range(1, len(prices)):
        low_price = min(prices[i], low_price)
        if prices[i] - low_price > 0:
            max_profit = max(max_profit, prices[i] - low_price)
    return max_profit

print(maxProfit([7,1,5,3,6,4]))


