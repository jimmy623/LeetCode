class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        low = prices[0]
        high = prices[0]
        profit = 0
        for i in prices:
            if i < low:
                low = i
                high = i
            elif i > high:
                high = i
                profit = max(profit,high-low)
        return profit
                
#Best Time to Buy and Sell Stock
#https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/