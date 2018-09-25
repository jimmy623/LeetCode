class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # nums = [Fraction(n) for n in nums]
        def dfs(ns):
            if len(ns) == 1:
                return abs(ns[0] - 24) < 10**-6
            for i in xrange(len(ns)):
                for j in xrange(len(ns)):
                    if i != j:
                        left = ns[i]
                        right = ns[j]
                        next = []
                        for k in xrange(len(ns)):
                            if k != i and k != j:
                                next.append(ns[k])
                        #+
                        if i > j:
                            next.append(left+right)
                            if dfs(next):
                                return True
                            else:
                                next.pop()
                        #*
                            next.append(left*right)
                            if dfs(next):
                                return True
                            else:
                                next.pop()
                        #-
                        next.append(left-right)
                        if dfs(next):
                            return True
                        else:
                            next.pop()
                        
                        #/
                        if right == 0:
                            continue
                        next.append(float(left)/right)
                        if dfs(next):
                            return True
            return False

        return dfs(nums)
s = Solution()
print s.judgePoint24([4,1,8,7])
# print s.judgePoint24([9,4,8,5])
# print s.judgePoint24([3,4,6,7])
# print s.judgePoint24([4,6,10])

#24 Game
#https://leetcode.com/problems/24-game/description/