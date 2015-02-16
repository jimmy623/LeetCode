class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        low = prices[0]
        pre = prices[0]
        profit = 0
        for i in prices:
            if i >= pre:
                pass
            else:
                if pre > low:
                    profit += pre - low
                low = i
            pre = i

                    
        if pre > low:
            profit += pre - low

        return profit   
            
#Best Time to Buy and Sell Stock II
#https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/