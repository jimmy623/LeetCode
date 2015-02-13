class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        n = len(s)
        if n < 4:
            return []
        result = []
        for i in range(1,4):
            p1 = s[0:i]
            n1 = int(p1)
            if n1 > 255 or (i-0 > 1 and s[0] == "0"):
                continue
            for j in range(i+1,i+4):
                p2 = s[i:j]
                n2 = int(p2)
                if n2 > 255 or (j-i > 1 and s[i] == "0"):
                    continue
                for k in range(j+1,j+4):
                    if k >= n:
                        continue
                    p3 = s[j:k]
                    n3 = int(p3)
                    if n3 > 255 or (k-j > 1 and s[j] == "0"):
                        continue
                    p4 = s[k:n]
                    n4 = int(p4)
                    if n4 > 255 or (n-k > 1 and s[k] == "0"):
                        continue
                    result.append(p1+"."+p2+"."+p3+"."+p4)
        return result
                    
                    
s = Solution()

ip = "25525511135"
ip = "0000"
ip = "101023"
print s.restoreIpAddresses(ip)
                    
                    
        

#Restore IP Addresses
#https://oj.leetcode.com/problems/restore-ip-addresses/