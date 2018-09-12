from sets import Set
class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        visited = Set()
        ans = []
        def dfs(pre):
        	for i in xrange(k):
        		c = str(i)
        		new = pre + c
        		if new not in visited:
        			visited.add(new)
        			dfs(new[1:])
        			ans.append(c)
        dfs("0" * (n-1))
        return "".join(ans) + "0" * (n-1)
#Cracking the Safe
#https://leetcode.com/problems/cracking-the-safe/description/