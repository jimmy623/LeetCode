class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        count = len(num)
        i =  0
        result = []
        
        while i < count:
            head = num[i]
            if head > 0:
                break
                
            start = i + 1
            end = count - 1
            while start < end:
                sum = num[i] + num[start] + num[end]
                if sum == 0:
                    result.append([num[i],num[start],num[end]])
                    vStart = num[start]
                    vEnd = num[end]
                    start += 1
                    end -= 1
                    while start < end and num[start] == vStart:
                        start += 1
                    while start < end and num[end] == vEnd:
                        end -= 1
                elif sum < 0:
                    start += 1
                else:
                    end -= 1
            
            while i < count and num[i] == head:
                i += 1
        return result

#3Sum
#https://oj.leetcode.com/problems/3sum/