class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        a = list(A)
        i = 0
        j = 0
        k = 0
        while i < m or j < n:
            if i == m:
                A[k] = B[j]
                j += 1
            elif j == n:
                A[k] = a[i]
                i +=1
            else:
                if a[i] < B[j]:
                    A[k] = a[i]
                    i += 1
                else:
                    A[k] = B[j]
                    j+= 1
            k+= 1
            
            
#Merge Sorted Array
#https://oj.leetcode.com/problems/merge-sorted-array/