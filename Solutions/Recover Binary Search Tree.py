# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        self.nodes = []
        self.first = None
        self.second = None
        self.iterateTree(root)
        #print self.nodes
        for i in range(len(self.nodes)):
            if self.first:
                n = self.nodes[i]
                pre = self.nodes[i-1]
                if n.val < pre.val:
                    self.second = n
            else:
                n = self.nodes[i]
                next = self.nodes[i+1]
                if n.val > next.val:
                    self.first = n
                    print self.first.val
                    
        #print self.first.val,self.second.val
        tmp =  self.first.val
        self.first.val = self.second.val
        self.second.val = tmp
        return root
                
    def iterateTree(self,node):
        if node.left:
            self.iterateTree(node.left)
        self.nodes.append(node)
        if node.right:
            self.iterateTree(node.right)
        

s = Solution()

root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(1)
s.recoverTree(root)

#Recover Binary Search Tree
#https://oj.leetcode.com/problems/recover-binary-search-tree/