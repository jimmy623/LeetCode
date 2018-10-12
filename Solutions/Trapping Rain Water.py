class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
        	return 0
        bars = [(height[0],0)]
        result = 0
        for i in xrange(1,len(height)):
        	for j in xrange(len(bars)):
        		if bars[j][0] < height[i]:
        			if j > 0:
        				result += (bars[j][0] - bars[j-1][0]) * (i-bars[j][1]-1)	
        		else:
        			if j > 0 and bars[j-1][0] < height[i]:
        				result += (height[i] - bars[j-1][0]) * (i - bars[j][1]-1)
        			if bars[j][0] == height[i]:
        				bars = [(height[i],i)] + bars[j+1:]
        			else:
        				bars = [(height[i],i)] + bars[j:]
        			break
        	if height[i] > bars[-1][0]:
        		bars = [(height[i],i)]
        	elif height[i] < bars[0][0]:
        		bars = [(height[i],i)] + bars
        return result

s = Solution()
print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print s.trap([4,2,3])

#Trapping Rain Water
#https://leetcode.com/problems/trapping-rain-water/description/