class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        board = []
        self.results = []
        for i in range(n):
            board.append(-1)
        
        self.addQueen(board,0)
        r = []
        for v in self.results:
            one = []
            for i in range(n):
                one.append("."*v[i]+"Q" + "."*(n-v[i]-1))
            r.append(one)
        return r
        
            
    def addQueen(self,board,row):
        if row == len(board):
            self.results.append(board)
            return

        for i in range(len(board)):
            
            flag = True
            for j in range(row):
                if board[j] == i or board[j] == i-(row-j) or board[j] == i+(row-j):
                    flag = False
                    break
                
            if flag:
                nBoard = list(board)
                nBoard[row] = i
                self.addQueen(nBoard,row+1)
        
s = Solution()
print s.solveNQueens(4)
#N-Queens
#https://oj.leetcode.com/problems/n-queens/