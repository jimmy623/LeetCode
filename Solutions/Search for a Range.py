class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if len(A) == 0:
            return [-1,-1]
        if target < A[0] or target > A[-1]:
            return [-1,-1]
        self.A = A
        self.target = target
        n = len(A)
        left = self.findLeft(0,n-1)
        right = self.findRight(0,n-1)
        return [left,right]
        
    def findLeft(self,s,e):
        while s < e:
            m = (s + e)/2
            if self.A[m] > self.target:
                e = m-1
            elif self.A[m] < self.target:
                s = m+1
            else:
                e = m
        if self.A[s] == self.target:
            return s
        else:
            return -1
           
    def findRight(self,s,e):
        while s < e:
            m = (s+e+1)/2
            if self.A[m] < self.target:
                s = m + 1
            elif self.A[m] > self.target:
                e = m - 1
            else:
                s = m
        if self.A[s] == self.target:
            return s
        else:
            return -1
        
s = Solution()
A = [5, 7, 7, 8, 8, 10]
A= [1,5]
print s.searchRange(A,4)
#Search for a Range
#https://oj.leetcode.com/problems/search-for-a-range/