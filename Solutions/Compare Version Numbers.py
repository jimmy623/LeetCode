class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        version1 = version1.split(".")
        version2 = version2.split(".")
        
        
        m = max(len(version1),len(version2))
        for i in range(m):
            if len(version1) > i:
                v1 = int(version1[i])
            else:
                v1 = 0
            if len(version2) > i:
                v2 = int(version2[i])
            else:
                v2 = 0
            
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1

        return 0
            
            
#Compare Version Numbers
#https://oj.leetcode.com/problems/compare-version-numbers/