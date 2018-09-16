class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """

        ws = []
        for i in xrange(len(indexes)):
            ws.append((indexes[i],sources[i],targets[i]))
        ws.sort()
        n = len(ws)
        result = []
        pindex = 0
        i = 0
        while i < len(S):
            if pindex >= n or i != ws[pindex][0]:
                result.append(S[i])
                i+=1
            else:
                w = ws[pindex][1]
                if i+len(w) > len(S) or S[i:i+len(w)] != w:
                    result.append(S[i:i+len(w)])
                    i+= len(w)
                else:
                    i += len(w)
                    result.append(ws[pindex][2])
                pindex += 1
        return "".join(result)
#Find And Replace in String
#https://leetcode.com/problems/find-and-replace-in-string/description/