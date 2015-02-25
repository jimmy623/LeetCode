# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root == None:
            return True
        r = self.check(root)
        print r
        if r == False:
            return False
        else:
            return True
        
        
    def check(self,node):
        if node == None:
            return 1
        l = self.check(node.left)
        r = self.check(node.right)
        if l == False or r == False:
            return False
        elif abs(l-r) > 1:
            return False
        else:
            return max(l,r) + 1
            
s = Solution()
print s.isBalanced(TreeNode(1))
        
        
#Balanced Binary Tree
#https://oj.leetcode.com/problems/balanced-binary-tree/