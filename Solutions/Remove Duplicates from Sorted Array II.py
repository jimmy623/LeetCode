class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A): 
        if len(A) == 0:
            return 0
        index = 1
        p = A[0]
        count = 1
        for i in range(1,len(A)):
            if A[i] != p:
                A[index] = A[i]
                p = A[i]
                index+=1
                count = 1
            elif count < 2:
                A[index] = A[i]
                index += 1
                count += 1
                
                
        return index
#Remove Duplicates from Sorted Array II
#https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array-ii/