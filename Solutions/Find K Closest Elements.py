class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        A = arr
        K = x
        C = k
        start = 0
        end = len(A) -1
        while start < end:
            mid = (start + end) / 2
            # print A[start],A[mid],A[end],K
            if A[mid] == K:
                start = mid
                break
            if A[mid] > K:
                end = mid - 1
            else:
                start = mid + 1

        p1 = start
        p2 = start
        while p2 - p1 < C:
            if p1  == 0:
                return A[:C]
            if p2 == len(A):
                return A[-C:]
            if K - A[p1-1] <= A[p2] - x:
                p1 -= 1
            else:
                p2 += 1
        return A[p1:p2]



        # cstart = start - C + 1
        # if cstart < 0:
        #     cstart = 0
    
        # cend = cstart + C

        # if cend + C-1 >= len(A):
        #     cend = len(A)-1 - (C-1)

        # while cstart < cend:
        #     print cstart,cend
        #     mid = (cstart + cend) / 2
        #     if K - A[mid] == A[mid+C-1] - K:
        #         cstart = mid
        #         break
        #     if K - A[mid] < A[mid+C-1] - K:
        #         cend = mid -1
        #     else:
        #         cstart = mid + 1
        # return A[cstart:cstart+C]

s = Solution()
# print s.findClosestElements([1,2,3,4,5],4,3)
# print s.findClosestElements([0,0,1,2,3,3,4,7,7,8],3,5)
print s.findClosestElements([0,1,2,2,2,3,6,8,8,9],5,9)

#Find K Closest Elements
#https://leetcode.com/problems/find-k-closest-elements/description/