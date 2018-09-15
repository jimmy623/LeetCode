from collections import defaultdict
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ds = [defaultdict(int) for _ in xrange(len(points))]
        for i,point1 in enumerate(points):
        	for point2 in points:
        		distance = (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
        		ds[i][distance] += 1
        count = 0
        for d in ds:
        	for i in d:
        		if d[i] > 1:
        			count += d[i] * (d[i]-1)
        return count
        
#Number of Boomerangs
#https://leetcode.com/problems/number-of-boomerangs/description/