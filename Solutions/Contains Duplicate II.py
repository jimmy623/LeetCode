class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        nn = []
        for i in range(len(nums)):
            nn.append((nums[i],i))
        nn.sort()
        for i in range(len(nn)-1):
            (x1,y1) = nn[i]
            (x2,y2) = nn[i+1]
            if x1 == x2 and (y2-y1)<=k:
                return True
        return False
#Contains Duplicate II
#https://leetcode.com/problems/contains-duplicate-ii/