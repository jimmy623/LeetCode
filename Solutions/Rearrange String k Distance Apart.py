from collections import Counter
class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        counter = Counter(s)
        chars = []
        for c in counter:
            chars.append([counter[c],c])
        chars.sort(reverse=True)
        n = len(s)
        maxCount = chars[0][0]
        same = 1
        for i in xrange(1,len(chars)):
            if chars[i][0] == maxCount:
                same += 1
            else:
                break
        if (maxCount-1) * k + same > n:
            return ""
        result = [""] * ((maxCount-1) * k + same)
        gap = k
        # print n,chars
        insert = False
        for count,c in chars:
            p = 0
            # print result
            for i in xrange(count):
                while True:
                    if p >= len(result):
                        p = 0
                        insert = True
                    if insert:
                        result.insert(p,c)
                        p += gap
                        break
                    else:
                        while p < len(result) and result[p] != "":
                            p += 1
                        if p < len(result):
                            result[p] = c
                            p += gap
                            break
                        
        return "".join(result)
            

s = Solution()
# print s.rearrangeString("aabbcc",2)
print s.rearrangeString("bbabcaccaaabababbaaaaccbbcbacbacacccbbcaabcbcacaaccbabbbbbcacccaccbabaccbacabca",1)
# print s.rearrangeString("bbabcaccaaabababbaaaaccbbcbacbacacccbbcaabcbcacaaccbabbbbbcacccaccbabaccbacabcabcacb",2)

#Rearrange String k Distance Apart
#https://leetcode.com/problems/rearrange-string-k-distance-apart/description/