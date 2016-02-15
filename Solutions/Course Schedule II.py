class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        dict = {}
        for [x,y] in prerequisites:
            if x in dict:
                dict[x].append(y)
            else:
                dict[x] = [y]
        order = []
        while len(dict.keys()):
            history = []
            remains = [dict.keys()[0]]
            while len(remains):
                course = remains.pop()
                history.append(course)
                pres = dict[course]
                for p in pres:
                    if p in history:
                        return []
                    if p in dict:
                        remains.append(p)
                    else:
                        if p not in order:
                            order.append(p)

            for k in history:
                del dict[k]
            history.reverse()
            
            for c in history:
                order.append(c)
        if len(order) < numCourses:
            for i in range(numCourses):
                if i not in order:
                    order.append(i)
        return order
            
s = Solution()
print s.findOrder(2,[[1,0]])
#Course Schedule II
#https://leetcode.com/problems/course-schedule-ii/