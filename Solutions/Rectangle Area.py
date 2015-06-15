#Rectangle Area
#https://leetcode.com/problems/rectangle-area/
class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        sA = (C-A) * (D-B)
        sB = (G-E) * (H-F)
        r = sA  + sB

        if C <= E:
            return r
        if G <= A:
            return r
        if B >= H:
            return r
        if F >= D:
            return r
            
        vs = [(A,B),(A,D),(C,D),(C,B),(E,F),(E,H),(G,H),(G,F)]
        
        xs = [A,C,E,G]
        xs.sort()
        ys = [B,D,F,H]
        ys.sort()
        
        total = (xs[3] - xs[0]) * (ys[3]- ys[0])
        
        upperLeft = 0
        if (xs[0],ys[3]) not in vs:
            upperLeft = (ys[3]-ys[2]) * (xs[1]-xs[0])
            
        upperRight = 0
        if (xs[3],ys[3]) not in vs:
            upperRight = (ys[3]-ys[2]) * (xs[3]-xs[2])

        lowerLeft = 0
        if (xs[0],ys[0]) not in vs:
            lowerLeft = (ys[1]-ys[0]) * (xs[1]-xs[0])
            
        lowerRight = 0
        if (xs[3],ys[0]) not in vs:
            lowerRight = (ys[1]-ys[0]) * (xs[3]-xs[2])
            
        
        total = total - upperLeft - upperRight - lowerLeft - lowerRight
        return total
        
        
s = Solution()
#print s.computeArea(-3,0,3,4,0,-1,9,2)
print s.computeArea(0,0,0,0,-1,-1,1,1)
            
        
        