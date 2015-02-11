class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        self.num = num
        return self.search(0,len(num)-1)
        
    def search(self,left,right):
        if self.num[left] < self.num[right]:
            return self.num[left]
        if right == left:
            return self.num[left]
        if right - left == 1:
            return min(self.num[left],self.num[right])
        
        middle = (left+right)/2
        if self.num[middle] > self.num[left]:
            return self.search(middle,right)
        else:
            return self.search(left,middle)
            
            
s = Solution()
#print s.findMin([4,5,6,7,0,1,2])
print s.findMin([1,2,3])
#Find Minimum in Rotated Sorted Array
#https://oj.leetcode.com/problems/find-minimum-in-rotated-sorted-array/

'''
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
'''