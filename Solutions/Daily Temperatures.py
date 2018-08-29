class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        memory = [0] * 101

        result = []
        for i in xrange(len(temperatures)-1,-1,-1):
        	t = temperatures[i]
        	memory[t] = i
        	diff = 300000
        	for j in xrange(t+1,101):
        		if memory[j] > i:
        			diff = min(diff,memory[j]-i)
        			if diff == 1:
        				break
        	if diff < 300000:
        		result.append(diff)
        	else:
        		result.append(0)
        result.reverse()
        return result

s = Solution()
print s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])     
#Daily Temperatures
#https://leetcode.com/problems/daily-temperatures/description/