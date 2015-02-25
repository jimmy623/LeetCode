class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        dict = {}
        n = len(num)
        if n == 1:
            return num[0]
        for i in num:
            if i in dict:
                count = dict[i]
                count += 1
                if count > n/2:
                    return i
                else:
                    dict[i] = count
            else:
                dict[i] = 1
#Majority Element
#https://oj.leetcode.com/problems/majority-element/