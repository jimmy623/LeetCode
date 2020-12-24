class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        result = [0 for _ in range(n)]
        callstack = []
        functionIndex = 0
        timestampIndex = 1
        previousTimeIndex = 2
        for log in logs:
        	items = log.split(":")
        	functionID = int(items[functionIndex])
        	action = items[timestampIndex]
        	timestamp = int(items[previousTimeIndex])
        	if action == "start":
        		if len(callstack) > 0:
        			callstack[-1][previousTimeIndex] += timestamp - callstack[-1][timestampIndex]
        		callstack.append([functionID,timestamp,0])
        	else:
        		time = timestamp - callstack[-1][timestampIndex] +1
        		result[callstack[-1][functionIndex]] += time + callstack[-1][previousTimeIndex]
        		callstack.pop()
        		if len(callstack) > 0:
        			callstack[-1][timestampIndex] = timestamp + 1
        	# print callstack
        return result
        		



s = Solution()
# n = 2
# logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
# n = 1
# logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
# n = 2
# logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]

n = 2
logs = ["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]
print s.exclusiveTime(n,logs)


#Exclusive Time of Functions
#https://leetcode.com/problems/exclusive-time-of-functions/