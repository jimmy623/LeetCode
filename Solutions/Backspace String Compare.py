class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # sS = []
        # sT = []
        # for c in S:
        #     if c != "#":
        #         sS.append(c)
        #     else:
        #         if sS:
        #             sS.pop()
        # for c in T:
        #     if c != "#":
        #         sT.append(c)
        #     else:
        #         if sT:
        #             sT.pop()
        # return sS == sT

        ps = len(S)-1
        pt = len(T)-1
        cs = 0
        ct = 0
        while True:
            while ps >= 0:
                if S[ps] == "#":
                    cs += 1
                    ps -= 1
                    continue
                elif cs:
                    cs -= 1
                    ps -= 1
                    continue
                else:
                    break
            while pt >= 0:
                if T[pt] == "#":
                    pt -= 1
                    ct += 1
                    continue
                elif ct:
                    ct -= 1
                    pt -= 1
                    continue
                else:
                    break
            #print ps,pt
            if ps < 0 and pt < 0:
                return True
            elif ps < 0 or pt < 0:
                return False

            if S[ps] == T[pt]:
                ps -= 1
                pt -= 1
            else:
                return False
s = Solution()
print s.backspaceCompare("ab#c","ab#c")

#Backspace String Compare
#https://leetcode.com/problems/backspace-string-compare/description/