class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def swap(i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        for i in xrange(len(nums)-1):
            #print nums
            if i % 2 == 0:
                if nums[i] > nums[i+1]:
                    nums[i],nums[i+1] = nums[i+1],nums[i]
            else:
                if nums[i] < nums[i+1]:
                    nums[i],nums[i+1] = nums[i+1],nums[i]


s = Solution()
nums = [3,5,2,1,6,4]
nums = [4,2,1,3]
s.wiggleSort(nums)
print nums
#Wiggle Sort
#https://leetcode.com/problems/wiggle-sort/description/