# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        # Store the mapping between old nodes and new nodes
        mapOldToNew ={None:None}
        
        # Clone all the old nodes with only labels.
        current = head
        while current != None:
            mapOldToNew[current] = RandomListNode(current.label)
            current = current.next
        
        # Assign the next and random of new cloned nodes.
        current = head
        while current != None:
            mapOldToNew[current].next = mapOldToNew[current.next]
            mapOldToNew[current].random = mapOldToNew[current.random]
            current = current.next
        
        # Return the cloned head
        return mapOldToNew[head]
        
#Copy List with Random Pointer
#https://oj.leetcode.com/problems/copy-list-with-random-pointer/