# from collections import Counter
# class Solution(object):
#     def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # sum1 = []
        # for a in A:
        # 	for b in B:
        # 		sum1.append(a+b)
       	# c1 = Counter(sum1)
       	# count = 0
        # sum2 = []
        # for c in C:
        # 	for d in D:
        # 		if c1[-(c+d)]:
        # 			count += c1[-(c+d)]
       	# return count

from collections import defaultdict
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        d1 = defaultdict(int)
        sum1 = []
        for a in A:
        	for b in B:
        		sum1.append(a+b)
        		d1[a+b]+=1
        count = 0		
        sum2 = []
        for c in C:
        	for d in D:
        		if d1[-(c+d)]:
        			count += d1[-(c+d)]

       	return count

#4Sum II
#https://leetcode.com/problems/4sum-ii/description/