# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.remain = []

    def read(self, buf, n):
        idx = 0
        while n > 0 and self.remain:
            buf[idx] = self.remain[0]
            del self.remain[0]
            idx += 1
            n -= 1

        while n > 0:
            buf4 = [""]*4
            l = read4(buf4)
            if not l:
                break
            for i in range(min(l, n)):
                buf[idx] = buf4[i]
                idx += 1
            if n < l:
                self.remain = buf4[n:l]
            n -= l
        return idx

#Read N Characters Given Read4 II - Call multiple times
#https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/description/