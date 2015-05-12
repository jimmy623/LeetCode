class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        dict = {}
        for [x,y] in prerequisites:
            if x in dict:
                dict[x].append(y)
            else:
                dict[x] = [y]
        
        while len(dict.keys()):
            history = []
            remains = [dict.keys()[0]]
            while len(remains):
                course = remains.pop()
                history.append(course)
                pres = dict[course]
                for p in pres:
                    if p in history:
                        return False
                    if p in dict:
                        remains.append(p)
            for k in history:
                del dict[k]
             
            
        return True
        
            
s = Solution()
n = 4
pre = [[0,1],[3,1],[1,3],[3,2]]
print s.canFinish(n,pre)
        
#Course Schedule
#https://leetcode.com/problems/course-schedule/