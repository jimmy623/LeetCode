import bisect
class RangeModule(object):

    def __init__(self):
        self.X = [0, 10**9]
        self.track = [False] * 2

    def addRange(self, left, right, track=True):
        def index(val):
            i = bisect.bisect_left(self.X,val)    
            if self.X[i] != val:
                self.X.insert(i,val)
                self.track.insert(i,self.track[i-1])
            return i

        l = index(left)
        r = index(right)
        self.X[l:r] = [left]
        self.track[l:r] = [track] 
        
    def queryRange(self, left, right):
        l = bisect.bisect(self.X,left)-1
        r = bisect.bisect_left(self.X,right)
        return all(self.track[l:r])

    def removeRange(self, left, right):
        self.addRange(left,right,False)

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)


#Range Module
#https://leetcode.com/problems/range-module/description/