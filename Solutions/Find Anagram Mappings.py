class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        m = [[] for i in xrange(100)] 
        k = sorted(A)
        #print m
        for i in xrange(len(B)):
        	#print i,A[i],m[A[i]]

        	m[k.index(B[i])].append(i)
        r = []
        #print m
        for n in A:
        	r.append(m[k.index(n)].pop())
        return r

s = Solution()
A= [12,28,46,32,50]
B = [50,12,32,46,28]
print s.anagramMappings(A,B)
#Find Anagram Mappings
#https://leetcode.com/problems/find-anagram-mappings/description/