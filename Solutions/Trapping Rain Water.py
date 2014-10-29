class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        length = len(A)
        head = 0
        tail = length - 1
        water = 0
        while head < tail:
            if A[head] <= A[head + 1]:
                head += 1
                continue
            else:
                current = A[head]
                next_high_index = head+1
                next_high_load = 0
                next = head+1
                has_equal_or_higher = False
                load = 0
                while next <= tail:
                    if A[next] > A[next_high_index]:
                        next_high_index = next
                        next_high_load = load
                    if A[next] >= current:
                        has_equal_or_higher = True
                        break
                    else:
                        load += A[next]
                        next += 1

                if has_equal_or_higher:
                    water += current * (next - head -1) - load
                    head = next
                else:
                    if next_high_index != head+1:
                        to_add = A[next_high_index] * (next_high_index - head - 1)  - next_high_load
                        water += to_add
                        head = next_high_index
                    else:
                        head += 1
        return water
        


A = [2,6,3,8,2,7,2,5,0] 
s = Solution()
print "water",s.trap(A)

#https://oj.leetcode.com/problems/trapping-rain-water/
#Trapping Rain Water 
