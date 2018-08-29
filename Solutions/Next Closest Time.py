from sets import Set
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        s = Set()
        # s = []
        for c in time:
        	if c in "0123456789":
        		# s.append(s)
        		s.add(c)
        # s.sort()
        split = time.index(":")
        self.split = split

        count = len(time) - 1
        permutations = [""]
        while count > 0:
        	new_per = []
        	for c in s:
        		for string in permutations:
        			new_per.append(string+c)
        	permutations = new_per
        	count -= 1

        minDiff = 9999
        minTime = ""
        for string in permutations:
        	#print string,minDiff,minTime
        	if self.isVaid(string):
        		diff = self.timeDiff(time[:split] + time[split+1:],string)
        		if diff < minDiff:
        			minTime = string[:split] + ":" + string[split:]
        			minDiff = diff
       	#print minDiff,minTime
        return minTime

    def isVaid(self,time):
    	# comp = time.split(":")
    	# hour = int(comp[0])
    	# minute = int(comp[1])
    	hour = int(time[0:self.split])
    	minute = int(time[self.split:])

    	return hour < 24 and minute < 60

    def timeDiff(self,time1,time2):
    	# comp1 = time1.split(":")
    	# hour1 = int(comp1[0])
    	# minute1 = int(comp1[1])

    	# comp2 = time2.split(":")
    	# hour2 = int(comp2[0])
    	# minute2 = int(comp2[1])
    	hour1 = int(time1[0:self.split])
    	minute1 = int(time1[self.split:])

    	hour2 = int(time2[0:self.split])
    	minute2 = int(time2[self.split:])

    	diff = minute2 - minute1 + (hour2 - hour1) * 60
    	#print "diff",time1,time2,diff
    	if diff <= 0:
    		diff += 60*24
    	return diff

s = Solution()
# print s.nextClosestTime("19:34")
# print s.nextClosestTime("23:59")
print s.nextClosestTime("20:48")
#Next Closest Time
#https://leetcode.com/problems/next-closest-time/description/