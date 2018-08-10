# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        #self.list = nestedList
        self.listStack = [nestedList]
        self.indexStack = [0]
        

    def next(self):
        """
        :rtype: int
        """
        n = self.listStack[-1][self.indexStack[-1]].getInteger()
        self.indexStack[-1] += 1            
        return n


    def hasNext(self):
        """
        :rtype: bool
        """
        while True:
            if len(self.listStack) == 0:
                return False
            if self.indexStack[-1] >= len(self.listStack[-1]):
                del self.indexStack[-1]
                del self.listStack[-1]
                continue
            if self.listStack[-1][self.indexStack[-1]].isInteger() == False:
                self.listStack.append(self.listStack[-1][self.indexStack[-1]].getList())
                self.indexStack[-1] += 1
                self.indexStack.append(0);
                continue
            return True
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

#Flatten Nested List Iterator
#https://leetcode.com/problems/flatten-nested-list-iterator/description/