from collections import defaultdict
class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """





        
        # graph = defaultdict(set)
        # cache = set()
        # incomings = defaultdict(int)
        # backEdges = []
        # for s,e in edges:
        # 	graph[s].add(e)
        # 	incomings[e] += 1
        # 	if (e,s) in cache:
        # 		backEdges.append([s,e])
        # 		backEdges.append([e,s])
        # 	cache.add((s,e))

        # search = edges+backEdges

        # for i in xrange(len(search)-1,-1,-1):
        # 	start,end = search[i]
        # 	incomings[end] -= 1
        # 	graph[start].remove(end)
        # 	root = None
        # 	# print start,end,incomings,graph
        # 	count = 0
        # 	for v in xrange(1,len(edges)+1):
        # 		if incomings[v] == 0:
        # 			count += 1
        # 			if count > 1:
        # 				root = None
        # 				break
        # 			if graph[v]:
        # 				root = v
        # 	if root:
        # 		return [start,end]
        # 	graph[start].add(end)
        # 	incomings[end] += 1



s = Solution()
# print s.findRedundantDirectedConnection([[1,2],[1,3],[2,3]])
# print s.findRedundantDirectedConnection([[1,2], [2,3], [3,4], [4,1], [1,5]])
# print s.findRedundantDirectedConnection([[2,1],[3,1],[4,2],[1,4]])
print s.findRedundantDirectedConnection([[4,2],[1,5],[5,2],[5,3],[2,4]])

        	
       
#Redundant Connection II
#https://leetcode.com/problems/redundant-connection-ii/description/