class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        
        dp = [999999 for i in range(n+1)]
        dp[n - 1] = 1; 
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                k = min(dp[j], dp[j + 1]) - dungeon[i][j]
                if k <= 0:
                    dp[j] = 1
                else:
                    dp[j] = k
        return dp[0];

s = Solution()
d = [
[-2,-3,3],
[-5,-10,1],
[10,30,-5]]
print s.calculateMinimumHP(d)
        

                        
                
                    
                
                    
#Dungeon Game
#https://oj.leetcode.com/problems/dungeon-game/