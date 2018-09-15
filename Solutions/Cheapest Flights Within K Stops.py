import heapq
from collections import defaultdict
# from sets import Set
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = defaultdict(dict)
        for s,d,cost in flights:
        	graph[s][d] = cost

        pq = [(0,0,src)]
        best = {}
        while pq:
        	cost,k,place = heapq.heappop(pq)
        	if k > K+1 or cost > best.get((k,place),float('inf')):
        		continue
        	if place == dst:
        		return cost

        	for d,val in graph[place].iteritems():
        		newCost = cost + val
        		if newCost < best.get((k+1, d), float('inf')):
        			heapq.heappush(pq,(newCost,k+1,d))
        			best[(k+1,d)] = newCost
        return -1





        # #bfs
        # imax = 999999
        # cities = [imax for _ in xrange(n)]
        # cities[src] = 0
        # for i in xrange(K+1):
        # 	newCities = list(cities)
        # 	for s,d,cost in flights:
        # 		if cities[s] != imax:
        # 			newCities[d] = min(newCities[d],cities[s]+cost)
        # 	cities = newCities
       	# if cities[dst] != imax:
       	# 	return cities[dst]
       	# else:
        # 	return -1

s = Solution()
# s.findCheapestPrice(4,[[0,1,1],[0,2,5],[1,2,1],[2,3,1]],0,3,1)
s.findCheapestPrice(5,[[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]],0,4,1)




#Cheapest Flights Within K Stops
#https://leetcode.com/problems/cheapest-flights-within-k-stops/description/