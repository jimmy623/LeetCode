class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        prev = None
        md = 0
        for i,s in enumerate(seats):
            if s == 1:
                if prev != None:
                    md = max(md,(i-prev)/2)
                else:
                    md = i
                prev = i
        md = max(len(seats)-1-prev,md)
        return md
s = Solution()
print s.maxDistToClosest([1,0,0,0,1,0,1])
#Maximize Distance to Closest Person
#https://leetcode.com/problems/maximize-distance-to-closest-person/description/