# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        
        l = self.isSameTree(p.left,q.left)
        r = self.isSameTree(p.right,q.right)
        if l and r:
            return True
        else:
            return False
#Same Tree
#https://oj.leetcode.com/problems/same-tree/