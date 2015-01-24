# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root == None:
            return 0
        
        self.min = 99999999
        self.iterate(root,0)
        return self.min    
        
        
    def iterate(self,node,depth):
        if node.left == None and node.right == None:
            if depth + 1 < self.min:
                self.min = depth + 1
                return
                
        if node.left:
                self.iterate(node.left,depth+1)
                
        if node.right:
                self.iterate(node.right,depth+1)
        
        
#Minimum Depth of Binary Tree
#https://oj.leetcode.com/problems/minimum-depth-of-binary-tree/