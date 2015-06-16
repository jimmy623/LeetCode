class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        nn = []
        for i in range(len(nums)):
            nn.append((nums[i],i))
        nn.sort()
        #print nn
        for i in range(len(nn)-1):
            (x1,y1) = nn[i]
            p = 1
            while i + p < len(nn):
                (x2,y2) = nn[i+p]
                if x2 - x1 > t:
                    break
                if abs(y2-y1)<=k:
                    return True
                p += 1
        return False
        
s = Solution()
#a = [0,10,22,15,0,5,22,12,1,5]
#t = 3
#k = 3
a = [1,3,6,2]
k = 1
t = 2

print s.containsNearbyAlmostDuplicate(a,k,t)
#Contains Duplicate III
#https://leetcode.com/problems/contains-duplicate-iii/