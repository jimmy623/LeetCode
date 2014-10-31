class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        col = len(board)
        row = len(board[0])
        for i in range(col):
            for j in range(row):
                result = self.search(board,i,j,word)
                if result:
                    return True
        return False

    def valid(self,board,i,j):
        if i < 0 or i >= len(board):
            return False
        if j < 0 or j >= len(board[0]):
            return False
        if board[i][j] == "$":
            return False
        return True

    def search(self,board,i,j,string):
        target = string[0]
        if not self.valid(board,i,j):
            return False
        if board[i][j] == target:
            if len(string) == 1:
                return True
            else:
                board[i][j] = "$"
                next = string[1:]
                up = self.search(board,i-1,j,next)
                left = self.search(board,i,j-1,next)
                right = self.search(board,i,j+1,next)
                down = self.search(board,i+1,j,next)
                result = up or left or right or down
                if result:
                    return True
                else:
                    board[i][j] = target
                    return False
        else:
            return False



board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
        ]


s = Solution()
result = s.exist(board,"SEE")
print result

#Word Search
#https://oj.leetcode.com/problems/word-search/
