# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root == None:
            return None
        
        l = root.left
        r = root.right
        root.left = r
        root.right = l
        self.invertTree(l)
        self.invertTree(r)
        return root
    
#Invert Binary Tree
#https://leetcode.com/problems/invert-binary-tree/