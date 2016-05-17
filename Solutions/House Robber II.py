class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        return max(self.find(nums),self.find(nums[1:] + [nums[0]]))
        
    
    def find(self,nums):
        dp = [0 for i in range(len(nums) + 2)]
        dp[-1] = (0,False)
        dp[-2] = (0,False)
        dp[-3] = (nums[-1],True)
        
        for i in range(len(nums)-2,-1,-1):
            v = nums[i]
            if(dp[i+1][0] == dp[i+2][0] + v):
                dp[i] = (dp[i+1][0],dp[i+1][1] and dp[i+2][1])
            elif(dp[i+1][0] >dp[i+2][0] + v):
                dp[i] = dp[i+1]
            else:
                dp[i] = (dp[i+2][0]+v,dp[i+2][1])
        
        if dp[0][1] == True:
            return dp[1][0]
        return dp[0][0]

        
#House Robber II        
#https://leetcode.com/problems/house-robber-ii/
#data = [2,7,9,3,1]
#data = [8,2,8,9,2]
data = [3,10,8,2,10,3,5,10,5,3,6]
s = Solution()
print s.rob(data)