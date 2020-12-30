# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.result = 0
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(False,False,root)
        return self.result
    def dfs(self,grandparent,parent,node):
        if not node:
            return
        if grandparent:
            self.result += node.val
        even = (node.val % 2 == 0)
        self.dfs(parent,even,node.left)
        self.dfs(parent,even,node.right)
        
        
#Sum of Nodes with Even-Valued Grandparent
#https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/