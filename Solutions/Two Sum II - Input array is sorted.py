class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers)-1
        while start < end:
            v = numbers[start] + numbers[end] 
            
            if v == target:
                return [start+1,end+1]
            elif v > target:
                end -= 1
            else:
                start += 1

#Two Sum II - Input array is sorted
#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/