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
        self.max = 0
        if not root:
            return 0
            
        self.iterate(root,1)
        
    def iterate(self,node,depth):
        
        
        
#Maximum Depth of Binary Tree
#https://oj.leetcode.com/problems/maximum-depth-of-binary-tree/