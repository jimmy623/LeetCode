class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == None:
            return None
        nodes = []
        p = head
        while p:
            nodes.append(p)
            p = p.next
        
        start = 0
        end = len(nodes)-1
        pre = None
        while start <= end:
            if pre:
                pre.next = nodes[start]
            nodes[start].next = nodes[end]
            pre = nodes[end]
            start += 1
            end -=1
        
        pre.next = None
            
        return head
#Reorder List
#https://oj.leetcode.com/problems/reorder-list/