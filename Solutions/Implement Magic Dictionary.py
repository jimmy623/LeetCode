from sets import Set
from collections import defaultdict
class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.data = defaultdict(int)
        self.original = Set(dict)
        for w in dict:
            for i in xrange(len(w)):
                can = w[:i]+"_"+w[i+1:]
                self.data[can] += 1
                # print can
        # print self.data

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        double = False
        if word in self.original:
            double = True
        for i in xrange(len(word)):
            can = word[:i]+"_"+word[i+1:]
            
            if double:
                if can in self.data and self.data[can] >= 2:
                    return True
            else:
                if can in self.data:
                    return True
            
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
#Implement Magic Dictionary