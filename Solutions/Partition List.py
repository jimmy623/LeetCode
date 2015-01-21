# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printList(head):
    print "print list"
    string = ""
    while head != None:
        string += str(head.val)+"->"
        head = head.next
    string = string[:-2]
    print string

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        less = None
        lp = None
        greater = None
        gp = None
        p = head
        while p != None:
            if p.val < x:
                if lp != None:
                    lp.next = p
                    lp = p
                else:
                    less = p
                    lp = p
            else:
                if gp != None:
                    gp.next = p
                    gp = p
                else:
                    greater = p
                    gp = p
            p = p.next
            
        if less == None or greater == None:
            return head
        else:
            lp.next = greater
            gp.next = None
            return less


a = ListNode(2)
b = ListNode(1)
a.next = b

s = Solution()
r = s.partition(a,2)
printList(r)

#Partition List
#https://oj.leetcode.com/problems/partition-list/