# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        p = head
        pv = None
        h = None
        while p:
            if p.val == val:
                pass
            else:
                if pv == None:
                    h = p
                else:
                    pv.next = p
                pv = p
            
            p = p.next
            
        if pv:
            pv.next = None
        return h
        
        
        
        
#Remove Linked List Elements
#https://leetcode.com/problems/remove-linked-list-elements/