# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.numbers = []
        self.dfs(node)
        start = 0
        end = len(numbers)-1
        while start < end:
            v = numbers[start] + numbers[end] 
            if v == target:
                return True
            elif v > target:
                end -= 1
            else:
                start += 1
        return False

    def dfs(self,node):
    	if node.left:
    		self.dfs(node.left)
    	self.result.append(node.val)
    	if node.right:
    		self.dfs(node.right)

#Two Sum IV - Input is a BST
#https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/