class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
    
        comp=lambda a,b:1 if a+b>b+a else -1 if a+b<b+a else 0
        num=map(str,num)
        num.sort(cmp=comp,reverse=True)
        return str(int("".join(num)))

s = Solution()
A = [3, 30, 34, 5, 9]
A = [824,938,1399,5607,6973,5703,9609,4398,8247]
print s.largestNumber(A)
#Largest Number
#https://oj.leetcode.com/problems/largest-number/