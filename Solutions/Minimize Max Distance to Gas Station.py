import heapq
class Solution(object):
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        # def possible(d):
        # 	if sum([int((stations[i]-stations[i-1])/d) for i in xrange(1,len(stations))]) < K:
        # 		return True
        # 	else:
        # 		return False
        # lo = 0
        # hi = 10**8
        # while hi - lo > 10**-6:
        # 	mid = (lo + hi) / 2.0
        # 	if possible(mid):
        # 		hi = mid
        # 	else:
        # 		lo = mid
        # return lo



        minmax = float(stations[-1] - stations[0]) / K
        distance = []
        for i in xrange(1,len(stations)):
        	d = stations[i] - stations[i-1]
        	n = max(1,int(d/minmax))
        	K -= (n-1)
       		heapq.heappush(distance,[-d/float(n),n])
       	for i in xrange(K):
       		[d,count] = heapq.heappop(distance)
       		heapq.heappush(distance,[float(d*count)/(count+1),count+1])
       	biggest = heapq.heappop(distance)
       	return -biggest[0]

#Minimize Max Distance to Gas Station
#https://leetcode.com/problems/minimize-max-distance-to-gas-station/description/