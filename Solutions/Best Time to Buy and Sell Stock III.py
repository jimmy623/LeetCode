class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        newPrices = []

        pre = 0
        start = 0
        i = 1
        while i < len(prices):
            if prices[i] >= prices[pre]:
                pass
            else:
                if pre > start:
                    newPrices.append(prices[start])
                    newPrices.append(prices[pre])
                start = i
                
            pre += 1
            i+=1
        
        if prices[pre] > prices[start]:
            newPrices.append(prices[start])
            newPrices.append(prices[pre])
        
        profit = 0
        for i in range(0,len(newPrices) / 2):
            temp = self.partProfit(0,i*2,newPrices) + self.partProfit(i*2,len(newPrices),newPrices)
            profit = max(profit,temp)
            
        
        return profit
    
    def partProfit(self,start,end,newPrices):
        if start == end:
            return 0
        
        low = newPrices[start]
        high = newPrices[start]
        profit = 0
        for i in range(start+1,end):
            if newPrices[i] < low:
                low = newPrices[i]
                high = newPrices[i]
            elif newPrices[i] > high:
                high = newPrices[i]
                profit = max(profit,high-low)

        return profit
        
s = Solution()
#s.maxProfit([1,2,4,2,5,7,2,4,9,0])
print s.maxProfit([1,2])
            







                
#     if len(prices) == 0:
#             return 0
#         low = prices[0]
#         high = prices[0]
#         profit = 0
#         for i in prices:
#             if i < low:
#                 low = i
#                 high = i
#             elif i > high:
#                 high = i
#                 profit = max(profit,high-low)
#         return profit
        
#Best Time to Buy and Sell Stock III
#https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
