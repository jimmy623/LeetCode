class Solution(object):
	def maxSlidingWindow(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		res = []
		if len(nums) == 0:
			return res
		pMax = -1
		maximum = -9999
		for i in range(len(nums)-k+1):
			if pMax < i:
				maximum = -9999
				for j in range(i,i+k):
					if nums[j] >= maximum:
						maximum = nums[j]
						pMax = j
			else:
				if nums[i+k-1] >= maximum:
					maximum = nums[i+k-1]
					pMax = i+k-1
			#print i,maximum,pMax
			res.append(maximum)
		return res

s = Solution()
# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
nums = [-6,-10,-7,-1,-9,9,-8,-4,10,-5,2,9,0,-7,7,4,-2,-10,8,7]
k = 7
print s.maxSlidingWindow(nums,k)

#Sliding Window Maximum
#https://leetcode.com/problems/sliding-window-maximum/description/