# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if root == None:
            return None
        tp = [root]
        tq = [root]
        node = root
        while node != p:
            if p.val < node.val:
                node = node.left
            else:
                node = node.right
            tp.append(node)
        
        node = root
        while node != q:
            if q.val < node.val:
                node = node.left
            else:
                node = node.right
            tq.append(node)
        
        i = 0
        while i< len(tp) and i<len(tq) and tp[i] == tq[i]:
            i += 1
        return tp[i-1]
            
        
#Lowest Common Ancestor of a Binary Search Tree
#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/