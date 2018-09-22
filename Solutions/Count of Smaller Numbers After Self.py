from sets import Set
# from collections import Counter
class Solution(object):
    def updateBIT(self,i,val):
        i+=1
        while i<len(self.BIT):
            self.BIT[i] += val
            i += (i&-i)

    def getSum(self,i):
        s = 0
        i += 1
        while i>0:
            s+= self.BIT[i]
            i -= (i&-i)
        # print s
        return s

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = sorted(list(Set(nums)))
        d = dict()
        for i,n in enumerate(l):
            d[n] = i
    
        result = []
        self.BIT = [0 for _ in xrange(len(l)+1)]
    
        for i in xrange(len(nums)-1,-1,-1):
            n = nums[i]
            index = d[n]
            result.append(self.getSum(index-1))
            self.updateBIT(index,1)

        result.reverse()
        return result
        
s = Solution()
print s.countSmaller([5,2,6,1])
#Count of Smaller Numbers After Self
#https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/