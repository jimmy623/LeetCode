class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        p = None
        delta = 1
        maxIndex = len(num)-1
        for i in range(len(num)-2,-1,-1):
            t = num[i]
            if t < num[maxIndex]:
                minIndex = maxIndex
                for j in range(i+1,len(num)):
                    print j
                    tj = num[j]
                    if tj > t and tj < num[minIndex]:
                        minIndex = j
                temp = num[i]
                num[i] = num[minIndex]
                num[minIndex] = temp
                b = num[i+1:len(num)]

                b.sort()
                num[i+1:len(num)] = b                
                p = i
                break
                
            else:
                maxIndex = i
                
            

        if p == None:
            num.reverse()
        
        return num
    
        
s = Solution()
print s.nextPermutation([1,3,2])
#print s.nextPermutation([4,2,0,2,3,2,0])
#print s.nextPermutation([1,2])
#Next Permutation
#https://oj.leetcode.com/problems/next-permutation/