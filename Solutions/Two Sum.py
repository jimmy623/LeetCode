class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        start = 0
        end = len(num)-1
        origin = list(num)
        num.sort()
        
        while start < end:
            v = num[start] + num[end] 
            
            if v == target:
                if num[start] != num[end]:
                    s = origin.index(num[start])
                    e = origin.index(num[end])
                    return (min(s,e)+1,max(s,e)+1)
                else:
                    s = None
                    e = None
                    t = num[start]
                    for i,j in enumerate(origin):
                        print i
                        if j == t:
                            if s == None:
                                s = i
                            else:
                                e = i
                                return (s+1,e+1)
            elif v > target:
                end -= 1
            else:
                start += 1
                

s = Solution()
print s.twoSum([-1,-2,-3,-4,-5], -8)
        
#Two Sum
#https://oj.leetcode.com/problems/two-sum/