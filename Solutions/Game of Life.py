class Solution(object):
	def gameOfLife(self, board):
		"""
		:type board: List[List[int]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		self.board = board
		self.m = len(board)
		self.n = len(board[0])
		for x in xrange(self.m):
			for y in xrange(self.n):
				(live,dead) = self.liveAndDeath(x,y)
				if board[x][y] == 1:
					if live < 2:
						board[x][y] = 2
					elif live > 3:
						board[x][y] = 2
				else:
					if live == 3:
						board[x][y] = -1
		for x in xrange(self.m):
			for y in xrange(self.n):
				if board[x][y] == 2:
					board[x][y] = 0
				if board[x][y] == -1:
					board[x][y] = 1
		
	def liveAndDeath(self,x,y):
		self.live = 0
		self.dead = 0

		def isValid(x,y):
			if x < 0 or x >= self.m:
				return False
			if y < 0 or y >= self.n:
				return False
			return True

		def visit(x,y):
			if isValid(x,y):
				if self.board[x][y] in [0,-1]:
					self.dead += 1
				elif self.board[x][y] in [1,2]:
					self.live += 1
		
		visit(x-1,y-1)
		visit(x-1,y)
		visit(x-1,y+1)
		visit(x,y-1)
		visit(x,y+1)
		visit(x+1,y-1)
		visit(x+1,y)
		visit(x+1,y+1)

		return (self.live,self.dead)
			
s = Solution()
data = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
s = s.gameOfLife(data)
print data

#Game of Life
#https://leetcode.com/problems/game-of-life/description/