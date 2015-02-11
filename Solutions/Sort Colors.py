class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        zeros = 0
        ones = 0
        twos = 0
        for i in A:
            if i == 0:
                zeros += 1
            elif i == 1:
                ones += 1
            else:
                twos += 1
        for i in range(zeros):
            A[i] = 0
        for i in range(zeros,zeros + ones+twos):
            A[i] = 1
        for i in range(zeros + ones,zeros+ones+twos):
            A[i] = 2

#Sort Colors
#https://oj.leetcode.com/problems/sort-colors/