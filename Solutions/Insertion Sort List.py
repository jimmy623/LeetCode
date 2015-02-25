# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head == None:
            return None
     
        p = head.next
        head.next = None
        tail = head
        while p:
            node = p
            next = p.next
            if node.val >= tail.val:
                tail.next = node
                node.next = None
                tail = node
                p = next
                continue
         
            if node.val < head.val:
                node.next = head
                head = node
            else:
                preIter = head
                iter = head.next
                while iter:
                    if node.val < iter.val:
                        preIter.next = node
                        node.next = iter
                        break
                    preIter = iter
                    iter = iter.next
                    
                if iter == None:
                    preIter.next = node
                    node.next = None
                    tail = node

            p = next
                
        return head
        
s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
# p = head
# for i in range(1,5000):
#     p.next = ListNode(i)
#     p = p.next
#     

def printList(node):
    while node:
        print node.val
        node = node.next
        

head = s.insertionSortList(head)
printList(head)
                
#Insertion Sort List
#https://oj.leetcode.com/problems/insertion-sort-list/