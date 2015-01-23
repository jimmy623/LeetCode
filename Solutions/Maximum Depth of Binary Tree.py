# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        self.max = 1
        if not root:
            return 0
            
        self.iterate(root,1)
        return self.max
        
    def iterate(self,node,depth):
        if depth > self.max:
            self.max = depth
            
        if node.left:
            self.iterate(node.left,depth + 1)
            
        if node.right:
            self.iterate(node.right,depth+1)
        
        
#Maximum Depth of Binary Tree
#https://oj.leetcode.com/problems/maximum-depth-of-binary-tree/