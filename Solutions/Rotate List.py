# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head == None:
            return None
        if k == 0:
            return head
            
        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        k = k%length
        if k == 0:
            return head
            
        p = head
        ptail = head
        count = 0
        while ptail.next:
            if count < k:
                count += 1
            else:
                p = p.next
            
            ptail = ptail.next
        
        if p == head and count < k:
            return head
            
        ptail.next = head
        newHead = p.next
        p.next = None
        return newHead
#Rotate List
#https://oj.leetcode.com/problems/rotate-list/