class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.data.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        temp = []
        while len(self.data):
            temp.append(self.data.pop())

        temp.pop()
        while len(temp):
            self.data.append(temp.pop())


    def peek(self):
        """
        :rtype: int
        """
        temp = []
        while len(self.data):
            temp.append(self.data.pop())
        result = temp[-1]
        while len(temp):
            self.data.append(temp.pop())
        return result

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.data):
            return False
        else:
            return True
#Implement Queue using Stacks
#https://leetcode.com/problems/implement-queue-using-stacks/
