#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root == None or p == None or q == None:
            return None

        stack = []
        self.search(root,p,stack)
        for i in range(len(stack)-1,-1,-1):
            node = stack[i]
            if i == len(stack)-1:
                self.search(node.left,q,stack)
                if stack[-1] != q:
                    stack.pop()
                else:
                    return node
                self.search(node.right,q,stack)

                if stack[-1] != q:
                    stack.pop()
                else:
                    return node
            else:
                if node == q:
                    return node
                last = stack.pop()
                theNext = None
                if last == node.left:
                    theNext = node.right
                else:
                    theNext = node.left
                self.search(theNext,q,stack)
                if stack[-1] != q:
                    stack.pop()
                else:
                    return node


    def search(self,node,p,stack):
        stack.append(node)
        if node == None:
            return
        if node == p:
            return
        self.search(node.left,p,stack)
        if stack[-1] != p:
            stack.pop()
        else:
            return
        self.search(node.right,p,stack)
        if stack[-1] != p:
            stack.pop()
        else:
            return


s = Solution()
head = TreeNode(1)
two = TreeNode(2)
head.right = two
print s.lowestCommonAncestor(head,two,head)



#Lowest Common Ancestor of a Binary Tree
#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
