# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {}
        
    def cloneGraph(self, node):
        if node == None:
            return None
        if node.label in self.dict:
            return self.dict[node.label]
        
        n = UndirectedGraphNode(node.label)
        self.dict[node.label] = n
        for nei in node.neighbors:
            nn = self.cloneGraph(nei)
            n.neighbors.append(nn)
        return n
#Clone Graph
#https://oj.leetcode.com/problems/clone-graph/