# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        pn = head
        p = head
        count = 0
        length = 0
        while p:
            if count <= n:
                count += 1
            else:
                pn = pn.next
            p = p.next
            length += 1
        if length == n:
            return pn.next
        else:
            if n == 1:
                pn.next = None
            else:  
                pn.next = pn.next.next
        
        return head
#Remove Nth Node From End of List
#https://oj.leetcode.com/problems/remove-nth-node-from-end-of-list/