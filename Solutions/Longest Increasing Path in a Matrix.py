class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        matrix = matrix
        cache = [[0 for _ in xrange(n)] for _ in xrange(m)]
        result = 0
        def dfs(i,j):
            if cache[i][j]:
                return cache[i][j]
            count = 1
            for a,b in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                val = matrix[i][j]
                if 0 <= a < m and 0<= b <n and matrix[a][b] > val:
                    count = max(count,1 + dfs(a,b))
            cache[i][j] = count
            return count

        for x in xrange(m):
            for y in xrange(n):
                result = max(result,dfs(x,y))
        return result


s = Solution()
print s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])

#Longest Increasing Path in a Matrix
#https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/