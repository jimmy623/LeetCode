class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        union = []
        mapping = {}
        def findParent(i):
        	if union[i][0] == -1:
        		return i
        	else:
        		parent = findParent(union[i][0])
        		union[i][0] = parent
        		return parent

        for row in accounts:
        	name = row[0]
        	emails = set()
        	for i in xrange(1,len(row)):
        		emails.add(row[i])
        	union.append([-1,name,emails])

        #Union Find
        for i,row in enumerate(union):
        	emails = row[2]
        	for email in emails:
        		if email in mapping:
        			group = mapping[email]
        			p1 = findParent(group)
        			p2 = findParent(i)
        			if p1 != p2:
        				union[p2][0] = p1
        		else:
        			mapping[email] = i
        #Unify results
        for i,row in enumerate(union):
        	if row[0] != -1:
        		parent = findParent(i)
        		for email in row[2]:
        			union[parent][2].add(email)
        #Format results
        result = []
        for i,row in enumerate(union):
        	if row[0] == -1:
        		result.append([row[1]]+sorted(row[2]))
        return result




        




s = Solution()
data = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
data = [["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]
print s.accountsMerge(data)
#Accounts Merge
#https://leetcode.com/problems/accounts-merge/