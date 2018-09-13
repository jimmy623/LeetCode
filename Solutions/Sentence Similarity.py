from sets import Set
from collections import defaultdict
class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
        	return False

        sim = defaultdict(Set)
        for a,b in pairs:
        	sim[a].add(b)
        	sim[b].add(a)
        for i in xrange(len(words1)):
        	a = words1[i]
        	b = words2[i]
        	if not (a == b or b in sim[a]):
        		return False
        return True




        
#Sentence Similarity
#https://leetcode.com/problems/sentence-similarity/description/