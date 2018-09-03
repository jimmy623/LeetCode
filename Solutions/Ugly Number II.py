class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """       
        if n == 1:
            return 1
        m = [1]
        i2 = 0
        i3 = 0
        i5 = 0
        next2 = 2
        next3 = 3
        next5 = 5
        p = 1
        while p < n:
            candidate = min(next2,next3,next5)
            m.append(candidate)
            if candidate == next2:
                i2+=1
                next2 = m[i2]*2
            if candidate == next3:
                i3+=1
                next3 = m[i3]*3
            if candidate == next5:
                i5+=1
                next5 = m[i5] * 5
            p += 1
            #print p,m[-1]
        return m[-1] 




#Ugly Number II
#https://leetcode.com/problems/ugly-number-ii/description/
s = Solution()
print s.nthUglyNumber(10)
#Ugly Number II
#https://leetcode.com/problems/ugly-number-ii/description/