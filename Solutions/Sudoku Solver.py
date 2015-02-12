class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.board = board
        self.stop = False
        self.blocks = [[],[],[],[],[],[],[],[],[]]
        self.rows = [[],[],[],[],[],[],[],[],[]]
        self.columns = [[],[],[],[],[],[],[],[],[]]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    self.rows[i].append(int(board[i][j]))
                    self.columns[j].append(int(board[i][j]))
                    self.blocks[(i/3)*3 + j/3].append(int(board[i][j]))
                    
        
        self.add(board,0,0)
        

    def next(self,x,y):
        if y == 8:
            return (x+1,0)
        else:
            return (x,y+1)
            
    def setKey(self,x,y,v):
        self.board[x][y] = str(v)
        self.rows[x].append(v)
        self.columns[y].append(v)
        self.blocks[(x/3)*3+y/3].append(v)
        
    def removeKey(self,x,y):
        v = self.board[x][y]
        self.board[x][y] = "."
        self.rows[x].remove(int(v))
        self.columns[y].remove(int(v))
        self.blocks[(x/3)*3+y/3].remove(int(v))
        
    def validKey(self,x,y,v):
        if v in self.rows[x]:
            return False
        if v in self.columns[y]:
            return False
        if v in self.blocks[(x)/3*3+y/3]:
            return False
        return True
            
    def add(self,board,x,y):
        if board[x][y] != ".":
            if x == 8 and y == 8:
                return True
            else:
                (nx,ny) = self.next(x,y)
                return self.add(board,nx,ny)
        else:  
            for i in range(1,10):
                if self.validKey(x,y,i):
                    self.setKey(x,y,i)
                    if x == 8 and y == 8:
                        return True
                    else:
                        (nx,ny) = self.next(x,y)
                        r = self.add(board,nx,ny)
                        if r:
                            return True
                if board[x][y] != ".":
                    self.removeKey(x,y)
                              
            return False    

def printBoard(board):
    print "=========================="
    for i in board:
        print i

s = Solution()
b = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]

# b = ["519748632","783652419","426139875","357986241","264317598","198524367","975863124","832491756","641275983"]
# b = ["519748632","783652419","426139875","357986241",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
board = []
for i in b:
    row = []
    for c in i:
        row.append(c)
    board.append(row)

#printBoard(board)
s.solveSudoku(board)

printBoard(board)

#Sudoku Solver
#https://oj.leetcode.com/problems/sudoku-solver/