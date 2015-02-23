class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n/2):
            for j in range(0,n-1-i*2):
                
                lower = i
                upper = n -1 -i
                
                v1 = matrix[i][lower + j]
                v2 = matrix[lower + j][upper]
                v3 = matrix[upper][upper-j]
                v4 = matrix[upper - j][lower]

                matrix[i][lower + j] = v4
                matrix[lower + j][upper] = v1
                matrix[upper][upper-j] = v2
                matrix[upper - j][lower] = v3

s = Solution()
m = [
[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]
]
r = s.rotate(m)
        
#Rotate Image
#https://oj.leetcode.com/problems/rotate-image/