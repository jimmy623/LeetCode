class Solution:
    # @return an integer
    def maxArea(self, height):
        max = 0
        count = len(height)
        maxLeft = height[0]
        maxRight = height[count-1]
        lefts = {0:maxLeft}
        rights = {count-1:maxRight}
        for i in range(1,count-1):
            if height[i] > maxLeft:
                maxLeft = height[i]
                lefts[i] = maxLeft
            if height[count - i -1] > maxRight:
                maxRight = height[count - i -1]
                rights[count - i -1] = maxRight
                
       
        for l in lefts.keys():
            for r in rights.keys():
                if l < r:
                    area = min(lefts[l],rights[r]) * (r-l)
                    if area > max:
                        max = area
        return max
                
s = Solution()
print s.maxArea([1,1])           
            
#Container With Most Water
#https://oj.leetcode.com/problems/container-with-most-water/