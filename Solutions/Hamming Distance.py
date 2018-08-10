class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        val = x ^ y
        dest = 0
        while val != 0:
            dest += 1
            val &= val - 1
        return dest

s = Solution()
s.hammingDistance(1,4)

#Hamming Distance
#https://leetcode.com/problems/hamming-distance/description/