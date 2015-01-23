# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if root == None:
            return []
        result = []
        
        nodes = []
        nodes.append(root)
        while len(nodes):
            
        
        
#Binary Tree Inorder Traversal
#https://oj.leetcode.com/problems/binary-tree-inorder-traversal/