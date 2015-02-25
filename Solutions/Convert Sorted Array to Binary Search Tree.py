# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        self.num = num
        head = self.genTree(0,len(num))
        return head
        
    def genTree(self,start,end):
        n = end - start
        print start,end
        if n == 0:
            return None
        if n == 1:
            return TreeNode(self.num[start])
        middle = (end+start)/2
        node = TreeNode(self.num[middle])
        node.left = self.genTree(start,middle)
        node.right = self.genTree(middle+1,end)
        return node
        
s = Solution()
s.sortedArrayToBST([-10,-3,0,5,9])
        
        
#Convert Sorted Array to Binary Search Tree
#https://oj.leetcode.com/problems/convert-sorted-array-to-binary-search-tree/