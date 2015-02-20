class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        
        if m>n:
            return self.findMedianSortedArrays(B,A)
            
        start = 0
        end = m
        while start <= end:
            i = (start + end + 1) / 2
            j = (m+n+1)/2 - i
            if i > 0 and j < n and A[i-1] > B[j]:
                end = i-1
            elif j > 0 and i < m and B[j-1] > A[i]:
                start = i+1
            else:
                if i == 0:
                    num1 = B[j-1]
                elif j == 0:
                    num1 = A[i-1]
                else:
                    num1 = max(A[i-1],B[j-1])
                
                if (m+n)%2 == 1:
                    return num1
                
                if i == m:
                    num2 = B[j]
                elif j == n:
                    num2 = A[i]
                else:
                    num2 = min(A[i],B[j])
                    
                return (num1 + num2) / 2.0
            
        
#Median of Two Sorted Arrays
#https://oj.leetcode.com/problems/median-of-two-sorted-arrays/