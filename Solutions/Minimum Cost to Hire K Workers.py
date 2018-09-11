class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        workers = sorted([float(w) / q, q] for w, q in zip(wage, quality))
        res = float('inf')
        qsum = 0
        heap = []
        for r, q in workers:
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > K: qsum += heapq.heappop(heap)
            if len(heap) == K: res = min(res, qsum * r)
        return res



        
    #   self.n = len(quality)


    #   self.min = 9999999999
        

    #   self.quality = quality
    #   self.wage = wage
    #   self.rate = [float(wage[i])/quality[i] for i in xrange(self.n)]
    #   self.select(0,K,[])

    #   return self.min

    # def check(self,stack):
        
    #   maxRate = max([self.rate[i] for i in stack])
    #   #print stack,maxRate
    #   cost = sum(self.quality[i] * maxRate for i in stack)
    #   self.min = min(self.min,cost)

    # def select(self,i,remain,stack):
    #   if remain == 0:
    #       self.check(stack)
    #       return
    #   if i >= self.n:
    #       return
        
    #   # print i,remain,stack
    #   stack.append(i)
    #   self.select(i+1,remain-1,stack)
    #   stack.pop()
    #   self.select(i+1,remain,stack)

s = Solution()
quality = [3,1,10,10,1] 
wage = [4,8,2,2,7]
K = 3

# quality = [10,20,5]
# wage = [70,50,30]
# K = 2
print s.mincostToHireWorkers(quality,wage,K)
#Minimum Cost to Hire K Workers
#https://leetcode.com/problems/minimum-cost-to-hire-k-workers/description/