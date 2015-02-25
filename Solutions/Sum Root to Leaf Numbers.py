# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if root == None:
            return 0
        self.sum = 0
        self.travers(root,0)
        return self.sum
        
    def travers(self,node,temp):
        temp = temp*10 + node.val
        if node.left == None and node.right == None:
            self.sum += temp
            return
        if node.left:
            self.travers(node.left,temp)
        if node.right:
            self.travers(node.right,temp)
        
    
#Sum Root to Leaf Numbers
#https://oj.leetcode.com/problems/sum-root-to-leaf-numbers/