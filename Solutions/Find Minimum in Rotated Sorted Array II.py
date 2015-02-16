class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        pre = num[0]
        for i in range(1,len(num)):
            if num[i] < pre:
                return num[i]
            pre = num[i]
        return num[0]
            
s = Solution()
#print s.findMin([3,3,1])           
a = [10,1,10,10,10]
print s.findMin(a)           
            
#Find Minimum in Rotated Sorted Array II
#https://oj.leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/