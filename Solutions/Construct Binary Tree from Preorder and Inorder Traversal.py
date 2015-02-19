# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def __repr__(self):
        return str(self.val)



class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        head = TreeNode(preorder[0])
        route = [head]
        preN = head
        
        for i in range(1,len(preorder)):
            v = preorder[i]
            n = TreeNode(v)
            inIndex = inorder.index(v)
            
            while len(route) and inIndex > inorder.index(route[-1].val):
                preN = route.pop()

            if inIndex < inorder.index(preN.val):
                preN.left = n
            else:
                preN.right = n
            preN = n
            route.append(n)
        return head

s = Solution()
preorder = [1,2,3]
inOrder = [2,3,1]
s.buildTree(preorder,inOrder)
            
#Construct Binary Tree from Preorder and Inorder Traversal
#https://oj.leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/