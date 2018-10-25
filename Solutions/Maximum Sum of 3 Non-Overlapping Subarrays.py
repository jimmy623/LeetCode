class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        sums = [sum(nums[:k])]
        for i in xrange(1,len(nums)-k+1):
        	sums.append(sums[-1]-nums[i-1]+nums[i+k-1])
        dp1 = [i for i in xrange(len(sums))]
        dp2 = [i for i in xrange(len(sums)-k)]
        dp3 = [i for i in xrange(len(sums)-2*k)]

        for i in xrange(len(dp1)-2,2*k-1,-1):
        	if sums[i] < sums[dp1[i+1]]:
        		dp1[i] = dp1[i+1]

        for i in xrange(len(dp2)-2,k-1,-1):
        	if sums[i] + sums[dp1[i+k]] < sums[dp2[i+1]]+sums[dp1[dp2[i+1]+k]]:
        		dp2[i] = dp2[i+1]

        for i in xrange(len(dp3)-2,-1,-1):
        	if sums[i] + sums[dp2[i+k]] + sums[dp1[dp2[i+k]+k]] < sums[dp3[i+1]] + sums[dp2[dp3[i+1]+k]] + sums[dp1[dp2[dp3[i+1]+k]+k]]:
        		dp3[i] = dp3[i+1]

        return [dp3[0],dp2[dp3[0]+k],dp1[dp2[dp3[0]+k]+k]]

        

s = Solution()
s.maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2)

#Maximum Sum of 3 Non-Overlapping Subarrays
#https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/