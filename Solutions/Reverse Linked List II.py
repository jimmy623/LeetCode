# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        count = 1
        p = head
        pre = None
        start = None
        beforeStart = None
        while True:
            next = p.next
            if count == m:
                beforeStart = pre
                start = p
                
            if count > m and count <= n:
                p.next = pre
                
            if count == n:
                start.next = next
                if beforeStart:
                    beforeStart.next = p
                else:
                    head = p
                return head
                
            pre = p
            p = next
            count += 1
            
                
#Reverse Linked List II
#https://oj.leetcode.com/problems/reverse-linked-list-ii/