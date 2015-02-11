class Solution:
    # @return an integer
    def totalNQueens(self, n):
        board = []
        self.results = []
        for i in range(n):
            board.append(-1)
        
        self.addQueen(board,0)
        
        return len(self.results)
        
            
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
        
#N-Queens II
#https://oj.leetcode.com/problems/n-queens-ii/