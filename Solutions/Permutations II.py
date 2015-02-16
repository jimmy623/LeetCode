class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        self.result = []
        self.dict = {}
        self.n = len(num)
        for i in num:
            if i in self.dict:
                self.dict[i] += 1
            else:
                self.dict[i] = 1
        #print self.dict
        keys = self.dict.keys()
        board = [None for x in range(self.n)]

        self.dfs(board,keys)
        return self.result
    
    def dfs(self,board,keys):
        if len(keys) == 0:
            self.result.append(board)
            return
        
        newKeys = list(keys)
        key = newKeys.pop()
        spaces = []
        for i in range(self.n):
            if board[i] == None:
                spaces.append(i)
        
        options = self.select(spaces,self.dict[key])

        for opt in options:
            newBoard = list(board)
            for i in opt:
                newBoard[i] = key
            self.dfs(newBoard,newKeys)
        
                
    
    def select(self,candidates,n):
        if len(candidates) == n:
            return [candidates]
        choices = []
        
        newCandidates = list(candidates)
        v = newCandidates.pop()

        if n == 1:
            choices.append([v])
        else:
            withit = self.select(newCandidates,n-1)
            for i in withit:
                i.append(v)
                choices.append(i)
        
        withoutit = self.select(newCandidates,n)
        choices += withoutit
        return choices
                
                
s = Solution()
#print s.select([0,1,2,3,4],3)
print s.permuteUnique([1,1,2])

#Permutations II
#https://oj.leetcode.com/problems/permutations-ii/