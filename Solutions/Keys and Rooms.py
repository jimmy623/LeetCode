class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        tbv = []
        def dfs(i):
        	if i in visited:
        		return
        	visited.add(i)
        	for k in rooms[i]:
        		dfs(k)
       	dfs(0)
       	return len(visited) == len(rooms)



#Keys and Rooms
#https://leetcode.com/problems/keys-and-rooms/