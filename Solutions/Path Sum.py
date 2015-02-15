# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        self.sum = sum
        return self.dfs(root,0)
        
    def dfs(self,node,temp):
        if node == None:
            return False
        
        temp += node.val
            
        if node.left == None and node.right == None:
            if temp == self.sum:
                return True
            else:
                return False
                
        return self.dfs(node.left,temp) or self.dfs(node.right,temp)

        
#Path Sum
#https://oj.leetcode.com/problems/path-sum/