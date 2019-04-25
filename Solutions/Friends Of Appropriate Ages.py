from collections import defaultdict
class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        # p = [0 for _ in xrange(150)]
        # for a in ages:
        # 	for i in xrange(int(a*0.5+8),a+1):
        # 		p[i] += 1
        # result = 0
        # for a in ages:
        # 	if p[a] > 0:
        # 		result += p[a]-1
        # return result
        d = defaultdict(int)
        for a in ages:
        	d[a] += 1
        k = sorted(d.keys())
        result = 0
        window = 0
        left = 0
        end = 0
        while end < len(k):
        	window += d[k[end]]
        	bar = k[end]*0.5+7
        	while left < end and k[left] <= bar:
        		window -= d[k[left]]
        		left+=1
        	if k[end] > 14:
        		result += d[k[end]] * (window-1)
        	end+=1
        return result


s = Solution()
data = [108,115,5,24,82]
data = [20,30,100,110,120]
data = [16,16]
data = [16,17,18]
data = [73,106,39,6,26,15,30,100,71,35,46,112,6,60,110]
print s.numFriendRequests(data)
#Friends Of Appropriate Ages
#https://leetcode.com/problems/friends-of-appropriate-ages/