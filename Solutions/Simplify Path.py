class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        folders = path.split("/")
        result = []
        for p in folders:
            #print result,p
            if p == "." or p == "":
                continue
            if p == "..":
                if len(result) > 0:
                    result.pop()
                continue
            
            result.append(p)
            
        
        str = ""
        if len(result):
            for d in result:
                str += "/"
                str += d
            return str
        else:
            return "/"
            

a = "/Z/Iyy/HSyT/ItVqc/.././//Z/.././.././../a/gK/../ZurH///x/../////././../.."
s = Solution()
print s.simplifyPath(a)
#Simplify Path
#https://oj.leetcode.com/problems/simplify-path/