# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if not root:
            return []
        result = []
        nodes = [root]
        while len(nodes):
            n = nodes[-1]
            result.append(n.val)
            nodes.remove(n)
            if n.right:
                nodes.append(n.right)
            if n.left:
                nodes.append(n.left)
                
        return result
        
        
#Binary Tree Preorder Traversal
#https://oj.leetcode.com/problems/binary-tree-preorder-traversal/