class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num=sorted(num);
        sum2={}
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                sumij=num[i]+num[j];
                if(sumij not in sum2):
                   sum2[sumij]=[];
                sum2[sumij].append((i,j));
        sum2 = sorted(sum2.items(), key=lambda x:x[0])
        print sum2
        res=set();
        i,j=0,len(sum2)-1;
        while(i<=j):
            total=sum2[i][0]+sum2[j][0];
            if(total==target):
                for k1 in range(len(sum2[i][1])):
                    for k2 in range(len(sum2[j][1])):
                        a,b=sum2[i][1][k1];
                        c,d=sum2[j][1][k2];
                        items= set([a,b,c,d]);
                        if(len(items)==4):
                            newItem=[num[fi] for fi in items];
                            newItem=tuple(sorted(newItem));
                            res.add((newItem));
                i+=1;
                j-=1;
            elif(total<target):
                i+=1;
            else:
                j-=1;

        resNums= [];
        for item in res:
            resNums.append([i for i in item]);
        return resNums;

        
s = Solution()
S = [1,0,-1,0,-2,2]
S = [-3,-2,-1,0,0,1,2,3]
print s.fourSum(S,0)
#4Sum
#https://oj.leetcode.com/problems/4sum/



'''
class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num.sort()
        n = len(num)
        i = 0
        result = []
        while i < n:
            v1 = num[i]
            j = i+1
            while j < n:
                v2 = num[j]
                start = j+1
                end = n-1
                while start < end:
                    v3 = num[start]
                    v4 = num[end]
                    sum = v1 + v2 + v3 + v4
                    if sum == target:
                        result.append([v1,v2,v3,v4])
                        start += 1
                        while start < end and num[start] == v3:
                            start += 1
                    elif sum > target:
                        end -= 1
                    else:
                        start += 1
                
                j+=1
                while j < n and num[j] == v2:
                    j+=1
                    
            i+=1
            while i<n and num[i] == v1:
                i += 1
        
        
        return result
'''