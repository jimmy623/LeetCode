class Solution(object):
	def reconstructQueue(self, people):
		"""
		:type people: List[List[int]]
		:rtype: List[List[int]]
		"""
		result = []
		people.sort(key = lambda (h,k): (-h,k))
		for [h,k] in people:
			result.insert(k,[h,k])
		return result




s = Solution()
# print s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
# data = [[2,4],[3,4],[9,0],[0,6],[7,1],[6,0],[7,3],[2,5],[1,1],[8,0]]
# print s.reconstructQueue(data)
#print s.reconstructQueue([[8,2],[4,2],[4,5],[2,0],[7,2],[1,4],[9,1],[3,1],[9,0],[1,0]])
print s.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
#output:[[6,0],[1,1],[7,1],[7,3],[2,4],[3,4],[0,6],[2,5],[8,0],[9,0]]
#expect:[[6,0],[1,1],[8,0],[7,1],[9,0],[2,4],[0,6],[2,5],[3,4],[7,3]]

#Queue Reconstruction by Height
#https://leetcode.com/problems/queue-reconstruction-by-height/description/