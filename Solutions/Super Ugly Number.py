class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1:
        	return 1
        count = len(primes)
        indexs = [0 for i in xrange(count)]
        nexts = list(primes)
        m = [1]
        p = 1
        while p < n:
        	can = min(nexts)
        	m.append(can)
        	for i in xrange(count):
        		if can == nexts[i]:
        			indexs[i] += 1
        			nexts[i] = m[indexs[i]] * primes[i]
        	p+=1
        	#print p,can
        return m[-1]
s = Solution()
n = 15
primes = [2,3,5]
n = 12
primes = [2,7,13,19]
print s.nthSuperUglyNumber(n,primes)
#Super Ugly Number
#https://leetcode.com/problems/super-ugly-number/description/