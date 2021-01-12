class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        m = len(houses)
        n = len(heaters)
        j = 0
        result = 0
       	for i in range(m):
       		h = houses[i]
       		if heaters[j] > h and j > 0:
       			j -= 1
       		distance = 10**10
       		while True:
       			distance = min(distance,abs(h-heaters[j]))
       			# print h,heaters[j],distance
       			if heaters[j] > h:
       				break
       			j+=1
       			if j == n:
       				j = j-1
       				break
       		result = max(distance,result)
       	return result

houses = [1,2,3,4]
heaters = [1,4]
s = Solution()
print s.findRadius(houses,heaters)

#Heaters
#https://leetcode.com/problems/heaters/