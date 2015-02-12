class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        start = 0
        count = gas[0] - cost[0]
        end = (1) % n
        
        while start < n:
            if count >= 0:
                count = count + gas[end] - cost[end]
                end = (end+1) % n
                if count >= 0:
                    if end == start:
                        return start
            else:
                count = count + cost[start] - gas[start]
                start += 1
                
        return -1
                
                
            
        
        
            
            
s = Solution()
#print s.canCompleteCircuit([1,2],[2,1])  
print s.canCompleteCircuit([5],[4])  
#Gas Station
#https://oj.leetcode.com/problems/gas-station/