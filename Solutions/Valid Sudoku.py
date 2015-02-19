from sets import Set
class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        blocks = [Set() for i in range(9)]
        rows = [Set() for i in range(9)]
        columns = [Set() for i in range(9)]
        bCount = [0 for i in range(9)]
        cCount = [0 for i in range(9)]
        rCount = [0 for i in range(9)]
        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if  v != ".":
                    rows[i].add(v)
                    rCount[i] += 1
                    columns[j].add(v)
                    cCount[j] += 1
                    blocks[(i/3)*3 + j/3].add(v)
                    bCount[(i/3)*3 + j/3] += 1
                    
        for i in range(9):
            if rCount[i] != len(rows[i]) or cCount[i] != len(columns[i]) or bCount[i] != len(blocks[i]):
                return False
        return True
                    
            
            
                
#Valid Sudoku
#https://oj.leetcode.com/problems/valid-sudoku/
