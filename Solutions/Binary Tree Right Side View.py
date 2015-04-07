# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        if root == None:
            return []
    
        nodes = [root]
        result = []
        while len(nodes):
            result.append(nodes[-1].val)
            newNodes = []
            for n in nodes:
                if n.left:
                    newNodes.append(n.left)
                if n.right:
                    newNodes.append(n.right)
            nodes = newNodes
            
        return result
#Binary Tree Right Side View
#https://leetcode.com/problems/binary-tree-right-side-view/