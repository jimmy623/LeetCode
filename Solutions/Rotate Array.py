class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        if k == 0:
            return nums

        count = 0
        i = 0
        while count != n:
            p = i
            temp = nums[i]
            while True:
                pre = temp
                target = (p+k)%n
                
                temp = nums[target]
                nums[target] = pre
                count += 1  
                p = target
                if p == i:
                    break
            i += 1
        return nums
            
s = Solution()
A = [1,2,3,4,5,6]
print s.rotate(A,4)
                
            
                
            
        
        
#Rotate Array
#https://oj.leetcode.com/problems/rotate-array/