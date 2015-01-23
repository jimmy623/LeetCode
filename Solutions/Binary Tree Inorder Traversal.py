# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if root == None:
            return []
        result = []
        
        nodes = []
        nodes.append(root)
        while len(nodes):
            n = nodes[-1]
            if n.left != None:
                nodes.append(n.left)
                n.left = None
                continue
            else:
                result.append(n.val)
                nodes.remove(n)
                if n.right != None:
                    nodes.append(n.right)
        return result      
        
#Binary Tree Inorder Traversal
#https://oj.leetcode.com/problems/binary-tree-inorder-traversal/