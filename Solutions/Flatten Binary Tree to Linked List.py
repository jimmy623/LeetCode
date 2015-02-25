# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root == None:
            return None
        
        self.nodes = [] 
        self.preorder(root)
        pre = self.nodes[0]
        
        for i in range(1,len(self.nodes)):
            node = self.nodes[i]
            pre.left = None
            pre.right = node
            pre = node
        
        pre.left = None    
        pre.right = None
        return self.nodes[0]
        
    def preorder(self,node):
        if node == None:
            return
        self.nodes.append(node)
        self.preorder(node.left)
        self.preorder(node.right)
        
s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
s.flatten(root)
#Flatten Binary Tree to Linked List
#https://oj.leetcode.com/problems/flatten-binary-tree-to-linked-list/