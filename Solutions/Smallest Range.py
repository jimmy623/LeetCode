from heapq import heappush,heappop
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        result = [-10**5,10**5]
        q = []
        for i in xrange(len(nums)):
        	heappush(q,(nums[i][0],i,0))
        biggest = max(q)
        while q:
        	val,group,index = heappop(q)
        	if biggest[0]-val < result[1]-result[0]:
        		result = [val,biggest[0]]
        	if index == len(nums[group]) -1:
        		break
        	else:
        		candidate = (nums[group][index+1],group,index+1)
        		if candidate[0] > biggest[0]:
        			biggest = candidate
        		heappush(q,candidate)
        return result


        
#Smallest Range
#https://leetcode.com/problems/smallest-range/description/