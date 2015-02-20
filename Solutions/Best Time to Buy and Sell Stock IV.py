class Solution:
    # @return an integer as the maximum profit 
    def maxProfit(self, k, prices):
        n = len(prices)
        if k > n/2:
            profit = 0
            for i in range(1,n):
                if prices[i] > prices[i-1]:
                    profit += prices[i]-prices[i-1]
            return profit
        r = [[0 for i in range(n)] for x in range(k+1)]

        for i in range(1,k+1):
            tempMax = r[i-1][0]-prices[0]
            for j in range(1,n):
                #print i,j,tempMax
                r[i][j] = max(r[i][j-1],prices[j]+tempMax)
                tempMax = max(tempMax,r[i-1][j-1]-prices[j])

        return r[k][n-1]
        
s = Solution()
s.maxProfit(2,[2,1,2,0,1])
        

#Best Time to Buy and Sell Stock IV
#https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/