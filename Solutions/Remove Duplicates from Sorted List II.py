class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
            return None
        
        start = None
        pre = None
        
        p = head 
        unique = True
        
        while p.next:
            if p.next.val == p.val:
                unique = False
            else:
                if unique:
                    if start == None:
                        start = p
                        pre = p
                    else:
                        pre.next = p
                        pre = p                
                unique = True
                    
            p = p.next
            
        
        if unique:
            if start == None:
                start = p
            else:
                pre.next = p
        else:
            if pre:
                pre.next = None
                
        return start
        
    
#Remove Duplicates from Sorted List II
#https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list-ii/