from sets import Set
class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        sumA = sum(A)
        possible = False
        for i in xrange(n/2+1):
            if sumA * i % n == 0:
                possible = True
                break
        if not possible:
            return False


        dp = [Set() for _ in xrange(n/2+1)]
        dp[0].add(0)
        for num in A:
            for i in xrange(n/2,0,-1):
                if dp[i-1]:
                    for s in dp[i-1]:
                        dp[i].add(s+num)
        for i in xrange(1,n/2+1):
            if sumA * i %n == 0:
                if sumA * i / n in dp[i]:
                    return True
        return False

s = Solution()
print s.splitArraySameAverage([1,6,1])





        # for i in xrange(1,(1<<n)-1):
        # 	sumB = 0.0
        # 	lenB = 0
        # 	subC = 0.0
        # 	lenC = 0
        # 	for k in xrange(n):
        # 		if 1<<k & i:
        # 			sumB += A[k]
        # 			lenB += 1
        # 			# B.append(A[k])
        # 		else:
        # 			sumC += A[k]
        # 			lenC += 1
        # 			# C.append(A[k])
        # 	# if sum(B)/float(len(B)) == sum(C)/float(len(C)):
        # 	if sumB/lenB == subC/lenC:
        # 		return True
        # return False
#Split Array With Same Average
#https://leetcode.com/problems/split-array-with-same-average/description/