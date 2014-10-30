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
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if head == None:
            return head
        remains = True
        last = None
        point = head
        while remains:
            nodes = []
            for i in range(k):
                nodes.append(point)
                if point.next == None:
                    remains = False
                    break
                point = point.next
            if len(nodes) != k:
                break

            if point == None:
                remains = False
                nodes[0].next = None
            else:
                nodes[0].next = nodes[k-1].next
            
            for i in range(k-1,0,-1):
                nodes[i].next = nodes[i-1]
            if last == None:
                 head = nodes[k-1]
            else:
                last.next = nodes[k-1]

            last = nodes[0]
            point = last.next
        return head






a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

s = Solution()
result = s.reverseKGroup(a,3)

printList(result)




#https://oj.leetcode.com/problems/reverse-nodes-in-k-group/
#Reverse Nodes in k-Group