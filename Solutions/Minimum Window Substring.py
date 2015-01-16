class Solution:
    # @return a string
    def minWindow(self, S, T):
        sLen = len(S)
        num = len(T)

        counts = {}
        collect = {}
        for c in T:
            if c in counts:
                counts[c] = counts[c]+1
            else:
                counts[c] = 1
            collect[c] = []

        cs = []
        min = ""
        index = 0
        while index < sLen:
            c = S[index]
            check = False
            if c in T:
                if len(collect[c]) < counts[c]:
                    collect[c].append((c,index))
                    cs.append((c,index))
                    
                    if len(cs) == num:
                        check = True
                else:    
                    old = collect[c][0]

                    collect[c].remove(old)
                    collect[c].append((c,index))
                    replace = False
                    if cs[0] == old:
                        check = True
 
                    cs.remove(old)
                    cs.append((c,index))
                    
                if len(cs) == num and check:
                    length = cs[num-1][1] - cs[0][1] + 1
                    if min == "":
                        min = S[cs[0][1]:cs[num-1][1]+1]
                    elif len(min) > length:
                        min = S[cs[0][1]:cs[num-1][1]+1]

            index += 1
        return min
    
S = "ADOBECODEBANC"
T = "ABCE"


s = Solution()
result = s.minWindow(S,T)
print result

#Minimum Window Substring 
#https://oj.leetcode.com/problems/minimum-window-substring/