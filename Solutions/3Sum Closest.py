class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        count = len(num)
        diff = 99999
        record = 0
        i = 0
        while i < count:
            head = num[i]
            start = i + 1
            end = count-1
            while start < end:
                sum = head + num[start] + num[end]
                if sum == target:
                    diff = 0
                    record = sum
                    break
                if sum < target:
                    start += 1
                    if abs(sum - target) < diff:
                        record = sum
                        diff = abs(sum - target)
                    
                if sum > target:
                    end -= 1
                    if abs(sum-target) < diff:
                        record = sum
                        diff = abs(sum - target)
            
            if diff == 0:
                break
            while i < count and num[i] == head:
                i+=1
                
        return record
            
        
        
s = Solution()
print s.threeSumClosest([-1,0,1,2,-1,-4],0)

#3Sum Closest
#https://oj.leetcode.com/problems/3sum-closest/

'''
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        count = len(num)
        closet = num[0] + num[1] + num[2]
        diff = abs(closet - target)
        for i in range(count):
            for j in range(i+1,count):
                for k in range(j+1,count):
                    sum = num[i] + num[j] + num[k]
                    if abs(sum - target) < diff:
                        diff = abs(sum-target)
                        closet = sum
        return closet
'''