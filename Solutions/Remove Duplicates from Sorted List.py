# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
            return None
        
        pre = head
        p = head.next
        while p:
            if p.val == pre.val:
                p = p.next
            else:
                pre.next = p
                pre = p
                p = p.next
        pre.next = None
        
        return head
        
#Remove Duplicates from Sorted List
#https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list/