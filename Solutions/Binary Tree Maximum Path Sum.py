# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.max = -99999999
        r = self.maxSingle(root)

        
        return self.max
        
    def maxSingle(self,node):
        if node.left == None and node.right == None:
            if node.val > self.max:
                self.max = node.val
                return node.val
        l = 0
        r = 0
            
        if node.left:
             l = self.maxSingle(node.left)
                
        if node.right:
           r = self.maxSingle(node.right)
                
        cMax= l + r + node.val
        if cMax > self.max:
            self.max = cMax
            
        upStream = node.val+max(l,r,0)
        if upStream > self.max:
            self.max = upStream
        return upStream
                
            
s = Solution()

root = TreeNode(2)
root.left = TreeNode(-1)
# root.right = TreeNode(3)            
print s.maxPathSum(root)
        
        
#Binary Tree Maximum Path Sum
#https://oj.leetcode.com/problems/binary-tree-maximum-path-sum/