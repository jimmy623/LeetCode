class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        r = [i for i in xrange(1,n+1)]
        for i in nums:
        	r[i] = 0
        p = 0
        for i in xrange(n+1):
        	if r[i] != 0:
        		r[p] = r[i]
        		p+=1
        return r[:p]

    # def findDisappearedNumbers(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     # For each number i in nums,
    #     # we mark the number that i points as negative.
    #     # Then we filter the list, get all the indexes
    #     # who points to a positive number
    #     for i in xrange(len(nums)):
    #         index = abs(nums[i]) - 1
    #         nums[index] = - abs(nums[index])

    #     return [i + 1 for i in range(len(nums)) if nums[i] > 0]
#Find All Numbers Disappeared in an Array
#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/