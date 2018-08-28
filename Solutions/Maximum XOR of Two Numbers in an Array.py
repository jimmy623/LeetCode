class Trie:
	def __init__(self):
		self.zero = None
		self.one = None

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        root = Trie()
        
        for n in nums:
        	node = root
        	for i in xrange(31,-1,-1):
        		if n & (1 << i):
        			if not node.one:
        				node.one = Trie()
        			node = node.one
        		else:
        			if not node.zero:
        				node.zero = Trie()
        			node = node.zero
        maxN = 0
        for n in nums:
        	node = root
        	candidate = 0
        	#print "n:",n
        	for i in xrange(31,-1,-1):
        		mask = 1 << i
        		if n & mask:
        			if node.zero:
        				node = node.zero
        			else:
        				node = node.one
        				candidate += mask
        		else:
        			if node.one:
        				node = node.one
        				candidate += mask
        			else:
        				node = node.zero
        		#print candidate
        	#print n,candidate
        	r = n ^ candidate
        	if  r > maxN:
        		maxN = r
        return maxN


s = Solution()
#print s.findMaximumXOR([3, 10, 5, 25, 2, 8])
print s.findMaximumXOR([5,5,5,19,12])

# 10 =      8 + 0 + 2 + 0
# 25 = 16 + 8 + 0 + 0 + 1
# 5  =          4 + 0 + 1
# 2 =               2 + 0
# 3 =               2 + 1
# 8 =       8 + 0 + 0

#Maximum XOR of Two Numbers in an Array
#https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/