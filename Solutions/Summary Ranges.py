class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return []
        result = []
        start = None
        end = None
        for i in nums:
            if start == None:
                start = i
                end = start
            else:
                if i == end+1:
                    end = i
                else:
                    if start == end:
                        result.append(str(start))
                    else:
                        result.append(str(start)+"->"+str(end))
                    start = i
                    end = i

        if start != None:
            if start == end:
                result.append(str(start))
            else:
                result.append(str(start)+"->"+str(end))
        return result
     
s = Solution()
s.summaryRanges([1,3])                   
            
#Summary Ranges
#https://leetcode.com/problems/summary-ranges/