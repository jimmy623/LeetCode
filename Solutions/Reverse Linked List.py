# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head == None:
            return None
        
        nodes = [head]
        p = head.next
        while p:
            nodes.append(p)
            p = p.next
        
        for i in range(len(nodes)-1,0,-1):
            nodes[i].next = nodes[i-1]
        
        nodes[0].next = None
        return nodes[-1]
        
        
        
        
        
#Reverse Linked List
#https://leetcode.com/problems/reverse-linked-list/