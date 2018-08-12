import heapq

def compare(a,b):
        if a[0] != b[0]:
            return a[0] - b[0]
        if a[2] == b[2]:
            if a[2] == "s":
                return b[1] - a[1]
            else:
                return a[1] - b[1]
        if a[2] == "s":
            return -1
        else:
            return 1
        

class Solution(object):
    

    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        points = []
        for b in buildings:
            points.append([b[0],b[2],"s"])
            points.append([b[1],b[2],"e"])
        
        points = sorted(points,cmp = compare)
        print points
        height = [0]
        maxHeight = 0
        result = []
        for p in points:
            if p[2] == "s":
                height.append(p[1])
                if p[1] > maxHeight:
                    result.append([p[0],p[1]])
                    maxHeight = p[1]
            else:
                height.remove(p[1])
                if p[1] == maxHeight:
                    height.sort()
                    maxHeight = height[-1]
                    if maxHeight != p[1]:
                        result.append([p[0],maxHeight])
        return result


    

s = Solution()
data = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
data = [[0,2,3],[2,5,3]]
data = [[1,2,1],[1,2,2],[1,2,3]]
print s.getSkyline(data)
# The Skyline Problem
#https://leetcode.com/problems/the-skyline-problem/description/