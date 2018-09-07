from sets import Set
from collections import defaultdict
# class edge(object):
# 	def __init__(self):
# 		self.end = None
# 		self.weight = 0.0

# class vertex(object):
# 	def __init__(self):
# 		self.val = ""
# 		self.edges = []
# 		e = edge()
# 		e.end = self
# 		e.weight = 1
# 		self.edges.append(e)

class Solution(object):

	def calcEquation(self, equations, values, queries):
		"""
		:type equations: List[List[str]]
		:type values: List[float]
		:type queries: List[List[str]]
		:rtype: List[float]
		"""


		d = defaultdict(list)

		for i,[a,b] in enumerate(equations):
			d[a].append([b,values[i]])
			d[b].append([a,1.0/values[i]])

		result = []
		for [start,end] in queries:
			if start == end:
				if start in d:
					result.append(1.0)
				else:
					result.append(-1.0)
			else:
				visited = Set()
				visited.add(start)
				candidate = list(d[start])
				found = False
				while candidate and not found:
					news = []
					for [key,val] in candidate:
						if key == end:
							result.append(val)
							found = True
							break
						else:
							visited.add(key)
							for [nk,nv] in d[key]:
								if nk not in visited:
									news.append([nk,val*nv])

					candidate = news
				if not found:
					result.append(-1.0)
		return result
							






equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

s = Solution()
print s.calcEquation(equations,values,queries)
#Evaluate Division
#https://leetcode.com/problems/evaluate-division/description/