# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None

        a,b = 1,1
        
        pa = headA
        while pa.next:
            a+=1
            pa = pa.next
            
        pb = headB
        while pb.next:
            b+= 1
            pb = pb.next
            
        if pa != pb:
            return None
        
        if a > b:
            count = a - b
            while count:
                headA = headA.next
                count -= 1
        else:
            count = b - a
            while count:
                headB = headB.next
                count -= 1
                
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA
            
        
        
        
        
#Intersection of Two Linked Lists
#https://oj.leetcode.com/problems/intersection-of-two-linked-lists/