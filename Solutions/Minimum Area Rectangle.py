from collections import defaultdict

class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        s = set()
        d = defaultdict(list)
        for point in points:
        	s.add((point[0],point[1]))
        	d[point[0]].append(point[1])
       	keys = d.keys()
       	keys.sort()
       	minArea = 0
       	for k in keys:
       		d[k].sort()
       	for i1 in range(len(keys)-1):
       		x1 = keys[i1]
       		for j1 in range(len(d[x1])-1):
       			y1 = d[x1][j1] 
       			for i2 in range(i1+1,len(keys)):
       				x2 = keys[i2]
       				for j2 in range(len(d[x2])):
       					y2 = d[x2][j2]
       					if y2 <= y1:
       						continue
       					if ((x1,y2) in s) and ((x2,y1) in s):
       						area = (x2-x1) * (y2-y1)
       						if minArea == 0:
       							minArea = area
       						else:
       							minArea = min(area,minArea)
       						break

       	return minArea







# points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]

s = Solution()
print s.minAreaRect(points)

#Minimum Area Rectangle
#https://leetcode.com/problems/minimum-area-rectangle/