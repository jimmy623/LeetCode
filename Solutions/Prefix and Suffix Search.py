# from sets import Set
# class Trie(object):
#   def __init__(self,val):
#       self.val = val
#       self.nodes = {}
#       self.isLeaf = False

class WordFilter(object):
    def __init__(self, words):
        self.d = {}
        for i,w in enumerate(words):
            l = len(w)
            for j in xrange(l+1):
                for k in xrange(l+1):
                    self.d[w[:j] + "." + w[k:]] = i
        print self.d

    def f(self, prefix, suffix):
        if prefix+"."+suffix in self.d:
            return self.d[prefix+"."+suffix]
        else:
            return -1



    # def __init__(self, words):
    #     """
    #     :type words: List[str]
    #     """
    #     self.words = words
    #     self.d = {}
    #     self.preRoot = Trie("")
    #     self.sufRoot = Trie("")
    #     for i,w in enumerate(words):
    #       self.processWord(w,self.preRoot)
    #       self.processWord(w[::-1],self.sufRoot)
    #       self.d[w] = i

    # def processWord(self,word,root):
    #   trie = root
    #   for c in word:
    #       if c in trie.nodes:
    #           trie = trie.nodes[c]
    #       else:
    #           newTrie = Trie(c)
    #           trie.nodes[c] = newTrie
    #           trie = newTrie
    #   trie.isLeaf = True
        
    # def searchWord(self,word,root):
    #   trie = root
    #   for c in word:
    #       if c in trie.nodes:
    #           trie = trie.nodes[c]
    #       else:
    #           return None
    #   return trie

    # def dfs(self,trie,stack,result,reverse=False):
    #   for c in trie.nodes:
    #       stack.append(c)
    #       self.dfs(trie.nodes[c],stack,result,reverse)
    #       stack.pop()
    #   if trie.isLeaf:
    #       if reverse:
    #           result.add("".join(stack[::-1]))
    #       else:
    #           result.add("".join(stack))

    # def findMax(self,words):
    #   m = -1
    #   for w in words:
    #       if self.d[w] > m:
    #           m = self.d[w]
    #   return m

    # def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        #TLE version
        # pre = self.searchWord(prefix,self.preRoot)
        # suf = self.searchWord(suffix[::-1],self.sufRoot)
        
        # if pre and suf:
        #   if prefix == "":
        #       sufSet = Set()
        #       self.dfs(suf,[c for c in suffix[::-1]],sufSet,True)
        #       s = sufSet
        #   elif suffix == "":
        #       preSet = Set()
        #       self.dfs(pre,[c for c in prefix],preSet)
        #       s = preSet
        #   else:
        #       preSet = Set()
        #       sufSet = Set()
        #       self.dfs(pre,[c for c in prefix],preSet)
        #       self.dfs(suf,[c for c in suffix[::-1]],sufSet,True)
        #       s = preSet.intersection(sufSet)

        #   m = 0
        #   for w in s:
        #       if self.d[w] > m:
        #           m = self.d[w]
        #   return m
        # else:
        #   return -1

["WordFilter","f","f","f","f","f","f","f","f","f","f"]
[[["abbbababbb","baaabbabbb","abababbaaa","abbbbbbbba","bbbaabbbaa","ababbaabaa","baaaaabbbb","babbabbabb","ababaababb","bbabbababa"]],["","abaa"],["babbab",""],["ab","baaa"],["baaabba","b"],["abab","abbaabaa"],["","aa"],["","bba"],["","baaaaabbbb"],["ba","aabbbb"],["baaa","aabbabbb"]]
words = ["abbbababbb","baaabbabbb","abababbaaa","abbbbbbbba","bbbaabbbaa","ababbaabaa","baaaaabbbb","babbabbabb","ababaababb","bbabbababa"]
# s = WordFilter(words)
# print s.f("","abaa")
s = WordFilter(["apple"])
print s.f("a","e")

        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
#Prefix and Suffix Search
#https://leetcode.com/problems/prefix-and-suffix-search/description/