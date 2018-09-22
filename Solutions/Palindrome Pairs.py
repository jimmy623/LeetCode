from sets import Set
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        positions = {}
        for i in xrange(len(words)):
        	positions[words[i]] = i

        result = Set()
        for i in xrange(len(words)):
        	word = words[i]
        	# print "words",i,word
        	chars = ["#"]
        	for c in word:
        		chars.append(c)
        		chars.append("#")
        	for j in xrange(len(chars)/2+1):
        		k = 1
        		while j-k >=0:
        			if chars[j-k] == chars[j+k]:
        				k+=1
        			else:
        				break
        		if j-k < 0:
        			left = chars[-2:j+k-1:-2]
        			s = "".join(left)
        			if s in positions:
        				if positions[s] != i:
        					result.add((positions[s],i))

        	for j in xrange(len(chars)/2,len(chars)):
        		k = 1
        		while j+k < len(chars):
        			if chars[j-k] == chars[j+k]:
        				k+=1
        			else:
        				break
        		if j+k >= len(chars):
        			right = chars[1:j-k+1:2]
        			right.reverse()
        			s = "".join(right)
        			if s in positions:
        				if positions[s] != i:
        					result.add((i,positions[s]))
        r = []
        for i,j in result:
        	r.append([i,j])
        return r


s = Solution()
words = ["abcd","dcba","lls","s","sssll"]
words = ["a",""]
words = ["a","abc","aba",""]
print s.palindromePairs(words)

#Palindrome Pairs
#https://leetcode.com/problems/palindrome-pairs/description/