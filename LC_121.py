""" Best Time To Buy and Sell Stock """

prices = [7,6,4,3,1]

""" Sliding window technique - O(n)"""
def maxProfit(prices):
    max_Profit = 0
    buy, sell = 0, 1

    while sell < len(prices):
        if prices[buy] < prices[sell]:
            profit = prices[sell] - prices[buy]
            max_Profit = max(max_Profit, profit)
        else:
            buy = sell
        sell += 1
    return max_Profit

print(maxProfit(prices))
