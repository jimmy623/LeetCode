from collections import deque
class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        height.append(0)
        n = len(height)
        
        keys = deque([0])
        maxArea = height[0]
        
        i = 1
        while i < n:
            
            if len(keys) == 0 or height[i] > height[keys[-1]]:
                keys.append(i)
                i+=1
                continue
            else:
                key = keys.pop()
                length = 1
                if len(keys) == 0:
                    length = i
                else:
                    length = i-keys[-1]-1
                area = height[key]*length
                maxArea = max(maxArea,area)
                    
        return maxArea
                    
                
            
            
         
s = Solution()
height = [0,2,0]
height = [2,1,5,6,2,3]
# height = [1,1]
# height = [2,1,2]
# 
# height = [4,2,0,3,2,5]
print s.largestRectangleArea(height)
