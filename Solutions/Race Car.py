# from math import log
from sets import Set
class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target == 0:
            return 0
        r = [[0,1]]
        count = 1
        visited = Set()
        while True:
            new = []
            for loc,speed in r:
                #A
                if loc+speed == target:
                    return count
                else:
                    if (loc+speed,speed*2) not in visited:
                        new.append([loc+speed,speed*2])
                #R
                ns = 1
                if speed > 0:
                    ns = -1
                if (loc,ns) not in visited:
                    new.append([loc,ns])
                    visited.add((loc,ns))

            r = new
            # print r
            count += 1

# class Solution(object):
#     def racecar(self, target):
#         dp = [0, 1, 4] + [float('inf')] * target
#         for t in xrange(3, target + 1):
#             k = t.bit_length()
#             if t == 2**k - 1:
#                 dp[t] = k
#                 continue
#             for j in xrange(k - 1):
#                 dp[t] = min(dp[t], dp[t - 2**(k - 1) + 2**j] + k - 1 + j + 2)
#             if 2**k - 1 - t < t:
#                 dp[t] = min(dp[t], dp[2**k - 1 - t] + k + 1)
#         return dp[target]


s = Solution()
# print s.racecar(3)
# print s.racecar(6)
# print s.racecar(15)
# print s.racecar(5)
print s.racecar(4)

#Race Car
#https://leetcode.com/problems/race-car/description/