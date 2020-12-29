class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        zeros = 0
        binaries = []

        for i in A:
            if i == 0:
                zeros +=1
        if zeros <= K:
            return n
        max_length = 0
        current = 0
        start = 0
        end = 0
        remain = K
        while end < n:
            if A[end] == 1:
                current += 1
                end+=1
            else:
                if remain > 0:
                    remain -= 1
                    end+=1
                else:
                    if A[start] == 0 and end > start:
                        remain +=1
                    start+=1
                    if end<start:
                        end = start
            max_length = max(max_length,end-start)
        return max_length

            
s = Solution()
A = [0,0,1,1,1,0,0]
K = 0
print s.longestOnes(A,K)


#Max Consecutive Ones III
#https://leetcode.com/problems/max-consecutive-ones-iii/