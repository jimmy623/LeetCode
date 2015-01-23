# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root == None:
            return []
        result = []
        nodes = [root]
        while len(nodes):
            n = nodes[-1]
            if n.left == None and n.right == None:
                result.append(n.val)
                nodes.remove(n)
                continue
            
            if n.right:
                nodes.append(n.right)
                n.right = None
                
            if n.left:
                nodes.append(n.left)
                n.left = None
        
        return result
        
        
s = Solution()

root = TreeNode(0)
print s.postorderTraversal(root)
            
#Binary Tree Postorder Traversal
#https://oj.leetcode.com/problems/binary-tree-postorder-traversal/