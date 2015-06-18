# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if root == None:
            return 0
        p = root
        depth = 1
        while p.left:
            depth += 1
            p = p.left

        start = 0
        end = 2 ** (depth - 1) - 1
        
        while start < end:

            middle = (start + end) / 2
            if self.nthNode(root,depth,middle) == None:
                end = middle-1
            else:
                if self.nthNode(root,depth,middle+1) == None:
                    start = middle
                    break
                else:
                    start = middle + 1
        
        return start + 2 ** (depth-1)
            
            
    def nthNode(self,root,depth,n):
        p = root
        d = 1
        start = 0
        end = 2 ** (depth-1) - 1
        while d < depth:
            if n <= (start+end)/2:
                p = p.left
                end = (start+end)/2
            else:
                p = p.right
                start = (start+end)/2+1
            d += 1
        return p
            
        
r = TreeNode(0)
r.left = TreeNode(1)
r.right = TreeNode(2)
r.left.left = TreeNode(3)
r.left.right = TreeNode(4)

#r.right.left = TreeNode(5)

s = Solution()
#print s.nthNode(r,3,0).val
print s.countNodes(r)
        
        
        
            
        
        
#Count Complete Tree Nodes
#https://leetcode.com/problems/count-complete-tree-nodes/