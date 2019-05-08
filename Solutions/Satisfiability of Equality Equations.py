class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        d = {}
        def findHead(c):
        	if c == d[c]:
        		return c
        	head = findHead(d[c])
        	d[c] = head
        	return head

        for e in equations:
        	if e[1] == "=":
        		c1 = e[0]
        		c2 = e[3]
        		if c1 not in d:
        			d[c1] = c1
        		if c2 not in d:
        			d[c2] = c2
        		d[findHead(c2)] = findHead(c1)
        		
       	for e in equations:
       		if e[1] == "!":
       			c1 = e[0]
        		c2 = e[3]
        		if c1 == c2:
        			return False
        		if c1 in d and c2 in d:
       				h1 = findHead(e[0])
       				h2 = findHead(e[3])
       				if h1 == h2:
       					return False

       	return True

#Satisfiability of Equality Equations
#https://leetcode.com/problems/satisfiability-of-equality-equations/