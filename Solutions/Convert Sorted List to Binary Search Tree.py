# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        self.num = []
        while head:
            self.num.append(head.val)
            head = head.next
        head = self.genTree(0,len(num))
        return head
        
    def genTree(self,start,end):
        n = end - start
        
        if n == 0:
            return None
        if n == 1:
            return TreeNode(self.num[start])
        middle = (end+start)/2
        node = TreeNode(self.num[middle])
        node.left = self.genTree(start,middle)
        node.right = self.genTree(middle+1,end)
        return node
#Convert Sorted List to Binary Search Tree
#https://oj.leetcode.com/problems/convert-sorted-list-to-binary-search-tree/