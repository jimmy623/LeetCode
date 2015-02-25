# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return None
        head = TreeNode(postorder[-1])
        route = [head]
        preN = head
        
        for i in range(len(inorder)-2,-1,-1):
            print i
            v = postorder[i]
            n = TreeNode(v)
            inIndex = inorder.index(v)
            
            while len(route) and inIndex < inorder.index(route[-1].val):
                preN = route.pop()
            
            if inIndex > inorder.index(preN.val):
                preN.right = n
            else:
                preN.left = n
            
            
            preN = n
            route.append(n)
        
        return head
        
s = Solution()
inOrder = [2,1]
preorder = [2,1]
s.buildTree(preorder,inOrder)
#Construct Binary Tree from Inorder and Postorder Traversal
#https://oj.leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/