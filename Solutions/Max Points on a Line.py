# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a

        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        
        max = 0
        uPoints = []
        pHash = {}
        for p in points:
            if (p.x,p.y) in pHash:
                pHash[(p.x,p.y)] = pHash[(p.x,p.y)] + 1
            else:
                uPoints.append(p)
                pHash[(p.x,p.y)] = 1
        
        if len(uPoints) == 1:
            return len(points)
        
        for i in range(0,len(uPoints)):
            p1 = uPoints[i]
            kHash = {"v":pHash[(p1.x,p1.y)]}
            current = 0
            for j in range(0,len(uPoints)):
                if i == j:
                    continue
                p2 = uPoints[j]
                if p1.x == p2.x:
                    count = kHash["v"] + pHash[(p2.x,p2.y)]
                    kHash["v"] = count
                    if count > max:
                        max = count
                else:
                    rate = float(p2.y - p1.y) / float(p2.x - p1.x)
                    count = 0
                    if rate in kHash:
                        count = kHash[rate] + pHash[(p2.x,p2.y)]
                    else:
                        count = pHash[(p1.x,p1.y)] + pHash[(p2.x,p2.y)]
                    kHash[rate] = count
                    if count > max:
                        max = count
        return max
        
ps = []

p = [(29,87),(145,227),(400,84),(800,179),(60,950),(560,122),(-6,5),(-87,-53),(-64,-118),(-204,-388),(720,160),(-232,-228),(-72,-135),(-102,-163),(-68,-88),(-116,-95),(-34,-13),(170,437),(40,103),(0,-38),(-10,-7),(-36,-114),(238,587),(-340,-140),(-7,2),(36,586),(60,950),(-42,-597),(-4,-6),(0,18),(36,586),(18,0),(-720,-182),(240,46),(5,-6),(261,367),(-203,-193),(240,46),(400,84),(72,114),(0,62),(-42,-597),(-170,-76),(-174,-158),(68,212),(-480,-125),(5,-6),(0,-38),(174,262),(34,137),(-232,-187),(-232,-228),(232,332),(-64,-118),(-240,-68),(272,662),(-40,-67),(203,158),(-203,-164),(272,662),(56,137),(4,-1),(-18,-233),(240,46),(-3,2),(640,141),(-480,-125),(-29,17),(-64,-118),(800,179),(-56,-101),(36,586),(-64,-118),(-87,-53),(-29,17),(320,65),(7,5),(40,103),(136,362),(-320,-87),(-5,5),(-340,-688),(-232,-228),(9,1),(-27,-95),(7,-5),(58,122),(48,120),(8,35),(-272,-538),(34,137),(-800,-201),(-68,-88),(29,87),(160,27),(72,171),(261,367),(-56,-101),(-9,-2),(0,52),(-6,-7),(170,437),(-261,-210),(-48,-84),(-63,-171),(-24,-33),(-68,-88),(-204,-388),(40,103),(34,137),(-204,-388),(-400,-106)]
   
for x in p:
    b = Point(x[0],x[1])
    ps.append(b)

s = Solution()
print s.maxPoints(ps) 
#Max Points on a Line
#https://oj.leetcode.com/problems/max-points-on-a-line/