class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """

        i1 = []
        i2 = []
        for i in range(len(words)):
        	if words[i] == word1:
        		i1.append(i)
        	if words[i] == word2:
        		i2.append(i)

        p1 = 0
        res = len(words)
        if word1 == word2:
        	for i in range(len(i1)-1):
        		res = min(res,i1[i+1]-i1[i])
        	return res
        for i in i2:
        	for j in range(p1,len(i1)):
        		p1 = j
        		if i1[j] > i:
        			res = min(res,i1[j]-i)
        			break
        		else:
        			res = min(res,i-i1[j])
        return res

#Shortest Word Distance III
#https://leetcode.com/problems/shortest-word-distance-iii/description/