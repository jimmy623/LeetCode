# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head == None:
            return None
        p1 = head
        p2 = head
        p3 = head
        
        while p1.next != None and p2.next != None and p2.next.next!=None:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                while p1 != p3:
                    p1 = p1.next
                    p3 = p3.next
                return p1
                
        
        return None
#Linked List Cycle II
#https://oj.leetcode.com/problems/linked-list-cycle-ii/