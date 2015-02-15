from sets import Set
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        numbers = Set()
        for i in num:
            numbers.add(i)

        result = 0 

        for i in num:
            if not i in numbers:
                continue
            numbers.remove(i)
            count = 1
            v = i - 1

            while v in numbers:
                count += 1
                numbers.remove(v)
                v -= 1
            v = i+1
            while v in numbers:
                count += 1

                numbers.remove(v)
                v += 1
            
            result = max(count,result)
        return result
                
                
s = Solution()
print s.longestConsecutive([100, 4, 200, 1, 3, 2])             
#Longest Consecutive Sequence
#https://oj.leetcode.com/problems/longest-consecutive-sequence/
