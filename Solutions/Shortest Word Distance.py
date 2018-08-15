class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        p1 = 0
        p2 = 0
        lastP2 = 0
        n = len(words)
        res = n;
        while words[p1] != word1:
        		p1 += 1
        lastP1 = p1
        while p2 < n:
        	while p2 < n and words[p2] != word2:
        		p2 += 1;
        	#print p1,p2,lastP1
        	if p2 < n:
        		lastP2 = p2
        		res = min(res,abs(p2-lastP1))

        	while p1 < p2:
        		p1 += 1
        		while p1 < n and words[p1] != word1:
        			p1 += 1
        		if p1 < n:
        			lastP1 = p1
        			#print "123",p1,p2,lastP1
        			res = min(res,abs(p2-p1))
        	p2+=1
        return res

s = Solution()
words = ["practice", "makes", "perfect", "coding", "makes"]
w1 = "coding"
w2 = "practice"
print s.shortestDistance(words,w1,w2)
#Shortest Word Distance
#https://leetcode.com/problems/shortest-word-distance/description/