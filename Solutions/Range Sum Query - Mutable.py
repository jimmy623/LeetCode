class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.BIT = [0 for _ in xrange(len(nums)+1)]
        for i,n in enumerate(nums):
            self.updateBIT(i,n)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        
        self.updateBIT(i,val - self.get(i))
        self.nums[i] = val

    def get(self,i):
        return self.nums[i]
        #return self.getSum(i) - self.getSum(i-1)

    def updateBIT(self,i,val):
        i+=1
        while i < len(self.BIT):
            self.BIT[i] += val
            i += (i&-i)

    def getSum(self,i):
        s = 0
        i += 1
        while i > 0:
            s += self.BIT[i]
            i -= (i&-i)
        return s
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.getSum(j) - self.getSum(i-1)

nums = [1, 3, 5]        
s = NumArray(nums)
print s.sumRange(0,2)
print s.getSum(1)
print s.update(1,2)

print s.sumRange(0,2)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)


#Range Sum Query - Mutable
#https://leetcode.com/problems/range-sum-query-mutable/description/