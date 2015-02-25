class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        n = len(ratings)
        self.num = 0
        dict = {}
        children = [0] + [0 for i in range(n)] + [0]
        ratings = [0] + ratings + [0]
        for i in range(n):
            v = ratings[i+1]
            if v in dict:
                dict[v].append(i+1)
            else:
                dict[v] = [i+1]
        keys = dict.keys()
        keys.sort()
        for k in keys:
            for i in dict[k]:
                flag = True
                r = k
                v = 1
                
                if r > ratings[i-1]:
                    v = max(v,children[i-1]+1)
                if r > ratings[i+1]:
                    v = max(v,children[i+1]+1)
                children[i] = v
                self.num+= v
        return self.num
        
        
        
                
s = Solution()
print s.candy([2,3])      
#Candy
#https://oj.leetcode.com/problems/candy/