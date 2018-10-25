# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
        	return []
        d = defaultdict(list)
        q = [(root,0)]
        while q:
        	nq = []
        	for node,p in q:
        		d[p].append(node.val)
        		if node.left:
        			nq.append((node.left,p-1))
        		if node.right:
        			nq.append((node.right,p+1))
        	q = nq
        l = min(d.keys())
        r = max(d.keys())
        result = []
        for i in xrange(l,r+1):
        	result.append(d[i])
        return result
        

        
#Binary Tree Vertical Order Traversal
#https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/