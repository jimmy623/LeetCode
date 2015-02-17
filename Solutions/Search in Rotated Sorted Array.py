class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        self.A = A
        self.target = target
        self.result = -1
        self.binarySearch(0,len(A)-1)
        return self.result
        
    def binarySearch(self,left,right):

        if self.A[left] < self.A[right]:
            if self.target < self.A[left] or self.target > self.A[right]:
                return
        
        if left == right:
            if self.A[left] == self.target:
                self.result = left
            return
            
        if right - left == 1:
            if self.A[left] == self.target:
                self.result = left
            elif self.A[right] == self.target:
                self.result = right
            return
        
        middle = (left+right)/2
        self.binarySearch(left,middle)
        self.binarySearch(middle+1,right)
        
        
        
        
s = Solution()
print s.search([1,3,5],1)
        
        
        
        
#Search in Rotated Sorted Array
#https://oj.leetcode.com/problems/search-in-rotated-sorted-array/