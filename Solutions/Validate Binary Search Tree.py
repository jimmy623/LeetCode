# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        if root == None:
            return True
        return self.valid(root,None,None)
        
    def valid(self,node,min,max):
        if node.left:
            if not (node.left.val < node.val):
                return False
            if min:
                if not (node.left.val > min):
                    return False
                    
            if not self.valid(node.left,min,node.val):
                return False
            
        if node.right:
            if not (node.right.val > node.val):
                return False
            if max:
                if not (node.right.val < max):
                    return False 
            if not self.valid(node.right,node.val,max):
                return False
        
        return True
        
        
#Validate Binary Search Tree
#https://oj.leetcode.com/problems/validate-binary-search-tree/