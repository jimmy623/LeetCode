class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[len(nums)-k]
        
#Kth Largest Element in an Array
#https://leetcode.com/problems/kth-largest-element-in-an-array/