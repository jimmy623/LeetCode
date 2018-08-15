from collections import defaultdict;
class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.data = defaultdict(list)
        self.n = len(words)
        for i in range(len(words)):
        	self.data[words[i]].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i1 = self.data[word1]
        i2 = self.data[word2]
        p1 = 0
        res = self.n
        for i in i2:
        	for j in range(p1,len(i1)):
        		
        		p1 = j
        		if i1[j] > i:
        			res = min(res,i1[j]-i)
        			break
        		else:
        			res = min(res,i-i1[j])
        return res
        


# Your WordDistance object will be instantiated and called as such:
words = ["a","a","b","b"]
obj = WordDistance(words)
print obj.shortest("a","b")
print obj.shortest("b","a")
#Shortest Word Distance II
#https://leetcode.com/problems/shortest-word-distance-ii/description/