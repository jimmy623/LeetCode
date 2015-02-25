class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
       
        n = len(A)
        p = 0
        
        for i in range(n):
            if A[i] == elem:
                continue
            if p != i:
                A[p] = A[i]
            p+= 1
        return p
                
        
        
#Remove Element
#https://oj.leetcode.com/problems/remove-element/