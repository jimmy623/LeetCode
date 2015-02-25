# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head == None:
            return None
        if head.next == None:
            return head
        
        pre = head
        p = head.next.next
        
        head.next.next = head
        head = head.next
        
        while p and p.next:
            next = p.next.next
            pre.next  = p.next
            p.next.next = p
            pre = p
            p = next
        
        if p == None:
            pre.next = None
        else:
            pre.next = p
                    
        return head
        
        
#Swap Nodes in Pairs
#https://oj.leetcode.com/problems/swap-nodes-in-pairs/