from sets import Set
from collections import defaultdict
# from collections import OrderedDict
class Trie(object):
	def __init__(self,val):
		self.val = val
		self.children = []

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        V = Set()
        root = Trie("")
        for w in words:
        	node = root
        	for c in w:
        		V.add(c)
        		if not node.children or node.children[-1].val != c:
        			child = Trie(c)
        			node.children.append(child)
        		node = node.children[-1]

        self.graph = defaultdict(Set)
        def dfs(trie):
        	keys = [node.val for node in trie.children]
        	for i in xrange(len(keys)-1):
        		self.graph[keys[i]].add(keys[i+1])
        	for node in trie.children:
        		dfs(node)
        dfs(root)
        V = list(V)

        def topoSortHelper(v,visited,stack,recStack):
        	visited[V.index(v)] = True
        	recStack[V.index(v)] = True
        	for i in self.graph[v]:
        		if visited[V.index(i)] == False:
        			if not topoSortHelper(i,visited,stack,recStack):
        				return False
        		elif recStack[V.index(i)]:   #check for cycle
        			return False
        	recStack[V.index(v)] = False
        	stack.insert(0,v)
        	return True

        def topoSort():
        	visited = [False] * len(V)
        	stack = []
        	recStack = [False] * len(V) 
        	for i in V:
        		if visited[V.index(i)] == False:
        			if not topoSortHelper(i,visited,stack,recStack):
        				return ""
        	return stack
        result = topoSort()
        return "".join(result)

s = Solution()
# print s.alienOrder(["wrt","wrf","er","ett","rftt"])
print s.alienOrder(["z","x","z"])


        
#Alien Dictionary
#https://leetcode.com/problems/alien-dictionary/description/