class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        result = None
        dsu = [-1] * (len(edges)+1)
        for s,e in edges:
        	ps = s
        	pe = e
        	while  dsu[ps] != -1:
        		ps = dsu[ps]
        	while  dsu[pe] != -1:
        		pe = dsu[pe]

        	if ps == pe:
        		result = [s,e]
        		continue
        	dsu[ps] = pe

        return result
        

#Redundant Connection
#https://leetcode.com/problems/redundant-connection/description/