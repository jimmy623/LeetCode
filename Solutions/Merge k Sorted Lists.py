# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        while None in lists:
            lists.remove(None)
        n = len(lists)
        if n == 0:
            return None
        head = None
        pre = None
        
        dict = {}
        for p in lists:
            while p:
                if p.val in dict:
                    dict[p.val].append(p)
                else:
                    dict[p.val] = [p]
                p = p.next
                    
        keys = dict.keys()
        keys.sort()
        for k in keys:
            for node in dict[k]:
                if head:
                    pre.next = node
                else:
                    head = node
                pre = node
        node.next = None
        return head
                
                
        
#Merge k Sorted Lists
#https://oj.leetcode.com/problems/merge-k-sorted-lists/

'''
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        while None in lists:
            lists.remove(None)
        n = len(lists)
        if n == 0:
            return None
        head = None
        pre = None
        
        while n:
            min = 0
            for i in range(1,n):
                if lists[i].val < lists[min].val:
                    min = i
            
            node = lists[min]
            if head:
                pre.next = node
            else:
                head = node
            
            pre = node
            if node.next == None:
                lists.pop(min)
            else:
                lists[min] = node.next
            
            n = len(lists)
            
        
        pre.next = None
        return head
'''