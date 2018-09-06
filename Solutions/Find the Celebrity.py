# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        # m = [True for i in xrange(n)]
        # for i in xrange(n):
        	
        # 	for j in xrange(n):
        # 		if m[j] and i != j:
       	# 			if not knows(i,j):
    				# 	m[j] = False
        # for i in xrange(n):
        # 	if m[i]:
        # 		flag = True
        # 		for j in xrange(n):
        # 			if i != j and knows(i,j):
        # 				flag = False
        # 				break
        # 		if flag:
        # 			return i

        # return -1
        if n < 2:
        	return -1
        stack = [i for i in xrange(n)]
        while len(stack) != 1:
        	a = stack.pop()
        	b = stack.pop()
        	if knows(a,b):
        		stack.append(b)
        	else:
        		stack.append(a)
        remain = stack[0]
        for i in xrange(n):
        	if i != remain:
        	 	if knows(remain,i) or not knows(i,remain):
        			return -1
        return remain
#Find the Celebrity
#https://leetcode.com/problems/find-the-celebrity/description/