# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        self.result = []
        if root == None:
            return []
        self.logLevel([root],False)
        return self.result
        
    def logLevel(self,nodes,flag):
        if len(nodes) == 0:
            return
        level = []
        next = []

        for n in nodes:
            level.append(n.val)
            if n.left:
                next.append(n.left)
            if n.right:
                next.append(n.right)
                
        if flag:
            level.reverse()
            
        self.result.append(level)
        
        self.logLevel(next,not flag)
        
#Binary Tree Zigzag Level Order Traversal
#https://oj.leetcode.com/problems/binary-tree-zigzag-level-order-traversal/