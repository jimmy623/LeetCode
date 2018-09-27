# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while n > 0:
        	buf4 = [""]*4
        	r = read4(buf4)
        	if not r:
        		return idx
        	for i in xrange(min(r,n)):
        		buf[idx] = buf4[i]
        		idx += 1
        	n -= r
        return idx
#Read N Characters Given Read4
#https://leetcode.com/problems/read-n-characters-given-read4/description/