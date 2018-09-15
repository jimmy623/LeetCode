class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        k = len(days[0])
        n = len(flights)

        last = [-1 for _ in xrange(n)]
        last[0] = 0
        week = 0
        while week < k:
            new = [-1 for _ in xrange(n)]
            for i,v in enumerate(last):
                if v >= 0:
                    new[i] = max(new[i],v+days[i][week])
                    for city,possible in enumerate(flights[i]):
                        if possible:
                            new[city] = max(new[city],v+days[city][week])
            last = new
            week += 1
        return max(last)



        # dfs kindof brute force
        # k = len(days[0])
        # n = len(flights)
        # self.maxHoliday = 0
        # def dfs(city,count,week):
        #     # print city,count,week
        #     if week == k:
        #         self.maxHoliday = max(self.maxHoliday,count)
        #         return
        #     for candidate,possible in enumerate(flights[city]):
        #         if possible:
        #             dfs(candidate,count+days[candidate][week],week+1)
        #     dfs(city,count+days[city][week],week+1)

        # dfs(0,0,0)
        # return self.maxHoliday


flights = [[0,1,1],[1,0,1],[1,1,0]]
days = [[1,3,1],[6,0,3],[3,3,3]]       

flights = [[0,0,0],[0,0,0],[0,0,0]]
days = [[1,1,1],[7,7,7],[7,7,7]]

flights = [[0,1,1],[1,0,1],[1,1,0]]
days = [[7,0,0],[0,7,0],[0,0,7]]
s = Solution()
print s.maxVacationDays(flights,days)
#Maximum Vacation Days
#https://leetcode.com/problems/maximum-vacation-days/description/