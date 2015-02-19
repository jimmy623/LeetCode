class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        pre = num[0]
        flag = True
        for i in range(1,len(num)):
            v = num[i]
            
            if v > pre:
                flag = True
            else:
                if flag:
                    return i-1
                flag = False
            pre = v
            
        if flag:
            return len(num)-1
        return -1
#Find Peak Element
#https://oj.leetcode.com/problems/find-peak-element/