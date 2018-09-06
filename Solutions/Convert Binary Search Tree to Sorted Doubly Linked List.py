"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
        	return root
        self.head = None
        self.lastOne = None
        self.inOrder(root)
        self.head.left = self.lastOne
        self.lastOne.right = self.head
        return self.head

    def inOrder(self,node):
    	if node.left:
    		self.inOrder(node.left)
    	if self.lastOne:
    		self.lastOne.right = node
    	if not self.head:
    		self.head = node
    	node.left = self.lastOne
    	self.lastOne = node
    	if node.right:
    		self.inOrder(node.right)

#Convert Binary Search Tree to Sorted Doubly Linked List
#https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/