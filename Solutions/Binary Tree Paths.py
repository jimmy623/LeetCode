# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.result = []
        if root == None:
        	return self.result;
        route = str(root.val)
        if root.left == None and root.right == None:
        	self.result.append(route)
    	if root.left:
    		self.dfs(root.left,route)
    	if root.right:
    		self.dfs(root.right,route)


        return self.result

    def dfs(self,node,route):
    	route = route + "->" + str(node.val)
    	if node.left == None and node.right == None:
    		self.result.append(route)
    		return
    	if node.left:
    		self.dfs(node.left,route)
    	if node.right:
    		self.dfs(node.right,route)


#Binary Tree Paths
#https://leetcode.com/problems/binary-tree-paths/