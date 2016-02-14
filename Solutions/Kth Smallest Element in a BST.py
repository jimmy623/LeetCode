# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        self.count = 1
        self.target = k
        return self.travel(root)
        
    def travel(self,node):
        #left
        if node.left != None:
            r = self.travel(node.left)
            if  r != None:
                return r
            
        #middle
        if self.count == self.target:
            return node.val
        else:
            self.count += 1
            
        #right
        if node.right != None:
            r = self.travel(node.right)
            if  r != None:
                return r
             
            
        return None    
        
    
        
#Kth Smallest Element in a BST
#https://leetcode.com/problems/kth-smallest-element-in-a-bst/