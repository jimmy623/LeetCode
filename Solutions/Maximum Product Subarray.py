class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        result = A[0]
        first  = []
        i = 0
        zeros = False
        while i < len(A):
            
            if A[i] <= 0:
                if A[i] == 0:
                    zeros = True
                first.append(A[i])
                i+=1
                continue
            else:
                p = A[i]
                i+=1
                while i < len(A) and A[i] > 0:
                    p *= A[i]
                    i+=1
                first.append(p)
        i = 0
        while i < len(first):

            if first[i] != 0:
                head = i
                p = first[i]
                i+=1
                while i < len(first) and first[i] != 0:
                    p *= first[i]
                    i+=1

                if p > 0:
                    if p > result:
                        result = p
                else:
                    s = head
                    e = i-1

                    pl = p
                    pr = p
                    while s < e:
                        if first[s] > 0:
                            pl /= first[s]
                            s+=1
                        else:
                            pl /= first[s]
                            break
                    s = head
                    e = i-1
                    while s < e:
                        if first[e] > 0:
                            pr /= first[e]
                            e -=1
                        else:
                            pr /= first[e]
                            break
                    p = max(pl,pr)
                    if p > result:
                        result = p
                    
            i += 1
        if result < 0 and zeros:
            return 0
        else:
            return result
                
            
s = Solution()
a = [2,3,-2,4]
a = [0]
a = [-5,0,2]
print s.maxProduct(a)
        

#Maximum Product Subarray
#https://oj.leetcode.com/problems/maximum-product-subarray/