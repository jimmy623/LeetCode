#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        pairs = []
        if root == None:
            return True
        
        
        
        pairs.append((root.left,root.right))
        while len(pairs):
            (left,right) = pairs.pop(0)
            
            if left == None and right == None:
                continue
            elif left == None or right == None:
                print left,right
                return False
            else:
                if left.val == right.val:
                    pairs.append((left.right,right.left))
                    pairs.append((left.left,right.right))
                else:
                    return False
        
        return True    
        
    

root = TreeNode(2)
left = TreeNode(3)
right = TreeNode(3)
left.left = TreeNode(4)
left.right = TreeNode(5)
right.left = TreeNode(5)
root.left = left
root.right = right

s = Solution()
print s.isSymmetric(root)

#Symmetric Tree
#https://oj.leetcode.com/problems/symmetric-tree/