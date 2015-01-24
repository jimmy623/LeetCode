# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        self.result = []
        if root == None:
            return []
        self.logLevel([root])
        print self.result
        self.result.reverse()
        return self.result
        
    def logLevel(self,nodes):
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
        self.result.append(level)
        self.logLevel(next)
        
        
s = Solution()
root = TreeNode(1)
print s.levelOrderBottom(root)
#Binary Tree Level Order Traversal II
#https://oj.leetcode.com/problems/binary-tree-level-order-traversal-ii/