class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace("-","")
        S = S.upper()
        remain = len(S) % K
        result = []
        count = K-remain
        for c in S:
            result.append(c)
            count += 1
            if (count % K) == 0:
                result.append("-")
        if result and result[-1] == "-":
            result.pop()
        return "".join(result)

s = Solution()
print s.licenseKeyFormatting("5F3Z-2e-9-w",4)
#License Key Formatting
#https://leetcode.com/problems/license-key-formatting/description/