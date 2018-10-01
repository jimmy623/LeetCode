class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
        	return ["0","1","8"]
        chars = "01689"
        d = {"0":"0","1":"1","8":"8","6":"9","9":"6"}
        bfs = [""]
        i = 0

        for i in xrange(0,n/2):
        	new = []
        	for s in bfs:
        		for c in d:
        			if i == 0 and c == "0":
        				continue
        			new.append(s+c)
        	bfs = new
        if n%2:
        	new = []
        	for s in bfs:
        		for c in "018":
        			new.append(s+c)
        	bfs = new
        for i in xrange(0,n/2):
        	new = []
        	for s in bfs:
        		new.append(s+d[s[n/2-1-i]])
        	bfs = new
        return bfs


#Strobogrammatic Number II
#https://leetcode.com/problems/strobogrammatic-number-ii/description/