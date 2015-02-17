# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        self.sum = sum
        self.result = []
        self.dfs(root,0,[])
        return self.result
        
    def dfs(self,node,temp,route):
        if node == None:
            return False
        
        temp += node.val
        newRoute = list(route)
        newRoute.append(node.val)
        if node.left == None and node.right == None:
            if temp == self.sum:
                self.result.append(newRoute)
                return
            else:
                return
        
        self.dfs(node.left,temp,newRoute)
        self.dfs(node.right,temp,newRoute)
#Path Sum II
#https://oj.leetcode.com/problems/path-sum-ii/