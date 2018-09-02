class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        self.nums = nums
        self.hash = {}
        count = self.dfs(target)
        return count
        

    def dfs(self,target):
    	# if currentSum > self.target:
    	# 	return
    	# if currentSum == self.target:
    	# 	self.result.append(route)
    	# 	return
    	#print target,self.hash
    	if target in self.hash:
    		return self.hash[target]

    	count = 0
    	for i in xrange(len(self.nums)):
    		n = self.nums[i]
    		if n > target:
    			break
    		if n == target:
    			count += 1
    			break

    		count += self.dfs(target-n)

    	self.hash[target] = count
    	return count

s = Solution()
print s.combinationSum4([1,2,3],4)

#Combination Sum IV
#https://leetcode.com/problems/combination-sum-iv/description/