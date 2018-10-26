class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # for i in xrange(len(nums)-1):
        # 	s = nums[i]
        # 	for j in xrange(i+1,len(nums)):
        # 		s += nums[j]
        # 		if k == 0:
        # 			return s == 0
        # 		elif s%k == 0:
        # 			return True
        # return False

        
        if k == 0:
            # if two continuous zeros in nums, return True
            # time O(n)
            for i in range(0, len(nums) - 1):
                if nums[i] == 0 and nums[i+1] == 0:
                    return True
            return False
        
        mods, cum_sum_mod_k = {0:-1}, 0
        for i, n in enumerate(nums):
            cum_sum_mod_k = (cum_sum_mod_k + n) % k
            if cum_sum_mod_k in mods and i - mods[cum_sum_mod_k] > 1:
                return True
            if cum_sum_mod_k not in mods:
                mods[cum_sum_mod_k] = i
        return False




#Continuous Subarray Sum
#https://leetcode.com/problems/continuous-subarray-sum/description/