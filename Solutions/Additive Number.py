class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        self.num = num
        for i in xrange(1,n):
        	for j in xrange(1,n-i):
        		if self.check(num[:i],num[i:i+j],i+j):
        			return True
        return False

    def check(self,first,second,index):
    	#print first,second
    	if index == len(self.num):
    		return True
    	if len(first) > 1 and first[0] == "0":
    		return False
    	if len(second) > 1 and second[0] == "0":
    		return False
    	f = int(first)
    	s = int(second)
    	add = f+s
    	string = str(add)
    	if len(string) > len(self.num)-index:
    		return False
    	else:
    		remain = self.num[index:index+len(string)]
    		if remain == string:
    			return self.check(second,remain,index+len(remain))
    		else:
    			return False

s = Solution()
print s.isAdditiveNumber("101")
print s.isAdditiveNumber("1023")
print s.isAdditiveNumber("123")
#print s.isAdditiveNumber("112358")
#print s.isAdditiveNumber("199100199")
#Additive Number
#https://leetcode.com/problems/additive-number/description/