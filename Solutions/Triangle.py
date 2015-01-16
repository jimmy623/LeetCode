class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        step = len(triangle) - 1
        if step == 0:
            return triangle[0][0]
        step -= 1
        while step >= 0:
            index = step
            while index >= 0:
                triangle[step][index] = triangle[step][index] + min(triangle[step+1][index],triangle[step+1][index+1])
                index -= 1
            step-=1
            
        return triangle[0][0]
                
t = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3],
]

s = Solution()
result = s.minimumTotal(t)
print result


#https://oj.leetcode.com/problems/triangle/
#Triangle
