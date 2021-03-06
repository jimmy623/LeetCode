# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        level = [root]
        while True:
            newLevel = []
            for i in range(len(level)-1):
                level[i].next = level[i+1]
            level[-1].next = None
            if level[0].left:
                for node in level:
                    newLevel.append(node.left)
                    newLevel.append(node.right)
                level = newLevel
            else:
                break
            
#Populating Next Right Pointers in Each Node
#https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node/