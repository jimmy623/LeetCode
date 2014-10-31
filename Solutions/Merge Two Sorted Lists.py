# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        string = "val:" + str(self.val) + " next:"
        if self.next == None:
            string += "None"
        else:
            string += str(self.next.val)
        return  string

def printList(head):
    print "print list"
    string = ""
    while head != None:
        string += str(head.val)+"->"
        head = head.next
    string = string[:-2]
    print string

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        head = None
        point = None
        while l1 != None or l2 != None:
            if head == None:
                if l1 == None:
                    return l2
                elif l2 == None:
                    return l1
                elif l1.val < l2.val:
                    head = l1
                    point = l1
                    l1 = l1.next
                else:
                    head = l2
                    point = l2
                    l2 = l2.next
                continue

            if l1 == None:
                point.next = l2
                point = l2
                l2 = l2.next
            elif l2 == None or l1.val < l2.val:
                point.next = l1
                point = l1
                l1 = l1.next
            else:
                point.next = l2
                point = l2
                l2 = l2.next

        return head




#####################

a = ListNode(1)
b = ListNode(2)
c = ListNode(2)
d = ListNode(3)

a.next = b
b.next = c
c.next = d

e = ListNode(2)
f = ListNode(3)
g = ListNode(5)

e.next = f
f.next = g

#####################

s = Solution()
result = s.mergeTwoLists(a,e)

printList(result)
#Merge Two Sorted Lists
#https://oj.leetcode.com/problems/merge-two-sorted-lists/
