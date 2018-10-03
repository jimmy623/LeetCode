class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        if int(low) > int(high):
        	return 0
        s = len(low)
        e = len(high)
        count = 0
        replace = {"0":"0","1":"1","8":"8","6":"9","9":"6"}
        #018
        #69

        def generate(n):
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


        def countForLength(length):
        	if length == 1:
        		return 3
        	product = 4 * 5**(length/2-1)
        	if length%2:
        		product *= 3
        	return product

        for length in xrange(s+1,e):
        	count += countForLength(length)
        # print count
        ln = int(low)
        hn = int(high)
        if len(low) == len(high):
        	nums = generate(len(low))
        	for n in nums:
        		if ln <= int(n) <= hn:
        			count +=1
        	return count


        ls = generate(len(low))
        hs = generate(len(high))

        for n in ls:
        	if  ln <= int(n):
        		count += 1
        for n in hs:
        	if int(n) <= hn:
        		count += 1
        return count


s = Solution()
print s.strobogrammaticInRange("50","100")
        
#Strobogrammatic Number III
#https://leetcode.com/problems/strobogrammatic-number-iii/description/