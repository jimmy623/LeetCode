class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        result = A[0]
        sum = 0
        for i in A:
            sum += i
            if sum > result:
                result = sum
            if sum < 0:
                sum = 0
        return result
             
s = Solution()

a= [-2,1,-3,4,-1,2,1,-5,4]
print s.maxSubArray(a)

            
            

#Maximum Subarray
#https://oj.leetcode.com/problems/maximum-subarray/