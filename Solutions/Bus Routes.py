# from sets import Set
from collections import defaultdict
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
        	return 0
        d = defaultdict(list)
        for i,route in enumerate(routes):
        	for stop in route:
        		d[stop].append(i)
        count = 1
        candidate = [S]
        visited = set([S])
        while candidate:
        	newCandidates = []
        	for stop in candidate:
        		for i in d[stop]:
        			route = routes[i]
        			for k in route:
        				if k not in visited:
        					if k == T:
        						return count
        					visited.add(k)
        					newCandidates.append(k)
        			routes[i] = []
        	candidate = newCandidates
        	count += 1
        return -1




        # if S == T:
        # 	return 0
        # d = defaultdict(Set)
        # rSet = []
        # for i in xrange(len(routes)):
        # 	route = routes[i]
        # 	rSet.append(Set(route))

        # count = 1
        # candidates = Set()
        # candidates.add(S)
        # visited = Set()
        # visited.add(S)
        # while candidates:
        # 	if T in candidates:
        # 		return count-1
        # 	visited.update(candidates)
        # 	alive = [True] * len(rSet)
        # 	newCandidates = Set()
        # 	for i in xrange(len(rSet)):
        # 		if candidates.intersection(rSet[i]):
        # 			newCandidates.update(rSet[i])
        # 	newCandidates.difference_update(visited)
        # 	candidates = newCandidates
        # 	count +=1
        # return -1

s = Solution()
print s.numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]],15,12)
#Bus Routes
#https://leetcode.com/problems/bus-routes/description/