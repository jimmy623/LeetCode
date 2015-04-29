class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        ds = {}
        dt = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            cs = s[i]
            ct = t[i]
            if cs in ds:
                if ct in dt:
                    if ds[cs] == dt[ct]:
                        pass
                    else:
                        return False
                else:
                    return False
            
            if cs not in ds:
                if ct not in dt:
                    ds[cs] = i
                    dt[ct] = i
                else:
                    return False
        return True
#Isomorphic Strings
#https://leetcode.com/problems/isomorphic-strings/