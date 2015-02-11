# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 == None and l2 == None:
            return None
        
        head = None
        p = None
        remain = 0
        while l1 or l2:
            v1 = 0
            v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            sum = v1+v2 + remain
            if sum >= 10:
                sum = sum-10
                remain = 1
            else:
                remain = 0
                
            if head == None:
                head = ListNode(sum)
                p = head
            else:
                p.next = ListNode(sum)
                p = p.next
                
        if remain:
            p.next = ListNode(1)
            
        return head
            
            
            
            
#Add Two Numbers
#https://oj.leetcode.com/problems/add-two-numbers/