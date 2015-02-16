class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):

        n = len(A)
        if n == 1:
            return 0
        step = 1
        position = 0
        maxx = A[0]
        while True:
            if maxx >= n-1:
                return step
            temp = maxx
            for i in range(position+1,temp+1):
                maxx = max(maxx,i+A[i])
            
            step += 1
            position = temp
                
        
        
s = Solution()
a = [1,1,1,1]
print s.jump(a)

#Jump Game II
#https://oj.leetcode.com/problems/jump-game-ii/

'''
from sets import Set
class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        n = len(A)
        if n == 1:
            return 0
        
        candidates = [0]
        visited = Set()
        
        step = 1
        while True:
            newCandidates = []
            for c in candidates:
                for i in range(c+A[c],c,-1):
                    #print c,i
                    if i >= n-1:
                        return step
                    
                    if not i in visited:
                        newCandidates.append(i)
                        visited.add(i)
                    
            candidates = newCandidates
            step += 1
            if len(candidates) == 0:
                break
        return None
'''