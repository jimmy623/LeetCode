# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head == None:
            return None
        
        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        
        r = self.sort(head,length)
        return r
            
    def sort(self,node,length):
        if length == 1:
            return node
        if length == 2:
            if node.val < node.next.val:
                return node
            else:
                head = None
                head = node.next
                head.next = node
                node.next = None
                return head
        middle = length / 2
        
        p = node
        count = 1
        while count < middle:
            p = p.next
            count += 1
        
        h1 = node
        h2 = p.next
        p.next = None
        
        r1 = self.sort(h1,middle)
        r2 = self.sort(h2,length-middle)
        head = self.mergeList(r1,r2)
        return head

    def mergeList(self,h1,h2):
        head = None
        if h1.val < h2.val:
            head = h1
            h1 = h1.next
        else:
            head = h2
            h2 = h2.next

        p = head
        while h1 or h2:
            if h1 == None:
                p.next = h2
                h2 = h2.next
            elif h2 == None:
                p.next = h1
                h1 = h1.next
            else:
                if h1.val < h2.val:
                    p.next = h1
                    h1 = h1.next
                else:
                    p.next = h2
                    h2 = h2.next
            p = p.next
        p.next = None
        return head
        
def printList(node):
    while node:
        print node.val
        node = node.next
        
s = Solution()
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(4)
r = s.sortList(head)
printList(r)
#Sort List
#https://oj.leetcode.com/problems/sort-list/