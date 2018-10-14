from collections import defaultdict

class Trie(object):
	def __init__(self):
		# self.val = None
		self.count = 0
		self.children = {}

class Solution(object):
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        root = Trie()
        d = {}
        groups = defaultdict(list)
        for i,word in enumerate(dict):
        	key = (len(word),word[0],word[-1])
        	groups[key].append([word,i])

        result = [None for _ in xrange(len(dict))]
        for group in groups.itervalues():
        	root = Trie()

        	for word,i in group:
        		p = root
        		for c in word:
        			if c not in p.children:
        				p.children[c] = Trie()
        			p.children[c].count += 1
        			p = p.children[c]
        	for word,i in group:
        		p = root
        		length = len(word)
        		for j,c in enumerate(word):
        			node = p.children[c]
        			if j >= length-3:
        				result[i] = word
        				break
        			if node.count == 1:
        				abbr = word[:j+1] + str(length - 2 - j) + word[-1]
        				result[i] = abbr
        				break
        			p = node
        return result
        # result = []
        # for i,word in enumerate(dict):
        # 	key = (len(word),word[0],word[-1])
        # 	p = d[key]
        # 	length = len(word)
        # 	for j,c in enumerate(word):
        # 		node = p.children[c]
        # 		if j >= length-3:
        # 			result.append(word)
        # 			break
        # 		if node.count == 1:
        # 			abbr = word[:j+1] + str(length - 2 - j) + word[-1]
        # 			result.append(abbr)
        # 			break
        # 		p = node
        # return result

        # result = []
        # d = defaultdict(int)
        # for i,word in enumerate(dict):
        # 	length = len(word)
        # 	for k in xrange(1,length-2):
        # 		abbr = word[:k] + str(length - 1 - k) + word[-1]
        # 		d[abbr] += 1
        # for i,word in enumerate(dict):
        # 	length = len(word)
        # 	for k in xrange(1,length-2):
        # 		abbr = word[:k] + str(length - 1 - k) + word[-1]
        # 		if d[abbr] == 1:
        # 			result.append(abbr)
        # 			break
        # 	if len(result) == i:
        # 	 	result.append(word)		
        # return result



#Word Abbreviation
#https://leetcode.com/problems/word-abbreviation/description/