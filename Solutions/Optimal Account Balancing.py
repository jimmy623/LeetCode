from collections import defaultdict
class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        self.d = defaultdict(int)
        for a,b,val in transactions:
            self.d[a] -= val
            self.d[b] += val
        account = []
        for k in self.d:
            if self.d[k]:
                account.append(self.d[k])
        self.accounts = account
        print self.accounts
        return self.dfs(0)

    def dfs(self,k):
        while k < len(self.accounts) and not self.accounts[k]:
            k+=1
        res = 99999999

        prev = 0
        for i in xrange(k+1,len(self.accounts)):
            if (self.accounts[i] != prev and self.accounts[i]*self.accounts[k] < 0):
                self.accounts[i] += self.accounts[k]
                res = min(res,1+self.dfs(k+1))
                self.accounts[i] -= self.accounts[k]
                prev = self.accounts[i]

        if res < 99999999:
            return res
        else:
            return 0


s = Solution()
print s.minTransfers([[0,1,10], [2,0,5]])
print s.minTransfers([[0,1,10], [1,0,1], [1,2,5], [2,0,5]])


#Optimal Account Balancing
#https://leetcode.com/problems/optimal-account-balancing/description/